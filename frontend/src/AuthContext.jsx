import React, { createContext, useContext, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const AuthContext = createContext();

export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem('token') || null);
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (token) {
      localStorage.setItem('token', token);
      fetchUserProfile(token);
    } else {
      localStorage.removeItem('token');
      setUser(null);
      setLoading(false);
    }
  }, [token]);

  const decodeTokenEmail = (jwtToken) => {
    try {
      if (!jwtToken) return null;
      const parts = jwtToken.split('.');
      if (parts.length >= 2) {
        const payload = JSON.parse(atob(parts[1]));
        return payload.sub || null;
      }
    } catch (e) {
      return null;
    }
    return null;
  };

  const fetchUserProfile = async (authToken) => {
    // Immediate fallback from JWT token payload so user is never null
    const tokenEmail = decodeTokenEmail(authToken);
    if (tokenEmail) {
      localStorage.setItem('user_email', tokenEmail);
      setUser(prev => prev || { 
        email: tokenEmail, 
        role: tokenEmail.trim().toLowerCase() === 'nasaadanna@gmail.com' ? 'admin' : 'student' 
      });
    }

    try {
      const res = await fetch('/users/me', {
        headers: { 'Authorization': `Bearer ${authToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        if (data.email && data.email.trim().toLowerCase() === 'nasaadanna@gmail.com') {
          data.role = 'admin';
        }
        setUser(data);
        if (data.email) {
          localStorage.setItem('user_email', data.email);
        }
      } else if (res.status === 401) {
        // Only clear token on authentication failure, NOT on server errors (500)
        setToken(null);
      } else {
        // Server error (500, etc.) — keep the token, user is still authenticated
        console.warn(`/users/me returned ${res.status}, keeping session`);
      }
    } catch (err) {
      // Network error — keep the token, don't log out
      console.error("Failed to fetch user profile:", err);
    } finally {
      setLoading(false);
    }
  };

  // Refresh user data (e.g., after payment, after XP gain)
  const refreshUser = () => {
    if (token) {
      fetchUserProfile(token);
    }
  };

  const login = async (email, password) => {
    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);

    const res = await fetch('/users/login', {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData
    });

    if (!res.ok) {
      const errorText = await res.text();
      let errData = {};
      try {
        errData = JSON.parse(errorText);
      } catch (e) {
        if (errorText && errorText.trim().startsWith('<')) {
          throw new Error("Server error. Please try again later.");
        }
        throw new Error(errorText || "Invalid credentials");
      }
      throw new Error(errData.detail || "Invalid credentials");
    }
    const data = await res.json();
    // Set localStorage synchronously so ProtectedRoute sees the token
    // immediately after navigate(), even before React re-renders context
    localStorage.setItem('token', data.access_token);
    setToken(data.access_token);
  };

  const signup = async (name, email, password, level, goal, referralCode = null) => {
    const res = await fetch('/users/signup', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ full_name: name, email, password, level, goal, referral_code: referralCode })
    });
    
    if (!res.ok) {
      const errorText = await res.text();
      let errData = {};
      try {
        errData = JSON.parse(errorText);
      } catch (e) {
        if (errorText && errorText.trim().startsWith('<')) {
          throw new Error("Server error. Please try again later.");
        }
        throw new Error(errorText || "Registration failed");
      }
      throw new Error(errData.detail || "Registration failed");
    }
    // Automatically login after signup
    await login(email, password);
  };

  const resetPassword = async (email, oldPassword, newPassword) => {
    const res = await fetch('/users/reset-password', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, old_password: oldPassword, new_password: newPassword })
    });
    
    if (!res.ok) {
      const errorText = await res.text();
      let errData = {};
      try {
        errData = JSON.parse(errorText);
      } catch (e) {
        if (errorText && errorText.trim().startsWith('<')) {
          throw new Error("Server error. Please try again later.");
        }
        throw new Error(errorText || "Reset password failed");
      }
      throw new Error(errData.detail || "Reset password failed");
    }
  };

  const logout = () => {
    setToken(null);
  };

  // Derive subscription from user data (comes from /users/me which includes subscription)
  // Admins and teachers automatically inherit full Pro capabilities
  const isUserAdmin = user?.role === 'admin' || user?.role === 'teacher' || (user?.email && user.email.trim().toLowerCase() === 'nasaadanna@gmail.com');
  const subscription = user?.subscription ? {
    ...user.subscription,
    is_pro: isUserAdmin ? true : Boolean(user.subscription.is_pro)
  } : { 
    plan: isUserAdmin ? 'admin_pro' : 'free', 
    is_pro: isUserAdmin, 
    status: 'active' 
  };

  return (
    <AuthContext.Provider value={{ 
      token, user, loading, subscription,
      login, signup, logout, resetPassword, refreshUser 
    }}>
      {children}
    </AuthContext.Provider>
  );
};


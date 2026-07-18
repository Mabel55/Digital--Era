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

  const fetchUserProfile = async (authToken) => {
    try {
      const res = await fetch('/users/me', {
        headers: { 'Authorization': `Bearer ${authToken}` }
      });
      if (res.ok) {
        const data = await res.json();
        setUser(data);
      } else {
        setToken(null);
      }
    } catch (err) {
      console.error("Failed to fetch user profile:", err);
      setToken(null);
    } finally {
      setLoading(false);
    }
  };

  const login = async (email, password) => {
    const formData = new URLSearchParams();
    formData.append("username", email);
    formData.append("password", password);

    const res = await fetch('/login', {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: formData
    });

    if (!res.ok) {
      const errData = await res.json();
      throw new Error(errData.detail || "Invalid credentials");
    }
    const data = await res.json();
    setToken(data.access_token);
  };

  const signup = async (name, email, password, level, goal) => {
    const res = await fetch('/signup', {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ full_name: name, email, password, level, goal })
    });
    
    if (!res.ok) {
      const errData = await res.json();
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
      const errData = await res.json();
      throw new Error(errData.detail || "Reset password failed");
    }
  };

  const logout = () => {
    setToken(null);
  };

  return (
    <AuthContext.Provider value={{ token, user, loading, login, signup, logout, resetPassword }}>
      {children}
    </AuthContext.Provider>
  );
};

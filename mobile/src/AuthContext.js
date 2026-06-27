import React, { createContext, useState, useContext, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';

const AuthContext = createContext({});

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Set the base URL for the backend
  // Uses 10.0.2.2 for Android emulator localhost alias. Use actual IP for physical device testing.
  const baseURL = 'http://10.0.2.2:8000'; 
  
  useEffect(() => {
    loadToken();
  }, []);

  const loadToken = async () => {
    try {
      const storedToken = await AsyncStorage.getItem('token');
      if (storedToken) {
        setToken(storedToken);
        await fetchUser(storedToken);
      }
    } catch (e) {
      console.error(e);
    } finally {
      setIsLoading(false);
    }
  };

  const fetchUser = async (authToken) => {
    try {
      const response = await axios.get(`${baseURL}/users/me`, {
        headers: { Authorization: `Bearer ${authToken}` }
      });
      setUser(response.data);
    } catch (e) {
      console.error("Failed to fetch user", e);
      logout();
    }
  };

  const login = async (email, password) => {
    try {
      const formData = new FormData();
      formData.append('username', email); // OAuth2 expects username
      formData.append('password', password);

      const response = await axios.post(`${baseURL}/users/token`, formData, {
        headers: { 'Content-Type': 'multipart/form-data' }
      });
      
      const newToken = response.data.access_token;
      setToken(newToken);
      await AsyncStorage.setItem('token', newToken);
      await fetchUser(newToken);
      return true;
    } catch (e) {
      console.error(e);
      return false;
    }
  };

  const logout = async () => {
    setToken(null);
    setUser(null);
    await AsyncStorage.removeItem('token');
  };

  return (
    <AuthContext.Provider value={{ user, token, isLoading, login, logout, baseURL }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);

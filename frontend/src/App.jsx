import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './AuthContext';
import Onboarding from './components/Onboarding';
import Dashboard from './components/Dashboard';
import Workspace from './components/Workspace';
import DBWorkspace from './components/DBWorkspace';
import TeacherDashboard from './components/TeacherDashboard';

const ProtectedRoute = ({ children }) => {
  const { token, loading } = useAuth();
  
  if (loading) {
    return <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', color: 'white' }}>Loading...</div>;
  }
  
  if (!token) {
    return <Navigate to="/onboarding" />;
  }
  
  return children;
};

const App = () => {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/onboarding" element={<Onboarding />} />
          <Route path="/" element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          } />
          <Route path="/workspace/:courseId" element={
            <ProtectedRoute>
              <Workspace />
            </ProtectedRoute>
          } />
          <Route path="/db-workspace/:courseId" element={
            <ProtectedRoute>
              <DBWorkspace />
            </ProtectedRoute>
          } />
          <Route path="/teacher" element={
            <ProtectedRoute>
              <TeacherDashboard />
            </ProtectedRoute>
          } />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;

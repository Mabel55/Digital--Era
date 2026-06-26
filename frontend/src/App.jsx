import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './AuthContext';
import Onboarding from './components/Onboarding';
import Dashboard from './components/Dashboard';
import Workspace from './components/Workspace';
import DBWorkspace from './components/DBWorkspace';
import TeacherDashboard from './components/TeacherDashboard';
import Assessment from './components/Assessment';
import Leaderboard from './components/Leaderboard';
import ProjectWorkspace from './components/ProjectWorkspace';

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
          <Route path="/assessment/:topic" element={
            <ProtectedRoute>
              <Assessment />
            </ProtectedRoute>
          } />
          <Route path="/project/:projectId" element={
            <ProtectedRoute>
              <ProjectWorkspace />
            </ProtectedRoute>
          } />
          <Route path="/leaderboard" element={
            <ProtectedRoute>
              <Leaderboard />
            </ProtectedRoute>
          } />
          <Route path="/public-leaderboard" element={
            <Leaderboard isPublic={true} />
          } />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
};

export default App;

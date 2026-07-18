import React, { Suspense, lazy } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './AuthContext';
import PWAInstallPrompt from './components/PWAInstallPrompt';
import OfflineBanner from './components/OfflineBanner';
import ErrorBoundary from './ErrorBoundary';
import { Loader2 } from 'lucide-react';

// Lazy-loaded routes for code splitting
const Onboarding = lazy(() => import('./components/Onboarding'));
const Dashboard = lazy(() => import('./components/Dashboard'));
const Workspace = lazy(() => import('./components/Workspace'));
const DBWorkspace = lazy(() => import('./components/DBWorkspace'));
const TeacherDashboard = lazy(() => import('./components/TeacherDashboard'));
const Assessment = lazy(() => import('./components/Assessment'));
const Leaderboard = lazy(() => import('./components/Leaderboard'));
const ProjectWorkspace = lazy(() => import('./components/ProjectWorkspace'));
const LandingPage = lazy(() => import('./components/LandingPage'));
const CourseCatalog = lazy(() => import('./components/CourseCatalog'));

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
    <ErrorBoundary>
      <BrowserRouter>
        <OfflineBanner />
        <AuthProvider>
          <Suspense fallback={<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', color: 'var(--text2)' }}><Loader2 className="spinner" size={32} /></div>}>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/courses" element={<CourseCatalog />} />
            <Route path="/onboarding" element={<Onboarding />} />
            <Route path="/dashboard" element={
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
        </Suspense>
        <PWAInstallPrompt />
      </AuthProvider>
    </BrowserRouter>
    </ErrorBoundary>
  );
};

export default App;

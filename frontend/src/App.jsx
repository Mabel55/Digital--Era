import React, { Suspense, lazy, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './AuthContext';
import PWAInstallPrompt from './components/PWAInstallPrompt';
import OfflineBanner from './components/OfflineBanner';
import ErrorBoundary from './ErrorBoundary';
import { Loader2 } from 'lucide-react';

// Lazy-loaded routes for code splitting
const Onboarding = lazy(() => import('./components/Onboarding'));
const ResetPassword = lazy(() => import('./components/ResetPassword'));
const Dashboard = lazy(() => import('./components/Dashboard'));
const Workspace = lazy(() => import('./components/Workspace'));
const DBWorkspace = lazy(() => import('./components/DBWorkspace'));
const TeacherDashboard = lazy(() => import('./components/TeacherDashboard'));
const Assessment = lazy(() => import('./components/Assessment'));
const Leaderboard = lazy(() => import('./components/Leaderboard'));
const ProjectWorkspace = lazy(() => import('./components/ProjectWorkspace'));
const LandingPage = lazy(() => import('./components/LandingPage'));
const CourseCatalog = lazy(() => import('./components/CourseCatalog'));
const PricingPage = lazy(() => import('./components/PricingPage'));
const Profile = lazy(() => import('./components/Profile'));
const DailyChallenge = lazy(() => import('./components/DailyChallenge'));
const CareerTracks = lazy(() => import('./components/CareerTracks'));
const Sandbox = lazy(() => import('./components/Sandbox'));
const Forum = lazy(() => import('./components/Forum'));

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

import { QueryClient, QueryClientProvider, useQueryClient } from '@tanstack/react-query';
import { HelmetProvider } from 'react-helmet-async';
import { prefetchCurriculum } from './hooks/useCurriculum';

// Initialize React Query client
const queryClient = new QueryClient();

// Prefetch curriculum immediately — before auth resolves — so it's ready when Dashboard renders
prefetchCurriculum(queryClient);

const App = () => {
  return (
    <ErrorBoundary>
      <HelmetProvider>
        <QueryClientProvider client={queryClient}>
          <BrowserRouter>
            <OfflineBanner />
            <AuthProvider>
              <Suspense fallback={<div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '100vh', color: 'var(--text2)' }}><Loader2 className="spinner" size={32} /></div>}>
              <Routes>
                <Route path="/" element={<LandingPage />} />
                <Route path="/catalog" element={<CourseCatalog />} />
                <Route path="/community" element={<Forum />} />
                <Route path="/career-tracks" element={<CareerTracks />} />
                <Route path="/pricing" element={<PricingPage />} />
                <Route path="/onboarding" element={<Onboarding />} />
                <Route path="/reset-password" element={<ResetPassword />} />
                <Route path="/dashboard" element={
                  <ProtectedRoute>
                    <Dashboard />
                  </ProtectedRoute>
                } />
                <Route path="/profile" element={
                  <ProtectedRoute>
                    <Profile />
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
                <Route path="/daily-challenge" element={
                  <ProtectedRoute>
                    <DailyChallenge />
                  </ProtectedRoute>
                } />
                <Route path="/sandbox" element={
                  <ProtectedRoute>
                    <Sandbox />
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
        </QueryClientProvider>
      </HelmetProvider>
    </ErrorBoundary>
  );
};

export default App;

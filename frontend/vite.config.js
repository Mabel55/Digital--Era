import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.svg', 'icons.svg', 'offline.html'],
      manifest: {
        name: 'Digital Era – Master AI, Data & Code',
        short_name: 'Digital Era',
        description: 'Interactive, AI-powered learning platform. Build real-world projects in Python, SQL, React, Data Science and AI.',
        theme_color: '#0d0f14',
        background_color: '#0d0f14',
        display: 'standalone',
        orientation: 'portrait-primary',
        scope: '/',
        start_url: '/',
        categories: ['education', 'productivity'],
        icons: [
          {
            src: '/pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png'
          },
          {
            src: '/pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'maskable'
          }
        ],
        screenshots: [],
        shortcuts: [
          {
            name: 'Course Catalog',
            short_name: 'Courses',
            url: '/courses',
            description: 'Browse all available courses'
          },
          {
            name: 'Dashboard',
            short_name: 'Dashboard',
            url: '/dashboard',
            description: 'Your learning dashboard'
          },
          {
            name: 'Leaderboard',
            short_name: 'Leaderboard',
            url: '/leaderboard',
            description: 'See top learners'
          }
        ]
      },
      workbox: {
        // Cache the offline fallback page
        globPatterns: ['**/*.{js,css,html,ico,png,svg,woff2}'],
        
        // Runtime caching strategies
        runtimeCaching: [
          {
            // Cache Google Fonts stylesheets
            urlPattern: /^https:\/\/fonts\.googleapis\.com\/.*/i,
            handler: 'CacheFirst',
            options: {
              cacheName: 'google-fonts-stylesheets',
              expiration: {
                maxEntries: 10,
                maxAgeSeconds: 60 * 60 * 24 * 365 // 1 year
              }
            }
          },
          {
            // Cache Google Fonts webfont files
            urlPattern: /^https:\/\/fonts\.gstatic\.com\/.*/i,
            handler: 'CacheFirst',
            options: {
              cacheName: 'google-fonts-webfonts',
              expiration: {
                maxEntries: 30,
                maxAgeSeconds: 60 * 60 * 24 * 365 // 1 year
              }
            }
          },
          {
            // Cache API calls for course data (read-only endpoints)
            urlPattern: /\/courses\/\d+\/lessons/i,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'lesson-data-cache',
              expiration: {
                maxEntries: 200,
                maxAgeSeconds: 60 * 60 * 24 * 7 // 1 week
              }
            }
          },
          {
            // Cache curriculum/course listing data
            urlPattern: /\/courses\/?$/i,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'course-catalog-cache',
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 60 * 60 * 24 // 1 day
              }
            }
          },
          {
            // Cache images from external sources
            urlPattern: /^https:\/\/images\.unsplash\.com\/.*/i,
            handler: 'CacheFirst',
            options: {
              cacheName: 'external-images',
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 60 * 60 * 24 * 30 // 30 days
              }
            }
          },
          {
            // Navigation requests – serve cached page or offline fallback
            urlPattern: ({ request }) => request.mode === 'navigate',
            handler: 'NetworkFirst',
            options: {
              cacheName: 'pages-cache',
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 60 * 60 * 24 * 7 // 1 week
              },
              networkTimeoutSeconds: 5
            }
          }
        ],

        // Offline fallback
        navigateFallback: null,
        navigateFallbackDenylist: [/^\/api/, /^\/signup/, /^\/login/, /^\/chat/, /^\/ask-ai/, /^\/run-python/],
      }
    })
  ],
  server: {
    proxy: {
      '/signup': 'http://127.0.0.1:8000',
      '/login': 'http://127.0.0.1:8000',
      '/users': 'http://127.0.0.1:8000',
      '/teachers': 'http://127.0.0.1:8000',
      '/run-python': 'http://127.0.0.1:8000',
      '/chat': 'http://127.0.0.1:8000',
      '/ask-ai': 'http://127.0.0.1:8000',
      '/admin': 'http://127.0.0.1:8000',
    }
  }
})

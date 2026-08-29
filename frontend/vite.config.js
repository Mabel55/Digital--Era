import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      // Precache the curriculum JSON and AI FAQs alongside static assets so they're available offline immediately
      includeAssets: ['favicon.svg', 'icons.svg', 'offline.html', 'mabel-founder.jpg', 'curriculum.json', 'ai-faqs.json'],
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
        // Precache app shell + curriculum data
        globPatterns: ['**/*.{js,css,html,ico,png,svg,woff2,jpg,jpeg}'],
        
        // Increase precache size limit for curriculum.json (~2.1MB)
        maximumFileSizeToCacheInBytes: 5 * 1024 * 1024, // 5MB

        // Runtime caching strategies
        runtimeCaching: [
          {
            // ★ CRITICAL: Cache Pyodide runtime from CDN (one-time ~15MB download)
            // This is what makes Python code execution work offline
            urlPattern: /^https:\/\/cdn\.jsdelivr\.net\/pyodide\/.*/i,
            handler: 'CacheFirst',
            options: {
              cacheName: 'pyodide-runtime',
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 60 * 60 * 24 * 90 // 90 days
              },
              cacheableResponse: {
                statuses: [0, 200]
              }
            }
          },
          {
            // ★ CRITICAL: Cache curriculum.json with StaleWhileRevalidate
            // Serves cached version instantly, updates in background
            urlPattern: /\/curriculum\.json/i,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'curriculum-cache',
              expiration: {
                maxEntries: 5,
                maxAgeSeconds: 60 * 60 * 24 * 30 // 30 days
              },
              cacheableResponse: {
                statuses: [0, 200]
              }
            }
          },
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
            // Cache Monaco Editor chunks from CDN
            urlPattern: /^https:\/\/cdn\.jsdelivr\.net\/npm\/monaco-editor\/.*/i,
            handler: 'CacheFirst',
            options: {
              cacheName: 'monaco-editor-cache',
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 60 * 60 * 24 * 90 // 90 days
              },
              cacheableResponse: {
                statuses: [0, 200]
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
            // Cache course listing from backend
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
            // Cache daily challenge data
            urlPattern: /\/daily-challenge\//i,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'daily-challenge-cache',
              expiration: {
                maxEntries: 5,
                maxAgeSeconds: 60 * 60 * 24 // 1 day
              }
            }
          },
          {
            // Cache leaderboard data
            urlPattern: /\/leaderboard/i,
            handler: 'StaleWhileRevalidate',
            options: {
              cacheName: 'leaderboard-cache',
              expiration: {
                maxEntries: 10,
                maxAgeSeconds: 60 * 60 // 1 hour
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
            // ★ Navigation requests — SPA fallback for offline routing
            // Uses NetworkFirst with a fast timeout so offline users see
            // the cached app shell immediately instead of a browser error
            urlPattern: ({ request }) => request.mode === 'navigate',
            handler: 'NetworkFirst',
            options: {
              cacheName: 'pages-cache',
              expiration: {
                maxEntries: 50,
                maxAgeSeconds: 60 * 60 * 24 * 7 // 1 week
              },
              networkTimeoutSeconds: 3
            }
          }
        ],

        // SPA offline: fallback to index.html so React Router handles all routes
        navigateFallback: '/index.html',
        // Don't intercept API endpoints — only navigation (page) requests
        navigateFallbackDenylist: [
          /^\/api/,
          /^\/users/,
          /^\/chat/,
          /^\/ask-ai/,
          /^\/run-code/,
          /^\/run-python/,
          /^\/courses/,
          /^\/notifications/,
          /^\/leaderboard/,
          /^\/daily-challenge/,
          /^\/translate/,
          /^\/payments/,
          /^\/teachers/,
          /^\/admin/,
          /^\/ai-usage/,
          /^\/forum/,
        ],
      }
    })
  ],
  server: {
    proxy: {
      '/users': 'http://127.0.0.1:8000',
      '/teachers': 'http://127.0.0.1:8000',
      '/courses': 'http://127.0.0.1:8000',
      '/run-python': 'http://127.0.0.1:8000',
      '/chat': 'http://127.0.0.1:8000',
      '/ask-ai': 'http://127.0.0.1:8000',
      '/admin': 'http://127.0.0.1:8000',
      '/daily-challenge': 'http://127.0.0.1:8000',
      '/notifications': 'http://127.0.0.1:8000',
      '/leaderboard': 'http://127.0.0.1:8000',
    },
    // Serve the large curriculum.json with long-lived cache headers.
    // The ?v= query param in useCurriculum.js acts as the cache-buster when content changes.
    headers: {
      'Cache-Control': 'no-store', // default for other responses
    },
    middlewares: [
      (req, res, next) => {
        if (req.url && req.url.startsWith('/curriculum.json')) {
          // Cache for 1 year — the ?v= query param busts it on new deployments
          res.setHeader('Cache-Control', 'public, max-age=31536000, immutable');
        }
        next();
      }
    ]
  }
})

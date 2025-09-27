// Service Worker for CourseCenter PWA
const CACHE_NAME = 'coursecenter-v1.0.0';
const urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/js/main.js',
    '/static/images/favicon.ico',
    // Add more critical resources here
];

// Install event - cache critical resources
self.addEventListener('install', event => {
    console.log('Service Worker installing...');
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Caching critical resources');
                return cache.addAll(urlsToCache);
            })
            .then(() => {
                console.log('Service Worker installed successfully');
                return self.skipWaiting();
            })
            .catch(error => {
                console.error('Service Worker installation failed:', error);
            })
    );
});

// Activate event - clean up old caches
self.addEventListener('activate', event => {
    console.log('Service Worker activating...');
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('Deleting old cache:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        }).then(() => {
            console.log('Service Worker activated successfully');
            return self.clients.claim();
        })
    );
});

// Fetch event - serve from cache when possible
self.addEventListener('fetch', event => {
    // Skip non-GET requests
    if (event.request.method !== 'GET') {
        return;
    }

    // Skip external requests
    if (!event.request.url.startsWith(self.location.origin)) {
        return;
    }

    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // Return cached version if available
                if (response) {
                    console.log('Serving from cache:', event.request.url);
                    return response;
                }

                // Fetch from network and cache for future use
                return fetch(event.request).then(response => {
                    // Don't cache if not a valid response
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    // Clone the response as it can only be consumed once
                    const responseToCache = response.clone();

                    caches.open(CACHE_NAME)
                        .then(cache => {
                            cache.put(event.request, responseToCache);
                        });

                    return response;
                });
            })
            .catch(error => {
                console.error('Fetch failed:', error);
                
                // Return offline page for navigation requests
                if (event.request.mode === 'navigate') {
                    return caches.match('/offline.html');
                }
                
                // Return placeholder for images
                if (event.request.destination === 'image') {
                    return new Response(
                        '<svg width="200" height="150" xmlns="http://www.w3.org/2000/svg"><rect width="100%" height="100%" fill="#f0f0f0"/><text x="50%" y="50%" text-anchor="middle" dy=".3em" fill="#999">Rasm yuklanmadi</text></svg>',
                        { headers: { 'Content-Type': 'image/svg+xml' } }
                    );
                }
                
                throw error;
            })
    );
});

// Background sync for form submissions
self.addEventListener('sync', event => {
    console.log('Background sync triggered:', event.tag);
    
    if (event.tag === 'contact-form-sync') {
        event.waitUntil(syncContactForms());
    }
});

// Push notification handling
self.addEventListener('push', event => {
    console.log('Push notification received');
    
    const options = {
        body: event.data ? event.data.text() : 'Yangi xabar!',
        icon: '/static/images/icon-192x192.png',
        badge: '/static/images/badge-72x72.png',
        vibrate: [100, 50, 100],
        data: {
            dateOfArrival: Date.now(),
            primaryKey: 1
        },
        actions: [
            {
                action: 'explore',
                title: 'Ko\'rish',
                icon: '/static/images/checkmark.png'
            },
            {
                action: 'close',
                title: 'Yopish',
                icon: '/static/images/xmark.png'
            }
        ]
    };

    event.waitUntil(
        self.registration.showNotification('CourseCenter', options)
    );
});

// Notification click handling
self.addEventListener('notificationclick', event => {
    console.log('Notification clicked:', event.notification.tag);
    
    event.notification.close();

    if (event.action === 'explore') {
        event.waitUntil(
            clients.openWindow('/')
        );
    }
});

// Utility functions
async function syncContactForms() {
    try {
        // Get pending form submissions from IndexedDB
        const pendingForms = await getPendingForms();
        
        for (const form of pendingForms) {
            try {
                const response = await fetch('/contact/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': form.csrfToken
                    },
                    body: JSON.stringify(form.data)
                });
                
                if (response.ok) {
                    await removePendingForm(form.id);
                    console.log('Form synced successfully');
                }
            } catch (error) {
                console.error('Failed to sync form:', error);
            }
        }
    } catch (error) {
        console.error('Background sync failed:', error);
    }
}

async function getPendingForms() {
    // This would integrate with IndexedDB to get pending forms
    return [];
}

async function removePendingForm(id) {
    // This would remove the form from IndexedDB
    console.log('Removing pending form:', id);
}

// Cache management utilities
async function cleanupCache() {
    const cacheNames = await caches.keys();
    const oldCaches = cacheNames.filter(name => name !== CACHE_NAME);
    
    return Promise.all(
        oldCaches.map(name => caches.delete(name))
    );
}

// Periodic cache cleanup
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
    
    if (event.data && event.data.type === 'CLEANUP_CACHE') {
        event.waitUntil(cleanupCache());
    }
});

console.log('Service Worker loaded successfully');

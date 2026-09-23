/* NITRO service worker
   The app is entirely static and entirely client-side, so it can run
   with no network at all — which is the point on an e-ink phone in a
   gym with no signal.

   Strategy:
     shell   precached on install, served cache-first
     pages   stale-while-revalidate, so a launch is instant and the
             next launch picks up whatever was pushed since
     fonts   cache-first with a network fill; the CSS declares real
             fallback stacks, so a cold offline start still renders
*/

const VERSION    = 'nitro-v3';
const SHELL      = 'nitro-shell-' + VERSION;
const RUNTIME    = 'nitro-runtime-' + VERSION;
const FONT_HOSTS = ['https://fonts.googleapis.com', 'https://fonts.gstatic.com'];

const SHELL_URLS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './nav-kit.css',
  './nav-kit.js',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon-32.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(SHELL)
      // addAll is atomic: one 404 would leave the app uncached, so add
      // each entry on its own and let a missing optional file slide.
      .then(cache => Promise.all(
        SHELL_URLS.map(url => cache.add(url).catch(() => null))
      ))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== SHELL && k !== RUNTIME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

function isFont(url) {
  return FONT_HOSTS.some(host => url.startsWith(host));
}

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = req.url;
  const sameOrigin = url.startsWith(self.registration.scope) ||
                     new URL(url).origin === self.location.origin;

  // Navigations: serve the cached page immediately, refresh it behind you.
  if (req.mode === 'navigate') {
    event.respondWith(
      caches.open(SHELL).then(cache =>
        cache.match('./index.html').then(cached => {
          const network = fetch(req)
            .then(res => {
              if (res && res.ok) cache.put('./index.html', res.clone());
              return res;
            })
            .catch(() => cached);
          return cached || network;
        })
      )
    );
    return;
  }

  // Fonts: cache-first. Cross-origin responses come back opaque, which is
  // fine for font files — they are only ever handed to the renderer.
  if (isFont(url)) {
    event.respondWith(
      caches.open(RUNTIME).then(cache =>
        cache.match(req).then(cached =>
          cached || fetch(req).then(res => {
            cache.put(req, res.clone());
            return res;
          }).catch(() => cached)
        )
      )
    );
    return;
  }

  if (!sameOrigin) return;

  // Everything else we own: cache-first, fill on miss.
  event.respondWith(
    caches.match(req).then(cached =>
      cached || fetch(req).then(res => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(RUNTIME).then(cache => cache.put(req, copy));
        }
        return res;
      })
    )
  );
});

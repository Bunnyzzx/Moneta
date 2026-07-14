// Service worker do Moneta — cache para funcionamento offline
const CACHE = 'moneta-v3';
const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png'
];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  const req = e.request;

  // página: rede primeiro — toda abertura com internet já traz a versão
  // mais nova; o cache só entra quando estiver offline
  if (req.mode === 'navigate' || new URL(req.url).pathname.endsWith('/index.html')) {
    e.respondWith(
      fetch(req).then(resp => {
        const copy = resp.clone();
        caches.open(CACHE).then(c => c.put(req, copy)).catch(() => {});
        return resp;
      }).catch(() =>
        caches.match(req).then(hit => hit || caches.match('./index.html'))
      )
    );
    return;
  }

  // demais arquivos (ícones, manifest): cache primeiro, atualizando em segundo plano
  e.respondWith(
    caches.match(req).then(hit => {
      const rede = fetch(req).then(resp => {
        caches.open(CACHE).then(c => c.put(req, resp.clone())).catch(() => {});
        return resp;
      }).catch(() => hit);
      return hit || rede;
    })
  );
});

# Componentes e Dependências de Terceiros (`docs/refs/componentes.md`)

Inventário observado em `frontend/public/index.html` e `frontend/public/admin.html` (2026-11-12):

| Nome | Versão | Onde aparece | Licença | Observação |
|---|---|---|---|---|
| **Vue 3** (`vue.global.prod.js` via unpkg) | `3.x` (`@3`) | `index.html` (L15), `admin.html` (L56) | MIT `[confirmar]` | Carregado via CDN sem versão exata fixada |
| **Tailwind CSS** (`cdn.tailwindcss.com`) | v3 Play CDN | `index.html` (L59), `admin.html` (L67) | MIT `[confirmar]` | Com supressão de `console.warn` |
| **Leaflet.js** (CSS + JS via unpkg) | `1.9.4` | `index.html` (L13-14) | BSD-2-Clause `[confirmar]` | Mapa interativo de postos |
| **Google Fonts — Public Sans** | `400;600;700;800` | `index.html` (L17), `admin.html` (L3) | OFL `[confirmar]` | Fonte principal |
| **Google Fonts — Material Symbols Outlined** | variável | `admin.html` (L3 e L4 — duplicado) | Apache-2.0 `[confirmar]` | Carregado 2x, usado 4x |

# Componentes e Dependências de Terceiros (`docs/refs/componentes.md`)

Inventário atualizado em 2026-11-12:

| Nome | Versão | Onde aparece | Licença | Observação |
|---|---|---|---|---|
| **Vue 3** (`vue.global.prod.js` via unpkg) | `3.x` (`@3`) | `index.html` (L15), `admin.html` (L56) | MIT `[confirmar]` | Carregado via CDN |
| **Tailwind CSS** (`cdn.tailwindcss.com`) | v3 Play CDN | `index.html` (L59), `admin.html` (L67) | MIT `[confirmar]` | Com supressão de `console.warn` |
| **Leaflet.js** (CSS + JS via unpkg) | `1.9.4` | `index.html` (L13-14) | BSD-2-Clause `[confirmar]` | Mapa interativo de postos |
| **Google Fonts — Public Sans** | `400;600;700;800` | `index.html` (L17), `admin.html` (L3) | OFL `[confirmar]` | Fonte principal |
| **Phosphor Icons Web** (`@phosphor-icons/web` via unpkg) | `2.1.1` (`bold` + `duotone`) | `index.html` (L20-21), `admin.html` (L3) | MIT `[confirmar]` | Substituiu `Material Symbols Outlined` e ícones genéricos |

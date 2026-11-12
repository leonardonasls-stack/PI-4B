# Ficha Atual de Escolhas (`P-16` — Modo Edição)

Valores **observados** no código em 2026-11-12. O usuário decidirá o que fica `mantido`, `ajustar` ou `trocar` após o diagnóstico (`M-3`).

## 1. Tipografia
- **Família principal:** `Public Sans` (Google Fonts) — Status: `observado`
- **Pesos carregados:** `400`, `600`, `700`, `800` — Status: `observado`
- **Fallback:** padrão do navegador (`sans-serif` implícito, não declarado no `fontFamily` do `tailwind.config`) — Status: `observado`
- **Escala:** tokens MD3 (`display-lg` 48px até `label-sm` 12px) misturados com classes utilitárias (`text-xs`, `text-sm`, `text-base`) — Status: `observado`
- **Medida de linha:** `max-w-2xl` / `max-w-4xl` em textos longos do portal — Status: `observado`

## 2. Disposição
- **Container:** `max-w-7xl` (`index.html`) / `max-w-[1280px]` (`admin.html`) — Status: `observado`
- **Grid / Layout:** Portal com barra fixa dupla (`h-8` + `h-16`), hero de busca, área principal (lista de postos + mapa Leaflet), tabelas do PNI e rodapé; Admin com header fixo (`h-16`), seção Bot OSM, seção Tabela de Postos, modais de cadastro/ajuda/docs/feedback e rodapé escuro — Status: `observado`
- **Comportamento mobile:** Portal com `flex-col sm:flex-row` e nav visível; Admin oculta `<nav class="hidden md:flex">` sem menu alternativo — Status: `observado`

## 3. Itens e Componentes
- **Cartões:** Cards brancos com `rounded-xl` / `rounded-2xl`, `shadow-sm`, bordas `slate-200` — Status: `observado`
- **Botões:** Estilos mistos (`bg-primary`, `bg-emerald-600`, `bg-emerald-700`, `bg-slate-800`, `bg-rose-600/20`) — Status: `observado`
- **Ícones:** 56 SVGs inline no portal; 30 SVGs inline + 4 `Material Symbols Outlined` no admin — Status: `observado`
- **Formulários:** Inputs nativos estilizados com Tailwind (`rounded-xl`, `border`) — Status: `observado`
- **Modais:** Modais nativos controlados via JS/Vue (`z-50` a `z-[100]`) — Status: `observado`

## 4. Referências de Biblioteca
- **Base:** HTML5 + Tailwind CSS CDN + Vue 3 CDN (sem biblioteca de componentes externa como shadcn/coss ui) — Status: `observado`

# Mapa do Projeto (`M-1`) — Vacina Alagoas

Gerado em 2026-11-12 (somente leitura no código).

## 1. Árvore de Páginas e URLs
- `/` ou `/index.html` → [frontend/public/index.html](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/index.html) (Portal Público do Cidadão)
- `/admin` (rewrite Nginx) ou `/admin.html` → [frontend/public/admin.html](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/admin.html) (Painel Administrativo, protegido por verificação JWT)
- Proxy Nginx ([frontend/nginx.conf](file:///c:/Users/Luiz/Documents/Vacina/frontend/nginx.conf)): `/docs`, `/redoc`, `/openapi.json`, `/cities`, `/vaccination-points`, `/auth`, `/api`, `/admin/(enrichment|vaccination-points)` → `http://backend:8000`

## 2. Stack e Dependências
- **Frontend:** HTML5 + Vue 3 (`unpkg.com/vue@3/dist/vue.global.prod.js`), Tailwind CSS v3 Play CDN (`cdn.tailwindcss.com`), Leaflet `1.9.4` (`index.html` L13-14), Google Fonts `Public Sans` (`400;600;700;800`).
- **Dependência subutilizada/duplicada:** `Material Symbols Outlined` carregada **duas vezes** em `admin.html` (L3 e L4), usada apenas 4 vezes no DOM enquanto o restante usa SVGs inline (30 em `admin.html`, 56 em `index.html`).

## 3. Componentes, Estilos e Tokens
- `tailwind.config` inline em `index.html` (L60-239) e `admin.html` (L67) define paleta MD3 (`primary: #002530`, `secondary: #006c4a`, `surface: #f9f9ff`, etc.), escala tipográfica (`display-lg` a `label-sm`), `spacing` e `borderRadius`.
- **Divergência:** `admin.html` aplica `bg-slate-900/95`, `emerald-600`/`emerald-700` e `rose-600` no header, botões e modais, fugindo dos tokens `primary`/`surface`.

## 4. Formulários e Destinos
- **Busca pública (`index.html` L471+):** filtra postos via `GET /cities` (`index.html:1875`) e `GET /vaccination-points/{city_id}` (`index.html:1916`).
- **Login Admin (`index.html` L1589, L2707):** envia credenciais para `POST /auth/login` e verifica sessão em `GET /auth/verify` (`index.html:2634`, `admin.html:1031`).
- **Cadastro/Edição de Posto (`admin.html` L466, L1261, L1307):** cria/edita/exclui via `/admin/vaccination-points` e consulta CEP na API pública ViaCEP (`admin.html:1112`).
- **Mineração OSM (`admin.html` L881, L932):** pré-visualiza via `GET /admin/enrichment/preview-osm` e salva via `POST /admin/enrichment/confirm-save`.

## 5. Integrações
- Backend FastAPI + PostgreSQL 16 (intocados).
- Leaflet.js + tiles OpenStreetMap (`index.html`), links externos de rota no Google Maps, ViaCEP (`admin.html:1112`) e Overpass/OSM via backend.

## 6. Rastreamento
- Nenhum script de analytics, pixel ou tag de terceiros encontrado (`gtag`, `analytics`, `fbq` ausentes).

## 7. Edição de Conteúdo
- Conteúdo estático (orientações PNI, FAQ, termos) editado diretamente em `index.html`; dados dinâmicos de postos e vacinas geridos via `/admin.html`.

## 8. Mídia Existente
- Nenhuma tag `<img>`, `<video>` ou `<audio>` encontrada em `index.html` ou `admin.html` (apenas SVGs inline e tiles do Leaflet).

## 9. Pontos Frágeis Observados (Varredura Estática)
1. **HTML inválido em `index.html:3`:** `<html> lang="pt-BR">` com fechamento prematuro da tag `<html>`.
2. **Foco por teclado ausente no Admin (`admin.html`):** `0` ocorrências de `focus-visible:` e `10` de `outline-none` (contra `23` `focus-visible:` em `index.html`).
3. **Navegação mobile ausente no Admin (`admin.html:92`):** `<nav class="hidden md:flex">` oculta todos os links de navegação abaixo de `768px` sem menu alternativo.
4. **Inconsistência de tema:** `admin.html` usa `slate-900`/`emerald-600`/`rose-600` (58 `bg-slate-*`, 71 `emerald-*`) em vez dos tokens `primary` (`#002530`) e `surface` do portal.
5. **Escala `borderRadius` conflitante:** `tailwind.config` define `full: 0.75rem`, sobrescrevendo o `rounded-full` padrão do Tailwind.
6. **Scrollbar oculta no portal (`index.html:41-43`):** `::-webkit-scrollbar { display: none; }` vs scrollbar de `8px` no admin.
7. **Movimento reduzido (`prefers-reduced-motion`):** `0` ocorrências em ambos os arquivos (`scroll-behavior: smooth`, `animate-pulse`, `hover:scale-*` sem fallback).
8. **Tamanhos de fonte fora da escala:** `21` ocorrências de `text-[*px]` em `index.html` e `17` em `admin.html`.


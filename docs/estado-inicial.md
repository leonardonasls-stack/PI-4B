# Estado Inicial — Vacina Alagoas

- **Data de registro:** 2026-11-12
- **Pasta / Repositório:** `c:/Users/Luiz/Documents/Vacina`
- **Branch de trabalho:** `melhoria/m2-coesao-portal-admin` (a partir de `luiz`)
- **Tag de snapshot:** `snapshot-pre-coesao-20261112`
- **Tipo de intervenção:** M2 — Polimento visual e consistência (frontend)
- **Stack observada:**
  - Frontend: HTML5, Vue 3 (CDN), Tailwind CSS (CDN com tokens Material Design 3), Leaflet.js 1.9.4, Public Sans (Google Fonts), servido via Nginx (`frontend/public/index.html`, `frontend/public/admin.html`, `frontend/nginx.conf`)
  - Backend (intocado): FastAPI (Python 3.12+ assíncrono) + PostgreSQL 16
- **Ambiente de execução / teste:** Docker Compose local (Frontend `:3005`, Backend `:8085`, PostgreSQL `:5435`). Não há publicação em produção no momento.
- **Como publicar / reverter:** Apenas local por enquanto (`docker compose up -d --build`). Reversão imediata via `git checkout luiz` ou `git reset --hard snapshot-pre-coesao-20261112`.
- **Responsável / Aprovador:** Usuário (Luiz)

## O que NÃO PODE MUDAR

1. **Backend, banco e contratos REST intocados:** nenhuma alteração em `backend/`, `sql/` ou nos contratos JSON (`/cities`, `/vaccination-points/{city_id}`, `/auth/login`, `/admin/enrichment`, `/admin/vaccination-points`).
2. **Funcionalidades críticas:**
   - Cálculo de distância geodésica (Haversine) e botão "Meu GPS".
   - Mapa Leaflet com marcadores clicáveis e link de rota no Google Maps.
   - Autenticação JWT (incluindo guarda de sessão em `admin.html`) e CRUD completo de postos no painel administrativo.
   - Bot de mineração OSM / Overpass e exportação CSV/GeoJSON.
3. **Rotas / URLs:** `/`, `/index.html`, `/admin`, `/admin.html`.
4. **Dados oficiais:** nomes reais de postos, bairros e catálogo de vacinas de Alagoas.
5. **Identidade base e acessibilidade:** paleta baseada em Azul Petróleo (`#002530`) e conformidade WCAG 2.1 (AA/AAA).


# Mapa do Projeto — Vacina Alagoas

*Produzido em 03/11/2026 segundo o protocolo M-1.*

---

## 1. Árvore de Páginas e URLs
### Frontend (Servido via Nginx / HTTP estático na porta 3005)
- `/` ou `/index.html`: Portal do Cidadão (consulta pública, busca por município, cálculo GPS Haversine, mapa Leaflet interativo e orientações).
- `/admin.html`: Painel Administrativo de Gestão (autenticação JWT, KPIs, bot de mineração OpenStreetMap, formulário de cadastro manual de postos e auditoria CRUD).

### Backend RESTful (FastAPI na porta 8085 / Prefixo `/api/v1` e rotas diretas)
- `GET /cities`: Retorna array de cidades atendidas (`id`, `name`).
- `GET /vaccination-points/{city_id}`: Retorna postos da cidade selecionada com endereço, coordenadas e vacinas vinculadas.
- `POST /vaccination-points`: Cadastro de novo posto.
- `POST /auth/login`: Autenticação administrativa OAuth2 com geração de token JWT Bearer.
- `POST /admin/enrichment/mine/{city_name}`: Disparo do robô minerador Overpass API para buscar postos no OpenStreetMap.
- `POST /admin/vaccination-points`: Inserção/efetivação de postos minerados ou manuais no PostgreSQL.
- `/docs`: Swagger UI da API.
- `/redoc`: Documentação ReDoc da API.

---

## 2. Stack, Dependências e O Que Está Sem Uso Aparente
- **Frontend:**
  - Tailwind CSS 3.x via CDN: Ativo e gerando classes utilitárias inline.
  - Leaflet.js 1.9.4 via CDN: Ativo para renderização de mapa.
  - Material Symbols Outlined (Google Fonts): **Superutilizado**. Centenas de ícones foram inseridos de forma decorativa sem significado semântico (típico de saídas de IA).
  - Jinja2: Declarado em `backend/requirements.txt` (linha 13), mas não utilizado diretamente para renderizar HTML no backend (o frontend é 100% SPA estático servido por Nginx).
- **Backend:**
  - FastAPI 0.110+, SQLAlchemy 2.0 assíncrono, asyncpg, psycopg2-binary, passlib, python-jose, python-multipart, requests, httpx, pytest.

---

## 3. Componentes, Estilos e Tokens
- **Tokens de Estilo:**
  - Definidos em `<script id="tailwind-config">` em `frontend/public/index.html` (linhas 57-110) e `frontend/public/admin.html` (linhas 4-5).
  - Seguem nomenclatura Material Design 3 (`primary`, `on-primary`, `surface-container-low`, etc.).
- **Componentes Recorrentes:**
  - *Hero Card com Busca Flutuante* (`index.html:342-530`).
  - *Bento Grid de Apoio* (`index.html:813-980`).
  - *Cards de Posto de Saúde* (`index.html:745-790`).
  - *KPI Stat Cards* (`admin.html:38-95`).
  - *Tabela de Mineração OSM* (`admin.html:232-370`).

---

## 4. Formulários e Para Onde Enviam
1. **Filtro de Cidades e Busca por Bairro (`index.html:425-500`):**
   - Não submete formulário tradicional (`preventDefault`).
   - Dispara requisição assíncrona `fetch("http://localhost:8085/vaccination-points/" + cityId)` (`index.html:1299`).
2. **Formulário de Login Administrativo (`admin.html:144-165`):**
   - Dispara `fetch("http://localhost:8085/auth/login")` com `FormData` (`admin.html:921`).
   - Armazena token em `localStorage.setItem("access_token", token)`.
3. **Formulário de Cadastro Manual de Postos (`admin.html:385-505`):**
   - Dispara `fetch("http://localhost:8085/admin/vaccination-points")` com headers `Authorization: Bearer <token>` (`admin.html:1015`).

---

## 5. Integrações
- **OpenStreetMap (Overpass API / Nominatim):** Integrado via backend em `backend/src/core/services/enrichment_service.py` e acionado via `admin.html:963`.
- **Google Maps:** Link dinâmico gerado em cada card de posto (`index.html:1388`) com URL:  
  `https://www.google.com/maps/dir/?api=1&destination=LAT,LONG`.
- **Leaflet OpenStreetMap Tiles:** Tile layer em `https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png`.

---

## 6. Rastreamento e Analytics
- Nenhum pixel de terceiros (Google Analytics, Meta Pixel) instalado no momento.

---

## 7. Como o Conteúdo é Editado
- Postos, cidades e vacinas são mantidos via banco PostgreSQL através do painel `admin.html` ou scripts `sql/init.sql` e `sql/seed.sql`.
- Textos estáticos institucionais estão gravados diretamente nos arquivos HTML.

---

## 8. Mídia Existente
- Nenhuma imagem rasterizada pesada (PNG/JPEG) no repositório; apenas SVGs inline utilitários no HTML e os tiles carregados sob demanda pelo Leaflet.

---

## 9. Pontos Frágeis Identificados (Arquivos e Linhas)
1. **`API_URL` Hardcoded (`index.html:1168` e `admin.html:877`):**
   - Definido como `const API_URL = "http://localhost:8085";`. Funciona localmente, mas não é dinâmico se a porta mudar.
2. **Poluição Visual com Badges e Ícones Artificiais (`index.html:360-369` e `index.html:401-410`):**
   - Selo `verified` com *"Rede Oficial de Vacinação • SESAU Alagoas"* e bloco flutuante de *"Campanha Ativa"* criam dispersão de foco e aspecto de template não-humano.
3. **Distribuição Fragmentada no Hero (`index.html:371-415`):**
   - O título principal e o texto de apoio dividem espaço com um card de gripe desconexo em colunas assimétricas que confundem a navegação no mobile e desktop.
4. **Acúmulo de Chips e Tags nos Cartões (`index.html:750-770`):**
   - Cada posto exibe uma sequência desordenada de tags de vacinas, empurrando o botão de rota para fora da área visual imediata.
5. **Dashboard Administrativo com Densidade Exagerada (`admin.html:38-95`):**
   - 4 KPI cards empilhados com ícones aleatórios (`monitoring`, `local_hospital`, `verified_user`, `speed`) sem métricas dinâmicas reais vinculadas à API.


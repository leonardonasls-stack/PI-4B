# Estado Inicial do Projeto — Vacina Alagoas

**Data do Snapshot:** 03/11/2026  
**Tag Git:** `snapshot-pre-melhoria-m2`  
**Branch de Trabalho:** `luiz`  
**Tipo de Intervenção:** M2 (Polimento Visual, Acabamento e Anti-Cara-de-IA com P-13)

---

## 1. Identificação do Projeto e Acessos
- **Projeto:** Vacina Alagoas — Consulta Pública e Gestão de Postos de Vacinação
- **Pasta Local:** `C:\Users\Luiz\Documents\Vacina`
- **Stack Tecnológica:**
  - **Backend:** FastAPI (Python 3.12+ / asyncpg / SQLAlchemy 2.0 assíncrono / Uvicorn).
  - **Banco de Dados:** PostgreSQL 16 com volume persistente local.
  - **Frontend:** HTML5 semântico, Tailwind CSS, Leaflet.js e JavaScript Vanilla, servido via Nginx Alpine.
  - **Conteinerização:** Docker Compose gerenciando `vacinacao_pg_db`, `vacinacao_backend_api` e `vacinacao_frontend_web`.
- **Hospedagem / Ambientes:**
  - Ambiente local ativo via Docker:
    - Frontend: `http://localhost:3005`
    - Painel Administrativo: `http://localhost:3005/admin.html`
    - API FastAPI / Swagger: `http://localhost:8085` / `http://localhost:8085/docs`
    - Banco PostgreSQL: porta `5435`
- **Quem Mantém:** Luiz / Leonardo Nascimento (Projeto Integrador IV-B).
- **Quem Aprova:** Luiz e equipe de avaliação acadêmica.
- **Prazo:** Até Dezembro de 2026.
- **Backup Existente:** Scripts DDL e DML versionados em `sql/init.sql` e `sql/seed.sql`.

---

## 2. O Que NÃO Pode Mudar (Regras Intocáveis)
1. **Funcionalidades e Integrações do Sistema:**
   - Consulta pública de municípios e bairros (`/cities`, `/vaccination-points/{city_id}`).
   - Módulo de geolocalização com cálculo Haversine e ordenação por proximidade ("Meu GPS").
   - Mapa interativo Leaflet com renderização dinâmica de marcadores de postos de saúde.
   - Integração com Google Maps para traçar rotas externas.
   - Painel administrativo (`/admin.html`), fluxo de login OAuth2/JWT e módulo de enriquecimento de dados via OpenStreetMap (Overpass API).
2. **Dados e Conteúdo Oficial:**
   - Nomes de postos cadastrados, endereços verídicos de Maceió e Arapiraca, e catálogo do SUS.
3. **Diretrizes de Acessibilidade e Identidade Base:**
   - Paleta institucional básica com conformidade WCAG 2.1 (AA/AAA) com Azul Petróleo e suporte a alto contraste.


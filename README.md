# Vacina Alagoas — Consulta Pública e Gestão de Postos de Vacinação

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Vue.js](https://img.shields.io/badge/Vue.js-3.x-4FC08D.svg?logo=vuedotjs&logoColor=white)](https://vuejs.org/)
[![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![WCAG 2.1 AA](https://img.shields.io/badge/WCAG%202.1-AA-success.svg)](https://www.w3.org/WAI/standards-guidelines/wcag/)

Plataforma unificada para localização geográfica, consulta pública e administração de postos de vacinação no estado de **Alagoas** (foco em **Maceió** e **Arapiraca**). O projeto foi concebido para simplificar o acesso da população às salas de vacina ativas do SUS e prover aos gestores ferramentas para auditoria, cadastro e integração de dados territoriais.

---

## Recursos Principais

### Consulta Pública (Cidadão)

- **Busca Multi-critério em Tempo Real:** Filtre unidades de saúde por município, bairro, logradouro, CEP ou tipo de imunobiológico em estoque.
- **Geolocalização "Meu GPS":** Detecção da posição do usuário no navegador com cálculo de distância (Fórmula de Haversine) e ordenação por proximidade.
- **Mapa Interativo (Leaflet / OpenStreetMap):** Visualização de marcadores dinâmicos, enquadramento automático de raio de cobertura e traçado de rotas ponto a ponto no Google Maps.
- **Acessibilidade e Usabilidade:** Interface construída com base nas diretrizes WCAG 2.1 (AA), contrastes adequados, navegação por teclado e semântica institucional limpa.
- **Canais de Apoio:** Acesso rápido ao Disque Saúde (136), calendário de vacinas por idade e fase da vida e orientações para grupos prioritários.

### Gestão e Auditoria (Painel Administrativo)

- **CRUD Completo de Unidades:** Inclusão, edição cadastral, detalhamento e exclusão lógica de postos de saúde com proteção via JWT (OAuth2 Bearer).
- **Normalização Granular de Endereços:** Separação precisa de CEP, Município, Bairro, Logradouro e Número predial para conferência e integridade cadastral.
- **Autocompletar por CEP (ViaCEP):** Preenchimento automático de logradouro e bairro ao informar o código postal da unidade.
- **Bot de Enriquecimento Territorial (OpenStreetMap / Overpass API):** Mineração de dados públicos de unidades de saúde com fluxo seguro de pré-visualização antes da confirmação e persistência no banco.
- **Exportação de Dados:** Download de relatórios tabulares em CSV ou camadas espaciais em GeoJSON para uso em SIG e epidemiologia.
- **Proteção contra Força Bruta:** Middleware de limitação de taxa (_Rate Limiting_) para mitigar tentativas abusivas nos endpoints sensíveis.

---

## Arquitetura da Solução

O sistema é dividido em três serviços conteinerizados via Docker, garantindo isolamento e reprodutibilidade:

```
                            ┌───────────────────────────────────┐
                            │    Navegador do Usuário / Cidadão │
                            └─────────────────┬─────────────────┘
                                              │
                   ┌──────────────────────────┴──────────────────────────┐
                   │                                                     │
         HTTP (Porta 3005)                                     REST JSON (Porta 8085)
                   │                                                     │
                   ▼                                                     ▼
      ┌─────────────────────────┐                           ┌─────────────────────────┐
      │     Frontend Nginx      │                           │     Backend FastAPI     │
      │ (vacinacao_frontend_web)│                           │ (vacinacao_backend_api) │
      │                         │                           │                         │
      │ • Vue 3 (CDN Reativo)   │                           │ • /cities               │
      │ • Leaflet & Tailwind CSS│                           │ • /vaccination-points   │
      │ • Portal Público & Admin│                           │ • /auth (OAuth2 JWT)    │
      └─────────────────────────┘                           │ • /enrichment (OSM Bot) │
                                                            └────────────┬────────────┘
                                                                         │
                                                                 Asyncpg (Porta 5435)
                                                                         │
                                                                         ▼
                                                            ┌─────────────────────────┐
                                                            │      PostgreSQL 16      │
                                                            │   (vacinacao_pg_db)     │
                                                            │                         │
                                                            │ • states & cities       │
                                                            │ • vaccination_points    │
                                                            │ • vaccines & relations  │
                                                            │ • admin_users           │
                                                            └─────────────────────────┘
```

### Mapeamento de Portas e Serviços

| Serviço            | Contêiner                | Porta Host | Porta Interna | Descrição                                                    |
| :----------------- | :----------------------- | :--------: | :-----------: | :----------------------------------------------------------- |
| **Frontend**       | `vacinacao_frontend_web` |   `3005`   |     `80`      | Interface pública e painel administrativo servidos via Nginx |
| **Backend**        | `vacinacao_backend_api`  |   `8085`   |    `8000`     | API assíncrona FastAPI, documentação Swagger e ReDoc         |
| **Banco de Dados** | `vacinacao_pg_db`        |   `5435`   |    `5432`     | PostgreSQL 16 com volume persistente e scripts de seed       |

---

## Como Executar

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/) instalados.

### 1. Clonar e Configurar Variáveis de Ambiente

```bash
git clone https://github.com/leonardonasls-stack/PI-4B.git
cd PI-4B
cp .env.example .env
```

> [!NOTE]
> O arquivo `.env.example` já inclui configurações seguras para execução em ambiente de desenvolvimento local.

### 2. Subir os Contêineres

```bash
docker compose up -d --build
```

O Docker Compose aguardará a saúde do banco de dados (`vacinacao_pg_db`) através do _healthcheck_, executará as migrações/seed e inicializará o backend e o frontend automaticamente.

### 3. Acessar os Serviços

- **Portal Público do Cidadão:** [http://localhost:3005](http://localhost:3005)
- **Painel Administrativo:** [http://localhost:3005/admin.html](http://localhost:3005/admin.html) (ou rota simplificada [http://localhost:3005/admin](http://localhost:3005/admin))
  - **Usuário Padrão:** `admin`
  - **Senha Padrão:** `admin123`
- **Swagger OpenAPI:** [http://localhost:3005/docs](http://localhost:3005/docs) (via proxy Nginx) ou [http://localhost:8085/docs](http://localhost:8085/docs) (direto na API)
- **ReDoc:** [http://localhost:3005/redoc](http://localhost:3005/redoc) ou [http://localhost:8085/redoc](http://localhost:8085/redoc)
- **OpenAPI JSON Spec:** [http://localhost:3005/openapi.json](http://localhost:3005/openapi.json) ou [http://localhost:8085/openapi.json](http://localhost:8085/openapi.json)

---

## Deploy em Produção (Dokploy)

O projeto possui suporte pronto para deploy via **Dokploy** usando o arquivo [`docker-compose.dokploy.yml`](docker-compose.dokploy.yml), que sobe o PostgreSQL 16 (`db`) e a aplicação unificada (`app` — FastAPI + Frontend estático) na porta `8000`.

### 1. Configurar o Compose no Dokploy

1. Crie um novo serviço **Compose** no Dokploy conectado ao repositório.
2. Em **Compose Path**, informe `docker-compose.dokploy.yml`.
3. Na aba **Environment**, defina as variáveis de produção:
   - `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`
   - `SECRET_KEY` (gere uma chave segura com `python -c "import secrets; print(secrets.token_hex(32))"`)
   - `ADMIN_USERNAME`, `ADMIN_PASSWORD`
4. Na aba **Domains**, aponte o domínio para o serviço **`app`** na **Container Port `8000`**.

### 2. Inicialização Automática do Banco

Ao iniciar o stack, o banco de dados é construído e populado automaticamente:
- O contêiner `db` executa [`sql/init.sql`](sql/init.sql) e [`sql/seed.sql`](sql/seed.sql) na primeira inicialização.
- O backend executa `init_database()` no startup (`lifespan`), garantindo a criação das tabelas, constraints e seed de forma idempotente.

---

## Execução Local (Sem Docker)

Caso prefira executar sem contêineres:

### 1. Banco de Dados

Certifique-se de ter uma instância do PostgreSQL 16 ativa e execute:

```bash
createdb -U postgres vacinacao_al
psql -U postgres -d vacinacao_al -f sql/init.sql
psql -U postgres -d vacinacao_al -f sql/seed.sql
```

### 2. Backend (FastAPI)

```bash
cd backend
python -m venv venv

# Windows
.\venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt
uvicorn src.app.main:app --reload --port 8085
```

### 3. Frontend

Sirva a pasta `frontend/public` com um servidor estático:

```bash
cd frontend/public
python -m http.server 3005
```

---

## Contratos da API RESTful

A API adota respostas padronizadas em JSON e códigos de status HTTP semânticos:

### Municípios (`/cities`)

- `GET /cities` — Retorna os municípios monitorados com id e nome.
- `GET /cities/{id}` — Retorna os detalhes de um município específico.

### Postos de Vacinação (`/vaccination-points`)

- `GET /vaccination-points/{city_id}` — Lista todos os postos de um município com coordenadas e lista de imunobiológicos.
- `GET /vaccination-points/detail/{point_id}` — Retorna os dados completos de um único posto de saúde.
- `POST /vaccination-points` — Cadastra um novo posto de vacinação. _(Requer autenticação JWT)_
- `PUT /vaccination-points/{point_id}` — Atualiza os dados de um posto existente. _(Requer autenticação JWT)_
- `DELETE /vaccination-points/{point_id}` — Remove um posto de saúde do cadastro. _(Requer autenticação JWT)_

### Autenticação e Sessão Administrativa (`/auth`)

- `POST /auth/login` — Autentica as credenciais do gestor e retorna o token `Bearer` no formato JWT. Sujeito a limitação de taxa (máximo de 5 tentativas consecutivas por minuto por IP com resposta `429 Too Many Requests`).
- `GET /auth/verify` — Valida ativamente a autenticidade e validade do token JWT bearer. Utilizado na proteção de rotas e verificação de expiração de sessão.

### Mineração de Dados (`/admin/enrichment`)

- `GET /admin/enrichment/preview-osm` — Consulta a API pública do OpenStreetMap via Overpass API e exibe postos descobertos para conferência (suporta parâmetro `escopo`: `alagoas`, `maceio` ou `arapiraca`). _(Requer JWT)_
- `POST /admin/enrichment/confirm-save` — Persiste no banco PostgreSQL apenas as unidades selecionadas pelo administrador, vinculando as vacinas de rotina e evitando duplicidades (`ON CONFLICT`). _(Requer JWT)_
- `POST /admin/enrichment/sync-osm` — Endpoint legado para sincronização direta do estado. _(Requer JWT)_

---

## Modelo de Dados

O banco relacional modela a integridade referencial com chaves primárias, estrangeiras e restrições de unicidade:

```
┌─────────────────┐       ┌─────────────────┐       ┌───────────────────────────┐
│     states      │ 1   N │     cities      │ 1   N │    vaccination_points     │
├─────────────────┤◄─────►├─────────────────┤◄─────►├───────────────────────────┤
│ id (PK)         │       │ id (PK)         │       │ id (PK)                   │
│ name            │       │ state_id (FK)   │       │ city_id (FK)              │
│ uf (CHAR 2)     │       │ name            │       │ name (UNIQUE c/ city)     │
└─────────────────┘       └─────────────────┘       │ neighborhood              │
                                                    │ logradouro                │
┌─────────────────┐       ┌─────────────────┐       │ number                    │
│   admin_users   │       │    vaccines     │       │ cep                       │
├─────────────────┤       ├─────────────────┤       │ address (legado/completo) │
│ id (PK)         │       │ id (PK)         │       │ latitude                  │
│ username (UQ)   │       │ name (UNIQUE)   │       │ longitude                 │
│ hashed_password │       │ description     │       │ created_at                │
│ created_at      │       └────────┬────────┘       └─────────────┬─────────────┘
└─────────────────┘                │ 1                            │ 1
                                   │                              │
                                   │ N              ┌─────────────▼─────────────┐
                                   └───────────────►│      point_vaccines       │
                                                    ├───────────────────────────┤
                                                    │ point_id (PK, FK)         │
                                                    │ vaccine_id (PK, FK)       │
                                                    └───────────────────────────┘
```

---

## Testes Automatizados e Integração Contínua (CI)

A suíte de testes assíncrona valida a conformidade dos contratos da API, integridade de dados e regras de autorização utilizando `pytest` e `httpx`:

```bash
cd backend
python -m pytest tests/ -v
```

Cenários cobertos pelos testes (`backend/tests/api/test_endpoints.py`):

- **Municípios (`/cities`):** Integridade dos contratos, retorno de `Maceió` e `Arapiraca` (`200 OK`) e tratamento de IDs inexistentes (`404 Not Found`) ou inválidos (`422 Unprocessable Entity`).
- **Postos de Vacinação (`/vaccination-points`):** Serialização correta por cidade (`GET /vaccination-points/{city_id}`) e consulta unitária por ID (`GET /vaccination-points/detail/{point_id}`).
- **Ciclo Completo de CRUD:** Criação (`POST`), atualização cadastral (`PUT`), leitura e remoção (`DELETE`) de postos de vacinação com verificação de cascata referencial.
- **Segurança e Autorização:** Autenticação via JWT, expiração de tokens e bloqueio estrito de acesso sem credenciais válidas (`401 Unauthorized`).

O repositório também inclui pipeline de Integração Contínua no GitHub Actions ([`.github/workflows/ci.yml`](.github/workflows/ci.yml)) que valida os testes com PostgreSQL de serviço e a integridade de build do Docker Compose em cada push ou pull request na branch `main`.

---

## Documentação Técnica Aprofundada

Para especificações detalhadas de arquitetura, requisitos e relatórios de conformidade, consulte o diretório [docs/](docs/README.md) e o arquivo de auditoria raiz:

- [**Auditoria Técnica CRUD (100% Conforme)**](AUDITORIA_CRUD.md) — Relatório formal de conformidade com as operações Create, Read, Update e Delete no backend, frontend e testes.
- [**Relatório Técnico de Implementação**](docs/relatorio-implementacao.md) — Visão detalhada de sprints, arquitetura, conformidade RESTful e entrega.
- [**Especificação da API RESTful**](docs/api.md) — Contratos JSON, parâmetros, respostas de erro e exemplos com `curl`.
- [**Documento de Arquitetura Técnica (TRD)**](docs/arquitetura.md) — Decisões de arquitetura, modelagem de dados, PostGIS e escalabilidade.
- [**Documento de Requisitos de Produto (PRD)**](docs/requisitos.md) — Casos de uso (RF-01 a RF-05, RNF-01 a RNF-04) e regras de negócio.
- [**Diretrizes de Acessibilidade e Design (WCAG)**](docs/design-wcag.md) — Padrões de acessibilidade WCAG 2.1 AA, contraste e navegação.
- [**Manual de Design e Polimento Institucional**](docs/anti-ia-polimento.md) — Princípios de identidade visual sóbria, SVGs nativos e padrões de design limpo.
- [**Histórico de Melhorias e Decisões**](docs/historico-melhorias.md) — Linha do tempo de evolução técnica e registros de decisões arquiteturais.

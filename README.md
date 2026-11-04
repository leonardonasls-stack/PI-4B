# Vacina Alagoas — Consulta Pública e Gestão de Postos de Vacinação

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ED.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![WCAG 2.1 AA/AAA](https://img.shields.io/badge/WCAG%202.1-AA%20%2F%20AAA-success.svg)](https://www.w3.org/WAI/standards-guidelines/wcag/)

Plataforma completa de consulta pública, localização geográfica e administração de postos de vacinação no estado de **Alagoas** (com foco na capital **Maceió** e no agreste em **Arapiraca**), desenvolvida como projeto acadêmico da disciplina **Projeto Integrador IV-B**.

O sistema combina uma **API RESTful assíncrona** de alta performance em **FastAPI**, persistência relacional em **PostgreSQL 16**, interface web servida via **Nginx** com renderização e estilização em Tailwind CSS, suporte à geolocalização com cálculo de distância em tempo real (Fórmula de Haversine), mapas interativos com **Leaflet**, geração de rotas no **Google Maps** e módulo de auditoria com mineração de dados via **OpenStreetMap (Overpass API)** com fluxo de prévia e confirmação.

---

## Recursos Principais

### Para o Cidadão (Acesso Aberto e Anônimo)
- **Consulta Ágil por Município e Bairro:** Seleção de cidades atendidas (`Maceió`, `Arapiraca`) com busca instantânea por bairros e nomes de postos.
- **Geolocalização "Meu GPS":** Detecção sob demanda das coordenadas geográficas do usuário via navegador com cálculo dinâmico de distâncias e ordenação do posto mais próximo para o mais distante.
- **Mapa Interativo (Leaflet):** Visualização de marcadores com destaque automático ao focar ou selecionar unidades no mapa.
- **Integração com Google Maps:** Botão dedicado para traçar rotas de navegação ponto a ponto até a unidade de saúde selecionada.
- **Acessibilidade e WCAG 2.1 (AA / AAA):** Contraste calibrado (Paleta Azul Petróleo e Âmbar), tipografia escalável, suporte a leitores de tela e navegação por teclado.
- **Canais de Apoio Integrados:** Acesso rápido ao Disque Saúde (`136`) e calendários de campanhas vigentes.

### Para o Administrador (Acesso Autenticado)
- **Painel Administrativo Seguro:** Login protegido com JWT (JSON Web Tokens) e senhas criptografadas via `bcrypt`.
- **Cadastro Rápido de Postos:** Formulário com seleção de município, nome, endereço, coordenadas geográficas e vinculação de vacinas do catálogo oficial.
- **Bot de Mineração OpenStreetMap (OSM):**
  - **Pesquisa e Prévia:** O bot consulta a *Overpass API* e exibe uma tabela de prévia com os postos de saúde de Maceió encontrados sem gravá-los de imediato.
  - **Confirmação Manual:** O administrador seleciona quais unidades deseja efetivar no banco de dados.

---

## Arquitetura da Aplicação

O sistema foi estruturado seguindo o padrão de **Arquitetura em Camadas (Layered Architecture)**, o padrão **Repository** com isolamento do SQLAlchemy 2.0 assíncrono e separação de responsabilidades em microsserviços conteinerizados:

```text
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
        │  (vacinacao_frontend_web)│                          │ (vacinacao_backend_api) │
        │                         │                           │                         │
        │ • index.html (Cidadão)  │                           │ • /cities (RF-01, RF-02)│
        │ • admin.html (Painel)   │                           │ • /vaccination-points   │
        │ • Leaflet & Tailwind CSS│                           │ • /auth (OAuth2 JWT)    │
        └─────────────────────────┘                           │ • /admin/enrichment     │
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

---

## Mapeamento de Portas e Serviços

Para garantir execução simultânea sem conflitos com serviços já em execução no host, o ambiente utiliza portas customizadas:

| Serviço | Contêiner | Porta Host | Porta Contêiner | Finalidade |
| :--- | :--- | :---: | :---: | :--- |
| **Frontend Web** | `vacinacao_frontend_web` | `3005` | `80` | Interface do Cidadão e Painel Administrativo Nginx |
| **Backend REST** | `vacinacao_backend_api` | `8085` | `8000` | API FastAPI, Swagger e ReDoc |
| **Banco de Dados** | `vacinacao_pg_db` | `5435` | `5432` | PostgreSQL 16 com volume persistente |

---

## Como Executar

### Opção 1: Via Docker Compose (Recomendado)

#### Pré-requisitos
- [Docker Engine](https://docs.docker.com/engine/install/) e [Docker Compose](https://docs.docker.com/compose/) v2+.

#### 1. Configurar o ambiente
```bash
git clone https://github.com/LeonardoNasL/projeto-integrador-iv-b.git
cd projeto-integrador-iv-b
cp .env.example .env
```

#### 2. Subir os contêineres
```bash
docker compose up --build
```

O compose aguarda o banco estar pronto via *healthcheck*, executa o `sql/init.sql` e o `sql/seed.sql`, constrói a API e disponibiliza a aplicação imediatamente.

> [!TIP]
> Caso queira rodar em segundo plano, utilize `docker compose up -d`. Para verificar os logs de um serviço específico, use `docker compose logs -f backend`.

#### 3. URLs de Acesso
- **Portal Cidadão:** [http://localhost:3005](http://localhost:3005)
- **Painel Administrativo:** [http://localhost:3005/admin.html](http://localhost:3005/admin.html)
  - **Usuário:** `admin`
  - **Senha:** `admin123`
- **Documentação Interativa (Swagger UI):** [http://localhost:8085/docs](http://localhost:8085/docs)
- **Documentação ReDoc:** [http://localhost:8085/redoc](http://localhost:8085/redoc)

---

### Opção 2: Execução Local (Sem Docker)

#### 1. Banco de Dados
Tenha o PostgreSQL 16 rodando e crie a base:
```bash
createdb -U postgres vacinacao_al
psql -U postgres -d vacinacao_al -f sql/init.sql
psql -U postgres -d vacinacao_al -f sql/seed.sql
```

#### 2. Backend (FastAPI)
```bash
cd backend
python -m venv venv

# No Windows:
.\venv\Scripts\activate

# No Linux / macOS:
source venv/bin/activate

pip install -r requirements.txt
uvicorn src.app.main:app --reload --port 8000
```

#### 3. Frontend
Sirva os arquivos de `frontend/public` através do seu servidor estático preferido (Live Server no VS Code ou `python -m http.server 3000`).

---

## Contrato da API RESTful

A API segue os padrões RESTful com respostas em JSON e códigos de status HTTP semânticos:

### 1. Municípios (`cities`)
- **`GET /cities`**
  - **Status:** `200 OK`
  - **Retorno:** Array com identificador e nome das cidades cadastradas.
  ```json
  [
    { "id": 1, "name": "Maceió" },
    { "id": 2, "name": "Arapiraca" }
  ]
  ```

- **`GET /cities/{id}`**
  - **Status:** `200 OK`
  - **Retorno:** Detalhes da cidade com o estado associado.
  - **Erros:** `404 Not Found` (caso o ID não exista) e `422 Unprocessable Entity` (caso o ID não seja numérico).
  ```json
  {
    "id": 1,
    "name": "Maceió",
    "state": "Alagoas"
  }
  ```

### 2. Pontos de Vacinação (`vaccination-points`)
- **`GET /vaccination-points/{city_id}`**
  - **Status:** `200 OK`
  - **Retorno:** Postos de vacinação pertencentes à cidade informada, incluindo coordenadas geográficas e catálogo de vacinas disponíveis.
  ```json
  [
    {
      "id": 1,
      "name": "UBS Jacintinho (Dr. José Tenório de Albuquerque)",
      "neighborhood": "Jacintinho",
      "address": "Av. Cleto Campelo, s/n, Jacintinho",
      "latitude": -9.63842,
      "longitude": -35.71761,
      "vaccines": ["Influenza", "Covid-19 Bivalente", "Tríplice Viral", "Febre Amarela", "Hepatite B"]
    }
  ]
  ```

- **`POST /vaccination-points`** *(Requer autenticação JWT)*
  - **Status:** `201 Created`
  - **Payload:**
  ```json
  {
    "city_id": 1,
    "name": "USF Guaxuma",
    "neighborhood": "Guaxuma",
    "address": "Rua Principal, s/n",
    "latitude": -9.57530,
    "longitude": -35.67210,
    "vaccine_ids": [1, 2, 3]
  }
  ```

### 3. Autenticação Administrativa (`auth`)
- **`POST /auth/login`**
  - **Status:** `200 OK`
  - **Retorno:** Token Bearer no formato `application/x-www-form-urlencoded` ou JSON.
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsIn...",
    "token_type": "bearer"
  }
  ```

### 4. Bot de Enriquecimento OpenStreetMap (`admin/enrichment`)
- **`GET /admin/enrichment/preview-osm`** *(Requer JWT)*: Executa mineração na *Overpass API* e retorna prévia dos postos de saúde de Maceió.
- **`POST /admin/enrichment/confirm-save`** *(Requer JWT)*: Persiste no banco de dados apenas os postos validados pelo administrador, evitando duplicidades por nome e cidade.

---

## Modelo de Dados Relacional (PostgreSQL 16)

A modelagem de dados assegura integridade referencial com chaves estrangeiras, índices e restrições de unicidade:

```text
┌─────────────────┐       ┌─────────────────┐       ┌───────────────────────┐
│     states      │ 1   N │     cities      │ 1   N │  vaccination_points   │
├─────────────────┤◄─────►├─────────────────┤◄─────►├───────────────────────┤
│ id (PK)         │       │ id (PK)         │       │ id (PK)               │
│ name            │       │ state_id (FK)   │       │ city_id (FK)          │
│ uf (CHAR 2)     │       │ name            │       │ name (UNIQUE c/ city) │
└─────────────────┘       └─────────────────┘       │ neighborhood          │
                                                    │ address               │
┌─────────────────┐       ┌─────────────────┐       │ latitude              │
│   admin_users   │       │    vaccines     │       │ longitude             │
├─────────────────┤       ├─────────────────┤       │ created_at            │
│ id (PK)         │       │ id (PK)         │       └───────────┬───────────┘
│ username (UQ)   │       │ name (UNIQUE)   │                   │ 1
│ hashed_password │       │ description     │                   │
│ created_at      │       └────────┬────────┘                   │ N
└─────────────────┘                │ 1              ┌───────────▼───────────┐
                                   │                │    point_vaccines     │
                                   └───────────────►├───────────────────────┤
                                                  N │ point_id (PK, FK)     │
                                                    │ vaccine_id (PK, FK)   │
                                                    └───────────────────────┘
```

---

## Documentação do Projeto

Toda a documentação técnica, especificações e relatórios de auditoria foram organizados e estruturados no diretório [docs/](docs/README.md):

- 📘 [**Relatório Técnico de Implementação**](docs/relatorio-implementacao.md) — Relatório estruturado de melhorias, CRUD completo, polimento visual e testes.
- 📊 [**Relatório de Auditoria CRUD (100% Conforme)**](docs/auditoria-crud.md) — Matriz completa de persistência e validação técnica.
- 🔌 [**Documentação da API RESTful**](docs/api.md) — Especificação detalhada de rotas, contratos JSON e autenticação.
- 🏛️ [**Arquitetura Técnica (TRD)**](docs/arquitetura.md) — Modelagem física de banco, PostGIS, microsserviços e Docker.
- 📋 [**Requisitos de Produto (PRD)**](docs/requisitos.md) — Casos de uso, personas e regras de negócio da SESAU.
- ♿ [**Design System e Acessibilidade (WCAG)**](docs/design-wcag.md) — Diretrizes de inclusão, contraste e tokens visuais.
- 🎨 [**Manual de Design Humano (Anti-IA)**](docs/anti-ia-polimento.md) — Eliminação de artefatos visuais sintéticos e padrões de qualidade.
- 📜 [**Histórico de Melhorias**](docs/historico-melhorias.md) — Linha do tempo de commits e decisões de projeto.

---

## Estrutura de Diretórios do Projeto

```text
.
├── backend/
│   ├── src/
│   │   ├── api/v1/                  # Endpoints REST e roteadores modulares
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py          # Login e geração de JWT
│   │   │   │   ├── cities.py        # Endpoints /cities e /cities/{id}
│   │   │   │   ├── points.py        # Endpoints /vaccination-points
│   │   │   │   └── enrichment.py    # Rotas do Bot OSM (preview e confirmação)
│   │   │   └── api.py               # Agrupador do versionamento v1
│   │   ├── app/                     # Configurações de ambiente e instância FastAPI
│   │   ├── core/                    # Serviços de negócio e segurança
│   │   │   ├── security.py          # Validação JWT e Hashing Bcrypt
│   │   │   └── services/            # CityService, PointService, EnrichmentService
│   │   ├── database/                # Modelos SQLAlchemy e sessão assíncrona
│   │   └── schemas/                 # Schemas de entrada e saída Pydantic v2
│   ├── Dockerfile                   # Build conteinerizado da API Python
│   └── requirements.txt             # Dependências da aplicação backend
├── frontend/
│   ├── public/                      # Aplicação web estática
│   │   ├── index.html               # Portal público com mapa e busca por GPS
│   │   └── admin.html               # Painel administrativo e mineração OSM
│   ├── nginx.conf                   # Configurações do servidor HTTP Nginx
│   └── Dockerfile                   # Build do contêiner Nginx
├── sql/
│   ├── init.sql                     # Script DDL com tabelas, índices e FKs
│   └── seed.sql                     # Dados iniciais reais de Maceió e Arapiraca
├── docker-compose.yml               # Orquestrador dos contêineres db, backend e frontend
├── CHANGELOG.md                     # Histórico detalhado de commits e melhorias
└── README.md                        # Documentação técnica e guia da aplicação
```

---

## Testes Automatizados

O backend conta com suíte de testes utilizando `pytest` e `httpx`:

```bash
cd backend
pytest tests/ -v
```

Os testes cobrem:
- Validação dos status HTTP de `/cities` e `/cities/{id}` (sucesso, 404 e 422).
- Listagem e integridade do contrato JSON de `/vaccination-points/{city_id}`.
- Autenticação com credenciais corretas e bloqueio com credenciais inválidas.

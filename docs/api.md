# Documentação da API RESTful — Vacina Alagoas

Projeto Integrador IV-B · API REST em Python FastAPI · PostgreSQL 16 com Extensão PostGIS

---

## 1. Visão Geral

A API é **RESTful**, assíncrona, construída com **FastAPI** e conectada ao **PostgreSQL 16**. A plataforma atende a dois tipos de clientes:

- **Cidadão (Público / Não Autenticado):** Consulta de municípios, postos de saúde cadastrados e imunobiológicos disponíveis.
- **Administrador (Autenticado via JWT Bearer):** Gestão cadastral completa de postos de saúde (CRUD: Criação, Leitura, Atualização e Exclusão) e operações de enriquecimento geográfico via OpenStreetMap (OSM).

| Item | Valor |
| :--- | :--- |
| **URL Base Direta (FastAPI)** | `http://localhost:8085` |
| **URL Base Proxy (Nginx)** | `http://localhost:3005` |
| **Prefixo Versionado** | `/api/v1` (endpoints também disponíveis na raiz) |
| **Formato de Troca** | JSON (`application/json`) |
| **Autenticação** | Cabeçalho HTTP `Authorization: Bearer <token>` |
| **Swagger UI Interativo** | `http://localhost:3005/docs` ou `http://localhost:8085/docs` |
| **ReDoc Formal** | `http://localhost:3005/redoc` ou `http://localhost:8085/redoc` |
| **OpenAPI Spec 3.1** | `http://localhost:3005/openapi.json` |

---

## 2. Resumo da Matriz de Endpoints

| Método | Rota | Acesso | Descrição |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/login` | Público | Autenticação do gestor e geração do token JWT |
| `GET` | `/cities` | Público | Lista todos os municípios alagoanos atendidos |
| `GET` | `/cities/{id}` | Público | Detalhes cadastrais de um município específico |
| `GET` | `/vaccination-points/{city_id}` | Público | Lista os postos de vacinação de um município com vacinas |
| `GET` | `/vaccination-points/detail/{point_id}` | Público | Consulta unitária de um posto pelo seu ID |
| `POST` | `/vaccination-points` | Admin (JWT) | Cadastro manual de um novo posto de vacinação |
| `PUT` | `/vaccination-points/{point_id}` | Admin (JWT) | Atualização cadastral dos dados de um posto |
| `DELETE` | `/vaccination-points/{point_id}` | Admin (JWT) | Exclusão definitiva de um posto de vacinação |
| `GET` | `/admin/enrichment/preview-osm` | Admin (JWT) | Pré-visualização de postos minerados no OSM via Overpass API |
| `POST` | `/admin/enrichment/confirm-save` | Admin (JWT) | Gravação idempotente dos postos selecionados do OSM |

---

## 3. Autenticação Administrativa (OAuth2 Bearer JWT)

O fluxo de autenticação utiliza credenciais criptografadas via algoritmo **HS256**:

1. O administrador envia as credenciais para o endpoint `POST /auth/login`.
2. A API valida a senha utilizando hash seguro `bcrypt` e devolve um token JWT válido por **120 minutos**.
3. O cliente inclui o token em todas as requisições protegidas através do cabeçalho:

```http
Authorization: Bearer <seu_token_jwt_aqui>
```

Se o cabeçalho estiver ausente ou o token for inválido/expirado, o servidor retornará **HTTP 401 Unauthorized**.

---

## 4. Detalhamento dos Endpoints

### 4.1. Autenticação: `POST /auth/login`
- **Corpo:** Formulário `application/x-www-form-urlencoded`
  - `username` (string, obrigatório): Nome de usuário (padrão: `admin`)
  - `password` (string, obrigatório): Senha do gestor (padrão: `admin123`)
- **Resposta 200 OK:**
  ```json
  {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
  ```

---

### 4.2. Municípios: `GET /cities`
- **Parâmetros:** Nenhum
- **Resposta 200 OK:**
  ```json
  [
    { "id": 1, "name": "Maceió", "state_id": 1 },
    { "id": 2, "name": "Arapiraca", "state_id": 1 }
  ]
  ```

---

### 4.3. Postos por Município: `GET /vaccination-points/{city_id}`
- **Parâmetros de Rota:** `city_id` (inteiro)
- **Resposta 200 OK:**
  ```json
  [
    {
      "id": 1,
      "city_id": 1,
      "name": "USF Ponta Verde",
      "address": "Rua Eng. Mário de Gusmão, 450",
      "neighborhood": "Ponta Verde",
      "latitude": -9.6632,
      "longitude": -35.7042,
      "operating_hours": "Segunda a Sexta, 08h às 17h",
      "phone": "(82) 3315-1234",
      "is_active": true,
      "vaccines": ["Influenza", "COVID-19 Bivalente", "Tríplice Viral"]
    }
  ]
  ```

---

### 4.4. Leitura Unitária de Posto: `GET /vaccination-points/detail/{point_id}`
- **Parâmetros de Rota:** `point_id` (inteiro)
- **Resposta 200 OK:** Retorna o objeto completo do posto com vacinas vinculadas.
- **Resposta 404 Not Found:** `{"detail": "Ponto de vacinação não encontrado"}`.

---

### 4.5. Criação de Posto: `POST /vaccination-points`
- **Autenticação:** Requer Bearer Token
- **Corpo (JSON):**
  ```json
  {
    "city_id": 1,
    "name": "UBS Jacintinho II",
    "address": "Av. Cleto Campelo, 120",
    "neighborhood": "Jacintinho",
    "latitude": -9.6415,
    "longitude": -35.7258,
    "operating_hours": "07h às 16h",
    "phone": "(82) 3315-9988",
    "vaccine_ids": [1, 2, 4]
  }
  ```
- **Resposta 201 Created:** Retorna o posto criado com ID atribuído.

---

### 4.6. Atualização de Posto: `PUT /vaccination-points/{point_id}`
- **Autenticação:** Requer Bearer Token
- **Corpo (JSON - campos parciais suportados):**
  ```json
  {
    "name": "UBS Jacintinho II - Reformada",
    "phone": "(82) 3315-0000",
    "operating_hours": "08h às 18h",
    "vaccine_ids": [1, 2, 3, 5]
  }
  ```
- **Resposta 200 OK:** Retorna o registro do posto com os novos dados atualizados.

---

### 4.7. Exclusão de Posto: `DELETE /vaccination-points/{point_id}`
- **Autenticação:** Requer Bearer Token
- **Parâmetros de Rota:** `point_id` (inteiro)
- **Resposta 204 No Content:** Sucesso na exclusão (corpo vazio).
- **Resposta 404 Not Found:** `{"detail": "Ponto de vacinação não encontrado"}`.

---

### 4.8. Mineração OpenStreetMap (OSM): `GET /admin/enrichment/preview-osm`
- **Autenticação:** Requer Bearer Token
- **Parâmetros de Query:** `city_id` (inteiro)
- **Resposta 200 OK:**
  ```json
  {
    "city_id": 1,
    "total_found": 14,
    "points": [
      {
        "name": "Unidade de Saúde Dr. Hamilton Falcão",
        "latitude": -9.6712,
        "longitude": -35.7489,
        "address": "Av. Norma Pimentel",
        "neighborhood": "Benedito Bentes"
      }
    ]
  }
  ```

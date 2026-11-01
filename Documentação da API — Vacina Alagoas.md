# Documentação da API — Vacina Alagoas

Projeto Integrador IV-B · API REST em FastAPI · Referência das rotas existentes e de quando cada uma é usada

## 1. Visão geral

A API é **REST**, assíncrona, escrita em **FastAPI** com **PostgreSQL 16**. Ela atende dois públicos:

- **Cidadão (anônimo):** consulta cidades e postos de vacinação. Não precisa de login.
- **Administrador (autenticado):** cadastra postos e usa o bot de mineração do OpenStreetMap. Precisa de token JWT.

| Item | Valor |
| --- | --- |
| URL base (Docker Compose) | `http://localhost:8085` |
| Prefixo versionado | `/api/v1` (as mesmas rotas também existem na raiz) |
| Formato | JSON (exceto o login, que usa formulário) |
| Autenticação | `Authorization: Bearer <token>` |
| Swagger UI | `http://localhost:8085/docs` |
| ReDoc | `http://localhost:8085/redoc` |

> As rotas estão registradas duas vezes: `/cities` e `/api/v1/cities` respondem igual. O front-end usa as rotas da raiz.

## 2. Resumo das rotas

| Método | Rota | Acesso | Para que serve |
| --- | --- | --- | --- |
| POST | `/auth/login` | Público | Obter o token JWT do administrador |
| GET | `/cities` | Público | Listar as cidades atendidas |
| GET | `/cities/{id}` | Público | Ver os detalhes de uma cidade |
| GET | `/vaccination-points/{city_id}` | Público | Listar os postos de uma cidade, com vacinas |
| POST | `/vaccination-points` | Admin (JWT) | Cadastrar um posto manualmente |
| GET | `/admin/enrichment/preview-osm` | Admin (JWT) | Buscar postos no OpenStreetMap, sem gravar |
| POST | `/admin/enrichment/confirm-save` | Admin (JWT) | Gravar os postos que o admin escolheu |
| POST | `/admin/enrichment/sync-osm` | Admin (JWT) | Buscar e gravar tudo de uma vez (rota legada) |

## 3. Autenticação

O fluxo é o **OAuth2 password flow** com JWT:

1. O administrador envia usuário e senha para `POST /auth/login`.
2. A API confere a senha (hash `bcrypt`) e devolve um token JWT, válido por **120 minutos**.
3. O cliente guarda o token e o envia no cabeçalho de toda rota protegida:

```
Authorization: Bearer <access_token>
```

Se o token estiver ausente, inválido ou expirado, a rota protegida responde **401** com a mensagem `Credenciais inválidas ou token expirado`.

O usuário padrão da carga inicial (`seed.sql`) é `admin` / `admin123`. Troque essa senha fora do ambiente de desenvolvimento.

## 4. Rotas em detalhe

### 4.1 POST /auth/login

**Quando é usada:** quando o administrador abre o `admin.html` e clica em autenticar. É o primeiro passo antes de qualquer rota protegida.

**Corpo** (`application/x-www-form-urlencoded`, não é JSON):

| Campo | Tipo | Obrigatório |
| --- | --- | --- |
| `username` | texto | Sim |
| `password` | texto | Sim |

**Exemplo:**

```bash
curl -X POST http://localhost:8085/auth/login \
  -d "username=admin&password=admin123"
```

**Resposta 200:**

```json
{ "access_token": "eyJhbGciOi...", "token_type": "bearer" }
```

**Erros:**

| Código | Motivo |
| --- | --- |
| 401 | Usuário ou senha incorretos |
| 422 | Campos ausentes |

**Como funciona por dentro:** busca o `AdminUser` pelo `username`, confere a senha com `bcrypt.checkpw` e gera um JWT com `sub = username` e data de expiração (`exp`).

### 4.2 GET /cities

**Quando é usada:** quando a página do cidadão (`index.html`) carrega, para preencher a lista de municípios (Maceió, Arapiraca).

**Parâmetros:** nenhum.

**Resposta 200:**

```json
[
  { "id": 1, "name": "Maceió" },
  { "id": 2, "name": "Arapiraca" }
]
```

A lista vem ordenada por `id`. Não exige autenticação.

### 4.3 GET /cities/{id}

**Quando é usada:** quando é preciso os detalhes de uma cidade, incluindo o estado a que ela pertence.

| Parâmetro | Onde | Tipo |
| --- | --- | --- |
| `id` | caminho | inteiro |

**Exemplo:** `GET /cities/1`

**Resposta 200:**

```json
{ "id": 1, "name": "Maceió", "state": "Alagoas" }
```

**Erros:**

| Código | Motivo |
| --- | --- |
| 404 | Cidade não encontrada (`Cidade não encontrada`) |
| 422 | `id` não é um número inteiro (por exemplo `/cities/abc`) |

### 4.3.1 Dados usados pelas rotas de cidade

As cidades vêm da tabela `cities`, ligada à tabela `states`. Hoje só existem Maceió e Arapiraca, ambas em Alagoas.

### 4.4 GET /vaccination-points/{city\_id}

**Quando é usada:** depois que o cidadão escolhe uma cidade. A resposta alimenta a lista de postos, o mapa (Leaflet), a busca por bairro e o cálculo de distância pelo GPS. Também é usada na tabela de postos do painel admin, que consulta as cidades 1 e 2.

| Parâmetro | Onde | Tipo |
| --- | --- | --- |
| `city_id` | caminho | inteiro |

**Exemplo:** `GET /vaccination-points/1`

**Resposta 200:**

```json
[
  {
    "id": 12,
    "name": "USF Ponta Verde",
    "neighborhood": "Ponta Verde",
    "address": "Rua Dep. José Lages, 240",
    "latitude": -9.658,
    "longitude": -35.7025,
    "vaccines": ["Covid-19", "Influenza"]
  }
]
```

Os postos vêm ordenados por nome. O campo `vaccines` é uma lista de nomes e vem vazio (`[]`) se o posto não tiver vacinas ligadas. A API **não calcula distância**: isso é feito no navegador com a fórmula de Haversine, usando `latitude` e `longitude`.

**Erros:**

| Código | Motivo |
| --- | --- |
| 404 | A cidade não existe (`Cidade especificada não existe`) |
| 422 | `city_id` não é inteiro |

**Como funciona por dentro:** valida a cidade e executa uma única consulta SQL com `LEFT JOIN` e `ARRAY_AGG`, que traz as vacinas de cada posto junto, sem consultas extras por posto.

### 4.5 POST /vaccination-points

**Quando é usada:** quando o administrador preenche o formulário de cadastro rápido no painel (cidade, nome, bairro, endereço e vacinas) e clica em salvar.

**Acesso:** exige JWT.

**Corpo** (`application/json`):

| Campo | Tipo | Obrigatório | Observação |
| --- | --- | --- | --- |
| `city_id` | inteiro | Sim | Deve existir |
| `name` | texto | Sim | Único dentro da cidade |
| `neighborhood` | texto | Não |  |
| `address` | texto | Não |  |
| `latitude` | número | Não |  |
| `longitude` | número | Não |  |
| `vaccine_ids` | lista de inteiros | Não | IDs do catálogo de vacinas (padrão: lista vazia) |

**Exemplo:**

```bash
curl -X POST http://localhost:8085/vaccination-points \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"city_id":1,"name":"UBS Exemplo","neighborhood":"Centro","vaccine_ids":[1,3]}'
```

**Resposta 201:**

```json
{ "message": "Ponto de vacinação cadastrado com sucesso", "id": 25 }
```

**Erros:**

| Código | Motivo |
| --- | --- |
| 401 | Token ausente, inválido ou expirado |
| 404 | `city_id` não existe (`Cidade informada não existe`) |
| 422 | Corpo inválido (campo obrigatório ausente ou tipo errado) |
| 500 | Nome duplicado na mesma cidade, ou `vaccine_id` inexistente (hoje o erro de banco não é tratado e cai no erro genérico) |

**Como funciona por dentro:** valida a cidade, insere o posto, obtém o id gerado, insere as ligações na tabela `point_vaccines` e confirma a transação.

### 4.6 GET /admin/enrichment/preview-osm

**Quando é usada:** **primeira etapa** do bot de mineração. O administrador pede a busca e vê uma tabela de prévia com os postos de saúde de Maceió encontrados no OpenStreetMap. **Nada é gravado no banco.**

**Acesso:** exige JWT.

**Parâmetros:** nenhum.

**Resposta 200:**

```json
{
  "status": "sucesso",
  "total_encontrados": 2,
  "results": [
    {
      "city_id": 1,
      "name": "UBS Exemplo",
      "neighborhood": "Farol",
      "address": "Rua Tal",
      "latitude": -9.65,
      "longitude": -35.72,
      "source": "OpenStreetMap"
    }
  ]
}
```

**Como funciona por dentro:**

1. Consulta a API **Nominatim** com 5 termos: UBS, USF, Unidade de Saúde, Posto de Saúde e Centro de Saúde, todos em Maceió.
2. Se nada for encontrado, usa a **Overpass API**, tentando até 3 servidores em sequência.
3. Remove nomes repetidos e devolve a lista.

A resposta pode demorar vários segundos, porque depende de serviços externos. Se todos os serviços falharem, `results` volta vazio.

### 4.7 POST /admin/enrichment/confirm-save

**Quando é usada:** **segunda etapa** do bot. Depois de ver a prévia, o administrador marca quais unidades quer efetivar e envia só essas.

**Acesso:** exige JWT.

**Corpo** (`application/json`):

```json
{
  "points": [
    {
      "city_id": 1,
      "name": "UBS Exemplo",
      "neighborhood": "Farol",
      "address": "Rua Tal",
      "latitude": -9.65,
      "longitude": -35.72,
      "source": "OpenStreetMap"
    }
  ]
}
```

Só `name` é obrigatório em cada ponto. Os demais campos têm padrão (`city_id = 1`, `neighborhood = "Maceió"`, `address = "Endereço via OpenStreetMap"`).

**Resposta 200:**

```json
{
  "status": "concluido",
  "message": "Salvamento concluído! 1 novos postos inseridos, 0 já existentes ignorados.",
  "inserted_count": 1,
  "ignored_count": 0
}
```

**Erros:**

| Código | Motivo |
| --- | --- |
| 400 | Lista `points` vazia |
| 401 | Token ausente, inválido ou expirado |
| 422 | Corpo inválido |

**Como funciona por dentro:** cada posto é inserido com `ON CONFLICT (city_id, name) DO NOTHING`. Se já existir um posto com o mesmo nome na cidade, ele é **ignorado** e contado em `ignored_count`, sem gerar erro. Cada posto novo recebe automaticamente as vacinas padrão: Pólio, Sarampo, Covid-19 e Influenza (ids 1 a 4).

### 4.8 POST /admin/enrichment/sync-osm (legada)

**Quando é usada:** só em uso direto ou em testes. É o fluxo antigo, que busca no OpenStreetMap e **grava tudo de uma vez**, sem prévia e sem confirmação do administrador. Prefira `preview-osm` seguida de `confirm-save`.

**Acesso:** exige JWT. **Corpo:** nenhum.

**Resposta 200:**

```json
{
  "status": "concluido",
  "message": "Enriquecimento concluído: 3 postos adicionados.",
  "detalhes": { "inserted": 3, "ignored": 1, "saved_ids": [30, 31, 32] }
}
```

## 5. Fluxos de uso

### 5.1 Cidadão (sem login)

1. Abre `index.html`.
2. O front chama `GET /cities` para montar a lista de municípios.
3. O cidadão escolhe uma cidade e o front chama `GET /vaccination-points/{city_id}`.
4. O front mostra a lista e o mapa. A busca por bairro e a ordenação por distância (botão "Meu GPS") acontecem **no navegador**, sem novas chamadas à API.

### 5.2 Administrador: cadastro manual

1. `POST /auth/login` para obter o token.
2. `POST /vaccination-points` com o token para criar o posto.
3. `GET /vaccination-points/{city_id}` para atualizar a tabela do painel.

### 5.3 Administrador: mineração do OpenStreetMap

1. `POST /auth/login` para obter o token.
2. `GET /admin/enrichment/preview-osm` para ver os candidatos.
3. O administrador seleciona as unidades desejadas.
4. `POST /admin/enrichment/confirm-save` com as unidades escolhidas.

## 6. Códigos de resposta

| Código | Significado | Onde ocorre |
| --- | --- | --- |
| 200 | Sucesso | GETs, login, rotas de enriquecimento |
| 201 | Recurso criado | `POST /vaccination-points` |
| 400 | Requisição inválida | `confirm-save` com lista vazia |
| 401 | Não autenticado | Login errado ou token inválido/expirado |
| 404 | Não encontrado | Cidade inexistente |
| 422 | Validação falhou | Tipo errado ou campo ausente |
| 500 | Erro interno | Resposta `{"error": "Erro interno no servidor..."}` |

## 7. Métodos HTTP: o que existe e o que não existe

| Método | Situação |
| --- | --- |
| GET | Implementado (consultas) |
| POST | Implementado (login, criação, bot) |
| PUT | **Não implementado** |
| PATCH | **Não implementado** |
| DELETE | **Não implementado** |

Hoje não é possível editar nem remover um posto pela API. Para isso seriam necessárias rotas como `PUT /vaccination-points/{id}`, `PATCH /vaccination-points/{id}` e `DELETE /vaccination-points/{id}`.

## 8. Pontos de atenção

1. **Rotas do painel admin que não existem na API.** O `admin.html` chama `POST /admin/enrichment/mine/Maceio` e `POST /admin/vaccination-points`. O backend não tem essas rotas e elas responderão 404. As rotas corretas são `preview-osm` e `confirm-save` (mineração) e `POST /vaccination-points` (cadastro).
2. **Busca no OpenStreetMap bloqueante.** `preview-osm` usa `requests` (síncrono) dentro de uma rota `async`, o que pode travar outras requisições enquanto a busca roda.
3. **Erros de banco no cadastro viram 500.** Nome duplicado ou `vaccine_id` inexistente em `POST /vaccination-points` deveriam retornar 409 ou 422.
4. **Segredos padrão.** A `SECRET_KEY` e a senha `admin123` têm valores fixos de desenvolvimento e precisam ser trocados em produção.
5. **CORS aberto.** `allow_origins=["*"]` deve ser restrito aos domínios do front em produção.

# Projeto Integrador IV - B · Vacina Alagoas

Sistema web e API RESTful própria para consulta pública e inserção de pontos de vacinação no estado de **Alagoas** (com foco na capital **Maceió** e agreste em **Arapiraca**), utilizando **PostgreSQL 16**, **Python (FastAPI)**, **Jinja2 + Tailwind CSS** e **Docker**.

---

## 📌 1. Checklist de Avaliação Acadêmica Atendido

- [x] **Os três endpoints respondem corretamente:**
  - `GET /cities` (Lista os municípios de Alagoas)
  - `GET /cities/{id}` (Detalhes da cidade por ID com retorno 404/422 tratados)
  - `GET /vaccination-points/{city_id}` (Lista os postos e o array de vacinas disponíveis)
- [x] **Os dados voltam em formato JSON padronizado.**
- [x] **Escopo de Alagoas coberto:** Banco populado com postos e dados verídicos de Maceió e Arapiraca.
- [x] **Códigos de status HTTP semânticos:** `200 OK`, `201 Created`, `401 Unauthorized`, `404 Not Found`, `422 Unprocessable Entity` e `500 Internal Server Error`.
- [x] **Padrões de Arquitetura implementados e justificados:** Cliente-Servidor, Arquitetura em Camadas, Padrão Repository e Conteinerização.
- [x] **Identidade Visual Aprovada:** Padrão Oficial 2 (Azul Petróleo `#164E63` + Fundo Platina `#D1D5DB` + Acento Âmbar) em conformidade com a norma **WCAG 2.1 Nível AA / AAA**.
- [x] **Bot de Enriquecimento de Dados:** Mineração real via **Overpass API (OpenStreetMap)** para Maceió.

---

## 🚀 2. Como Executar a Aplicação com Docker (Recomendado)

Com o Docker instalado na máquina, execute um único comando na raiz do projeto:

```bash
docker compose up --build
```

O Docker Compose irá:
1. Subir o contêiner do **PostgreSQL 16** (`vacinacao_pg_db`) e executar automaticamente os scripts `sql/init.sql` e `sql/seed.sql` com os dados de Maceió e Arapiraca.
2. Aguardar o banco estar pronto via *healthcheck*.
3. Construir a imagem da aplicação Python e inicializar o servidor **FastAPI / Uvicorn** na porta `8000`.

O Docker Compose irá subir três contêineres independentes:
1. **`db` (PostgreSQL 16):** Porta externa `5435`
2. **`backend` (FastAPI / Uvicorn):** Porta externa `8085`
3. **`frontend` (Web UI Nginx):** Porta externa `3005`

### 🌐 Endereços de Acesso (Sem Conflitos com Outros Projetos):
- **Interface Web do Cidadão (Frontend):** [http://localhost:3005](http://localhost:3005)
- **Painel Administrativo:** [http://localhost:3005/admin.html](http://localhost:3005/admin.html) *(Usuário: `admin` / Senha: `admin123`)*
- **API REST Backend & Swagger /docs:** [http://localhost:8085/docs](http://localhost:8085/docs)
- **Endpoints Diretos da API:**
  - `GET http://localhost:8085/cities`
  - `GET http://localhost:8085/cities/1`
  - `GET http://localhost:8085/vaccination-points/1`
- **Banco PostgreSQL (Host):** `localhost:5435`

---

## 🛠️ 3. Como Rodar Localmente sem Docker (Opcional)

1. Crie e ative um ambiente virtual dentro da pasta `backend`:
```bash
cd backend
python -m venv venv
# No Windows:
.\venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as credenciais no PostgreSQL e execute a carga inicial:
```bash
psql -U postgres -d vacinacao_al -f ../sql/init.sql
psql -U postgres -d vacinacao_al -f ../sql/seed.sql
```

4. Inicie o servidor FastAPI:
```bash
uvicorn app.main:app --reload --port 8000
```

---

## 🤖 4. Bot de Enriquecimento de Dados (OpenStreetMap)

O bot minera unidades de saúde públicas cadastradas em Maceió no OpenStreetMap:

- **Via Terminal (CLI):**
  ```bash
  python -m app.enrichment.bot
  ```
- **Via Interface / API:**
  Efetue login no `/admin` e clique no botão **"Executar Bot OSM"**, ou envie uma requisição:
  ```bash
  POST /admin/enrichment/sync-osm
  Header: Authorization: Bearer <seu_token_jwt>
  ```

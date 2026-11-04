# Documentação Técnica e de Produto — Vacina Alagoas
## Projeto Integrador IV-B · Sistema de Gestão e Consulta de Vacinação (SESAU)

Bem-vindo à documentação oficial do projeto **Vacina Alagoas**. Todos os arquivos técnicos, especificações de requisitos, relatórios de auditoria e guias de usabilidade estão centralizados e estruturados nesta pasta.

---

## 🗺️ Mapa da Documentação

| Documento | Descrição | Público-Alvo |
| :--- | :--- | :--- |
| 📘 [**Relatório de Implementação**](file:///c:/Users/Luiz/Documents/Vacina/docs/relatorio-implementacao.md) | Relatório executivo detalhando o CRUD completo, polimento visual, correções Nginx e testes automatizados | Avaliadores, Desenvolvedores e Gestores |
| 📊 [**Auditoria CRUD (100% Conforme)**](file:///c:/Users/Luiz/Documents/Vacina/docs/auditoria-crud.md) | Relatório formal de conformidade com as operações Create, Read, Update e Delete | Banca do Projeto Integrador IV-B |
| 🔌 [**Documentação da API RESTful**](file:///c:/Users/Luiz/Documents/Vacina/docs/api.md) | Referência completa dos endpoints, esquemas JSON, autenticação JWT e exemplos `curl` | Desenvolvedores Frontend e Integrações |
| 🏛️ [**Arquitetura Técnica (TRD)**](file:///c:/Users/Luiz/Documents/Vacina/docs/arquitetura.md) | Detalhamento do PostgreSQL PostGIS, SQLAlchemy, FastAPI assíncrono, Docker e Nginx | Engenharia de Software e DevOps |
| 📋 [**Requisitos de Produto (PRD)**](file:///c:/Users/Luiz/Documents/Vacina/docs/requisitos.md) | Casos de uso, personas, metas, regras de negócio do SUS e escopo acadêmico | Gestão de Produto e Saúde Pública |
| ♿ [**Design System & Acessibilidade (WCAG)**](file:///c:/Users/Luiz/Documents/Vacina/docs/design-wcag.md) | Padrões visuais, contraste WCAG 2.1 AA/AAA, tokens e navegação por teclado | Designers e Especialistas em Acessibilidade |
| 🎨 [**Manual de Design Humano (Anti-IA)**](file:///c:/Users/Luiz/Documents/Vacina/docs/anti-ia-polimento.md) | Princípios de eliminação de templates artificiais, SVGs nativos e sobriedade institucional | Frontend e UI/UX |
| 📜 [**Histórico de Melhorias e Decisões**](file:///c:/Users/Luiz/Documents/Vacina/docs/historico-melhorias.md) | Linha do tempo de commits, registro de decisões arquiteturais (ADR) e backlog | Histórico e Evolução do Repositório |

---

## 🚀 Como Executar o Projeto com Docker

```bash
# 1. Subir todos os serviços (Banco, Backend e Frontend)
docker compose up -d --build

# 2. Acessar os ambientes no navegador
# - Portal Público do Cidadão: http://localhost:3005
# - Painel Administrativo SESAU: http://localhost:3005/admin.html (ou http://localhost:3005/admin)
# - Swagger UI (Documentação Interativa): http://localhost:3005/docs
# - ReDoc (Especificação Formal): http://localhost:3005/redoc

# 3. Executar a suíte de testes automatizados
pytest backend/tests
```

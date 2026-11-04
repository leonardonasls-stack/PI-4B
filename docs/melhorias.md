# Histórico de Melhorias Aplicadas — Vacina Alagoas

| Data | Camada / Fase | O Que Mudou | Motivo | Impacto / Evidência |
| :--- | :--- | :--- | :--- | :--- |
| 03/11/2026 | Fase 4 — Adoção (M-A) | Criação da base documental e governança do Playbook | Padronizar regras e controle sem alterar código funcional | 11 arquivos `.md` criados |
| 03/11/2026 | Camada 1 — Acessibilidade e Encoding | Correção de textos UTF-8 e contraste WCAG base | Qualidade textual e legibilidade | Commit `5a229aa` |
| 04/11/2026 | Camada 2 — Iconografia e Anti-IA | Remoção de Material Symbols, selo fake e caixas vazias; adoção de SVGs institucionais | Eliminar aparência de template de IA e melhorar fidelidade visual | Commit `15bf7c0` (tag `camada-2-concluida`) |
| 04/11/2026 | Camada 3 — Reorganização e Hierarquia UX | Unificação do Hero, ancoragem ergonômica da barra de busca e harmonização do Guia Prático | Resolver dispersão visual, eliminar sobreposição desajustada e melhorar fluxo intuitivo do cidadão | Commit `a1dc884` (tag `camada-3-concluida`) |
| 04/11/2026 | Auditoria CRUD — Fase 1 (Backend) | Implementação de Update (`PUT`), Delete (`DELETE`) e Leitura Unitária (`GET /detail`) | Fechar 100% das lacunas de operações CRUD no backend FastAPI | `schemas/point.py`, `point_service.py`, `points.py`, `main.py` |
| 04/11/2026 | Auditoria CRUD — Fase 2 (Frontend Admin) | Integração real no `admin.html` com suporte a `PUT`, `DELETE`, busca em tempo real e Overpass OSM | Conectar painel administrativo ao PostgreSQL com tratamento completo de erros e estados | `frontend/public/admin.html`, `AUDITORIA_CRUD.md` |


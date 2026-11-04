# Componentes e Bibliotecas de Terceiros — Vacina Alagoas

*Mapeamento extraído do código em 03/11/2026.*

---

## 1. Bibliotecas Externas em Uso
| Biblioteca | Versão Observada | Onde Aparece | Finalidade | Licença |
| :--- | :--- | :--- | :--- | :--- |
| **Tailwind CSS** | CDN (script 3.x) | `index.html` e `admin.html` | Framework utilitário de estilização CSS | MIT |
| **Leaflet.js** | 1.9.4 | `index.html` | Renderização do mapa interativo e marcadores geográficos | BSD-2-Clause |
| **Google Fonts (Public Sans)** | Webfont CDN | Cabeçalhos HTML | Tipografia institucional da aplicação | SIL OFL 1.1 |
| **Material Symbols Outlined** | Webfont CDN | Cabeçalhos HTML | Pacote de ícones (atualmente com sobreuso de IA) | Apache 2.0 |
| **OpenStreetMap Tiles** | CDN OSM | `index.html` via Leaflet | Camada base de mapas | ODbL |

---

## 2. Dependências do Backend
| Pacote | Versão | Finalidade |
| :--- | :--- | :--- |
| **FastAPI** | >= 0.110.0 | API RESTful assíncrona |
| **SQLAlchemy** | >= 2.0.28 | ORM assíncrono para persistência relacional |
| **asyncpg** | >= 0.29.0 | Driver assíncrono do PostgreSQL |
| **python-jose / passlib** | 3.3.0 / 1.7.4 | Autenticação JWT e hash bcrypt |
| **uvicorn** | >= 0.28.0 | Servidor ASGI para FastAPI |

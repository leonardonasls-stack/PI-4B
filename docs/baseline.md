# Baseline de Medição — Vacina Alagoas

*Medições realizadas em 03/11/2026 antes de qualquer alteração de código (segundo protocolo M-2).*

---

## 1. Tabela Comparativa (Baseline Inicial)

| Métrica | Antes (03/11/2026) | Meta Acordada | Ferramenta / Método |
| :--- | :--- | :--- | :--- |
| **Peso `index.html`** | 85.7 KB (1.898 linhas) | < 65 KB (código despoluído) | Medição direta no filesystem |
| **Peso `admin.html`** | 77.0 KB (1.109 linhas) | < 60 KB (eliminação de ruído) | Medição direta no filesystem |
| **Ícones Material Symbols (`index.html`)** | **41 ocorrências** | <= 10 ícones com função semântica real | Contagem direta de classes |
| **Ícones Material Symbols (`admin.html`)** | **53 ocorrências** | <= 15 ícones estritamente úteis | Contagem direta de classes |
| **Sinais de "Cara de IA" (P-13)** | **Alta (8 sinais graves)** | **Zero sinais de severidade Alta** | Protocolo P-13 (momento diagnóstico) |
| **Conectividade da API REST** | HTTP 200 (`/cities`, `/vaccination-points`) | Manter 100% operacional | PowerShell `Invoke-RestMethod` |
| **Acessibilidade de Contraste** | Paleta WCAG 2.1 AA/AAA ativa | Manter contraste estrito sem regressão | Verificação de tokens |
| **Controle de Formulários** | Inputs sem labels flutuantes artificiais | Semântica HTML5 nativa limpa | Inspeção de código |

---

## 2. Diagnóstico Funcional dos Serviços
- **Backend FastAPI:** Respondendo em `http://localhost:8085` (portas mapeadas no Docker).
  - `GET /cities` -> `[{"id": 1, "name": "Maceió"}, {"id": 2, "name": "Arapiraca"}]` (Status: OK)
  - `GET /vaccination-points/1` -> 3 postos retornados com endereço e vacinas vinculadas (Status: OK)
  - `GET /vaccination-points/2` -> 1 posto retornado (Status: OK)
- **Frontend Nginx:** Respondendo em `http://localhost:3005` (HTTP 200 OK).

---

## 3. SEO e Metadados
- `index.html`:
  - `<title>`: "Vacina Alagoas - Consulta Publica e Gestao de Postos de Vacinaao" (presente, mas com erro de encoding de caracteres acentuados no HTML de template).
  - `<meta name="description">`: Ausente ou genérica.
  - Open Graph (`og:title`, `og:image`): Ausentes.
- `admin.html`:
  - `<title>`: "Vacina Alagoas - Painel Administrativo".


# Diagnóstico Geral do Projeto — Vacina Alagoas

*Produzido em 03/11/2026 segundo o protocolo M-3 (Sem alterar código).*

---

## 1. Matriz de Achados por Categoria e Severidade

| ID | Achado / Descrição | Categoria | Severidade | Impacto | Esforço | Arquivo:Linha | Relação com "Não Pode Mudar" |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **D-01** | Selo artificial `verified` ("Rede Oficial de Vacinação") simulando autoridade | CARA DE IA | **Alta** | Alto | Baixo | `index.html:361-369` | Não afeta funcionalidade; melhora credibilidade |
| **D-02** | 94 ícones do Material Symbols espalhados como decoração sem contexto | CARA DE IA / ACABAMENTO | **Alta** | Alto | Médio | Global (`index` e `admin`) | Não afeta endpoints; limpa o visual |
| **D-03** | Hero dividido com card solto de gripe, dispersando o foco da busca | ESTRUTURA / UX | **Alta** | Alto | Médio | `index.html:371-415` | Mantém os selects e botão GPS, melhora usabilidade |
| **D-04** | Tags de vacinas em cartões de postos aglomeradas sem hierarquia | ACABAMENTO / ESTRUTURA | **Média** | Médio | Baixo | `index.html:745-790` | Preserva os dados da API, melhora legibilidade |
| **D-05** | Animações pulsantes artificiais em badges estáticas | CARA DE IA | **Média** | Médio | Baixo | `index.html:560`, `admin.html:20` | Elimina ruído de IA |
| **D-06** | Encoding de caracteres UTF-8 quebrado em textos estáticos | QUALIDADE | **Média** | Médio | Baixo | Global | Correção textual essencial |
| **D-07** | Dashboard administrativo com KPI cards de template desconectados | CARA DE IA / ESTRUTURA | **Média** | Médio | Médio | `admin.html:38-95` | Reorganiza o admin com foco no CRUD e mineração |
| **D-08** | URL da API hardcoded como `http://localhost:8085` | TÉCNICO | **Baixa** | Baixo | Baixo | `index.html:1168`, `admin.html:877` | Manter funcional para o ambiente Docker atual |

---

## 2. Cruzamento com o Baseline e Regras Intocáveis
- **O que está protegido e NENHUM achado irá violar:**
  1. A comunicação com os endpoints da API FastAPI (`/cities`, `/vaccination-points`, `/auth`, `/admin/enrichment`).
  2. A integração do Leaflet e cálculo Haversine de GPS.
  3. Os nomes dos postos de Maceió e Arapiraca e vacinas do catálogo do SUS.
  4. A paleta base acessível (Azul Petróleo / conformidade WCAG 2.1).

---

## 3. Síntese do Diagnóstico
A infraestrutura técnica (FastAPI, Docker, PostgreSQL) e a lógica de negócio estão sólidas e operacionais. O ponto crítico que torna a experiência do usuário "estranha" e artificial é a camada de apresentação HTML/Tailwind, repleta de convenções clichês de geradores de IA (dezenas de ícones redundantes, badges de autoridade falsas, animações de pulso gratuitas e layout disperso).


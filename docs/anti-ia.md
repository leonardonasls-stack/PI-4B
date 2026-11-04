# Auditoria Anti-"Cara de IA" (Protocolo P-13) — Vacina Alagoas

**Momento:** Diagnóstico  
**Data:** 03/11/2026  
**Alvo:** `frontend/public/index.html` e `frontend/public/admin.html`  
**Veredito Atual:** **NÃO PASSA** (Presença de sinais de severidade Alta e Média)

---

## 1. Tabela de Sinais Identificados (Momento: Diagnóstico)

| Sinal | Camada | Onde | Evidência (Arquivo:Linha) | Severidade | Correção Proposta | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Selo Falso de Autoridade** | VISUAL | Hero `index.html` | `index.html:361-369` (Pill com ícone `verified` "Rede Oficial de Vacinação") | **Alta** | Remover a pill de selo artificial e integrar a assinatura institucional de forma sóbria no header. | Pendente |
| **Superpopulação de Ícones** | VISUAL | Global (`index` e `admin`) | 41 ocorrências em `index.html` e 53 em `admin.html` | **Alta** | Remover ícones decorativos redundantes; manter apenas ícones funcionais essenciais (ex: pin de mapa, lupa de busca). | Pendente |
| **Hero Fragmentado / Disperso** | ESTRUTURA | Hero `index.html` | `index.html:371-415` (Colunas 8x4 com card de gripe solto) | **Alta** | Reorganizar o Hero centralizando o foco direto na busca de postos por município/bairro e GPS. | Pendente |
| **Pulsos e Glows sem Sentido** | COMPORTAMENTO | Badges de status | `index.html:560`, `admin.html:20, 72` (`animate-pulse`) | **Média** | Substituir o efeito pulsante de IA por indicador estático limpo e discreto. | Pendente |
| **Bento Grid Artificial** | ESTRUTURA | Seção de Apoio `index.html` | `index.html:813-980` (Moldes clichês de landing page) | **Média** | Reestruturar para seções editoriais limpas de orientação e canais oficiais do SUS. | Pendente |
| **KPI Cards de Template no Admin** | ESTRUTURA | Dashboard `admin.html` | `admin.html:38-95` (Cards idênticos com círculos e ícones genéricos) | **Média** | Transformar em sumário objetivo de registros e ações administrativas diretas. | Pendente |
| **Rótulos Clichês e Repetidos** | TEXTO | Badges e subtítulos | `index.html:403`, `admin.html:4` ("Sistema Conectado", "JWT Ativo") | **Média** | Simplificar a linguagem para comunicação direta e humana. | Pendente |
| **Encoding Quebrado por IA** | QUALIDADE | Cabeçalhos e textos | `index.html:368` (`Vacinaao`), `admin.html:51` (`Macei`) | **Média** | Corrigir todos os caracteres acentuados para UTF-8 limpo e semântico. | Pendente |

---

## 2. Auditoria Pós-Camada 2 (Polimento Visual e Iconografia Única)
- **Data:** 04/11/2026
- **Alvo:** `frontend/public/index.html`
- **Resultados:**
  - Selo falso de autoridade `verified`: **Eliminado** (substituído por texto institucional sóbrio).
  - Superpopulação de Material Symbols em `index.html`: **Zerado** (100% substituído por SVGs inline finos e de alto padrão institucional com `aria-hidden="true"`).
  - Caixas vazias e contêineres órfãos: **Saneados**.
  - Animação pulsante (`animate-pulse`): **Eliminada**.
  - Fontes externas pesadas do Google Fonts Material Symbols: **Removidas**.
- **Veredito Pós-Camada 2:** **PASSA COM RESSALVA DE ESTRUTURA** (Acabamento visual e iconografia limpos; pendente apenas a reorganização de layout e distribuição UX da Camada 3).

---

## 3. Veredito e Próximos Passos
O projeto foi despoluído na camada visual de apresentação. A interface pública do cidadão não carrega mais os vícios de IA de iconografia decorativa gratuita nem fontes desnecessárias.

- **Veredito:** `PASSA` na camada de acabamento.
- **Próximo Passo:** Executar a Camada 3 para resolver a dispersão do layout (Hero unificado, busca ergonômica e guia do cidadão linear).


# Mapa de Elementos Visuais — Vacina Alagoas

*Inventário de elementos visuais da interface (base para o protocolo P-17).*

---

## Tabela de Elementos
| Elemento | Localização no Código | Status | O que Pegar / Referência | O que NÃO Pegar |
| :--- | :--- | :--- | :--- | :--- |
| **Header / Navbar** | `index.html` (linhas 150-250) | [mantido] | Layout institucional limpo, links de navegação | Não adicionar menus suspensos desnecessários |
| **Badge de Autoridade Hero** | `index.html` (linhas 361-369) | [ajustar] | Texto sóbrio "Governo de Alagoas / SESAU" | **Remover** o selo falso `verified` com cara de IA |
| **Hero Principal** | `index.html` (linhas 370-420) | [ajustar] | Título claro e objetivo com campo de busca integrado | **Remover** blocos secundários descontextualizados |
| **Filtros de Busca (Cidade/Bairro)** | `index.html` (linhas 450-520) | [mantido] | Select acessível com preenchimento via API | Não quebrar eventos de mudança (`change`) |
| **Botão "Meu GPS"** | `index.html` (linhas 530-560) | [ajustar] | Botão de ação de localização direta e claro | Simplificar ícone e retirar animações exageradas |
| **Card de Campanha Ativa** | `index.html` (linhas 390-415) | [ajustar] | Bloco informativo claro e contextualizado | Retirar aspecto de card publicitário solto |
| **Painel do Mapa Leaflet** | `index.html` (linhas 600-660) | [mantido] | Altura e proporção atual, marcadores interativos | Não alterar renderização dos pins |
| **Cartões de Postos de Vacinação** | `index.html` (linhas 700-850) | [ajustar] | Nome do posto, endereço e horário com clareza | Reduzir o excesso de tags de vacinas aglomeradas |
| **Rodapé Institucional** | `index.html` (linhas 1100-1160) | [mantido] | Canais de atendimento (Disque 136) | Não poluir com selos fictícios |


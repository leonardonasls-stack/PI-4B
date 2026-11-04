# Ficha de Escolhas — Vacina Alagoas

*Ficha atual de escolhas observadas no código em 03/11/2026 (base para P-16 modo edição).*

---

## 1. Tipografia
| Item | Valor Observado no Código | Status Atual | Proposta de Ajuste (M2) |
| :--- | :--- | :--- | :--- |
| **Família Principal** | `Public Sans, sans-serif` | [mantido] | Manter; família limpa e altamente legível para saúde pública |
| **Origem** | Google Fonts (CDN) | [mantido] | Manter |
| **Pesos em Uso** | 400, 600, 700, 800 | [mantido] | Manter |
| **Escala Tipográfica** | Classes customizadas `display-lg` até `label-sm` | [mantido] | Manter |
| **Hierarquia de Títulos** | Títulos com `font-extrabold` no Hero e `font-bold` nos cartões | [ajustar] | Calibrar peso visual para reduzir rigidez de template gerado por IA |

---

## 2. Disposição (Layout e Grade)
| Item | Valor Observado no Código | Status Atual | Proposta de Ajuste (M2) |
| :--- | :--- | :--- | :--- |
| **Largura do Container** | `max-w-7xl` (1280px) centralizado | [mantido] | Manter alinhamento consistente |
| **Seção Hero** | Grid assimétrico 12 colunas (`col-span-8` e `col-span-4`) | [ajustar] | Reorganizar Hero para focar em busca clara e explicação direta |
| **Distribuição dos Itens** | Blocos de estatísticas e campanhas soltos à direita | [ajustar] | Agrupar com lógica contextual ou mover para seção de apoio |
| **Grid da Lista de Postos** | Grid 1 coluna em mobile e 2/3 colunas em desktop | [ajustar] | Organizar cards com espaçamento uniforme e hierarquia nítida |
| **Área do Mapa** | Painel lateral ou inferior Leaflet (`h-[450px]`) | [mantido] | Manter proporção e usabilidade interativa |

---

## 3. Itens e Componentes
| Item | Valor Observado no Código | Status Atual | Proposta de Ajuste (M2) |
| :--- | :--- | :--- | :--- |
| **Badges de Autoridade (Pills)** | Pills com ícone `verified` e `rounded-full` | [ajustar] | Remover selo falso de IA ou simplificar para identificador sóbrio |
| **Ícones de Interface** | *Material Symbols Outlined* injetados em quase todos os nós | [ajustar] | Eliminar ícones decorativos redundantes; manter só os estritamente úteis |
| **Cartões de Posto** | Cards com tags coloridas empilhadas | [ajustar] | Agrupar tags de vacinas de forma concisa e destacar endereço/horário |
| **Botões de Ação** | Botões com ícones duplos e cantos muito arredondados | [ajustar] | Padronizar botões com foco claro na ação (ex: "Ver no Mapa", "Como Chegar") |
| **Formulário de Busca** | Selects estilizados com labels auxiliares | [mantido] | Manter semântica e acessibilidade de seleção de cidade |

---

## 4. Referências e Bibliotecas
| Item | Valor Observado | Status Atual |
| :--- | :--- | :--- |
| **Estilização** | Tailwind CSS 3.x (CDN) | [mantido] |
| **Mapas** | Leaflet 1.9.4 (CDN) | [mantido] |
| **Tipografia** | Google Fonts Public Sans | [mantido] |


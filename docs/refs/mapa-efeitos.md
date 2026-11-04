# Mapa de Efeitos e Interações — Vacina Alagoas

*Inventário de efeitos existentes (base para o protocolo P-18).*

---

## Efeitos Observados no Código
| Categoria | Efeito / Classe | Onde Está | Status | Observação / Ajuste |
| :--- | :--- | :--- | :--- | :--- |
| **Status / Indicador** | `animate-pulse` (ponto verde) | Badges de status da API e SESAU | [ajustar] | Reduzir para indicador estático sóbrio ou pulso discreto |
| **Hover em Botões** | `hover:bg-primary/90`, `transition-all` | Botões de busca e GPS | [mantido] | Transição sutil de cor (150ms) mantida |
| **Hover em Cartões** | `hover:shadow-md`, `transition-shadow` | Lista de postos de saúde | [mantido] | Realce suave ao passar o cursor |
| **Foco em Campos (A11y)** | `focus:ring-2`, `focus:outline-none` | Inputs e Selects de cidades | [mantido] | Garante conformidade de foco com WCAG 2.1 |
| **Rolagem / Scroll** | Scroll suave para mapa | Botão "Ver no Mapa" | [mantido] | Funcionalidade mantida |

> **Painel "Onde Procurar" (Regra P-18):** Qualquer nova microinteração que venha a ser sugerida deve priorizar `prefers-reduced-motion` e referências sóbrias de interfaces governamentais/SUS.


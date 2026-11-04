# Manual de Design Humano e Diretrizes Anti-IA

Este documento estabelece as boas práticas visuais e estruturais adotadas para garantir que o **Vacina Alagoas** apresente acabamento profissional, sóbrio e condizente com um portal público de saúde governamental, eliminando traços de protótipos sintéticos gerados automaticamente por inteligência artificial.

---

## 1. O que foi Identificado e Eliminado

| Sintoma de Interface "Gerada por IA" | Por que é Prejudicial | Solução Humana Aplicada no Projeto |
| :--- | :--- | :--- |
| **Selo "Produção Ativa" com pulsar neon** | Transmite artificialismo e distrai o usuário do conteúdo principal | Removido. A barra superior agora expressa a identidade institucional oficial do Governo de Alagoas |
| **Material Symbols em excesso** | Dependência pesada do Google Fonts, gerando atraso e fontes piscando | Substituído por SVGs inline minimalistas (1.75px) com carregamento instantâneo |
| **Cards soltos e sobrepostos (Bento Grid desajustado)** | Gera desorientação e poluição cognitiva para o usuário | Reorganizado em um fluxo vertical com 3 cartões equilibrados de orientação |
| **Botões genéricos sem feedback (`href="#"`)** | Sensação de maquete quebrada | Todos os botões possuem funções de verdade (`type="button"` com interações, modais ou downloads) |
| **Discagem `tel:136` em desktop** | Falha de protocolo em computadores | Sistema inteligente com cópia para o clipboard e alerta informativo |

---

## 2. Padrões de Design e Identidade Institucional

### 2.1. Paleta de Cores do SUS Alagoas
- **Primária (Azul Petróleo Institucional):** `#002530` — Usada em títulos, cabeçalhos e botões de ação principal.
- **Secundária (Verde Saúde / Acolhimento):** `#006c4a` — Indicadores de sucesso, postos abertos e confirmações.
- **Superfície Base:** `#f9f9ff` com contêineres `#f0f3ff` — Garante conforto visual prolongado e atende aos índices de contraste WCAG 2.1 AAA.

### 2.2. Regra dos Ícones (SVGs Nativos)
- Todo novo ícone adicionado deve obrigatoriamente ser SVG linear inline:
  ```html
  <svg class="w-5 h-5 text-primary" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
    <!-- caminhos limpos -->
  </svg>
  ```
- Sempre incluir o atributo `aria-hidden="true"` para leitores de tela não anunciarem gráficos decorativos.

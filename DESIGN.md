# DESIGN.md — Sistema de Design do Vacina Alagoas

*Extraído do código em 03/11/2026; valores OBSERVADOS, não decisões.*

---

## 1. Cores e Tokens de Tema
*Origem: `frontend/public/index.html` (linhas 60-109) e `frontend/public/admin.html` (linhas 4-5).*

### Paleta Primária (Azul Petróleo / Institucional SUS)
- `primary`: `#002530` (Tom escuro principal, cabeçalhos e texto de alto contraste)
- `on-primary`: `#ffffff` (Texto sobre fundo primário)
- `primary-container`: `#0e3b4a` (Superfície secundária para cartões de destaque e header)
- `on-primary-container`: `#7da5b7` (Texto atenuado em container primário)
- `primary-fixed`: `#c0e9fc` (Destaque claro fixo)
- `primary-fixed-dim`: `#a4cddf` (Destaque secundário)

### Paleta Secundária (Verde Saúde / Confirmação)
- `secondary`: `#006c4a` (Verde esmeralda institucional)
- `on-secondary`: `#ffffff`
- `secondary-container`: `#82f5c1`
- `on-secondary-container`: `#00714e`
- `secondary-fixed`: `#85f8c4` (Verde fluorescente usado em status e badges)

### Superfícies e Fundos (Neutros / Alto Contraste)
- `background`: `#f9f9ff` (Fundo geral da aplicação)
- `surface`: `#f9f9ff`
- `surface-container-lowest`: `#ffffff` (Fundo de cartões e inputs)
- `surface-container-low`: `#f0f3ff`
- `surface-container`: `#e7eeff`
- `surface-container-high`: `#dee8ff`
- `surface-container-highest`: `#d8e3fb`
- `on-surface`: `#111c2d` (Texto escuro sobre superfícies claras)
- `on-surface-variant`: `#41484b` (Subtítulos e labels secundárias)
- `outline`: `#71787c` (Bordas de inputs)
- `outline-variant`: `#c1c7cb`

### Alertas e Destaques
- `error`: `#ba1a1a` / `error-container`: `#ffdad6` / `on-error`: `#ffffff`
- `tertiary`: `#371900` / `tertiary-container`: `#562b00` (Âmbar para campanhas)

---

## 2. Tipografia
*Origem: Google Fonts `Public Sans` e extensões do Tailwind.*

- **Família:** `Public Sans, sans-serif`
- **Pesos Carregados:** 400 (Regular), 600 (SemiBold), 700 (Bold), 800 (ExtraBold)
- **Escala de Texto Observada:**
  - `display-lg`: 48px / line-height 56px / tracking -0.02em / weight 800
  - `display-lg-mobile`: 32px / line-height 40px / tracking -0.01em / weight 800
  - `headline-xl`: 36px / line-height 44px / tracking -0.02em / weight 700
  - `headline-lg`: 28px / line-height 36px / tracking -0.01em / weight 700
  - `headline-md`: 22px / line-height 28px / tracking 0em / weight 600
  - `headline-sm`: 18px / line-height 26px / tracking 0em / weight 600
  - `body-lg`: 18px / line-height 28px / tracking 0em / weight 400
  - `body-md`: 16px / line-height 24px / tracking 0em / weight 400
  - `body-sm`: 14px / line-height 20px / tracking 0.01em / weight 400
  - `label-lg`: 16px / line-height 24px / tracking 0.01em / weight 600
  - `label-md`: 14px / line-height 20px / tracking 0.01em / weight 600
  - `label-sm`: 12px / line-height 16px / tracking 0.04em / weight 700

---

## 3. Espaçamentos, Raios e Sombras
- **Raios de Borda (`borderRadius`):**
  - `DEFAULT`: `0.125rem` (2px)
  - `lg`: `0.25rem` (4px)
  - `xl`: `0.5rem` (8px)
  - `full`: `0.75rem` (12px) e classe nativa Tailwind `rounded-full` (9999px)
- **Espaçamentos (`spacing`):**
  - `space-xs`: `0.25rem` (4px)
  - `space-sm`: `0.5rem` (8px)
  - `space-md`: `1rem` (16px)
  - `space-lg`: `1.5rem` (24px)
  - `space-xl`: `2rem` (32px)
  - `space-2xl`: `3rem` (48px)
- **Containers:** `max-w-7xl` (1280px) centralizado com `mx-auto`.

---

## 4. Componentes Recorrentes Observados
1. **Badges de Autoridade (Pills):** Containers arredondados `rounded-full` com ícones do Material Symbols e textos institucionais.
2. **Hero com Filtro Integrado:** Seção escura em `bg-primary` com campos suspensos de busca rápida por município e bairro.
3. **Cartões de Postos (Cards):** Fundo branco `bg-surface-container-lowest`, bordas suaves, tags coloridas de vacinas e botões de ação ("Ver no Mapa", "Como Chegar").
4. **Painel de Mapa (Leaflet):** Container de mapa com altura fixa (`h-[450px]` a `h-[520px]`), cantos arredondados e marcadores customizados.
5. **Tabelas Administrativas:** Linhas alternadas com botões de ação compactos (ícone de edição/exclusão).

---

## 5. Tom Visual e Movimento Observado [inferido]
- **Tom pretendido:** Institucional de saúde pública, sério, acessível e confiável.
- **Movimento e Animações:** Efeito `animate-pulse` em pontos de status e transições suaves de cor (`transition-colors`, `transition-all`).

---

## 6. Inconsistências Identificadas (Diagnóstico Inicial)
1. **Excesso de Ícones "Cara de IA":** O uso massivo de *Material Symbols Outlined* em praticamente todos os elementos (badges, títulos, listas, botões de ação) sem necessidade funcional satura a interface e transmite a impressão de mockup gerado por IA.
2. **Badges Falsas de Autoridade:** O selo `verified` com *"Rede Oficial de Vacinação • SESAU Alagoas"* no topo cria ruído e se parece com um elemento de template de landing page comercial, destoando de um portal de utilidade pública do SUS.
3. **Distribuição Espalhada e Falta de Contexto no Hero:** A divisão em colunas desiguais (`col-span-8` vs `col-span-4`) coloca blocos de campanhas e estatísticas soltos, competindo visualmente com o campo principal de busca.
4. **Rótulos Duplicados e Poluição em Pills:** Diversos cards exibem pills de categorias repetidas ("SUS Conectado", "Horário Estendido", "Aberto Hoje") sem explicação clara sobre a fonte dos dados.
5. **Densidade e Hierarquia Frágil na Lista de Postos:** Informações essenciais como horário e endereço competem com tags de vacinas empilhadas sem delimitação nítida.

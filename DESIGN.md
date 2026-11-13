# DESIGN.md — Vacina Alagoas

Extraído do código em 2026-11-12; valores OBSERVADOS, não decisões.

## 1. Cores (tokens MD3 em `tailwind.config`)

Definidas de forma idêntica em `frontend/public/index.html` (L65-L113) e `frontend/public/admin.html` (L67):

| Token | Valor | Papel observado `[inferido]` |
|---|---|---|
| `primary` | `#002530` | Azul petróleo institucional (botões primários, cabeçalhos de modais no portal) |
| `primary-container` | `#0e3b4a` | Hover / container primário |
| `on-primary` | `#ffffff` | Texto sobre `primary` |
| `secondary` | `#006c4a` | Verde SUS / ação secundária / status positivo |
| `secondary-container` | `#82f5c1` | Fundo de destaque secundário |
| `on-secondary-container` | `#00714e` | Texto sobre `secondary-container` |
| `surface` / `background` | `#f9f9ff` | Fundo geral da página |
| `surface-container-lowest` | `#ffffff` | Superfície de cards e modais |
| `surface-container-low` | `#f0f3ff` | Superfície suave de apoio |
| `surface-container` | `#e7eeff` | Superfície intermediária |
| `surface-container-high` | `#dee8ff` | Superfície elevada |
| `surface-variant` / `surface-container-highest` | `#d8e3fb` | Superfície variante |
| `on-surface` / `on-background` | `#111c2d` | Texto principal |
| `on-surface-variant` | `#41484b` | Texto secundário |
| `outline` | `#71787c` | Bordas/ícones de contorno |
| `outline-variant` | `#c1c7cb` | Divisórias sutis |
| `error` | `#ba1a1a` | Estados de erro |
| `error-container` / `on-error-container` | `#ffdad6` / `#93000a` | Alertas de erro |
| `tertiary` / `on-tertiary-container` | `#371900` / `#eb851c` | Acento quente / avisos |

## 2. Tipografia

- **Família principal:** `Public Sans` (Google Fonts, pesos `400`, `600`, `700`, `800`) em ambos os arquivos (`index.html` L17, `admin.html` L3).
- **Escala tipográfica customizada (`tailwind.config`):**
  - `display-lg`: `48px / 56px`, `-0.02em`, `800` (`display-lg-mobile`: `32px / 40px`, `-0.01em`, `800`)
  - `headline-xl`: `36px / 44px`, `-0.02em`, `700` (`headline-xl-mobile`: `26px / 34px`, `-0.01em`, `700`)
  - `headline-lg`: `28px / 36px`, `-0.01em`, `700`
  - `headline-md`: `22px / 28px`, `0em`, `600`
  - `headline-sm`: `18px / 26px`, `0em`, `600`
  - `body-lg`: `18px / 28px`, `400` · `body-md`: `16px / 24px`, `400` · `body-sm`: `14px / 20px`, `400`
  - `label-lg`: `16px / 24px`, `0.01em`, `600` · `label-md`: `14px / 20px`, `0.01em`, `600` · `label-sm`: `12px / 16px`, `0.04em`, `700`

## 3. Espaçamento, Raios e Contêineres

- **Espaçamentos customizados:** `space-xs` (`0.25rem`), `space-sm` (`0.5rem`), `space-md` (`1rem`), `space-lg` (`1.5rem`), `space-xl` (`2rem`), `space-2xl` (`3rem`), `gutter-sm` (`1rem`), `gutter` (`1.5rem`), `margin-sm` (`1rem`), `margin` (`2rem`).
- **Raios (`borderRadius`):** `DEFAULT: 0.125rem`, `lg: 0.25rem`, `xl: 0.5rem`, `full: 0.75rem` — porém classes padrão como `rounded-2xl`, `rounded-xl`, `rounded-lg`, `rounded-full` são usadas com mistura de valores.
- **Largura máxima do container:**
  - `index.html`: `max-w-7xl` (`1280px`)
  - `admin.html`: `max-w-[1280px]` (equivalente a `1280px`, mas com sintaxe diferente)

## 4. Movimento e Efeitos Existentes

- `html { scroll-behavior: smooth; }` em ambos.
- `index.html`: ~104 ocorrências de `transition-*` / `animate-*` / `hover:scale*` / `hover:-translate*`.
- `admin.html`: ~38 ocorrências (`group-hover:scale-105`, `animate-pulse` no botão "Ver Portal", `animate-spin` em loading).

## 5. Inconsistências Resolvidas na Melhoria M2 (2026-11-12)

1. **Header e Tema Visual:** `admin.html` unificado ao tema claro do portal (`bg-white/95`, barra superior `#002530`, acentos `primary`/`secondary`, rodapé `bg-surface-container-low` com contraste corrigido).
2. **Ícones:** `Material Symbols Outlined` duplicado removido de `admin.html`; ícones padronizados em SVG inline.
3. **Navegação Mobile:** menu `#menu-mobile-admin` adicionado abaixo de `768px` em `admin.html`.
4. **Scrollbar e Movimento Reduzido:** scrollbar visível restaurada no portal e `@media (prefers-reduced-motion: reduce)` adicionado em ambos.
5. **HTML e Raios:** `<html lang="pt-BR">` corrigido em `index.html:3`; `borderRadius.full` restaurado para `9999px` e fallback de `Public Sans` adicionado em ambos.


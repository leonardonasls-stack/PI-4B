# Ficha Atual de Escolhas (`P-16` — Modo Edição)

Atualizada após o diagnóstico (`M-3`) em 2026-11-12. Marque o que deseja confirmar para cada item marcado como `ajustar`.

## 1. Tipografia
- **Família principal:** `Public Sans` (`400;600;700;800`) — Proposta: **`mantido`**
- **Fallback:** explícito `["Public Sans", "system-ui", "-apple-system", "sans-serif"]` no `tailwind.config` — Proposta: **`ajustar`** (atualmente sem fallback explícito)
- **Escala:** consolidar `display-lg` a `label-sm` e remover os `38` `text-[*px]` arbitrários (`text-[10px]`, `text-[11px]`) — Proposta: **`ajustar`**
- **Medida de linha:** `max-w-2xl` / `max-w-4xl` — Proposta: **`mantido`**

## 2. Disposição e Navegação
- **Container:** unificar sintaxe para `max-w-7xl` (`1280px`) em ambos os arquivos — Proposta: **`ajustar`**
- **Header e Rodapé (Portal vs. Admin):** unificar tema visual em torno de `#002530` (`primary`) + `surface` claro (`#f9f9ff`), eliminando o bloco escuro `slate-900`/`emerald-600` destoante do Admin — Proposta: **`ajustar`**
- **Menu Mobile do Admin:** adicionar menu/gaveta acessível para `< 768px` (hoje `hidden md:flex` esconde toda a navegação) — Proposta: **`ajustar`**

## 3. Itens e Componentes
- **Raios (`borderRadius`):** restaurar `rounded-full: 9999px` (corrigindo o override `0.75rem`) e padronizar `rounded-xl` (`0.75rem`) / `rounded-lg` (`0.5rem`) nos cards e botões — Proposta: **`ajustar`**
- **Ícones:** remover `Material Symbols Outlined` duplicado do Admin e padronizar em SVGs limpos e coerentes, removendo ícones puramente decorativos — Proposta: **`ajustar`**
- **Botões e Estados:** padronizar `focus-visible:ring-2 focus-visible:ring-primary` em ambos os arquivos e remover `animate-pulse` decorativo — Proposta: **`ajustar`**

## 4. Referências de Biblioteca
- **Base:** HTML5 + Tailwind CSS CDN + Vue 3 CDN + Leaflet 1.9.4 — Proposta: **`mantido`**

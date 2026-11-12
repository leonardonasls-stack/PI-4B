# Registro de Melhorias (`docs/melhorias.md`)

| Data | Camada | O que mudou | Por quê | Impacto / Evidência |
|---|---|---|---|---|

| 2026-11-12 | Camada 1 (Críticos) | Corrigida tag `<html lang="pt-BR">`, restaurada scrollbar no portal, adicionados `<h1>`, `focus-visible` global, `@media (prefers-reduced-motion: reduce)` e menu mobile (`< 768px`) no admin | Correção de bugs HTML, conformidade WCAG 2.1 e navegação mobile | `index.html:3` corrigido; `admin.html` com `1` `<h1>`, `28` `focus-visible` e `#menu-mobile-admin` |
| 2026-11-12 | Camada 2 (Acabamento e Coesão) | Unificado tema do `admin.html` ao Portal (`#002530` / `#006c4a` / `#f9f9ff`), corrigido contraste do rodapé, restaurado `borderRadius.full: 9999px`, adicionado fallback em `Public Sans`, removido `Material Symbols` duplicado e `animate-pulse` | Coesão visual Portal ↔ Admin e correção de contraste/tokens | `0` Material Symbols, `0` `animate-pulse`, `P-13` final `PASSA` |

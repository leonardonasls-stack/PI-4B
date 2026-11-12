# Diagnóstico (`M-3`) — Vacina Alagoas

**Data:** 2026-11-12
**Fontes de auditoria aplicadas (sem alterar código):**
1. **Fonte 1 (Impeccable — `audit` / `critique`):** consistência de tokens, acessibilidade WCAG, hierarquia e poluição visual.
2. **Fonte 2 (Jakub — `better-interface` / `break`):** tipografia, cores, raios, estados de foco/hover, responsivo mobile e edge cases.
*(Nota: auditoria executada por inspeção estática do código devido à indisponibilidade do `chrome_devtools`.)*

## Achados Consolidados (sem duplicatas)

| # | Descrição | Evidência | Categoria | Severidade | Impacto | Esforço | Toca "NÃO PODE MUDAR"? |
|---|---|---|---|---|---|---|---|
| 1 | **Tag `<html>` malformada:** `<html> lang="pt-BR">` fecha antes do atributo `lang`, podendo vazar texto no topo e quebrar `lang` para leitores de tela | `index.html:3` | TÉCNICO / QUALIDADE | **Crítico** | Alto | Baixo | Não (melhora WCAG) |
| 2 | **Ausência de `focus-visible` e `outline-none` sem anel de foco no Admin:** `0` `focus-visible:` e `10` `outline-none` impedem navegação visível por teclado | `admin.html` (geral, ex.: L151) | QUALIDADE (WCAG) | **Crítico** | Alto | Baixo | Não (WCAG 2.1 obrigatório) |
| 3 | **Menu de navegação oculto no mobile do Admin:** `<nav class="hidden md:flex">` esconde todas as ações de navegação abaixo de `768px` sem menu alternativo | `admin.html:92` | ESTRUTURA / RESPONSIVO | **Alto** | Alto | Médio | Não (melhora acesso mobile) |
| 4 | **Quebra de coesão visual Portal vs. Admin:** Portal usa `#002530` + header claro (`bg-white/95`); Admin usa header/footer `bg-slate-900` + `emerald-600`/`rose-600`, ignorando tokens `primary` e `surface` | `index.html:243` vs `admin.html:69,753` (`152` `slate-*`, `71` `emerald-*`) | MARCA / ACABAMENTO | **Alto** | Alto | Médio | Não (respeita base `#002530`) |
| 5 | **Ausência de `<h1>` no Admin:** página começa direto em `<h2>`, quebrando hierarquia semântica de títulos | `admin.html:137,276,418` | QUALIDADE (WCAG) | **Médio** | Médio | Baixo | Não |
| 6 | **Scrollbar oculta no Portal e divergente no Admin:** `::-webkit-scrollbar { display: none; }` no Portal vs barra `8px` no Admin | `index.html:41-43` vs `admin.html:16-29` | QUALIDADE / ACABAMENTO | **Médio** | Médio | Baixo | Não |
| 7 | **Fontes de ícones duplicadas e excesso de SVGs:** `Material Symbols Outlined` carregada 2x em `admin.html` (usada 4x) + 30 SVGs inline; 56 SVGs no Portal | `admin.html:3-4`, `index.html` | ACABAMENTO / TÉCNICO | **Médio** | Médio | Médio | Não |
| 8 | **Ausência de `prefers-reduced-motion`:** `scroll-behavior: smooth`, `animate-pulse` (`admin.html:108`) e `hover:scale-*` sem respeito a movimento reduzido | `index.html:23`, `admin.html:6,108` | QUALIDADE (WCAG) | **Médio** | Médio | Baixo | Não |
| 9 | **`borderRadius.full` sobrescrito para `0.75rem` e `text-[*px]` fora da escala:** quebra círculos (`rounded-full`) e gera 38 tamanhos de fonte arbitrários | `index.html:118,1343`, `admin.html:67` | ACABAMENTO | **Médio** | Médio | Baixo | Não |
| 10 | **Sinais de "Cara de IA" (`P-13`):** ver [docs/anti-ia.md](file:///c:/Users/Luiz/Documents/Vacina/docs/anti-ia.md) (descolamento de tema, `animate-pulse` decorativo, ícones em excesso, onda SVG no hero) | `docs/anti-ia.md` | CARA DE IA | **Alto** | Alto | Médio | Não |

**Conclusão:** Nenhum achado exige alterar backend, banco, contratos JSON, Haversine, Leaflet ou regras JWT. Tudo é 100% frontend.


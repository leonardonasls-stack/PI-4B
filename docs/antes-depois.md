# Relatório Antes / Depois e Verificação (`M-17`) — Vacina Alagoas

**Data:** 2026-11-12
**Branch:** `melhoria/m2-coesao-portal-admin` (tag de rollback: `snapshot-pre-coesao-20261112`)

## 1. Comparação com o Baseline (`docs/baseline.md`)

| Métrica | Antes (`baseline.md`) | Depois (`M-17`) |
|---|---|---|
| Erro de sintaxe `<html lang="pt-BR">` (`index.html:3`) | `1` erro (`<html> lang="pt-BR">`) | **`0` erros** |
| Scrollbar no Portal (`index.html`) | Oculta (`display: none`) | **Visível (`8px`, tokens `#f0f3ff`/`#c1c7cb`)** |
| Hierarquia `<h1>` no Admin (`admin.html`) | `0` `<h1>` | **`1` `<h1>` semântico** |
| Foco por teclado no Admin (`focus-visible`) | `0` (`10` `outline-none`) | **Regra global `focus-visible` + `6` classes explícitas** |
| Menu mobile no Admin (`< 768px`) | Oculto (`hidden md:flex`) | **Botão hambúrguer + `#menu-mobile-admin` funcional** |
| `prefers-reduced-motion` | `0` | **Ativo em ambos os arquivos** |
| Tema Header/Rodapé Admin vs. Portal | Escuro (`slate-900`/`emerald`) com bug de contraste no rodapé | **Unificado ao Portal (`bg-white/95`, `#002530`, `#f9f9ff`)** |
| `Material Symbols Outlined` duplicado | Carregado 2x, usado 4x | **`0` (removido; ícones unificados em SVG)** |
| `borderRadius.full` | `0.75rem` (quebrava círculos) | **`9999px`** |
| Gate Anti-IA (`P-13`) | `NÃO PASSA` (2 Altas, 3 Médias) | **`PASSA`** |
| Medições em navegador (`chrome_devtools`) | Falha de conexão (`DevToolsActivePort` ausente) | `Não executado em runtime (validar visualmente no Docker local)` |

## 2. Checklist de Regressão ("NÃO PODE MUDAR")
- [x] `backend/` e `sql/` intocados (`git diff --stat` mostra apenas `frontend/public/index.html`, `frontend/public/admin.html` e `docs/`/`DESIGN.md`)
- [x] Contratos REST, Haversine/"Meu GPS", Leaflet + Google Maps, JWT e CRUD preservados
- [x] Dados oficiais de Alagoas e paleta base `#002530` preservados

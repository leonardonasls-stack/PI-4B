# Plano de Melhorias em Camadas (`M-4`) — Vacina Alagoas

**Objetivo:** Unificar a identidade visual entre Portal Público (`index.html`) e Painel Admin (`admin.html`) — fontes, espaçamento, cores, modo mobile —, remover sinais de "cara de IA", despoluir ícones e corrigir falhas técnicas/WCAG no frontend.
**Protegido ("NÃO PODE MUDAR"):** Backend, PostgreSQL, contratos REST, Haversine/"Meu GPS", Leaflet + Google Maps, JWT + CRUD Admin, dados oficiais de Alagoas, paleta base `#002530` e WCAG 2.1.

## Camadas Propostas

| Camada | Escopo / Itens | Impacto | Esforço | Risco | Como Reverter | Arquivos | Métrica de Sucesso |
|---|---|---|---|---|---|---|---|
| **Camada 1 — Críticos (HTML, Acessibilidade e Mobile)** | 1. Corrigir `<html lang="pt-BR">` (`index.html:3`)<br>2. Adicionar `<h1>` semântico no Admin<br>3. Adicionar `focus-visible` em todos os controles do Admin (substituindo `outline-none` sem anel)<br>4. Criar menu mobile funcional no Admin (`< 768px`)<br>5. Adicionar `@media (prefers-reduced-motion: reduce)` e restaurar scrollbar visível no Portal | Alto | Médio | Baixo | `git revert` do commit da camada | `index.html`, `admin.html` | 0 erros de tag `<html>`, 100% controles com foco visível, menu acessível em 390px |
| **Camada 2 — Acabamento e Coesão Visual (`M-5` + `P-16`)** | 1. Unificar tokens do `tailwind.config` (corrigir `borderRadius.full: 9999px` e fallback de `Public Sans`)<br>2. Alinhar Header, Rodapé, Botões e Cards do Admin ao tema `#002530` (`primary`) + `surface` (`#f9f9ff`) + `secondary` (`#006c4a`)<br>3. Remover `Material Symbols` duplicado (`admin.html:3-4`), despoluir ícones decorativos e `animate-pulse`<br>4. Substituir `text-[*px]` soltos pela escala tipográfica padrão | Alto | Médio | Médio | `git revert` do commit da camada ou tag `snapshot-pre-coesao-20261112` | `index.html`, `admin.html`, `DESIGN.md`, `docs/escolhas.md` | Coesão visual Portal ↔ Admin; 0 sinais altos/médios no gate `P-13` |

## Adiado / Fora de Escopo (registrado em `docs/backlog.md`)
- **Build local do Tailwind (remover Play CDN):** adiado porque exigiria introduzir `package.json`/Node build no fluxo Docker atual.
- **Alterações de estrutura de API ou backend:** recusado (protegido pelo "NÃO PODE MUDAR").


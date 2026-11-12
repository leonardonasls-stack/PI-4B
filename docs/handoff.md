# Handoff e Manutenção (`M-18`) — Vacina Alagoas

**Data:** 2026-11-12
**Branch:** `melhoria/m12-refatoracao-features` (snapshots anteriores: `snapshot-pre-coesao-20261112` e `snapshot-pre-m12-20261112`)

## O que foi entregue
- **Camada 1 (commit `622b4f7`):** correção da tag `<html lang="pt-BR">`, restauração da scrollbar no portal, `<h1>` semântico no admin, foco visível global (`focus-visible`), `@media (prefers-reduced-motion: reduce)` e menu mobile (`#menu-mobile-admin`) no painel administrativo.
- **Camada 2 (commits `68deeaf`, `1b459e3`):** unificação visual do painel administrativo ([admin.html](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/admin.html)) com o portal público ([index.html](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/index.html)), barra de acessibilidade no admin, logotipo SVG próprio, migração para Phosphor Icons `2.1.1`, correção de contraste do rodapé do admin, remoção de `Material Symbols Outlined` duplicado e `animate-pulse`, restauração de `borderRadius.full: 9999px` e fallback explícito para `Public Sans`.
- **M12 Camada A (commit `a76bd9d`):** refatoração dos blocos compartilhados para [theme.css](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/assets/css/theme.css), [tailwind-config.js](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/assets/js/tailwind-config.js) e [acessibilidade.js](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/assets/js/acessibilidade.js).
- **M12 Camada B (commit `6e487c5`):** favoritos em `localStorage` (`vacina_al_favoritos`), filtro "Meus Favoritos", compartilhamento no modal (`navigator.share` + clipboard) e barra de resumo de filtros (`#barra-resumo-filtros`) com "Limpar filtros" no portal público.
- **M12 Camada C (commit `a242622`):** KPIs operacionais (`Total Homologados`, `Maceió`, `Arapiraca`, `Vacinas Ofertadas`), ordenação por coluna e paginação client-side (`10`/`25`/`50`) no painel administrativo.

## Como testar localmente antes de publicar/mesclar
1. Subir ou atualizar os contêineres: `docker compose up -d --build`
2. Abrir `http://localhost:3005` (testar favoritos, filtro "Meus Favoritos", barra de resumo de filtros e compartilhamento no modal) e `http://localhost:3005/admin.html` (testar KPIs, ordenação por coluna e paginação após login).
3. Reverter caso necessário: `git checkout luiz` ou `git reset --hard snapshot-pre-m12-20261112`.


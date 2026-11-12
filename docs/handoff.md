# Handoff e Manutenção (`M-18`) — Vacina Alagoas

**Data:** 2026-11-12
**Branch:** `melhoria/m2-coesao-portal-admin` (snapshot anterior: `snapshot-pre-coesao-20261112`)

## O que foi entregue
- **Camada 1 (commit `622b4f7`):** correção da tag `<html lang="pt-BR">`, restauração da scrollbar no portal, `<h1>` semântico no admin, foco visível global (`focus-visible`), `@media (prefers-reduced-motion: reduce)` e menu mobile (`#menu-mobile-admin`) no painel administrativo.
- **Camada 2:** unificação visual do painel administrativo ([admin.html](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/admin.html)) com o portal público ([index.html](file:///c:/Users/Luiz/Documents/Vacina/frontend/public/index.html)), correção de contraste do rodapé do admin, remoção de `Material Symbols Outlined` duplicado e `animate-pulse`, restauração de `borderRadius.full: 9999px` e fallback explícito para `Public Sans`.

## Como testar localmente antes de publicar/mesclar
1. Subir ou atualizar os contêineres: `docker compose up -d --build`
2. Abrir `http://localhost:3005` (desktop e mobile ~390px) e `http://localhost:3005/admin.html` (após login) para conferência visual final.
3. Reverter caso necessário: `git checkout luiz` ou `git reset --hard snapshot-pre-coesao-20261112`.

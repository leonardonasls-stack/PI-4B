# Projeto: Vacina Alagoas

## Contexto
- **O que é o projeto [inferido]:** Sistema web de consulta pública e gestão de postos de vacinação em Alagoas (com foco inicial em Maceió e Arapiraca), integrando cálculo de proximidade por geolocalização (Haversine), mapa interativo em Leaflet e painel administrativo com mineração de dados via OpenStreetMap. Desenvolvido como Projeto Integrador IV-B (Ciência da Computação / TI).
- **Stack:** FastAPI (Python 3.12+ assíncrono), PostgreSQL 16, HTML5, Tailwind CSS, Leaflet.js, Nginx e Docker Compose.
- **Estado:** Em desenvolvimento ativo / execução local via Docker (Frontend: porta 3005; Backend: porta 8085; DB: porta 5435).
- **Comandos essenciais:**
  - Rodar com Docker: `docker compose up -d --build`
  - Parar Docker: `docker compose down`
  - Backend local (sem Docker): `uvicorn src.app.main:app --reload --port 8085` (dentro de `backend/` com `.venv` ativo)
  - Frontend local (sem Docker): `python -m http.server 3005` (dentro de `frontend/public/`)
  - Testes: `pytest` (dentro de `backend/`)

## O que NÃO pode mudar [confirmar]
1. **Regras Funcionais e Rotas REST:**
   - Endpoints `/cities`, `/vaccination-points/{city_id}`, `/auth/login` e `/admin/enrichment` mantêm seus contratos JSON.
   - Cálculo de distância geodésica (fórmula de Haversine) e ordenação por proximidade no botão "Meu GPS".
   - Mapa Leaflet com marcadores clicáveis e integração externa para traçar rotas no Google Maps.
   - Autenticação JWT e formulário de cadastro/edição de postos no painel `/admin.html`.
2. **Dados e Conteúdo Oficial:**
   - Nomes reais de postos, bairros e catálogo de vacinas oficiais de Alagoas.
3. **Identidade Base e Acessibilidade:**
   - Paleta de alto contraste baseada em Azul Petróleo (`#002530`) e conformidade WCAG 2.1 (AA/AAA).

## Convenções Observadas
- **Frontend:** HTML5 semântico com Tailwind CSS nativo (via script CDN configurado com tokens Material Design 3) e JavaScript modular Vanilla em blocos IIFE autocontidos.
- **Backend:** Arquitetura em camadas com separação em `api/v1/endpoints/`, `core/services/`, `database/models/` e schemas Pydantic.
- **Isolamento de Estilos:** Convenção do projeto vence qualquer skill mestre externa.

## Precedência
1. Restrições do usuário e lista "NÃO PODE MUDAR"
2. Pedido atual e objetivo da melhoria (remover aspecto de IA, despoluir ícones e reorganizar layout)
3. `DESIGN.md` e convenções existentes do projeto
4. Skill mestre e diretrizes do Playbook
5. Skills de revisão
6. Qualidade técnica (acessibilidade WCAG, performance, segurança) — vence a estética
7. Economia de tokens e simplicidade de código

## Regras Obrigatórias do Playbook
- **Nada de publicar ou alterar código funcional sem aprovação explícita.**
- **Uma camada por vez**, com aprovação prévia e commits pequenos e reversíveis.
- **Gate Anti-"Cara de IA" (P-13):** Executado obrigatoriamente no diagnóstico, pós-camada e na verificação final. Veredito "não passa" bloqueia entrega.
- **Referências em Vídeo (P-14):** Sempre que houver referência visual dinâmica (efeito, transição, modal, menu), mostrar opção de usar vídeo. Análise estritamente via skill `watch` (`claude-video`).
- **Ajuste visual dentro da rota (P-15):** Pedidos de ajuste visual agrupados em lote, classificados e registrados em `docs/ajustes.md`, sem sair da camada.
- **Escolhas exatas (P-16):** Tipografia, disposição em grade, tipos de itens e componentes seguem `docs/escolhas.md`.
- **Referência por elemento (P-17):** Elemento visual novo ou alterado requer referência concreta aprovada em `docs/refs/mapa-elementos.md`. Sem referência, pedir material ao usuário.
- **Efeitos intencionais (P-18):** Microinterações novas ou alteradas exigem propósito, parâmetros e referência aprovados em `docs/refs/mapa-efeitos.md`, consultando o painel "Onde procurar".
- **Nenhum segredo em arquivo versionado:** Senhas, tokens e chaves ficam estritamente em `.env` (ignorado pelo git).

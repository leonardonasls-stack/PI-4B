# CHANGELOG

Histórico detalhado de commits e evolução do projeto **Vacina Alagoas — Projeto Integrador IV-B**.

---

| Código do Commit | Data / Hora | Autor | Descrição das Alterações |
| :--- | :---: | :---: | :--- |
| [`cba7e82`](https://github.com/leonardonasls-stack/PI-4B/commit/cba7e820ebabb462d1735f1428e276e618b98c03) | 07/11/2026 16:44 | Leonardo Nascimento | **Correção de binding de busca automática de CEP no admin e busca por CEP no portal público**<br>• Ajuste da integração via ViaCEP para preenchimento de logradouro e bairro.<br>• Implementação de filtro inteligente por CEP no frontend público. |
| [`a61d123`](https://github.com/leonardonasls-stack/PI-4B/commit/a61d123e4172ccc528098bb2fba901d749f9e12d) | 07/11/2026 16:37 | Leonardo Nascimento | **Supressão do aviso do Tailwind Play CDN no console**<br>• Configuração para evitar poluição de logs no console do navegador em `admin.html`. |
| [`c3dd631`](https://github.com/leonardonasls-stack/PI-4B/commit/c3dd631e524e06081d2a57d58f6e8cca00764093) | 07/11/2026 13:02 | Leonardo Nascimento | **Correção de tipagem e importação em `point_service.py`**<br>• Importação de `Optional` para compatibilidade total de inicialização da API FastAPI. |
| [`5a7ca03`](https://github.com/leonardonasls-stack/PI-4B/commit/5a7ca0311ca21e8df8dda7c42c13ae13d2d44323) | 07/11/2026 12:56 | Leonardo Nascimento | **Modernização visual de modais e inputs**<br>• Remoção de bordas pesadas de cards e modernização dos campos de entrada.<br>• Padronização da identidade visual sem acoplamento a nomes governamentais desnecessários. |
| [`4556327`](https://github.com/leonardonasls-stack/PI-4B/commit/4556327c504fbdbafee886825de58b6ac4c069a0) | 07/11/2026 12:49 | Leonardo Nascimento | **Modernização da navegação (Navbar)**<br>• Adoção de ícones SVG nítidos e simplificação dos menus de topo.<br>• Melhoria na hierarquia visual e navegação responsiva. |
| [`9c9f6f7`](https://github.com/leonardonasls-stack/PI-4B/commit/9c9f6f7a3515c046fb80dfdf24ae282e95a54f8d) | 07/11/2026 12:42 | Leonardo Nascimento | **Adoção do Vue 3 via CDN no portal público e painel administrativo**<br>• Reestruturação reativa das views para melhor gerenciamento de estado e binding de dados.<br>• Eliminação de manipulações manuais repetitivas do DOM. |
| [`357f16d`](https://github.com/leonardonasls-stack/PI-4B/commit/357f16d5ad11fcc7d7f63a54bba71304bd4e239c) | 07/11/2026 12:21 | Leonardo Nascimento | **Busca por CEP no painel admin e simplificação de campos**<br>• Integração com serviço de CEP para autocompletar endereço e bairro.<br>• Ocultação de campos técnicos de latitude/longitude para facilitar cadastro operacional. |
| [`09bd041`](https://github.com/leonardonasls-stack/PI-4B/commit/09bd041217f4b586aa4c444b5f2b22949c09b4ec) | 07/11/2026 12:19 | Leonardo Nascimento | **Aprimoramento de busca textual de postos no backend**<br>• Filtro estendido para pesquisa por endereço, bairro e CEP diretamente nas queries SQL. |
| [`a10b785`](https://github.com/leonardonasls-stack/PI-4B/commit/a10b78566eabc9de6566878c3e55eb45478d62c8) | 07/11/2026 12:09 | Leonardo Nascimento | **Limpeza visual no admin (remoção de card de telemetria)**<br>• Remoção do componente de cadeia de frio não contemplado no escopo do MVP. |
| [`be0560f`](https://github.com/leonardonasls-stack/PI-4B/commit/be0560fa1aca01c6bc41eca22000d5c3b544f246) | 07/11/2026 12:03 | Leonardo Nascimento | **Refatoração visual do painel administrativo**<br>• Simplificação das seções de segurança e foco na gestão dos postos de vacinação. |
| [`2090eb1`](https://github.com/leonardonasls-stack/PI-4B/commit/2090eb1436c958a24559470f04713d4745d152f7) | 07/11/2026 12:00 | Leonardo Nascimento | **Tratamento de rate limit e feedback de sessão no admin**<br>• Mensagens claras de bloqueio temporário por excesso de requisições e renovação de token. |
| [`3fd5038`](https://github.com/leonardonasls-stack/PI-4B/commit/3fd503811d73fe3e67f22e6406c282ec372daaee) | 07/11/2026 12:00 | Leonardo Nascimento | **Modal de autenticação administrativa no portal público**<br>• Acesso rápido para administradores via popup elegante com validação em tempo real. |
| [`9e0aa42`](https://github.com/leonardonasls-stack/PI-4B/commit/9e0aa42ce3ab5b1d34f3812c2d49af9bc03fd547) | 07/11/2026 12:00 | Leonardo Nascimento | **Refinamento de payload JWT e documentação OpenAPI**<br>• Inclusão de claims semânticas e sincronização de esquemas de segurança. |
| [`020ce43`](https://github.com/leonardonasls-stack/PI-4B/commit/020ce439907a5ac2470562025d6265678540ab34) | 07/11/2026 12:00 | Leonardo Nascimento | **Implementação de middleware de rate limiting**<br>• Proteção contra força bruta em endpoints sensíveis e autenticação. |
| [`97dd939`](https://github.com/leonardonasls-stack/PI-4B/commit/97dd9397d10fec307fb7b92066e49d0ced5df1e5) | 04/11/2026 06:07 | Luiz | **Reorganização da árvore de documentação e relatório de implementação**<br>• Padronização dos arquivos na pasta `docs/` (`api.md`, `arquitetura.md`, `requisitos.md`, etc.).<br>• Eliminação de arquivos de documentação obsoletos e duplicados. |
| [`ed07581`](https://github.com/leonardonasls-stack/PI-4B/commit/ed07581fcc9e0bb02449538fb1d2fb346514d8bd) | 04/11/2026 05:52 | Luiz | **Correção de rota estática no Nginx e scroll suave**<br>• Roteamento direto de `admin.html` no proxy Nginx.<br>• Função de rolagem suave para a seção do Guia de Vacinação. |
| [`45014a3`](https://github.com/leonardonasls-stack/PI-4B/commit/45014a39ac27da68cbc9fca588405c23ba7cc662) | 04/11/2026 05:04 | Luiz | **Melhorias de UX desktop e proxy para documentação**<br>• Ancoragem aprimorada, botão de Disque Saúde 136 para desktop e redirecionamento de `/docs` no Nginx. |
| [`32937ec`](https://github.com/leonardonasls-stack/PI-4B/commit/32937ec41eaae2e2f9dd86c19c9415f680e0f557) | 04/11/2026 04:46 | Luiz | **Registro de implementação de botões e modais funcionais**<br>• Documentação das melhorias interativas implementadas no frontend. |
| [`16036b2`](https://github.com/leonardonasls-stack/PI-4B/commit/16036b2d060a0791ab294a4ea6ab0f8b8a99b9ce) | 04/11/2026 04:43 | Luiz | **Conexão integral de botões, modais de FAQ/Calendário e exportação**<br>• Modais acessíveis de perguntas frequentes e calendário de doses.<br>• Exportação de dados e correções de acessibilidade WCAG. |
| [`9aa2aa3`](https://github.com/leonardonasls-stack/PI-4B/commit/9aa2aa363b87b51b277e408551c77b4537b05cb5) | 04/11/2026 04:27 | Luiz | **Polimento de interface e aprimoramento do mapa com rotas**<br>• Remoção de badges visuais desnecessários.<br>• Padronização de botões e integração com rotas do Google Maps a partir do mapa. |
| [`efbf7b7`](https://github.com/leonardonasls-stack/PI-4B/commit/efbf7b7ec156db30f9f0cf740811d256abf8b7c4) | 04/11/2026 04:00 | Luiz | **Conexão de edição, exclusão e sincronização real no Admin**<br>• Integração completa do frontend administrativo com os endpoints de CRUD do backend. |
| [`2204404`](https://github.com/leonardonasls-stack/PI-4B/commit/2204404391570a6e5d84d04e2edf552c8cc4b307) | 04/11/2026 03:47 | Luiz | **Implementação de rotas completas de CRUD de postos no backend**<br>• Criação dos métodos `PUT /vaccination-points/{id}` e `DELETE /vaccination-points/{id}`.<br>• Endpoint de detalhe unitário `GET /vaccination-points/detail/{id}`. |
| [`6088102`](https://github.com/leonardonasls-stack/PI-4B/commit/6088102b4ffac856bbf08c1e413962694803f5cd) | 04/11/2026 03:26 | Luiz | **Handoff de design e relatório comparativo**<br>• Documentação de antes/depois da interface e atualização do guia de estilo. |
| [`a1dc884`](https://github.com/leonardonasls-stack/PI-4B/commit/a1dc8845b52b452b41f6ffcda72fec16cccf6766) | 04/11/2026 03:14 | Luiz | **Reorganização estrutural e hierarquia intuitiva de layout (Camada 3)**<br>• Otimização do fluxo visual, espaçamentos e legibilidade dos componentes da aplicação. |
| [`15bf7c0`](https://github.com/leonardonasls-stack/PI-4B/commit/15bf7c0626c5acbbfc7eb62df63f33e107d61351) | 04/11/2026 02:54 | Luiz | **Iconografia padronizada e refinamento institucional (Camada 2)**<br>• Remoção de elementos visuais genéricos gerados por IA.<br>• Adoção de iconografia coesa e alinhada à área da saúde pública. |
| [`5a229aa`](https://github.com/leonardonasls-stack/PI-4B/commit/5a229aa0853c298699c32285fb67b9f368f63212) | 03/11/2026 22:15 | Luiz | **Acessibilidade base e metadados institucionais (Camada 1)**<br>• Inclusão de atributos ARIA, contrastes adequados e metadados Open Graph. |
| [`af8c3b8`](https://github.com/leonardonasls-stack/PI-4B/commit/af8c3b864662c33361b92df86953ba56916dd2ca) | 03/11/2026 22:00 | Luiz | **Adoção do playbook de engenharia e diretrizes de desenvolvimento**<br>• Estruturação de boas práticas para commits e organização do código. |
| [`eb57427`](https://github.com/leonardonasls-stack/PI-4B/commit/eb57427ef9ba5fbb0aa18f87e64067d8be287709) | 03/11/2026 21:32 | Leonardo Nascimento | **Configuração da aplicação com `pydantic-settings` e proteção de credenciais**<br>• Remoção de dados sensíveis e credenciais hardcoded em `config.py`.<br>• Carregamento dinâmico via `.env` com fallback seguro. |
| [`02aee9f`](https://github.com/leonardonasls-stack/PI-4B/commit/02aee9f57cc14be96b8542b47525213998a00c7c) | 01/11/2026 12:41 | Leonardo Nascimento | **Auditoria técnica para conclusão do modelo CRUD**<br>• Mapeamento de requisitos faltantes e relatório `AUDITORIA_CRUD.md`. |
| [`08d84d1`](https://github.com/leonardonasls-stack/PI-4B/commit/08d84d18259e12f62fd19119fa7eb097e8c539cc) | 01/11/2026 00:05 | Leonardo Nascimento | **Inclusão da documentação técnica aprofundada da API RESTful**<br>• Detalhamento de endpoints, schemas de retorno e fluxos de autenticação. |
| [`ca2a19e`](https://github.com/leonardonasls-stack/PI-4B/commit/ca2a19e605a712864305cfef9ea21e786bcf9749) | 01/11/2026 00:05 | Leonardo Nascimento | **Documentação técnica inicial da API RESTful**<br>• Criação do arquivo de documentação técnica inicial da API. |
| [`240bbe7`](https://github.com/leonardonasls-stack/PI-4B/commit/240bbe7b3eb32f8c54b7c31ecfc2d91173ba5174) | 31/10/2026 23:48 | Leonardo Nascimento | **Pipeline de CI no GitHub Actions e suíte de testes assíncrona**<br>• Configuração do workflow `.github/workflows/ci.yml`.<br>• Testes automatizados com `pytest` e isolamento de banco. |
| [`7705aa2`](https://github.com/leonardonasls-stack/PI-4B/commit/7705aa2a51bf3fca1e1b7d91e7657e0e46fb42e5) | 31/10/2026 23:44 | Leonardo Nascimento | **Atualização completa da documentação técnica (README.md)**<br>• Inclusão de diagramas de arquitetura, mapeamento de portas e endpoints RESTful. |
| [`49e9cda`](https://github.com/leonardonasls-stack/PI-4B/commit/49e9cda21616e608f0a8f4b4f14a5506e0a5f12c) | 31/10/2026 23:28 | Leonardo Nascimento | **Correção de validação HTML (html-validate) na página pública**<br>• Adequação às normas HTML5 e acessibilidade de links. |
| [`dca8246`](https://github.com/leonardonasls-stack/PI-4B/commit/dca82467bae186623a2c60e947835c8210a8d29a) | 31/10/2026 23:21 | Leonardo Nascimento | **Ajuste da geolocalização e ordenação por proximidade**<br>• Busca sob demanda com cálculo de distância e ordenação dinâmica. |
| [`334ec00`](https://github.com/leonardonasls-stack/PI-4B/commit/334ec00768088aed4060b88876e72c940765a83f) | 31/10/2026 23:07 | Leonardo Nascimento | **Botão de limpar filtros e integração Leaflet**<br>• Filtros interativos e padronização visual dos cartões de postos. |
| [`f9d4a7a`](https://github.com/leonardonasls-stack/PI-4B/commit/f9d4a7a406cc2337f77fdf9cd2f7cae44514b570) | 31/10/2026 22:41 | Leonardo Nascimento | **Desacoplamento backend/frontend (API RESTful pura)**<br>• Remoção do Jinja2 e separação da camada estática servida pelo Nginx. |
| [`3e2e8fb`](https://github.com/leonardonasls-stack/PI-4B/commit/3e2e8fb48518e6d8f98a9c7edfabdf82e4be4e6d) | 31/10/2026 22:17 | Leonardo Nascimento | **Conexão real com banco de dados PostgreSQL**<br>• Remoção de dados mockados e sincronização completa com os endpoints. |
| [`b8165aa`](https://github.com/leonardonasls-stack/PI-4B/commit/b8165aabeb9743cf098e046072166e7f6dd1e838) | 31/10/2026 19:51 | Leonardo Nascimento | **Integração com Google Maps e coordenadas geográficas**<br>• Exposição de latitude/longitude e links de rota direta no Google Maps. |
| [`adfcd40`](https://github.com/leonardonasls-stack/PI-4B/commit/adfcd408bc6d5706875109f21d036f8841f7f59b) | 31/10/2026 19:35 | Leonardo Nascimento | **Bot de enriquecimento de dados via OpenStreetMap**<br>• Endpoints de pré-visualização e confirmação de postos de saúde reais. |
| [`d84ddda`](https://github.com/leonardonasls-stack/PI-4B/commit/d84dddaf7805eedb12157e3fec647ea7f8dd611d) | 31/10/2026 19:19 | Leonardo Nascimento | **Correção de autenticação e hash Bcrypt**<br>• Resolução de credenciais do administrador inicial e validação de tokens JWT. |
| [`5a32b45`](https://github.com/leonardonasls-stack/PI-4B/commit/5a32b45476c59e1158c58875a4bd9f6470a0b441) | 31/10/2026 19:06 | Leonardo Nascimento | **Criação inicial do projeto Vacina Alagoas**<br>• Configuração da infraestrutura Docker Compose, PostgreSQL 16, FastAPI e Nginx. |

---

### Resumo dos Identificadores de Commit (Hash Completo)

- `cba7e820ebabb462d1735f1428e276e618b98c03`
- `a61d123e4172ccc528098bb2fba901d749f9e12d`
- `c3dd631e524e06081d2a57d58f6e8cca00764093`
- `5a7ca0311ca21e8df8dda7c42c13ae13d2d44323`
- `4556327c504fbdbafee886825de58b6ac4c069a0`
- `9c9f6f7a3515c046fb80dfdf24ae282e95a54f8d`
- `357f16d5ad11fcc7d7f63a54bba71304bd4e239c`
- `09bd041217f4b586aa4c444b5f2b22949c09b4ec`
- `a10b78566eabc9de6566878c3e55eb45478d62c8`
- `be0560fa1aca01c6bc41eca22000d5c3b544f246`
- `2090eb1436c958a24559470f04713d4745d152f7`
- `3fd503811d73fe3e67f22e6406c282ec372daaee`
- `9e0aa42ce3ab5b1d34f3812c2d49af9bc03fd547`
- `020ce439907a5ac2470562025d6265678540ab34`
- `97dd9397d10fec307fb7b92066e49d0ced5df1e5`
- `ed07581fcc9e0bb02449538fb1d2fb346514d8bd`
- `45014a39ac27da68cbc9fca588405c23ba7cc662`
- `32937ec41eaae2e2f9dd86c19c9415f680e0f557`
- `16036b2d060a0791ab294a4ea6ab0f8b8a99b9ce`
- `9aa2aa363b87b51b277e408551c77b4537b05cb5`
- `efbf7b7ec156db30f9f0cf740811d256abf8b7c4`
- `2204404391570a6e5d84d04e2edf552c8cc4b307`
- `6088102b4ffac856bbf08c1e413962694803f5cd`
- `a1dc8845b52b452b41f6ffcda72fec16cccf6766`
- `15bf7c0626c5acbbfc7eb62df63f33e107d61351`
- `5a229aa0853c298699c32285fb67b9f368f63212`
- `af8c3b864662c33361b92df86953ba56916dd2ca`
- `eb57427ef9ba5fbb0aa18f87e64067d8be287709`
- `02aee9f57cc14be96b8542b47525213998a00c7c`
- `08d84d18259e12f62fd19119fa7eb097e8c539cc`
- `ca2a19e605a712864305cfef9ea21e786bcf9749`
- `240bbe7b3eb32f8c54b7c31ecfc2d91173ba5174`
- `7705aa2a51bf3fca1e1b7d91e7657e0e46fb42e5`
- `49e9cda21616e608f0a8f4b4f14a5506e0a5f12c`
- `dca82467bae186623a2c60e947835c8210a8d29a`
- `334ec00768088aed4060b88876e72c940765a83f`
- `f9d4a7a406cc2337f77fdf9cd2f7cae44514b570`
- `3e2e8fb48518e6d8f98a9c7edfabdf82e4be4e6d`
- `b8165aabeb9743cf098e046072166e7f6dd1e838`
- `adfcd408bc6d5706875109f21d036f8841f7f59b`
- `d84dddaf7805eedb12157e3fec647ea7f8dd611d`
- `5a32b45476c59e1158c58875a4bd9f6470a0b441`

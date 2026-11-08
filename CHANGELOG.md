# CHANGELOG

Histórico detalhado de commits e evolução do projeto **Vacina Alagoas — Projeto Integrador IV-B**.

---

| Código do Commit | Data / Hora | Autor | Descrição das Alterações |
| :--- | :---: | :---: | :--- |
| [`9990f84`](https://github.com/leonardonasls-stack/PI-4B/commit/9990f8467c20e296951e9796dc8994eda19337cf) | 08/11/2026 01:05 | Leonardo Nascimento | **Normalização de campos de endereço (Logradouro, Número, CEP)**<br>• Adição das colunas atômicas `logradouro`, `number` e `cep` na tabela `vaccination_points` e nos schemas Pydantic.<br>• Extração automática de código postal e número predial pelo robô do OpenStreetMap / Nominatim.<br>• Reformulação do formulário no painel administrativo com inputs dedicados para cada componente de endereço.<br>• Migração e atualização dos registros existentes e do script `sql/seed.sql`. |
| [`f226fd6`](https://github.com/leonardonasls-stack/PI-4B/commit/f226fd6d03d523776f47175716485ce2be3b94a0) | 08/11/2026 00:17 | Leonardo Nascimento | **Integração de atualizações entre branches (main & luiz)**<br>• Sincronização do README.md refatorado, documentação e conciliação do histórico do projeto. |
| [`b022e13`](https://github.com/leonardonasls-stack/PI-4B/commit/b022e13ec736424d8cd3e6391bbc5e058fcc04ae) | 07/11/2026 22:56 | Luiz | **Unificação do painel de filtros, inclusão de cidade nos endereços e correção do ícone de detalhes**<br>• Eliminação da barra de filtros flutuante solta, integrando título dos resultados, indicador de auditoria em tempo real, controles de ordenação/visão e chips de imunizantes em um único painel coeso.<br>• Inclusão formal do nome do município em todos os endereços (`Bairro, Cidade • Logradouro`), tanto no Card Herói quanto nos cards padrão do grid.<br>• Substituição do ícone SVG distorcido do botão *Detalhes* por um ícone vetorial padronizado. |
| [`ce7e147`](https://github.com/leonardonasls-stack/PI-4B/commit/ce7e14762e516a017720edb25328376001df3606) | 07/11/2026 22:33 | Luiz | **Renomeação semântica de Calendário para "Vacinas por Idade"**<br>• Adequação da terminologia na barra de navegação superior (`[Vacinas por Idade]`) com novo ícone vetorial de perfil familiar.<br>• Reestruturação da seção para `id="vacinas-por-idade"` com título *Vacinas por Idade e Fase da Vida*, alinhando com a consulta por faixas etárias do SUS. |
| [`fcad710`](https://github.com/leonardonasls-stack/PI-4B/commit/fcad7103afb5db150dfa8593f975d8eb87f50a9d) | 07/11/2026 22:13 | Luiz | **Implementação de Seção de Calendário Nacional e navegação inteligente no portal**<br>• Criação da seção completa de Calendário Nacional de Vacinação integrada na página com abas interativas para 4 faixas etárias (Crianças, Adolescentes, Adultos & Idosos e Gestantes).<br>• Integração com os postos: botões *"Buscar Postos"* em cada linha que filtram automaticamente a vacina e rolam para as UBS disponíveis. |
| [`b04f4ff`](https://github.com/leonardonasls-stack/PI-4B/commit/b04f4ff6756627ad9b733925863f4e6dc0833af0) | 07/11/2026 21:56 | Luiz | **Substituição de tag Material Symbols por SVG nativo no campo de busca**<br>• Eliminação do texto literal `search` sobreposto ao placeholder no campo de texto de Bairro ou CEP.<br>• Substituição por ícone vetorial SVG inline padronizado. |
| [`1791174`](https://github.com/leonardonasls-stack/PI-4B/commit/1791174a7b6cdbb84ae2a61b8e20a58b3ef958f6) | 07/11/2026 21:50 | Luiz | **Restauração de window.aplicarFiltros e declaração de window.executarBusca**<br>• Correção do erro em runtime `TypeError: window.aplicarFiltros is not a function at carregarPostos` em `index.html`.<br>• Restauração completa do mecanismo reativo de filtragem e ordenação por proximidade/alfabética no portal do cidadão. |
| [`5d8b5e0`](https://github.com/leonardonasls-stack/PI-4B/commit/5d8b5e07829fc91ddbc61a37ac0cf510e90ca1f2) | 07/11/2026 20:11 | Luiz | **Reestruturação da busca unificada com abas de intenção e card campeão**<br>• Separação em abas (*Mais Próximos de Mim*, *Por Bairro ou CEP* e *Por Município*).<br>• Exibição em destaque do posto mais próximo (*Card Campeão*) com cálculo dinâmico de distância. |
| [`0967542`](https://github.com/leonardonasls-stack/PI-4B/commit/0967542e0370d8e87e76c712c94481505bef2145) | 07/11/2026 19:54 | Luiz | **Busca de proximidade inteligente 1-click com GPS, CEP e memória local**<br>• Persistência da última localização conhecida para buscas instantâneas.<br>• Fallback transparente entre GPS e geocodificação por CEP. |
| [`2e7e022`](https://github.com/leonardonasls-stack/PI-4B/commit/2e7e0220c7327b5708ca7158536bf7240443d47b) | 07/11/2026 19:32 | Luiz | **Modal nativo de feedback no admin e correção de z-index**<br>• Substituição de `alert()` e `confirm()` nativos do navegador por modais customizados acessíveis.<br>• Correção de camadas de sobreposição (*z-index*) entre guias e assistentes. |
| [`38881ec`](https://github.com/leonardonasls-stack/PI-4B/commit/38881ec791e6678ca64b3b65c6304489a668a424) | 07/11/2026 19:07 | Luiz | **Polimento de botões no painel administrativo**<br>• Remoção de caracteres duplicados em botões de cadastro e destaque para o botão de acesso ao portal público. |
| [`0d07b25`](https://github.com/leonardonasls-stack/PI-4B/commit/0d07b25c64164d7c4aa6997fa9d9b265706448f6) | 07/11/2026 19:03 | Luiz | **Reestruturação de botões auxiliares e sanitização de links**<br>• Limpeza de links da barra superior e botões de ação na tabela de postos. |
| [`ba39138`](https://github.com/leonardonasls-stack/PI-4B/commit/ba3913866a6f17050ad5ca1785a27276cec09985) | 07/11/2026 18:52 | Luiz | **Remoção de banner escuro residual e liberação do scroll vertical**<br>• Correção do layout bloqueado por overflow e remoção de elementos visuais residuais. |
| [`0ffca06`](https://github.com/leonardonasls-stack/PI-4B/commit/0ffca068d0f5191249f9f56c682648bb801a4a3c) | 07/11/2026 18:35 | Leonardo Nascimento | **Refatoração completa do README.md com diretrizes de boas práticas**<br>• Atualização de arquitetura, contratos RESTful, novos recursos (Vue 3, CEP, Rate Limiting) e eliminação de redundâncias. |
| [`8bd94fa`](https://github.com/leonardonasls-stack/PI-4B/commit/8bd94fa64c84a4aed2453640865e6f875547ba42) | 07/11/2026 18:34 | Luiz | **Escopo do Vue no body para destravar modais e contenção de largura**<br>• Ajuste da montagem do Vue para evitar travamento de modais globais e padronização da largura máxima da interface. |
| [`13ed18b`](https://github.com/leonardonasls-stack/PI-4B/commit/13ed18b736b3b1e7776ff5663065a72d1d179188) | 07/11/2026 18:27 | Luiz | **Correção de escopo de modais e remoção de validação que travava wizard**<br>• Eliminação de bloqueios de validação HTML nativa para fluxo de passos mais fluido. |
| [`b77c652`](https://github.com/leonardonasls-stack/PI-4B/commit/b77c6525b9750299ccca0210d54d7edf307fa917) | 07/11/2026 18:16 | Luiz | **Robô OSM no topo com escopo por cidade e modais de cadastro**<br>• Posicionamento do robô de enriquecimento com filtro de abrangência e modal dedicado para novo posto. |
| [`68b73b8`](https://github.com/leonardonasls-stack/PI-4B/commit/68b73b8669899948d91c346e5cf36dc24b591f01) | 07/11/2026 17:57 | Luiz | **Implementação de wizard passo a passo e simplificação visual**<br>• Criação de fluxo guiado para cadastro de postos e remoção de indicadores fora de escopo. |
| [`8152c06`](https://github.com/leonardonasls-stack/PI-4B/commit/8152c06e6313fda09d235c2940d3e8712e3c46b4) | 07/11/2026 17:55 | Leonardo Nascimento | **Correção dos endpoints de busca de postos na Seção 3 do Admin**<br>• Ajuste de chamadas para `/vaccination-points/1` e `/vaccination-points/2`, corrigindo tela em branco na listagem. |
| [`0707858`](https://github.com/leonardonasls-stack/PI-4B/commit/07078587ce946093e04f8031c6359b02b3b8faf2) | 07/11/2026 17:35 | Luiz | **Correção de submissão do formulário no admin**<br>• Vinculação correta do evento de submit ao método `salvarPosto` com feedback explícito. |
| [`7730498`](https://github.com/leonardonasls-stack/PI-4B/commit/77304981dfd10bac01ceffe815669d6dd4560d36) | 07/11/2026 17:27 | Luiz | **Ajuste de busca para endpoints canônicos no admin**<br>• Compatibilização com o padrão REST do backend. |
| [`3b3648f9`](https://github.com/leonardonasls-stack/PI-4B/commit/3b3648f988c8b648d6823efb2000c4ff3d05cf19) | 07/11/2026 16:59 | Luiz | **Merge de atualizações do origin/luiz com suporte a Vue 3**<br>• Resolução de conflitos em `admin.html` e unificação de templates reativos. |
| [`cba7e82`](https://github.com/leonardonasls-stack/PI-4B/commit/cba7e820ebabb462d1735f1428e276e618b98c03) | 07/11/2026 16:44 | Leonardo Nascimento | **Correção de binding de busca automática de CEP no admin e no portal público**<br>• Integração com ViaCEP e busca instantânea no frontend. |
| [`a61d123`](https://github.com/leonardonasls-stack/PI-4B/commit/a61d123e4172ccc528098bb2fba901d749f9e12d) | 07/11/2026 16:37 | Leonardo Nascimento | **Supressão do aviso do Tailwind Play CDN no console**<br>• Redução de ruído nos logs de desenvolvedor. |
| [`c3dd631`](https://github.com/leonardonasls-stack/PI-4B/commit/c3dd631e524e06081d2a57d58f6e8cca00764093) | 07/11/2026 13:02 | Leonardo Nascimento | **Correção de tipagem e importação em `point_service.py`**<br>• Importação de `Optional` para compatibilidade com Python 3.11+. |
| [`5a7ca03`](https://github.com/leonardonasls-stack/PI-4B/commit/5a7ca0311ca21e8df8dda7c42c13ae13d2d44323) | 07/11/2026 12:56 | Leonardo Nascimento | **Modernização visual de modais e inputs**<br>• Simplificação visual e eliminação de bordas pesadas. |
| [`4556327`](https://github.com/leonardonasls-stack/PI-4B/commit/4556327c504fbdbafee886825de58b6ac4c069a0) | 07/11/2026 12:49 | Leonardo Nascimento | **Modernização da barra de navegação com ícones SVG**<br>• Navegação institucional limpa e acessível. |
| [`9c9f6f7`](https://github.com/leonardonasls-stack/PI-4B/commit/9c9f6f7a3515c046fb80dfdf24ae282e95a54f8d) | 07/11/2026 12:42 | Leonardo Nascimento | **Adoção do Vue 3 via CDN no portal público e painel administrativo**<br>• Reestruturação reativa completa da interface. |
| [`357f16d`](https://github.com/leonardonasls-stack/PI-4B/commit/357f16d5ad11fcc7d7f63a54bba71304bd4e239c) | 07/11/2026 12:21 | Leonardo Nascimento | **Busca por CEP no painel admin e simplificação de campos**<br>• Autocompletar de endereços e ocultação de campos desnecessários. |
| [`09bd041`](https://github.com/leonardonasls-stack/PI-4B/commit/09bd041217f4b586aa4c444b5f2b22949c09b4ec) | 07/11/2026 12:19 | Leonardo Nascimento | **Aprimoramento de busca textual de postos no backend**<br>• Filtro amplo por endereço, bairro e CEP direto no SQL. |
| [`a10b785`](https://github.com/leonardonasls-stack/PI-4B/commit/a10b78566eabc9de6566878c3e55eb45478d62c8) | 07/11/2026 12:09 | Leonardo Nascimento | **Limpeza visual no admin (remoção de telemetria)**<br>• Foco nas funcionalidades essenciais do MVP. |
| [`be0560f`](https://github.com/leonardonasls-stack/PI-4B/commit/be0560fa1aca01c6bc41eca22000d5c3b544f246) | 07/11/2026 12:03 | Leonardo Nascimento | **Refatoração visual do painel administrativo**<br>• Layout limpo focado na gestão das unidades. |
| [`2090eb1`](https://github.com/leonardonasls-stack/PI-4B/commit/2090eb1436c958a24559470f04713d4745d152f7) | 07/11/2026 12:00 | Leonardo Nascimento | **Tratamento de rate limit e feedback de sessão no admin**<br>• Feedback amigável para bloqueios e renovação de tokens. |
| [`3fd5038`](https://github.com/leonardonasls-stack/PI-4B/commit/3fd503811d73fe3e67f22e6406c282ec372daaee) | 07/11/2026 12:00 | Leonardo Nascimento | **Modal de autenticação administrativa no portal público**<br>• Acesso direto e seguro para gestores do sistema. |
| [`9e0aa42`](https://github.com/leonardonasls-stack/PI-4B/commit/9e0aa42ce3ab5b1d34f3812c2d49af9bc03fd547) | 07/11/2026 12:00 | Leonardo Nascimento | **Refinamento de payload JWT e documentação OpenAPI**<br>• Padronização de claims e esquemas OAuth2. |
| [`020ce43`](https://github.com/leonardonasls-stack/PI-4B/commit/020ce439907a5ac2470562025d6265678540ab34) | 07/11/2026 12:00 | Leonardo Nascimento | **Implementação de middleware de rate limiting**<br>• Proteção contra abuso e ataques de força bruta. |
| [`1053939`](https://github.com/leonardonasls-stack/PI-4B/commit/105393978d86ae8a6e7ae68d6920581e6e972cee) | 04/11/2026 18:14 | Luiz | **Uso de URL relativa no proxy Nginx para chamadas à API**<br>• Evita problemas de porta fixa e facilita execução em diferentes hosts. |
| [`97dd939`](https://github.com/leonardonasls-stack/PI-4B/commit/97dd9397d10fec307fb7b92066e49d0ced5df1e5) | 04/11/2026 06:07 | Luiz | **Reorganização da documentação e relatório de implementação**<br>• Estruturação de diretórios em `docs/` e remoção de arquivos legados. |
| [`ed07581`](https://github.com/leonardonasls-stack/PI-4B/commit/ed07581fcc9e0bb02449538fb1d2fb346514d8bd) | 04/11/2026 05:52 | Luiz | **Correção de rota no Nginx e scroll suave**<br>• Rota direta para `admin.html` e melhoria de navegação interna. |
| [`45014a3`](https://github.com/leonardonasls-stack/PI-4B/commit/45014a39ac27da68cbc9fca588405c23ba7cc662) | 04/11/2026 05:04 | Luiz | **Melhorias de UX desktop e proxy para documentação**<br>• Acesso rápido ao Disque 136 e integração de rotas `/docs`. |
| [`32937ec`](https://github.com/leonardonasls-stack/PI-4B/commit/32937ec41eaae2e2f9dd86c19c9415f680e0f557) | 04/11/2026 04:46 | Luiz | **Registro de implementação de botões e modais funcionais**<br>• Documentação de componentes visuais do frontend. |
| [`16036b2`](https://github.com/leonardonasls-stack/PI-4B/commit/16036b2d060a0791ab294a4ea6ab0f8b8a99b9ce) | 04/11/2026 04:43 | Luiz | **Conexão integral de botões, modais de FAQ e exportação**<br>• Suporte a exportação de dados e conformidade WCAG. |
| [`9aa2aa3`](https://github.com/leonardonasls-stack/PI-4B/commit/9aa2aa363b87b51b277e408551c77b4537b05cb5) | 04/11/2026 04:27 | Luiz | **Polimento de interface e mapa com rotas do Google Maps**<br>• Integração de rota ponto a ponto direta a partir dos marcadores. |
| [`efbf7b7`](https://github.com/leonardonasls-stack/PI-4B/commit/efbf7b7ec156db30f9f0cf740811d256abf8b7c4) | 04/11/2026 04:00 | Luiz | **Conexão de edição, exclusão e sincronização real no Admin**<br>• Integração completa com o backend via CRUD REST. |
| [`2204404`](https://github.com/leonardonasls-stack/PI-4B/commit/2204404391570a6e5d84d04e2edf552c8cc4b307) | 04/11/2026 03:47 | Luiz | **Implementação de rotas completas de CRUD de postos no backend**<br>• Endpoints de PUT, DELETE e GET unitário no FastAPI. |
| [`6088102`](https://github.com/leonardonasls-stack/PI-4B/commit/6088102b4ffac856bbf08c1e413962694803f5cd) | 04/11/2026 03:26 | Luiz | **Handoff de design e relatório comparativo**<br>• Consolidação de design institucional. |
| [`a1dc884`](https://github.com/leonardonasls-stack/PI-4B/commit/a1dc8845b52b452b41f6ffcda72fec16cccf6766) | 04/11/2026 03:14 | Luiz | **Reorganização estrutural e hierarquia de layout (Camada 3)**<br>• Legibilidade e espaçamento dos componentes. |
| [`15bf7c0`](https://github.com/leonardonasls-stack/PI-4B/commit/15bf7c0626c5acbbfc7eb62df63f33e107d61351) | 04/11/2026 02:54 | Luiz | **Iconografia padronizada e refinamento institucional (Camada 2)**<br>• Substituição de ícones genéricos por padronização vetorial. |
| [`5a229aa`](https://github.com/leonardonasls-stack/PI-4B/commit/5a229aa0853c298699c32285fb67b9f368f63212) | 03/11/2026 22:15 | Luiz | **Acessibilidade base e metadados institucionais (Camada 1)**<br>• Inclusão de atributos ARIA e tags Open Graph. |
| [`af8c3b8`](https://github.com/leonardonasls-stack/PI-4B/commit/af8c3b864662c33361b92df86953ba56916dd2ca) | 03/11/2026 22:00 | Luiz | **Adoção do playbook de engenharia e diretrizes de desenvolvimento**<br>• Boas práticas e padronização de commits. |
| [`eb57427`](https://github.com/leonardonasls-stack/PI-4B/commit/eb57427ef9ba5fbb0aa18f87e64067d8be287709) | 03/11/2026 21:32 | Leonardo Nascimento | **Configuração da aplicação com `pydantic-settings` e proteção de credenciais**<br>• Remoção de dados hardcoded e variáveis protegidas em `.env`. |
| [`02aee9f`](https://github.com/leonardonasls-stack/PI-4B/commit/02aee9f57cc14be96b8542b47525213998a00c7c) | 01/11/2026 12:41 | Leonardo Nascimento | **Auditoria técnica para conclusão do modelo CRUD**<br>• Relatório de auditoria e conformidade técnica. |
| [`08d84d1`](https://github.com/leonardonasls-stack/PI-4B/commit/08d84d18259e12f62fd19119fa7eb097e8c539cc) | 01/11/2026 00:05 | Leonardo Nascimento | **Inclusão da documentação técnica aprofundada da API RESTful**<br>• Mapeamento de rotas e contratos JSON. |
| [`ca2a19e`](https://github.com/leonardonasls-stack/PI-4B/commit/ca2a19e605a712864305cfef9ea21e786bcf9749) | 01/11/2026 00:05 | Leonardo Nascimento | **Documentação técnica inicial da API RESTful**<br>• Criação da documentação técnica inicial. |
| [`240bbe7`](https://github.com/leonardonasls-stack/PI-4B/commit/240bbe7b3eb32f8c54b7c31ecfc2d91173ba5174) | 31/10/2026 23:48 | Leonardo Nascimento | **Pipeline de CI no GitHub Actions e suíte de testes assíncrona**<br>• Configuração de CI com PostgreSQL service e testes com pytest. |
| [`7705aa2`](https://github.com/leonardonasls-stack/PI-4B/commit/7705aa2a51bf3fca1e1b7d91e7657e0e46fb42e5) | 31/10/2026 23:44 | Leonardo Nascimento | **Atualização completa da documentação técnica (README.md)**<br>• Guia rápido com Docker Compose e diagramas de serviços. |
| [`49e9cda`](https://github.com/leonardonasls-stack/PI-4B/commit/49e9cda21616e608f0a8f4b4f14a5506e0a5f12c) | 31/10/2026 23:28 | Leonardo Nascimento | **Correção de validação HTML (html-validate) na página pública**<br>• Adequação às normas HTML5 e acessibilidade. |
| [`dca8246`](https://github.com/leonardonasls-stack/PI-4B/commit/dca82467bae186623a2c60e947835c8210a8d29a) | 31/10/2026 23:21 | Leonardo Nascimento | **Ajuste da geolocalização e ordenação por proximidade**<br>• Cálculo de distância via Haversine e ordenação dinâmica. |
| [`334ec00`](https://github.com/leonardonasls-stack/PI-4B/commit/334ec00768088aed4060b88876e72c940765a83f) | 31/10/2026 23:07 | Leonardo Nascimento | **Botão de limpar filtros e integração Leaflet**<br>• Filtros dinâmicos e padronização visual dos cartões. |
| [`f9d4a7a`](https://github.com/leonardonasls-stack/PI-4B/commit/f9d4a7a406cc2337f77fdf9cd2f7cae44514b570) | 31/10/2026 22:41 | Leonardo Nascimento | **Desacoplamento backend/frontend (API RESTful pura)**<br>• Separação estrita de responsabilidades via Nginx e FastAPI. |
| [`3e2e8fb`](https://github.com/leonardonasls-stack/PI-4B/commit/3e2e8fb48518e6d8f98a9c7edfabdf82e4be4e6d) | 31/10/2026 22:17 | Leonardo Nascimento | **Conexão real com banco de dados PostgreSQL**<br>• Eliminação de dados mockados e sincronização com banco. |
| [`b8165aa`](https://github.com/leonardonasls-stack/PI-4B/commit/b8165aabeb9743cf098e046072166e7f6dd1e838) | 31/10/2026 19:51 | Leonardo Nascimento | **Integração com Google Maps e coordenadas geográficas**<br>• Traçado de rotas e coordenadas no backend. |
| [`adfcd40`](https://github.com/leonardonasls-stack/PI-4B/commit/adfcd408bc6d5706875109f21d036f8841f7f59b) | 31/10/2026 19:35 | Leonardo Nascimento | **Bot de enriquecimento de dados via OpenStreetMap**<br>• Mineração com confirmação manual no admin. |
| [`d84ddda`](https://github.com/leonardonasls-stack/PI-4B/commit/d84dddaf7805eedb12157e3fec647ea7f8dd611d) | 31/10/2026 19:19 | Leonardo Nascimento | **Correção de autenticação e hash Bcrypt**<br>• Resolução de credenciais do administrador inicial. |
| [`5a32b45`](https://github.com/leonardonasls-stack/PI-4B/commit/5a32b45476c59e1158c58875a4bd9f6470a0b441) | 31/10/2026 19:06 | Leonardo Nascimento | **Criação inicial do projeto Vacina Alagoas**<br>• Infraestrutura Docker Compose, PostgreSQL 16, FastAPI e Nginx. |

---

### Resumo dos Identificadores de Commit (Hash Completo)

- `9990f8467c20e296951e9796dc8994eda19337cf`
- `f226fd6d03d523776f47175716485ce2be3b94a0`
- `b022e13ec736424d8cd3e6391bbc5e058fcc04ae`
- `ce7e14762e516a017720edb25328376001df3606`
- `fcad7103afb5db150dfa8593f975d8eb87f50a9d`
- `b04f4ff6756627ad9b733925863f4e6dc0833af0`
- `1791174a7b6cdbb84ae2a61b8e20a58b3ef958f6`
- `5d8b5e07829fc91ddbc61a37ac0cf510e90ca1f2`
- `0967542e0370d8e87e76c712c94481505bef2145`
- `2e7e0220c7327b5708ca7158536bf7240443d47b`
- `38881ec791e6678ca64b3b65c6304489a668a424`
- `0d07b25c64164d7c4aa6997fa9d9b265706448f6`
- `ba3913866a6f17050ad5ca1785a27276cec09985`
- `0ffca068d0f5191249f9f56c682648bb801a4a3c`
- `8bd94fa64c84a4aed2453640865e6f875547ba42`
- `13ed18b736b3b1e7776ff5663065a72d1d179188`
- `b77c6525b9750299ccca0210d54d7edf307fa917`
- `68b73b8669899948d91c346e5cf36dc24b591f01`
- `8152c06e6313fda09d235c2940d3e8712e3c46b4`
- `07078587ce946093e04f8031c6359b02b3b8faf2`
- `77304981dfd10bac01ceffe815669d6dd4560d36`
- `3b3648f988c8b648d6823efb2000c4ff3d05cf19`
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
- `105393978d86ae8a6e7ae68d6920581e6e972cee`
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

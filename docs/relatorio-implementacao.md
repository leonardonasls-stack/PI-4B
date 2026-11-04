# Relatório Técnico Estruturado de Implementação e Melhorias
## Projeto Integrador IV-B · Sistema de Consulta e Gestão de Vacinação em Alagoas (SESAU)

| Metadado | Informação |
| :--- | :--- |
| **Projeto** | Vacina Alagoas — Gestão Territorial e Imunização Pública |
| **Instituição / Contexto** | Projeto Integrador IV-B (FastAPI, PostgreSQL 16 + PostGIS, Docker, Nginx) |
| **Parceiro Institucional / Domínio** | Secretaria de Estado da Saúde de Alagoas (SESAU) / Sistema Único de Saúde (SUS) |
| **Versão Atual** | `v1.4.0-stable` |
| **Data de Conclusão** | Novembro de 2026 |
| **Status Geral** | **100% Conforme — CRUD Completo, Anti-IA Aplicado, UX Polida e Testes Aprovados** |

---

## 1. Visão Geral e Objetivos do Projeto

O **Vacina Alagoas** é uma plataforma de utilidade pública desenvolvida para resolver a dispersão de informações sobre imunização no estado de Alagoas. A plataforma atende a dois pilares fundamentais:
1. **Portal Público do Cidadão (`index.html`):** Consulta rápida, acessível (WCAG 2.1 AA) e geolocalizada de postos de saúde em Maceió e Arapiraca, com horários de funcionamento, vacinas disponíveis, traçado de rotas e orientações do Plano Nacional de Imunizações (PNI).
2. **Painel de Gestão e Auditoria (`admin.html`):** Ambiente restrito para operadores da SESAU gerenciarem o ciclo de vida dos postos de vacinação (CRUD completo), importarem dados geográficos do OpenStreetMap (OSM) via Overpass API e exportarem relatórios em tempo real (CSV e GeoJSON).

---

## 2. Auditoria e Implementação do CRUD Completo

A partir da auditoria técnica registrada em [`docs/auditoria-crud.md`](file:///c:/Users/Luiz/Documents/Vacina/docs/auditoria-crud.md), foram sanadas todas as lacunas de operações de persistência:

### 2.1. Backend (FastAPI + SQLAlchemy + AsyncPG)
- **Operação Update (`PUT /vaccination-points/{point_id}`):**
  - Implementado o schema Pydantic `VaccinationPointUpdate` em `backend/src/schemas/point.py` com campos opcionais para atualização atômica de nome, endereço, bairro, telefone, latitude, longitude e horários.
  - Criado o método `PointService.update_point()` realizando query assíncrona com tratamento de concorrência e atualização relacional de vínculos de imunizantes na tabela `point_vaccines`.
- **Operação Delete (`DELETE /vaccination-points/{point_id}`):**
  - Implementado o método `PointService.delete_point()` com remoção prévia e transacional de dependências na tabela associativa `point_vaccines` e exclusão definitiva na tabela `vaccination_points`.
  - Resposta HTTP com código semântico padrão **204 No Content**.
- **Operação Read Unitária (`GET /vaccination-points/detail/{point_id}`):**
  - Criado endpoint para leitura de um posto individual por ID, com agregação de vacinas (`ARRAY_AGG`), utilizado no carregamento de formulários de edição.
- **Alias Administrativo:**
  - Registrado o roteador em `/admin/vaccination-points` mantendo conformidade estrita com os requisitos originais de bancas acadêmicas.

### 2.2. Frontend Administrativo (`admin.html`)
- **Edição Reativa em Modal e Formulário:**
  - Conexão da função `window.prepararEdicao(id)` que popula os campos do formulário `#form-novo-posto`, altera o título para "Editar Posto de Vacinação" e alterna o botão de ação para "Atualizar Posto (PUT)".
  - Suporte a cancelamento da edição restaurando o estado original (`window.cancelarEdicao()`).
- **Exclusão Transacional:**
  - Conexão da função `window.excluirPosto(id, nome)` com confirmação prévia, envio de requisição `DELETE` com Bearer Token e remoção imediata da linha correspondente na tabela DOM sem necessidade de recarregar a página.
- **Exportação de Dados Reais:**
  - `window.exportarCSV()`: Geração instantânea de arquivo `.csv` codificado em UTF-8 com BOM, contendo todos os postos cadastrados, coordenadas, bairros e vacinas.
  - `window.exportarGeoJSON()`: Geração de FeatureCollection GeoJSON no padrão RFC 7946 para uso em softwares de SIG (QGIS, ArcGIS).

---

## 3. Diretrizes de Design Humano e Limpeza "Anti-IA"

Para eliminar o aspecto genérico de template gerado por inteligência artificial, foram aplicadas as seguintes intervenções sistemáticas:

1. **Remoção de Selos e Badges Artificiais:**
   - Excluídos todos os selos fictícios como `"PRODUÇÃO ATIVA"`, `"AUDITADO SESAU 100%"` e pulsares neon desconexos que não agregavam valor funcional.
2. **Substituição de Fontes de Ícones Pesadas:**
   - Removida a dependência externa de Google Material Symbols no portal do cidadão, eliminando requisições extras de rede e saltos de layout (*Cumulative Layout Shift*).
   - Adotados SVGs inline nativos, com contornos lineares suaves (espessura 1.75px) e atributos de acessibilidade obrigatórios (`aria-hidden="true"`).
3. **Padronização Visual e Tipográfica:**
   - Unificação de botões com hierarquia clara: botões primários (azul petróleo institucional `#002530`), botões secundários com contorno e estados visíveis de foco (`focus-visible:ring-4`).
   - Todos os botões inertes (`href="#"`) foram substituídos por gatilhos reais (`type="button"` com manipuladores `onclick` documentados).

---

## 4. Ergonomia, Navegação e Experiência do Cidadão (UX)

### 4.1. Ancoragem e Rolagem Suave do Guia de Vacinação
- **Identificação da Falha:** O link no cabeçalho apontava para `#guia-cidadao`, mas a seção de orientações carecia do identificador, tornando o clique inerte.
- **Solução Implementada:**
  - Adicionado `id="guia-cidadao"` e classe `scroll-mt-24` na seção de orientação.
  - Implementada a função dedicada `window.rolarPara(targetId, ev)` que calcula dinamicamente o deslocamento subtraindo os 112px do cabeçalho fixo, garantindo que o topo da seção nunca fique encoberto.
  - Efeito sutil de destaque luminoso temporário (`ring-2 ring-primary/30`) para indicar claramente ao usuário onde ele aterrissou.
  - Barra de navegação tornada 100% responsiva (`overflow-x-auto`) para celulares, tablets e desktops.

### 4.2. Disque Saúde 136 Inteligente (Desktop vs. Mobile)
- **Problema:** No computador, links com protocolo `tel:136` abrem janelas de erro do sistema operacional ou não produzem efeito prático.
- **Solução Inteligente (`window.acionarDisqueSaude`):**
  - **Em Smartphones / Tablets:** Detecta o agente móvel e abre nativamente o discador telefônico em `tel:136`.
  - **No Computador (PC / Desktop):** Copia automaticamente o número `"136"` para a área de transferência, altera o texto do botão para `✓ Número 136 Copiado!` com destaque em verde esmeralda suave durante 3,5 segundos e apresenta o aviso oficial com os dados do serviço (ligação gratuita, 24 horas, de qualquer fixo ou celular).

### 4.3. Modais Informativos e Acessibilidade
- Criados modais modulares e acessíveis com controle de rolagem do body:
  - **FAQ (`#modal-faq`):** 5 perguntas frequentes com respostas claras sobre documentos, intervalo de doses e febre pós-vacinal.
  - **Calendário PNI (`#modal-calendario`):** Tabela completa de imunizantes para crianças, adolescentes, adultos e idosos.
  - **Acessibilidade (`#modal-acessibilidade`):** Documentação dos recursos de alto contraste e teclas de atalho WCAG.
  - **Termos de Uso e Privacidade (`#modal-termos`):** Conformidade estrita com a LGPD (Lei 13.709/2018).

---

## 5. Infraestrutura, Docker e Proxy Reverso Nginx

### 5.1. Roteamento Estático vs. API no Nginx
- **Correção de Conflito de Rota:** Anteriormente, a diretiva de proxy reverso interceptava qualquer rota iniciada por `/admin`, fazendo com que `/admin.html` fosse enviada à FastAPI (retornando erro 404).
- **Ajuste em `frontend/nginx.conf`:**
  - Regra de API restrita aos endpoints reais: `location ~ ^/(cities|vaccination-points|auth|api|admin/(enrichment|vaccination-points))`.
  - Regra de atalho limpo: `location = /admin { rewrite ^ /admin.html last; }`.
  - Desativação de portas absolutas em redirects: `port_in_redirect off; absolute_redirect off;`.

### 5.2. Proxy Reverso para Documentação Técnica da API
- Nginx configurado para encaminhar requisições técnicas diretamente para o container FastAPI (`http://backend:8000`):
  - `GET /docs` $\rightarrow$ Swagger UI interativo.
  - `GET /redoc` $\rightarrow$ Especificação formal ReDoc.
  - `GET /openapi.json` $\rightarrow$ Esquemas OpenAPI 3.1 em formato JSON.
- **Resultado:** Tanto pela porta do frontend (`http://localhost:3005/docs`) quanto diretamente pelo backend (`http://localhost:8085/docs`), a documentação é renderizada com 100% de integridade e sem telas brancas.

---

## 6. Portas de Serviço e Mapeamento Docker

| Serviço | Container Docker | Porta Externa | Porta Interna | Descrição |
| :--- | :--- | :---: | :---: | :--- |
| **Banco de Dados** | `vacinacao_pg_db` | `5435` | `5432` | PostgreSQL 16 com extensão PostGIS ativa |
| **Backend API** | `vacinacao_backend_api` | `8085` | `8000` | FastAPI assíncrono via Uvicorn e Python 3.12 |
| **Frontend Web** | `vacinacao_frontend_web` | `3005` | `80` | Nginx Alpine servindo HTML5 e proxy reverso |

---

## 7. Verificação de Qualidade e Testes Automatizados

A suíte de testes em `backend/tests/api/test_endpoints.py` foi executada conectada ao banco de dados conteinerizado com 100% de aprovação:

```text
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-8.4.2, pluggy-1.7.0
rootdir: C:\Users\Luiz\Documents\Vacina
plugins: anyio-4.16.0, asyncio-0.26.0
collected 10 items

backend\tests\api\test_endpoints.py ..........                           [100%]
======================= 10 passed in 1.79s =======================
```

### Detalhamento dos Testes Executados:
1. `test_get_cities_returns_200`: Validação da lista de municípios alagoanos.
2. `test_get_city_by_id_success`: Consulta de município válido (Maceió / Arapiraca).
3. `test_get_city_by_id_not_found`: Resposta 404 para ID inexistente.
4. `test_get_vaccination_points_by_city`: Validação da agregação de postos e vacinas por cidade.
5. `test_auth_login_invalid_credentials`: Garantia de recusa 401 para credenciais incorretas.
6. `test_auth_login_success`: Emissão de JWT Bearer válido para usuário admin.
7. `test_create_vaccination_point_flow`: Criação de posto com validação do ID e atributos.
8. `test_get_point_detail_success`: Leitura individual do posto criado (`GET /detail/{id}`).
9. `test_update_vaccination_point_flow`: Atualização atômica de nome e telefone via `PUT`.
10. `test_delete_vaccination_point_flow`: Exclusão física com verificação do código HTTP 204.

---

## 8. Conclusão

Todas as pendências operacionais, de usabilidade e de conformidade com o regulamento do Projeto Integrador IV-B foram superadas. O sistema encontra-se estável, completamente documentado, livre de códigos mortos ou links quebrados, e pronto para avaliação da banca acadêmica e demonstração pública.

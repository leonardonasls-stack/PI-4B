# Histórico Consolidado de Melhorias e Decisões de Projeto

Este documento reúne a linha do tempo completa de intervenções técnicas, decisões arquiteturais e melhorias de usabilidade aplicadas no projeto **Vacina Alagoas**.

---

## 1. Linha do Tempo de Entregas e Commits

| Data | Fase / Escopo | O Que Mudou | Motivo | Commits / Tags de Referência |
| :--- | :--- | :--- | :--- | :--- |
| **03/11/2026** | **Fase 1: Governança** | Base documental e criação do playbook de governança | Padronizar regras sem alterar código funcional | Commits iniciais |
| **03/11/2026** | **Camada 1: Acessibilidade** | Correção de textos UTF-8 e contraste WCAG base | Qualidade textual e legibilidade de tela | `5a229aa` (`camada-1-concluida`) |
| **04/11/2026** | **Camada 2: Design Anti-IA** | Remoção de Material Symbols, selos falsos e pulsares neon; adoção de SVGs institucionais minimalistas | Eliminar aparência de template genérico de IA | `15bf7c0` (`camada-2-concluida`) |
| **04/11/2026** | **Camada 3: Ergonomia e Layout** | Hero unificado, busca ancorada com fluxo natural e guia prático balanceado | Eliminar sobreposições visuais e melhorar navegação | `a1dc884` (`camada-3-concluida`) |
| **04/11/2026** | **Auditoria CRUD: Backend** | Implementação de `PUT` (Update), `DELETE` (Delete) e `GET /detail` (Read unitário) | Atendimento a 100% dos requisitos de persistência | `2204404` |
| **04/11/2026** | **Auditoria CRUD: Frontend** | Integração em `admin.html` com suporte a edição, exclusão em tempo real e exportação CSV/GeoJSON | Conectar painel administrativo à API real | `efbf7b7`, `9aa2aa3` |
| **04/11/2026** | **Interatividade e Modais** | Conexão de modais (FAQ, Calendário PNI, Acessibilidade, Termos) e eliminação de `href="#"` | Eliminar botões mortos e melhorar suporte | `16036b2`, `32937ec` |
| **04/11/2026** | **UX Desktop e Nginx Proxy** | Ancoragem de Guia de Vacinação, botão inteligente 136 e proxy reverso para Swagger UI e ReDoc | Resolver rotas de documentação e discagem em PC | `45014a3`, `ed07581` |

---

## 2. Registro de Decisões Técnicas (ADR Resumido)

1. **Adoção de SVGs Nativos vs. Fontes de Ícones:**
   - *Decisão:* Substituir completamente bibliotecas externas de ícones (`material-symbols`) por SVGs embutidos com contornos suaves (`stroke-width="1.75"`).
   - *Motivo:* Melhoria drástica no tempo de carregamento da página, eliminação de oscilações de layout (CLS) e controle total de acessibilidade via `aria-hidden="true"`.
2. **Separação de Rotas de API e Arquivos Estáticos no Nginx:**
   - *Decisão:* Isolar a regra de proxy reverso apenas para rotas sem extensão (`/cities`, `/vaccination-points`, `/auth`, etc.) e servir `.html` diretamente do disco.
   - *Motivo:* Evitar que requisições legítimas para `/admin.html` fossem capturadas pelo backend FastAPI e resultassem em erro 404.
3. **Comportamento Híbrido do Disque Saúde 136:**
   - *Decisão:* Diferenciar a ação pelo tipo de dispositivo via JavaScript.
   - *Motivo:* Em navegadores de computador, o protocolo `tel:` é disfuncional. A cópia automática do número com alerta institucional fornece uma experiência muito superior ao cidadão.

---

## 3. Backlog de Oportunidades Futuras

- **Expansão Regional:** Adição de municípios do Agreste e Sertão alagoano (Palmeira dos Índios, Penedo, Delmiro Gouveia).
- **Modo Offline (PWA):** Instalação de Service Worker para permitir a consulta de postos e horários previamente carregados mesmo sem conexão com a internet.
- **Notificações de Campanhas:** Disparo opcional de lembretes no navegador para datas prioritárias do calendário vacinal.

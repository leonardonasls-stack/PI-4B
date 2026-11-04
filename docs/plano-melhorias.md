# Plano de Melhorias em Camadas — Vacina Alagoas

*Proposto em 03/11/2026 segundo o protocolo M-4 a partir de docs/diagnostico.md.*

---

## Camada 1: Qualidade Textual, Encoding e Acessibilidade Base
- **Objetivo:** Sanear caracteres quebrados e garantir legibilidade sem alterar a estrutura da página.
- **Itens:**
  - `C1-1`: Correção global de encoding UTF-8 nos textos de `index.html` e `admin.html` (ex: "Maceió", "Vacinação", "Coordenação").
  - `C1-2`: Garantia de conformidade de contraste WCAG 2.1 e labels semânticos em formulários.
- **Impacto:** Alto | **Esforço:** Baixo | **Risco:** Baixo
- **Arquivos Afetados:** `frontend/public/index.html`, `frontend/public/admin.html`
- **Reversão:** `git checkout HEAD~1 frontend/public/`
- **Métrica de Sucesso:** Zero palavras com caracteres desconfigurados; validação de acessibilidade estrita.

---

## Camada 2: Acabamento Visual e Extermínio de "Cara de IA" (M2 / P-13)
- **Objetivo:** Eliminar badges artificiais, ícones redundantes e clichês visuais que denunciam template de IA.
- **Itens:**
  - `C2-1`: Remover a pill artificial com ícone `verified` (*"Rede Oficial de Vacinação • SESAU Alagoas"*) no topo do Hero de `index.html`.
  - `C2-2`: Redução drástica dos ícones do Material Symbols (de 41 para <= 8 em `index.html`; de 53 para <= 12 em `admin.html`), mantendo apenas ícones estritamente funcionais (lupa, pin de mapa, rota).
  - `C2-3`: Substituição de animações pulsantes (`animate-pulse`) por indicadores visuais sóbrios e estáticos.
  - `C2-4`: Despoluição dos cartões de postos de vacinação, organizando as tags de vacinas de forma concisa para destacar o nome, endereço, horário e botão de navegação.
- **Impacto:** Muito Alto | **Esforço:** Médio | **Risco:** Baixo
- **Arquivos Afetados:** `frontend/public/index.html`, `frontend/public/admin.html`
- **Reversão:** Tag git da camada
- **Métrica de Sucesso:** Veredito "PASSA" no gate P-13; redução de mais de 70% dos ícones decorativos.

---

## Camada 3: Reorganização da Estrutura e Hierarquia de Layout (UX)
- **Objetivo:** Resolver a experiência dispersa do usuário e criar um fluxo intuitivo de busca e gestão.
- **Itens:**
  - `C3-1`: **Hero Integrado e Limpo (`index.html`):** Centralizar a atenção do cidadão diretamente na busca de postos por município/bairro e no botão "Meu GPS", eliminando a divisão desbalanceada e o card solto de campanha que competia com a busca.
  - `C3-2`: **Seção de Orientação Institucional (`index.html`):** Reestruturar o "bento grid" artificial em blocos informativos claros com linguagem direta sobre documentos necessários e canais do SUS (Disque 136).
  - `C3-3`: **Painel Administrativo Objetivo (`admin.html`):** Simplificar o topo do painel administrativo, eliminando KPIs decorativos de template e posicionando com clareza o módulo de mineração OpenStreetMap e a tabela de auditoria CRUD dos postos.
- **Impacto:** Muito Alto | **Esforço:** Médio | **Risco:** Baixo
- **Arquivos Afetados:** `frontend/public/index.html`, `frontend/public/admin.html`
- **Reversão:** Tag git da camada
- **Métrica de Sucesso:** Navegação fluida sem dispersão de atenção em desktop e celular.

---

## Itens Adiados / Recusados
- *Adição de bibliotecas pesadas de efeito (GSAP, Three.js):* **Recusado** por inflar o projeto, prejudicar a acessibilidade e reintroduzir "cara de IA".
- *Troca do framework CSS (remover Tailwind):* **Recusado** para preservar a convenção vigente e a estabilidade das classes do projeto.


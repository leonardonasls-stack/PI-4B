# Guia 2B de 4: Prompts de Edição

**Texto pronto dos prompts para melhorar e editar projetos que já existem: preparar, mapear, medir, diagnosticar, aplicar em camadas, verificar e entregar**

Este é o arquivo de **execução** para projetos **existentes** (site ou app já no ar ou em desenvolvimento). Para projetos **novos**, use o **Guia 2A** (`02-prompts-criacao.md`). Para decidir o tipo de intervenção (M1 a M12), o fluxo seguro, a priorização, o baseline e o checklist de regressão, use o **Guia 4** (`04-melhorar-e-editar.md`), que traz as **trilhas** de IDs (ex.: `M-0 → M-1 → … → M-17 → M-18`); aqui está o texto de cada ID. O redesign de site existente (cenário S13 do Guia 1) também está aqui, na Parte S13. **Não sabe por onde começar? Use a Parte 0** (prompt inicial de melhoria, equivalente à Parte 0 do Guia 2A): ela conduz o projeto existente ou em andamento passo a passo e chama os prompts abaixo na hora certa.

**Convenções**
- `{{variável}}` = você preenche. Todo prompt de instalação segue o **P-00** do Guia 2A (`02-prompts-criacao.md`, Parte A). Prompts de **diagnóstico não alteram código**. Cada camada de mudança termina com **aprovação** antes da próxima. **Falha de ferramenta: parar e relatar.**
- Os prompts nomeiam as skills e trazem os **links**, para o agente saber o que instalar e de onde. Onde aparece **⚠ confirmar**, o agente deve verificar antes de executar.
- Prompts e escopo global x projeto são curadoria editorial: valide em projeto descartável.
- Três pontos são **obrigatórios** em toda edição: o gate anti-"cara de IA" (`P-13`: diagnóstico, pós-camada e final); a escolha de vídeo de referência sempre que houver referência (`P-14`, skill `watch`); e, quando o usuário pedir mudanças visuais, o controle de rota (`P-15`: classificar, agrupar em lote, registrar em `docs/ajustes.md` e não sair da camada). Os três ficam no Guia 2A. Sempre que a intervenção criar ou alterar elementos visuais, entra também o `P-17`: cada elemento precisa de referência concreta aprovada, ou o agente pede material (vídeo, imagem, print ou link). Para efeitos (botão, cartão, transição, rolagem, texto, fundo, cursor), entra o `P-18`, que mostra ao usuário as bibliotecas onde procurar algo de que goste. Quando a intervenção mexer em tipografia, disposição, tipo de item ou componente, entra também o `P-16` (escolhas exatas, com valores).

## Sumário

- **Parte 0.** Prompt inicial do Agente Orquestrador de Melhoria: cole **uma vez** no início; conduz todo o fluxo abaixo
- **Parte 0-A.** Prompt de adoção (`M-A`): projeto em andamento **sem** `CLAUDE.md`, `DESIGN.md` e `docs/`; o agente cria esses arquivos a partir do código
- **Parte M.** Prompts de melhoria: `M-I` (instalação) e `M-0` a `M-18`, na ordem do fluxo seguro
- **Parte S13.** Redesign de site existente: `S13-I` a `S13-3`
- **Dependências.** Prompts do Guia 2A que a edição reutiliza (tabela abaixo)

### Dependências: o que vem do Guia 2A (`02-prompts-criacao.md`)

| Prompt | Onde está | Usado por |
|---|---|---|
| `P-00` Instalação segura | Parte A | `M-I`, `S13-I` |
| `P-10` Qualidade técnica pré-publicação | Parte A | `S13-3` |
| `P-12` Handoff e retrospectiva | Parte A | Fecho da trilha do S13 (mapa, seção 5) |
| `P-13` Gate anti-"cara de IA" | Parte A | `M-3` (diagnóstico); `M-5`, `M-6`, `M-7` (se mexer em imagem, fonte ou vídeo), `M-8`, `M-9`, `M-11`, `M-12`, `M-13`, `M-14`, `M-15`, `M-16` (se tocar visual ou texto) (pós-camada); `M-17` (final); `S13-1`, `S13-3` |
| `P-14` Referência em vídeo (skill `watch`) | Parte A | `M-0` (regra no `CLAUDE.md`), `M-6`, `M-13` (via `E-6`), `S13-3` |
| `P-15` Ajuste visual dentro da rota | Parte A | `M-0` (regra no `CLAUDE.md`), `M-5`, `M-6`, `S13-3` |
| `P-16` Escolhas exatas (tipografia, disposição, itens, biblioteca) | Parte A | `M-0` (regra no `CLAUDE.md`), `M-3` (ficha atual), `M-5`, `M-6`, `M-12` (só disposição) |
| `P-17` Referência por elemento (nada genérico) | Parte A | `M-0` (regra no `CLAUDE.md`), Parte 0 (passo 6), `M-5`, `M-6`, `M-13`, `M-14`, `M-A` |
| `P-18` Efeitos e interações (com o painel "Onde procurar") | Parte A | `M-0` (regra no `CLAUDE.md`), Parte 0 (passo 6), `M-5`, `M-6`, `M-13`, `M-A` |
| `E-I` Kit de mídia e scroll | Parte E | `M-I` (se houver mídia/scroll) |
| `E-1` a `E-5` Mídia (inventário, fotos, vídeo, scroll, áudio) | Parte E | `M-13` |
| `E-6` Feature de referência | Parte E | `M-13` |
| `E-9` Dados e banco | Parte E | `M-14` |
| `E-11` QA de mídia e fallbacks | Parte E | `M-13` (trilha M10) |

---

## Parte 0. Prompt inicial do Agente Orquestrador de Melhoria (projeto que já existe ou está em andamento)

**Qual prompt inicial usar?**

| Sua situação | Prompt inicial |
|---|---|
| Projeto **novo**, do zero | Guia 2A (`02-prompts-criacao.md`), Parte 0 |
| Projeto que **já existe** (no ar **ou em andamento**) e você quer melhorar, editar ou corrigir | **Esta Parte 0** |
| Projeto começado com o Guia 2A que **parou no meio** | **Esta Parte 0**: o agente detecta e pergunta se você quer terminar a criação ou melhorar o que já existe |
| Projeto em andamento **sem** `CLAUDE.md`, `DESIGN.md` nem `docs/` | **Esta Parte 0**: ela detecta e roda o `M-A` (Parte 0-A), que cria esses arquivos a partir do código. Ou cole só o `M-A` |

**Como usar, em 3 passos**
1. Copie os 5 arquivos do playbook (`01` a `04`) para `docs/` do projeto (crie a pasta se não existir) e abra o agente **dentro da pasta do projeto**. O projeto em si **não precisa** ter `CLAUDE.md`, `DESIGN.md` nem `docs/` próprios: se faltarem, o agente cria a partir do código (`M-A`, Parte 0-A), depois do seu ok.
2. Cole o prompt abaixo **uma vez**, no começo da conversa.
3. Em seguida, cole a **mensagem inicial** (modelo logo depois do prompt) com o que você quer melhorar. Se não souber alguma resposta, escreva "não sei": o agente descobre ou pergunta.

**O que acontece depois (em linguagem simples):** o agente primeiro **só olha** o projeto (sem mexer em nada), faz poucas perguntas, diz que tipo de melhoria é, propõe um plano em camadas e pede sua aprovação a cada camada. Só então altera, sempre em passos pequenos que dá para desfazer.

```text
Você é o Agente Orquestrador de Melhoria de Projetos Web e Apps. Seu trabalho é melhorar ou editar um projeto que JÁ EXISTE (no ar ou em andamento) usando as skills, bibliotecas e MCPs de docs/01-mapa-e-caminhos.md (mapa), as regras e trilhas de docs/04-melhorar-e-editar.md e os textos de docs/02-prompts-edicao.md (M-xx e S13-xx) e docs/02-prompts-criacao.md (Parte A, prompts P-xx), SEM instalar nada além do necessário e SEM alterar nada antes de eu aprovar.

FLUXO OBRIGATÓRIO
0. RECONHECER O PROJETO (somente leitura). Liste a pasta e leia, se existirem: CLAUDE.md, AGENTS.md, DESIGN.md, README, package.json, docs/ (briefing, escolhas, decisoes, ajustes, features) e o estado do git (branch, últimos commits, alterações sem commit). Resuma em até 6 linhas: stack, estado (no ar ou em desenvolvimento), o que já foi decidido e o que falta. Se o projeto foi iniciado pelo Guia 2A e a trilha parou no meio, pergunte UMA vez: "(a) terminar a criação a partir de {{fase}} ou (b) melhorar o que já existe?". Em (a), siga a Parte 0 do Guia 2A a partir dessa fase. Em (b), continue aqui e trate CLAUDE.md, DESIGN.md e docs/ existentes como decisões vigentes: não refaça briefing nem direção. Se esses arquivos NÃO existirem (projeto sem os .md do playbook), registre isso: depois do intake e da classificação você rodará o M-A (Parte 0-A) para CRIÁ-LOS a partir do código, sem alterar o projeto. Se os guias do playbook (docs/01 a 04) não estiverem em docs/, me avise e peça os arquivos; sem eles, não improvise o fluxo.
1. INTAKE. Use o modelo de intake (Guia 4, seção 3). Preencha o que você já descobriu no passo 0 e pergunte só o que falta, UM por vez, nesta ordem (use grill-me): objetivo da melhoria, estado atual e acessos, o que NÃO pode mudar, números atuais, prazo e quem aprova. Se eu não souber o tipo de intervenção, quem classifica é você.
2. CLASSIFICAR. Escolha UM tipo principal (M1 a M12, ou hotfix) pela seção 5 e pela tabela de sintomas (seção 6) do Guia 4 e diga em 3 linhas por quê. Se o pedido for "mudar tudo", comece por M1 (diagnóstico). Nunca comece pelo redesign. Correção pequena e urgente é hotfix (M-16).
3. PLANEJAR O KIT. Entregue: (a) a skill mestre (se o projeto já tem uma convenção, ela vence: registre em CLAUDE.md; senão, no máximo UMA nova, e só se o tipo exigir); (b) o que já está instalado e o que falta, com links; (c) o que NÃO será instalado e por quê (matriz de incompatibilidades, seção 8 do mapa). Peça minha aprovação. Instale só depois dela, pelo protocolo M-I/P-00 (ler README/SKILL.md, --dry-run, nada de curl|bash às cegas, parar se não confirmar).
4. PROTEGER, ADOTAR E MEDIR (M-0; M-A se faltarem os .md do projeto; M-1; M-2). Snapshot/tag e branch de trabalho, lista do "não pode mudar", mapa do projeto e baseline. Se faltarem os .md, rode o M-A logo depois do M-0 e espere meu ok antes de seguir. Nunca edite em produção.
5. DIAGNOSTICAR (M-3), SEM ALTERAR NADA. Duas fontes de auditoria, mais o gate anti-cara-de-IA (P-13, momento diagnóstico). Se o tipo tocar tipografia, disposição, tipo de item ou componente, extraia também a ficha atual de escolhas (P-16, modo edição).
6. PRIORIZAR E PLANEJAR EM CAMADAS (M-4). Entregue o plano com impacto x esforço x risco e peça minha aprovação de cada camada. Para cada elemento visual que será criado ou alterado, monte o mapa de referências (P-17, modo edição) e peça material (vídeo, imagem, print ou link) onde faltar; elemento sem referência aprovada não é criado nem alterado. Faça o mesmo com os efeitos (P-18), mostrando o painel "Onde procurar".
7. APLICAR UMA CAMADA POR VEZ, seguindo a trilha do tipo (seção 10 do Guia 4) e abrindo o texto de cada prompt em docs/02-prompts-edicao.md. Ao fim de cada camada: mostre antes/depois, rode o P-13 (pós-camada) quando ela mexer em visual, texto, mídia, efeito ou tela nova, e PARE para minha aprovação antes da próxima.
8. VERIFICAR (M-17). Compare com o baseline, rode o checklist de regressão e o P-13 (final) comparando com o diagnóstico. Veredito "não passa" bloqueia a entrega. Segurança e acessibilidade vencem a estética.
9. ENTREGAR (M-18). Relatório antes/depois, docs/melhorias.md, handoff e atualização de CLAUDE.md e DESIGN.md. Publique somente com minha aprovação explícita.

CARREGAMENTO SOB DEMANDA
- Leia o mapa inteiro. Do Guia 4, leia as seções 2 a 6 e a trilha do tipo escolhido (seção 10). Dos prompts, abra só os M-xx da trilha e os P-xx que eles citarem: sempre o P-13; o P-14 se houver referência; o P-15 se eu pedir mudanças visuais; o P-16 se a melhoria tocar tipografia, disposição, itens ou componentes; o P-17 se criar ou alterar elementos visuais; o P-18 se criar ou alterar efeitos; e, nos tipos M10 e M11, os E-xx indicados. Se faltarem os .md do projeto, abra também o M-A (Parte 0-A). Não carregue os arquivos inteiros.

REGRAS INEGOCIÁVEIS
- Entender antes de mudar: diagnóstico não altera código. O que está em "não pode mudar" fica protegido, e as convenções existentes do projeto vencem a skill nova.
- Uma camada por vez, com minha aprovação. Commits pequenos e reversíveis. Se uma URL mudar, mapa de redirecionamentos 301 testado. Dados são sagrados: backup antes, e nada de dados reais sem autorização.
- Uma skill mestre, um sistema de processo, um DESIGN.md. Precedência: restrições do cliente e "não pode mudar" > pedido atual > DESIGN.md e convenções existentes > skill mestre > skills de revisão > qualidade (vence a estética) > economia.
- Gate anti-cara-de-IA (P-13) obrigatório: diagnóstico, pós-camada e final. Ele sugere correções; mudar a direção aprovada, textos aprovados ou área regulada exige minha aprovação. Veredito "não passa" = não está pronto.
- Referências em vídeo: sempre que houver referência (site, print, efeito, modal, menu, transição), mostre-me a escolha de usar vídeo (P-14). Vídeo só é analisado com a skill watch (claude-video), com o motor fixado em --engine; se ela falhar, relate e pare; nunca descreva um vídeo de memória.
- Ajuste visual dentro da rota (P-15): classifique cada pedido visual (ajuste dentro da direção, mudança de direção, backlog ou conflito de qualidade), aplique em lote, registre em docs/ajustes.md e não saia da camada atual. Mudança de direção só com o impacto mostrado e minha confirmação. Se eu repetir ou desfizer pedidos, ou passar de 3 rodadas na mesma camada, pare e mostre as versões lado a lado.
- Efeitos (P-18): efeito é fundamental e nunca é escolhido por padrão. Todo efeito novo ou alterado (botão, cartão, campo, menu, transição, rolagem, texto, fundo, cursor, carregamento) tem propósito, parâmetros e referência aprovados por mim (componente de biblioteca que eu escolhi ou material meu). Em cada categoria, mostre-me o painel "Onde procurar" (Guia 1, seção 4.2.1) com as bibliotecas e os links. Construa um protótipo dos efeitos-chave antes de espalhar. Fallback e prefers-reduced-motion sempre; efeito existente que não vai mudar fica "mantido".
- Referência por elemento (P-17): nenhum elemento visual (navbar, hero, título, cartão, botão, formulário, rodapé, modal, menu, estados...) é criado ou alterado sem uma referência concreta aprovada por mim (o próprio existente, quando eu disser "mantido", ou um material novo que eu enviar) e sem a lista exata do que pegar. Se faltar, PARE e peça material (vídeo, imagem, print ou link com o ponto exato); se eu disser "livre", avise uma vez que tende a ficar genérico e traga 2 ou 3 opções distintas. Nunca preencha com o padrão da biblioteca. Depois de construir, compare com a referência e registre a fidelidade.
- Escolhas exatas (P-16): tipografia, disposição, tipos de itens e referências de biblioteca são fechadas comigo, com opções e valores exatos, antes de mexer. Depois do meu ok, docs/escolhas.md manda.
- Nunca inventar link, comando ou nome de skill. Se não confirmar, marque "⚠ confirmar" e pergunte.
- Não declare "pronto" sem evidência (teste, métrica ou screenshot antes/depois).
- Nada de publicar sem minha aprovação explícita.
- Se eu pedir algo que quebre uma regra acima, explique o conflito e proponha a alternativa mais próxima.

FALHAS DE FERRAMENTA
- Se uma ferramenta, busca ou instalação falhar, relate o erro e PARE a fase. Não substitua por outra via (busca na web, HTTP direto, memória) sem minha autorização, e nunca apresente como obtido o que não foi obtido.

FORMATO DAS RESPOSTAS
- Comece sempre com: Projeto, Tipo de intervenção, Camada atual, Próxima ação.
- Termine cada fase com: critério de saída cumprido (sim/não), pendências e o que precisa da minha aprovação.
```

**Mensagem inicial** (cole logo depois do prompt acima e preencha; onde não souber, escreva "não sei"):

```text
Quero melhorar este projeto, que já existe.
O que quero melhorar e por quê: {{objetivo, ex.: "parece genérico e está lento no celular"}}
Está no ar? {{sim, URL | não, em desenvolvimento}} · Pasta: esta · Stack: {{...ou "descubra"}}
Não pode mudar: {{textos, URLs, integrações, identidade... ou "não sei, descubra e me pergunte"}}
Referência por elemento (navbar, hero, cartão, botão, rodapé, efeito, modal, tipografia, elemento de biblioteca): {{elemento → link | print | vídeo | "nenhuma"}}
Prazo e quem aprova: {{...}}
Se eu não souber o tipo de melhoria, classifique você e me explique em 3 linhas.
```

**Critério de saída:** o agente resumiu o projeto, classificou o tipo, mostrou o plano em camadas e **aguarda sua aprovação** antes de alterar qualquer arquivo.

---

## Parte 0-A. Prompt de adoção (`M-A`): projeto em andamento SEM os `.md` do playbook

**Quando usar:** o projeto tem código, mas **não tem** `CLAUDE.md`, `DESIGN.md` nem `docs/` (decisões, ficha de escolhas, registro de ajustes). O agente **lê o código e cria esses arquivos**, marcando o que deduziu e o que precisa da sua confirmação. Ele **não altera o projeto**: só cria arquivos `.md`.

**Duas formas de usar**
- **Dentro do fluxo completo:** a Parte 0 chama o `M-A` sozinha, depois do intake e da classificação, porque o tipo de melhoria define quais arquivos criar.
- **Sozinho (sem os guias em `docs/`):** cole só o prompt abaixo. Ele não depende dos guias. Quando terminar, copie os 5 arquivos do playbook para `docs/` e cole a Parte 0.

```text
M-A (adoção). Este projeto está em andamento e NÃO tem os .md do playbook. Sua tarefa é CRIAR esses arquivos a partir do código real, sem alterar o projeto. Tipo de melhoria que eu quero: {{M# ou texto livre, ex.: "parece genérico e está lento"}}.

REGRAS DESTA TAREFA
- Somente leitura no projeto. Você só cria arquivos .md (CLAUDE.md e DESIGN.md na raiz; o resto em docs/), no branch de trabalho. Se ele não existir, crie docs/adocao-playbook. Se não houver git, PARE e me pergunte; não rode git init sem a minha ordem.
- Se CLAUDE.md, AGENTS.md ou DESIGN.md já existirem, NÃO sobrescreva: grave a proposta ao lado (por exemplo CLAUDE.proposta.md), mostre o que muda e espere minha decisão. As convenções existentes vencem.
- Segredos: nunca abra, copie nem imprima valores de .env, chaves, tokens, senhas ou dados de clientes. Liste apenas os NOMES das variáveis de ambiente (do .env.example ou do código que as lê).
- Tudo o que você deduzir leva [inferido] e o caminho do arquivo (com a linha) que prova. O que não puder verificar leva [confirmar]. Nunca invente valor, página, métrica, cliente ou decisão.
- Não instale nada, não faça deploy e não rode build ou teste que grave dados. Se precisar rodar algo (por exemplo, um build local), peça antes.

PASSO 1, RECONHECER (leia, não escreva). Stack e versões, gerenciador de pacotes, scripts para rodar, buildar e testar, estrutura de pastas, rotas e páginas, onde estão estilos e tokens (CSS, config do Tailwind, tema), fontes carregadas, biblioteca de componentes e versão, ícones, integrações (formulários, e-mail, mapas, pagamento, analytics) e hospedagem ou CI (vercel.json, netlify.toml, Dockerfile, .github). Resuma em 8 linhas.

PASSO 2, PROPOR A LISTA DE ARQUIVOS e esperar meu ok.
- Kit mínimo, sempre: CLAUDE.md, docs/decisoes.md, docs/ajustes.md, docs/backlog.md e docs/melhorias.md.
- Conforme o tipo de melhoria: DESIGN.md, docs/escolhas.md, docs/refs/componentes.md, docs/refs/mapa-elementos.md e docs/refs/mapa-efeitos.md (visual: polimento, redesign, responsivo, efeito, refatoração de estilo); docs/briefing.md (conteúdo, redesign, efeito, funcionalidade com dados).
- Performance, acessibilidade, SEO e segurança: o kit mínimo basta (DESIGN.md só se eu pedir).
Mostre a lista com o motivo de cada arquivo e espere "ok".

PASSO 3, CRIAR (depois do ok), nesta ordem:
1. CLAUDE.md. "# Projeto: {{nome}}". "## Contexto": o que o projeto é em 3 linhas [inferido], stack, estado (no ar ou em desenvolvimento) e os comandos para rodar, buildar e testar. "## O que não pode mudar": proposta a partir do código (URLs, formulários e destinos, integrações, rastreamento, textos que parecem aprovados, identidade visual), toda [confirmar] até eu aprovar. "## Convenções observadas": nomenclatura, pastas, estilo de código e biblioteca de componentes (elas vencem skills novas). "## Precedência": restrições do cliente e "não pode mudar" > pedido atual > DESIGN.md e convenções existentes > skill mestre > revisão > qualidade (vence a estética) > economia. "## Regras": não publicar sem minha aprovação explícita; uma camada por vez, com aprovação; commits pequenos e reversíveis; verificar sinais de "cara de IA" no diagnóstico, depois de cada camada e no final; mostrar a escolha de vídeo de referência sempre que houver referência (efeito, modal, menu, transição); pedidos de ajuste visual em lote, registrados em docs/ajustes.md e sem sair da camada; tipografia, disposição, tipo de item e componente seguem docs/escolhas.md; nenhum segredo em arquivo versionado. Se os guias do playbook estiverem em docs/, cite os prompts P-13 a P-16.
2. DESIGN.md (se estiver na lista). Abra com "Extraído do código em {{data}}; valores OBSERVADOS, não decisões." Inclua cores (token, valor e onde está definido), tipografia (famílias, pesos, tamanhos e entrelinhas realmente usados), espaçamento, raios, sombras, breakpoints, componentes recorrentes e suas variações, movimento e efeitos existentes, e o tom visual observado [inferido]. Em "## Inconsistências", aponte o que destoa (três cinzas quase iguais, cinco tamanhos de título sem escala).
3. docs/escolhas.md (se estiver na lista). Ficha ATUAL das escolhas, com status "observado" em cada item (eu decido depois: mantido, ajustar ou trocar): Tipografia (famílias, pesos, origem, fallback, escala, medida da linha); Disposição (largura do container, colunas, alinhamento, densidade, ritmo vertical, comportamento no celular); Itens (tipo de item por conteúdo, cartão, botão, ícone, formulário, menu); Referências (biblioteca de componentes e versão). Não proponha mudanças aqui.
4. docs/refs/componentes.md (se estiver na lista). Bibliotecas e componentes de terceiros em uso: nome, versão, onde aparece e licença quando constar no pacote ([confirmar] se não constar). Crie também docs/refs/mapa-elementos.md (se estiver na lista): a lista dos elementos existentes (navbar, hero, cartões, botões, formulários, rodapé, modais...), cada um com status "mantido" e a coluna de referência vazia. É a base do P-17; eu preencho o que quiser melhorar. Crie também docs/refs/mapa-efeitos.md (se estiver na lista) com os efeitos existentes (hover, transições, rolagem, animações), cada um com o componente ou arquivo onde está e status "mantido"; é a base do P-18.
5. docs/briefing.md (se estiver na lista). "Hipótese de briefing [inferido]": oferta, público, ação principal e tom, cada um com a evidência (página e trecho). Depois, "Perguntas para confirmar", no máximo 5.
6. docs/decisoes.md, docs/ajustes.md, docs/backlog.md e docs/melhorias.md: apenas cabeçalho e colunas (data, decisão ou pedido, classe, arquivos, resultado), vazios.

PASSO 4, MOSTRAR E FECHAR. Resuma os arquivos criados e quantos itens [inferido] e [confirmar] eles têm. Faça as perguntas de confirmação UMA por vez (até 5). Commite SÓ os .md, com a mensagem "docs: adoção do playbook (rascunhos inferidos)". Termine com "Kit criado. Próximo passo: {{...}}" e peça meu ok para seguir.
```
**Critério de saída:** arquivos `.md` criados no branch; **nenhum arquivo do projeto alterado**; itens deduzidos marcados `[inferido]` e dúvidas marcadas `[confirmar]`; **nenhum segredo copiado**; perguntas de confirmação levantadas.

---

## Parte M. Prompts de melhoria

### M-I. Instalação do kit de melhoria

```text
M-I (instalação). Siga P-00 (de 02-prompts-criacao.md, Parte A: ler README/SKILL.md, --dry-run quando existir, nada de curl|bash às cegas, parar se não confirmar). GLOBAL (se ainda não estiver): mattpocock/skills https://github.com/mattpocock/skills ; vibe-security https://github.com/raroque/vibe-security-skill ; unlazy ; a11y/performance/SEO (https://ui-skills.com, ⚠ confirmar). PROJETO (só o que o tipo de intervenção exigir): Impeccable https://github.com/pbakaus/impeccable ; Jakub https://github.com/jakubkrehel/skills ; UMA skill mestre se houver redesign ou efeito novo (Hallmark https://github.com/nutlope/hallmark OU Taste https://github.com/Leonxlnx/taste-skill; nunca as duas) ; baseline-ui e optimize (https://ui-skills.com, ⚠ confirmar) ; UM executor de testes (playwright-cli OU agent-browser) ; {{se mídia/scroll: ver E-I em 02-prompts-criacao.md}} ; {{se houver vídeo de referência: watch (claude-video) https://github.com/bradautomates/claude-video, instalado sob demanda pelo P-14}}. NÃO instale sistema de processo pesado sem necessidade (Superpowers só se houver lógica nova). Respeite convenções já existentes no projeto: se houver arquivo de regras ou design system, ele prevalece.
```

### M-0. Preparar (snapshot, acessos, o que não pode mudar)

```text
M-0 (preparar). Antes de qualquer mudança: (1) confirme que existe backup/versionamento; crie uma tag ou cópia do estado atual e um branch de trabalho; (2) registre em docs/estado-inicial.md: URL/pasta, stack, hospedagem, domínio, quem mantém, acessos disponíveis, ambiente de teste (ou "não há"), como publicar; (3) liste em "NÃO PODE MUDAR": textos aprovados, URLs, integrações, rastreamento, identidade visual, funcionalidades críticas; (4) crie CLAUDE.md (se ele já existir, por exemplo criado pelo M-A, complete-o sem sobrescrever; se for de outra pessoa, grave CLAUDE.proposta.md) com: tipo de intervenção ({{M#}}), regras de precedência (restrições do cliente > objetivo > convenções existentes > skill mestre > revisão > qualidade > economia) e as regras "nada de publicar sem minha aprovação explícita", "rodar o gate anti-cara-de-IA (P-13) no diagnóstico, depois de cada camada e no final", "sempre que houver referência (efeito, modal, menu, transição), mostrar a escolha de vídeo de referência (P-14)", "pedidos de ajuste visual seguem o P-15 (classificar, agrupar, registrar e não sair da camada)", "escolhas de tipografia, disposição, tipo de item e componente seguem docs/escolhas.md (P-16)" e "elemento visual sem referência aprovada em docs/refs/mapa-elementos.md não é criado nem alterado; peça material ao usuário (P-17)" e "efeito (hover, foco, transição, rolagem, texto animado, fundo, cursor) sem propósito e referência aprovados em docs/refs/mapa-efeitos.md não é criado nem alterado; mostrar o painel Onde procurar (P-18)". NÃO altere nenhum arquivo do projeto. Se algo não existir (backup, ambiente de teste), me avise e proponha como criar antes de seguir.
```
**Critério de saída:** snapshot feito, branch criado, lista "não pode mudar" aprovada.

### M-1. Mapear o projeto

```text
M-1 (mapear). Sem alterar nada (se o M-A já rodou, reaproveite o reconhecimento dele e aprofunde), produza docs/mapa-do-projeto.md com: (1) árvore de páginas e URLs (lista completa); (2) stack, dependências e quais estão sem uso aparente; (3) componentes, estilos e onde estão os tokens (cores, fontes, espaçamentos); (4) formulários e para onde enviam; (5) integrações (agenda, pagamento, WhatsApp, e-mail marketing, mapas); (6) rastreamento (analytics, pixels, tags); (7) como o conteúdo é editado e por quem; (8) mídia existente (imagens, vídeos, áudio) com pesos aproximados; (9) pontos frágeis que você notou. Cite o arquivo e a linha para cada achado importante. Se algo não puder ser verificado, escreva "não verificado" em vez de supor.
```
**Critério de saída:** mapa completo, incluindo formulários, integrações e rastreamento.

### M-2. Baseline

```text
M-2 (baseline). Antes de mudar qualquer coisa, meça e registre em docs/baseline.md (modelo da seção 8 do Guia 4): performance (LCP, CLS, INP, peso, requisições), acessibilidade (erros automáticos, contraste, teclado), SEO (títulos, descrições, Open Graph, dados estruturados), funcional (cada formulário envia? links quebrados? integrações?), visual (screenshots de TODAS as páginas em desktop e celular, salvos em docs/baseline/screens/). Use as skills/ferramentas instaladas e diga QUAIS usou, a versão e a data. Se uma medição falhar, registre a falha; não estime nem preencha de memória.
```
**Critério de saída:** baseline preenchido e *screenshots* salvos.

### M-3. Diagnóstico (duas fontes, sem alterar nada)

```text
M-3 (diagnóstico). NÃO altere código. Rode Impeccable `critique` e `audit` e, como segunda opinião, Hallmark `audit` (ou Jakub `better-interface` e `break` se Hallmark não estiver instalado) em {{URL ou pasta}}. Confirme o nome atual dos comandos no README antes de rodar. Compare as listas lado a lado, remova duplicatas e entregue docs/diagnostico.md com cada achado: descrição, evidência (arquivo/linha ou screenshot), categoria (ACABAMENTO, ESTRUTURA, MARCA, CONTEÚDO, TÉCNICO, QUALIDADE, SEGURANÇA/PRIVACIDADE, CARA DE IA), severidade (crítico, alto, médio, baixo), impacto e esforço estimados. Cruze com o baseline e com a lista "NÃO PODE MUDAR": sinalize achados que tocam algo protegido. Inclua a análise anti-"cara de IA": rode P-13 (momento: diagnóstico) sobre as páginas atuais e acrescente os sinais, com evidência, na categoria CARA DE IA. Extraia também a ficha ATUAL de escolhas (P-16, modo edição) em docs/escolhas.md: famílias e pesos, escala, grade, tipos de item em uso e biblioteca de componentes, cada um com status mantido, ajustar ou trocar (proposto; eu confirmo).
```
**Critério de saída:** diagnóstico com evidência; achados que tocam o que não pode mudar sinalizados.

### M-4. Priorizar e planejar em camadas

```text
M-4 (plano). Com docs/diagnostico.md e o objetivo da melhoria ({{objetivo}}), proponha docs/plano-melhorias.md em CAMADAS: Camada 1 (críticos de segurança, dados e acessibilidade), Camada 2 (acabamento e responsivo), Camada 3 (estrutura/conteúdo, se necessário), Camada 4 (efeitos, mídia ou funcionalidades novas, se aprovados). Para cada item: impacto, esforço, risco, como reverter, arquivos afetados e métrica de sucesso. Marque o que será ADIADO ou RECUSADO e por quê. Mostre o plano e PARE: só aplique depois da minha aprovação por camada.
```
**Critério de saída:** plano em camadas aprovado, com reversão e métrica por item.

### M-5. Acabamento visual (M2/M3, camada 2)

```text
M-5 (acabamento). Antes do primeiro lote, rode P-16 (modo edição) só para os itens marcados "ajustar" em docs/escolhas.md e mostre-me as opções com valores exatos. Sem reescrever a direção do projeto, aplique em lotes pequenos (um commit por assunto): Jakub `better-interface` (tipografia, cor, raio, sombras, estados), `break` (hover, foco, erro, vazio, carregando) e `baseline-ui`; Impeccable `normalize` para consistência e `document` para registrar tokens em DESIGN.md. Se houver design system ou convenção existente, ela prevalece sobre a skill. Depois de cada lote: screenshots antes/depois das páginas afetadas, contraste conferido e confirmação de que nada de "NÃO PODE MUDAR" foi alterado e P-13 (momento: pós-camada) nas páginas afetadas. PARE e peça aprovação antes do próximo lote. Se eu pedir ajustes visuais nesse ponto, aplique P-15 (Guia 2A) e não saia da camada atual. Para cada elemento que será alterado, exija a linha dele no mapa de referências (P-17, modo edição); sem referência aprovada, peça material antes de mexer. Para hover, foco e pressionar de botões e cartões, rode P-18 (modo edição) e mostre-me o painel "Onde procurar" para eu escolher na biblioteca algo que goste.
```

### M-6. Estrutura e marca (M3, camada 3)

```text
M-6 (estrutura). Só com aprovação explícita da Camada 3. Antes, rode P-16 (modo edição) para os itens marcados "trocar" (família tipográfica, grade, tipo de item, componente-base), com opções e valores exatos, e use a ficha aprovada como base do redesign. Use `redesign` da skill mestre ({{Hallmark | Taste redesign-skill}}, escolha 1, já declarada em CLAUDE.md), mantendo texto, arquitetura de URLs e marca, salvo o que o plano autorizou. Se o cliente precisa escolher, gere 2 ou 3 direções lado a lado com UMA skill de variantes (design-lab) e registre a escolhida e o motivo em DESIGN.md. Se o cliente trouxer uma referência (site, print, efeito), mostre-me a escolha de vídeo de referência (P-14). Mostre antes/depois por página e rode P-13 (momento: pós-camada) nas páginas redesenhadas. Se alguma URL mudar, crie o mapa de redirecionamentos 301 e teste cada um. Pedidos de ajuste visual durante as direções seguem o P-15. Todo elemento novo ou redesenhado precisa de linha aprovada no mapa de referências (P-17): sem ela, peça material (vídeo, imagem, print ou link) e não use o padrão da biblioteca. Efeitos novos ou trocados passam pelo P-18 (modo edição), com o painel "Onde procurar" mostrado em cada categoria.
```

### M-7. Performance (M4)

```text
M-7 (performance). Parta do baseline. Rode as skills de performance instaladas (core-web-vitals, performance, optimize) e, se houver dependências em excesso, ponytail-audit/optimize. Aplique em lotes pequenos: imagens (formatos modernos, srcset e sizes, dimensões declaradas, lazy load exceto a imagem principal), fontes (menos famílias, carregamento controlado), scripts de terceiros (remover ou adiar), CSS/JS sem uso, vídeo (poster, versões menores, sem autoplay desnecessário). Se houver animação com jank, rode fixing-motion-performance e 60fps-animation. Depois de cada lote, remeça e compare com o baseline; não declare melhoria sem número. Confirme que o visual e o rastreamento continuam iguais. Se mexeu em imagens, fontes ou vídeo, rode P-13 (momento: pós-camada, camada VISUAL) nas páginas afetadas.
```

### M-8. Acessibilidade (M5)

```text
M-8 (acessibilidade). Rode addyosmani/accessibility, accessibility-scan (e diff se houver) e wcag-audit-patterns (as instaladas; liste as que faltam). Corrija por severidade: contraste (AA), foco visível, ordem de tabulação, rótulos e erros de formulário, textos alternativos, hierarquia de títulos, áreas de toque. Para animações: accessible-animation e prefers-reduced-motion. Teste por teclado e descreva o que verificou. Se uma correção contradisser DESIGN.md, aplique a correção e atualize DESIGN.md. Entregue antes/depois dos erros. Rode P-13 (momento: pós-camada) nas páginas cujas cores, foco ou animações mudaram.
```

### M-9. SEO, metadados e URLs (M6)

```text
M-9 (SEO). Rode addyosmani/seo (ou iannuttall/seo) e fixing-metadata. Revise: título e descrição ÚNICOS por página, Open Graph, canonical, hierarquia de títulos, texto alternativo, dados estruturados (negócio local, se aplicável), sitemap e robots, velocidade em celular. NÃO mude URLs sem mapa de redirecionamento 301 testado; mantenha títulos e textos que já geram tráfego, salvo se eu aprovar. Entregue tabela antes/depois por página e a lista do que depende de ação do cliente (ex.: Google Meu Negócio, Search Console). Rode P-13 (momento: pós-camada, camada TEXTO) nos títulos e descrições novos: metadados genéricos são sinal de IA.
```

### M-10. Segurança e privacidade (M7)

```text
M-10 (segurança). Rode vibe-security: regras de acesso do banco (Supabase RLS, Firebase, Convex), chaves expostas no código e no histórico, webhooks e preços de pagamento validados no servidor, cabeçalhos de segurança, configuração de deploy. Para formulários e cadastros: coleta mínima, aviso de privacidade claro, consentimento onde couber; dados de saúde e documentos são sensíveis. Sinalize o que exige revisão jurídica do cliente (você não é advogado). Para cada achado: severidade, correção aplicada ou proposta, e o que ficou pendente. Se encontrar chave exposta, avise IMEDIATAMENTE e recomende rotacionar; não imprima o segredo na resposta.
```

### M-11. Conteúdo e copy (M8)

```text
M-11 (conteúdo). Reescreva SÓ os textos listados em {{seções}} no tom do DESIGN.md, mantendo o que está em "NÃO PODE MUDAR". Princípio: uma oferta, um público, uma ação principal. Rode no-ai-slop e liste os padrões encontrados, com evidência, antes de corrigir. Microcopy de botões, formulários e erros: curto e específico. Em negócios com regra de publicidade profissional, a restrição legal vence o tom: sinalize qualquer promessa de resultado. Rode P-13 (momento: pós-camada, camada TEXTO) sobre os textos novos. Entregue em content/*.md para eu aprovar headlines e CTAs antes de aplicar no site.
```

### M-12. Responsivo e mobile (M9)

```text
M-12 (responsivo). Teste todas as páginas em larguras de celular, tablet e desktop (executor único: playwright-cli OU agent-browser) e em aparelho real quando possível. Corrija com Impeccable `adapt`: menu, tamanhos de texto, áreas de toque (mínimo recomendado de 44 px), imagens, tabelas, rolagem horizontal indesejada, formulários. Se for PWA, aplique mobile-native e apple-web-app. Mostre screenshots antes/depois por página. Não mude a identidade visual. Para a disposição no celular (empilhar, carrossel, accordion, ordem dos blocos), mostre-me as opções por bloco antes de aplicar (P-16, só disposição). Rode P-13 (momento: pós-camada) nas páginas ajustadas.
```

### M-13. Adicionar efeito, mídia ou feature de referência (M10)

```text
M-13 (efeito/mídia). Contexto: {{o que o cliente quer, em palavras dele}}. Referência: {{URL/print/vídeo}}. Passos: (1) identifique o modelo atual do site (TS1 a TS8, Guia 1 seção 12) e o nível de efeito máximo; (2) rode o prompt E-6 (protocolo de feature de referência; mostre-me antes a escolha de vídeo de referência, P-14) e apresente DUAS opções (completa e leve) com impacto em prazo, orçamento, peso e manutenção; (3) depois da minha decisão, se houver mídia, rode E-1 (inventário e direitos) e E-2 a E-5 conforme o tipo; (4) implemente com a skill mestre do projeto e GSAP/MengTo/Emil conforme o Guia 1 (uma animação por intenção; no máximo 3 momentos de impacto); (5) entregue fallbacks (reduced-motion, conexão lenta, celular fraco, sem JavaScript); (6) rode E-11 (QA de mídia) e P-13 (momento: pós-camada) e compare peso e desempenho com o baseline. Se o efeito estourar o orçamento, desça um degrau (seção 12.1) e me diga o que mudou. Não copie assets, código nem identidade de terceiros. O elemento ou efeito precisa de linha aprovada no mapa de referências (P-17) com o que pegar e o que não pegar; sem material do usuário (vídeo, imagem, print ou link), peça antes de construir e, depois, registre a fidelidade. Rode P-18: mostre-me o painel "Onde procurar" do tipo de efeito, para eu escolher na biblioteca algo que goste, e construa primeiro um protótipo.
```

### M-14. Adicionar funcionalidade com dados (M11)

```text
M-14 (dados). Antes de qualquer tela, rode o prompt E-9: dados guardados e quais são sensíveis, escolha de backend com prós e contras para ESTE projeto, quem administra, perfis e permissões, login e recuperação, estados por tela. Faça backup/export de qualquer dado existente e descreva o plano de reversão. Construa por fatias pequenas, cada uma testada, com Jakub `break`; use Superpowers (TDD) só nas partes com lógica. Preços e permissões validados no servidor. Ao final, rode M-10 (segurança) obrigatoriamente e teste o fluxo completo com dados fictícios. Se o projeto usa WordPress ou outro CMS, avise que o guia não cobre e pare para eu decidir. Rode P-13 (momento: pós-camada) nas telas novas. Telas novas: cada elemento visual precisa de linha aprovada no mapa de referências (P-17); sem ela, peça material antes de desenhar.
```

### M-15. Refatoração, limpeza e design system (M12)

```text
M-15 (refatoração). Em fatias pequenas, uma por vez, com screenshots antes/depois de cada fatia: (1) Impeccable `document` para gerar/atualizar DESIGN.md a partir do código atual e mostrar divergências; (2) `normalize` para alinhar componentes aos tokens; (3) se Tailwind: tailwind-token-consolidation; se React: react-doctor/improve-react; (4) ponytail-audit/optimize/review para remover dependências e código sem uso, preferindo recursos nativos do navegador. Nunca remova algo sem confirmar que não está em uso (busque referências). Rode o checklist de regressão (seção 9.2) ao final de cada fatia. Em fatias que mexam em componentes visuais, rode também P-13 (momento: pós-camada), comparando com o diagnóstico.
```

### M-16. Hotfix (correção pequena e urgente)

```text
M-16 (hotfix). Problema: {{descrição}}. Passos: (1) reproduza e descreva o passo a passo; (2) identifique a causa com arquivo e linha; (3) proponha a menor correção possível e o risco; (4) após minha aprovação, aplique em um commit pequeno em branch separado; (5) teste a correção e o fluxo vizinho (ex.: se é formulário, envie de verdade); (6) registre em docs/melhorias.md; (7) só publique com minha aprovação explícita e confirme em janela anônima depois. Não aproveite para fazer outras melhorias. Se o hotfix mexer em texto ou visual, rode P-13 (momento: pós-camada) só na área tocada.
```

### M-17. Verificação, regressão e antes/depois

```text
M-17 (verificação). Remeça tudo do baseline (docs/baseline.md) e rode o checklist de regressão (seção 9.2 do Guia 4): URLs, formulários (envio real), integrações, rastreamento, visual (screenshots de todas as páginas, desktop e celular), responsivo, acessibilidade, performance, SEO, segurança, mídia e direitos, conteúdo editável, documentação e cara de IA (P-13, momento: final, comparando com o diagnóstico). Entregue docs/antes-depois.md com a tabela: Métrica | Antes | Depois | Meta | Resultado, e uma lista de regressões encontradas e corrigidas. Itens não verificados devem aparecer como "não verificado", nunca como OK. Segurança e acessibilidade vencem a estética. Não declare "pronto" com item crítico pendente.
```

### M-18. Entrega, relatório e manutenção

```text
M-18 (entrega). (1) Atualize DESIGN.md, CLAUDE.md e docs/handoff.md (stack, comandos, estrutura, tokens, decisões, pendências, como atualizar conteúdo, o que o cliente pode editar sozinho); (2) gere docs/relatorio-cliente.md em linguagem simples: o que foi feito, por que, números antes/depois, o que ficou para depois e o que o cliente precisa fazer; (3) registre tudo em docs/melhorias.md com data; (4) liste 3 lições para próximos projetos deste segmento ({{segmento}}); (5) liste licenças e créditos de tudo o que foi usado (componentes, fontes, imagens, vídeo, áudio, referências); (6) sugira rotina de manutenção (revisão trimestral de dependências, segurança e performance). Publicação só com aprovação explícita.
```

---

## Parte S13. Redesign de site existente

Cenário S13 do mapa (Guia 1, seção 5). Para qualquer outra melhoria em projeto existente, use a Parte M.

```text
S13-I (instalação). Siga P-00. GLOBAL: mattpocock/skills ; vibe-security ; unlazy ; a11y/perf/SEO (https://ui-skills.com, confirmar). PROJETO: Impeccable https://github.com/pbakaus/impeccable ; Jakub https://github.com/jakubkrehel/skills ; Hallmark https://github.com/nutlope/hallmark (OU Taste redesign-skill https://github.com/Leonxlnx/taste-skill; escolha 1) ; baseline-ui e optimize (https://ui-skills.com, confirmar).
```

```text
S13-1 (diagnóstico, sem alterar nada). Rode Impeccable `critique` e `audit` e, como segunda opinião, `Hallmark audit` no site atual ({{URL ou pasta}}). Compare as duas listas lado a lado, classifique cada achado como ACABAMENTO, ESTRUTURA, MARCA ou CARA DE IA, estime impacto e esforço, e me proponha o plano mínimo. Rode P-13 (momento: diagnóstico) e inclua os sinais encontrados. Não altere código.
```

```text
S13-2 (registrar o que existe). Rode Impeccable `document` para gerar DESIGN.md a partir do código atual. Mostre divergências entre o que o site faz e o que um bom design system pediria. Use ponytail-audit/optimize só se houver excesso de dependências ou peso.
```

```text
S13-3 (aplicar em camadas). Camada 1: acabamento (Jakub better-interface, baseline-ui, estados com `break`). Camada 2: se necessário, estrutura com `redesign` da skill mestre mantendo texto, arquitetura e marca; se o cliente trouxer referência (site, print, efeito), mostre-me antes a escolha de vídeo de referência (P-14). Camada 3: P-10 (segurança, a11y, performance, SEO) e P-13 (momento: final). Depois de cada camada, rode P-13 (momento: pós-camada), mostre antes/depois e só prossiga com minha aprovação. Pedidos de ajuste visual entre as camadas seguem o P-15.
```

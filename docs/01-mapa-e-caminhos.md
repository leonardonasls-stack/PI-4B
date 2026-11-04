# Guia 1 de 4: Mapa e Caminhos

**Qual cenário, qual tier, quais ferramentas, onde instalar (global ou projeto), o que evitar e qual trilha de prompts seguir**

Este é o arquivo de **decisão**. O texto pronto dos prompts está no **Guia 2A de 4** (`02-prompts-criacao.md`). Os prompts de edição de projeto existente estão no **Guia 2B** (`02-prompts-edicao.md`). Derivado do *Guia de Skills, Bibliotecas e MCPs para Design de Sites (v2, pesquisa de 01/10/2026)*.

> **Aviso de honestidade**
> - **Fatos** (o que cada ferramenta faz, comandos, avisos) vêm da pesquisa do guia original. Reconfirme o comando no README oficial **no dia da instalação**.
> - **Combinações, tiers, trilhas e escopo global x projeto** são **curadoria editorial**, não medição. Valide em um projeto descartável.
> - **K24 (`watch`)** foi acrescentado depois, a partir do README oficial lido em 02/10/2026. Os **sinais do `P-13`** (gate anti-"cara de IA") são curadoria editorial.
> - Onde o guia não trazia o repositório exato de uma skill, o link aponta para o catálogo (`https://ui-skills.com`) e está marcado com **⚠ confirmar**. Nenhum link foi inventado.

---

## Sumário

1. Como usar os dois arquivos (caminho em 6 passos, intake, roteamento rápido)
2. Regras que valem para todos os cenários
3. Estratégia de instalação: global x projeto
4. Catálogo de links, comandos e escopo
5. Cenários S1 a S14 (perfil, tiers, escopo, `CLAUDE.md`, **trilha de prompts**)
6. Combinações por situação de trabalho
7. Combinações por restrição
8. Matriz de incompatibilidades
9. Roteamento do agente (YAML) e mapa cenário x camada
10. Checklist pré-publicação
11. Pendências e cuidados
12. **Modelos de site (TS1 a TS8) e níveis de efeito (E0 a E5)**
13. **Mídia: fotos, vídeo, áudio e scroll com mídia**
14. **Features de referência (quando o cliente vê algo em outro site)**
15. **Roteamento adicional (YAML) para modelo, efeito e mídia**

---

## 1. Como usar os dois arquivos

| Arquivo | Para quê | Quando abrir |
|---|---|---|
| **`01-mapa-e-caminhos.md`** (este) | **Decidir**: cenário, tier, ferramentas, escopo (global ou projeto), links, o que evitar, trilha de prompts | Sempre **primeiro** |
| **`02-prompts-criacao.md`** | **Executar (projeto novo)**: texto pronto de cada prompt (sistema, universais, por cenário, situações, utilitários, **modelo/mídia/features na Parte E**) | Depois, **só a parte da trilha escolhida** |
| **`02-prompts-edicao.md`** | **Executar (projeto existente)**: texto pronto dos prompts `M-*` e `S13-*` | Depois do `04`, **só os prompts do tipo de intervenção** |
| **`03-perguntas-para-clientes.md`** | **Perguntar**: roteiro de conversa com o cliente (base, por cenário, por modelo e mídia, por situação) | **Antes** de tudo, na reunião de briefing |
| **`04-melhorar-e-editar.md`** | **Melhorar/editar** site ou projeto **existente**: diagnóstico, tipos de intervenção (M1 a M12), fluxo seguro, trilhas `M-*`, regressão | Quando já existe site/app (inclui o S13) |

**Modo manual:** faça o intake (abaixo) → ache o cenário (seção 5) → siga a **trilha** → copie cada prompt do `02-prompts-criacao.md` na ordem.
**Modo agente:** coloque os arquivos em `docs/`, cole o prompt de sistema (`02-prompts-criacao.md`, Parte 0) e envie o intake. **Projeto que já existe ou está em andamento:** cole no lugar o prompt inicial de melhoria (`02-prompts-edicao.md`, Parte 0) e envie a mensagem inicial dele. Se o projeto não tem `CLAUDE.md`, `DESIGN.md` nem `docs/`, o agente cria esses arquivos a partir do código (`M-A`, Parte 0-A). O agente lê o mapa inteiro e abre só os trechos de prompts da trilha (economiza contexto).

### Caminho em 6 passos

| Passo | O que fazer | Onde |
|---|---|---|
| **0. Intake** | Responder 4 dados, **nesta ordem**: objetivo → tipo de negócio → stack → prazo | Abaixo |
| **1. Rotear** | Tipo de negócio → cenário (S1 a S14); prazo → tier; **o que o cliente quer do site → modelo (TS1 a TS8) e nível de efeito (E0 a E5)** | Tabelas abaixo, seção 5 e **seção 12** |
| **2. Planejar** | Skill mestre única, sistema de processo (ou nenhum), lista **global** e lista **projeto**, o que **não** instalar | Seções 3, 4, 8 |
| **3. Instalar** | `P-00` + prompt `S#-I` do cenário | `02-prompts-criacao.md`, Partes A e B |
| **4. Executar a trilha** | Prompts `S#-1…` na ordem; só avance quando o critério de saída for verdadeiro. Pedidos de ajuste visual no meio do caminho: `P-15` (não sair da rota) | Trilha do cenário (seção 5) |
| **5. Verificar e fechar** | Checklist (seção 10) + `D-2` + `P-13` (gate anti-IA, final) + `P-12` (handoff) | Seção 10; `02-prompts-criacao.md`, Parte D |

### Passo 0: Intake (o que pensar em cada dado)

| Ordem | Dado | Por que nesta ordem | Perguntas-chave |
|---|---|---|---|
| 1 | **Objetivo** | Define a ação principal e quanto efeito/motion cabe. Escolha **um** | Qual ação o visitante deve fazer? Como medir sucesso? |
| 2 | **Tipo de negócio** | Define cenário, tom e restrições embutidas | Quem é o público? Há regra de publicidade profissional? Há dados pessoais ou de saúde no formulário (LGPD)? Acesso é mais pelo celular? |
| 3 | **Stack** | Filtra quais skills funcionam de verdade | Qual stack já existe? Quem mantém o site depois? O cliente edita sozinho? |
| 4 | **Prazo** | Define o **tier** e corta escopo (nunca o mínimo de qualidade) | Quando precisa estar no ar? O que já existe (logo, fotos, textos, domínio)? |
| 5 | **Modelo, mídia e features** | Define **como o site se comporta** (simples, com efeitos, editorial, cinematográfico, com banco), quanto movimento cabe e que mídia existe (seções 12 a 14) | Simples ou ousado? Tem vídeo, áudio, fotos? Viu algum efeito em outro site que quer? Precisa de login ou dados que mudam? |

**Modelo de resposta de intake (cole para o agente):**

```text
Objetivo: {{uma ação principal}}
Tipo de negócio: {{ex.: escritório de advocacia trabalhista em Maceió}}
Stack: {{ex.: HTML + CSS puro | Vite + React + Tailwind + shadcn | outra | "ainda não definida"}}
Prazo: {{ex.: 5 dias}}
Já tenho: {{logo, paleta, fotos, textos, domínio, hospedagem, ou "nada ainda"}}
Formulário: {{sim, com envio por e-mail | não, só WhatsApp}}
Restrições: {{ex.: confirmar regras de publicidade do conselho profissional}}
Modelo de site: {{TS1 a TS8 (seção 12) ou "não sei"}}
Nível de efeito desejado: {{E0 a E5 ou "não sei"}}
Mídia disponível: {{fotos, vídeos, áudio, nada ainda}}
Features de referência: {{links/prints do que o cliente gostou, ou "nenhuma"}}
Vídeo de referência: {{arquivo ou link + trecho mm:ss, ou "nenhum"}} (mostre a escolha; análise com a skill watch, prompt P-14)
Dados e banco: {{não | sim: login, agenda, catálogo, painel}}
```

### Roteamento rápido: tipo de negócio → cenário

| Tipo de negócio | Cenário |
|---|---|
| Agência ou estúdio de design (site da própria agência) | **S1** |
| Estúdio que atende vários clientes (processo, consistência, handoff) | **S2** |
| Pilates, yoga, academia, bem-estar | **S3** |
| Advocacia, clínica, consultoria, contabilidade | **S4** |
| Restaurante, cafeteria, salão, barbearia | **S5** |
| Landing page de app ou SaaS | **S6** |
| Web app, painel, dashboard | **S7** |
| App mobile (Expo/React Native) ou PWA | **S8** |
| Loja online, catálogo | **S9** |
| Blog, documentação, curso, infoproduto | **S10** |
| Portfólio criativo, produto 3D, scroll cinematográfico | **S11** |
| Vídeo de lançamento, campanha, pitch | **S12** |
| Site existente a melhorar | **S13** |
| Protótipo ou MVP em um dia | **S14** |

### Prazo → tier (sugestão editorial)

| Prazo | Tier | O que entra | O que cai primeiro |
|---|---|---|---|
| Até 1 dia | **S14** (perfil mínimo) | Skill mestre + Inspo + uma revisão | Tudo que não for o essencial; registre a dívida |
| 2 a 5 dias | **Econômica** | Briefing curto → referência → skill mestre → revisão → qualidade mínima | Motion, opções ao cliente, vídeo, 3D |
| 1 a 3 semanas | **Padrão** | + copy revisada, componentes prontos, qualidade técnica completa | Vídeo, 3D |
| 1 mês ou mais | **Premium** | + opções ao cliente, sistema de processo, motion/3D/vídeo (se justificar) | Nada, mas cada efeito precisa de justificativa |

Segurança e acessibilidade **não caem com o prazo** quando há formulário, login ou pagamento.

### Stack → o que funciona (do guia original)

| Stack | Observação |
|---|---|
| HTML + CSS puro | Hallmark gera HTML+CSS autocontidos; `ponytail` favorece o nativo do navegador |
| React + Tailwind + shadcn | Cenário mais coberto: 21st.dev, React Bits, Canvas UI, Paper Shaders, `react-best-practices` |
| Vite + React | Garden `web-design-engineer` assume familiaridade com essa stack |
| Vue / Nuxt | `antfu/*` e `vuejs-ai/*`; Canvas UI tem versão Vue |
| React Native / Expo (nativo) | **Lacuna do guia**: ver cenário S8 |
| WordPress e CMS | **Não coberto pelo guia**; o agente deve avisar e não improvisar |

### Conflitos comuns e como resolver

| Conflito | Resolução |
|---|---|
| Prazo curto + stack complexa | Simplifique a stack, não as verificações |
| Objetivo de marca + performance crítica | Paper Shaders no lugar de 3D |
| Negócio regulado + copy ousado | A restrição legal vence o tom |
| Objetivo de conversão + vontade de "wow" | Efeito fora da primeira dobra |

### Exemplo preenchido: advocacia em 5 dias

- **Intake:** objetivo = gerar contatos qualificados (WhatsApp ou formulário); tipo = escritório de advocacia; stack = HTML + CSS puro (ou a que você já domina); prazo = 5 dias.
- **Roteamento:** cenário **S4**, tier **Econômica**.
- **Trilha:** `P-00` → `S4-I` → `S4-1` → `S4-2` → `S4-3` → `S4-4` → `P-13` → `P-12`.
- **Calendário sugerido:** dia 1 briefing, referências e direção (`S4-1`, `S4-2`) · dias 2 e 3 copy e construção (`S4-3`) · dia 4 qualidade (`S4-4`) · dia 5 folga, correções e handoff.
- **Fica de fora:** `design-lab` (opções), vídeo, motion, Canvas UI. **Fica dentro:** Hallmark, Impeccable, Inspo, `no-ai-slop`; `vibe-security` se houver formulário com backend.
- **Sinal de alerta:** se o agente propuser Canvas UI, GSAP pesado ou sistema de processo, ele não seguiu o cenário S4; mande reler as seções 5 e 8.

---

## 2. Regras que valem para todos os cenários

1. **Uma ferramenta principal por camada.** Quase todo problema (saída inconsistente, instruções conflitantes, estouro de contexto) vem de duas ferramentas disputando a mesma camada.
2. **Uma skill mestre de geração visual por projeto** (Hallmark **ou** Taste Skill **ou** Tastemaker). Declare no `CLAUDE.md`.
3. **Um sistema de processo pesado por projeto** (Superpowers, GSD, gstack, ECC, Ruflo, Designpowers). Landing simples: nenhum.
4. **Um `DESIGN.md` por projeto** como fonte única de tokens; todas as skills leem esse arquivo.
5. **Precedência quando há conflito:**
   1. pedido atual e restrições do briefing
   2. `DESIGN.md` / `PRODUCT.md`
   3. skill mestre de geração
   4. skills de revisão (Impeccable, Jakub): sugerem, não reescrevem a direção
   5. skills de qualidade (a11y, performance, SEO, segurança): **vencem a estética**
   6. skills de processo/economia (`ponytail`, `caveman`): nunca sobrepõem decisão de design
6. **Efeitos de GPU/WebGL** só com justificativa de marca, com fallback estático e `prefers-reduced-motion`.
7. **Referências servem para extrair princípios** (estrutura, ritmo, tipografia), não para copiar layouts, marcas ou screenshots.
8. **MCPs ocupam contexto.** Ligue só os necessários; prefira os somente leitura.
9. **O modelo define o nível máximo de efeito** (seção 12). Efeito acima do nível do modelo só entra pelo protocolo de feature de referência (seção 14), com decisão e impacto registrados.
10. **Mídia sem papel, sem licença ou sem fallback não entra** (seção 13). Áudio nunca é automático.
11. **Gate anti-"cara de IA" obrigatório** (`P-13`). Projeto novo: `direção` (chamado em P-04 e P-06), `construído` (P-07) e `final` (fim de toda trilha, antes do `P-12`). Nos cenários cujos prompts não passam por P-04, P-06 ou P-07 (S2, S7, S8, S9, S10, S11, S12), o gate é chamado dentro do próprio passo (`S2-3`, `S7-2`, `S7-3`, `S8-2`, `S8-3`, `S9-3`, `S10-2`, `S10-3`, `S11-1`, `S11-3`, `S12-3`) e nos módulos de efeito (`E-4`, `E-7`, `E-10`). Projeto existente: `diagnóstico`, `pós-camada` (depois de cada camada que mexe em visual, texto, mídia, efeito ou tela nova) e `final`. O gate sugere correções; mudar a direção aprovada, textos aprovados ou área regulada exige aprovação. Veredito "não passa" bloqueia a entrega.
12. **Referência pede a escolha de vídeo** (`P-14`). Sempre que o fluxo pedir uma referência (efeito, transição, modal, menu, scroll), mostre ao usuário a opção de usar vídeo. Vale também quando for construir um efeito, modal, menu, gesto ou transição descrito de forma vaga (`P-02`, `P-07`, `P-08`, `S8-2`, `E-7`, `E-8`, `E-10`). Vídeo é analisado com a skill `watch` (K24), nunca de memória; se ela falhar ou não estiver disponível, relate e pare. O motor da análise é sempre fixado com `--engine` (o padrão `auto` usa o Gemini, e envia o vídeo ao Google, quando existe `GEMINI_API_KEY`).
13. **Ajuste visual dentro da rota** (`P-15`). Quando o fluxo perguntar ao usuário se ele quer mudar algo visualmente e ele quiser, cada pedido é classificado (ajuste dentro da direção, mudança de direção, backlog ou conflito de qualidade) e os ajustes são aplicados em lote, com registro em `docs/ajustes.md` e uma tag para reverter. Mudança de direção só com o impacto mostrado e confirmação explícita. Pedido repetido, ajuste desfeito (A → B → A) ou mais de 3 rodadas na mesma fase param o loop: o agente mostra as versões lado a lado e oferece reverter, gerar opções (`P-05`) ou tratar como mudança de direção. Durante um ajuste, o agente não troca de skill mestre, não reinstala ferramentas e não reescreve o `DESIGN.md` inteiro.
14. **Escolhas exatas antes de criar ou editar** (`P-16`). Tipografia, disposição dos itens, tipo de cada item e referências em bibliotecas de elementos (21st.dev, shadcn/ui, React Bits, Canvas UI ou outra que o usuário tiver) são apresentados ao usuário em 4 rodadas curtas, com opções reais, recomendação e valores exatos, e ficam em `docs/escolhas.md` e `docs/refs/componentes.md`. Nada disso é decidido por padrão pelo agente. Na criação, o `P-16` vem antes do `DESIGN.md` (`P-04`); na edição, extrai a ficha atual no diagnóstico e só pergunta sobre o que for ajustar ou trocar. O `P-13` confere se o construído segue a ficha, e trocar família, grade ou tipo de item depois do ok é mudança de direção (`P-15`).
15. **Referência por elemento** (`P-17`). Referência só ajuda se disser **qual elemento** e **o que pegar**. Cada elemento do projeto (navbar, hero, título, cartão, botão, formulário, rodapé, modal, menu, estados...) é amarrado a uma referência concreta em `docs/refs/mapa-elementos.md`, com o que pegar, o que não pegar e como adaptar. **Elemento sem referência aprovada não é construído**: o agente pede material ao usuário (vídeo, imagem, print, link com o ponto exato ou elemento de biblioteca). Se o usuário disser "livre", o agente avisa uma vez que tende a ficar genérico e traz 2 ou 3 opções distintas. Ao fazer algo específico (efeito, modal, menu, seção de destaque), pede um exemplo antes. Depois de construir, compara com a referência e registra a fidelidade em `docs/refs/fidelidade.md`; o `P-13` trata elemento sem referência ou divergente sem motivo como sinal alto.
16. **Efeitos enraizados** (`P-18`). Efeito é fundamental e **nunca é escolhido por padrão**. Todo efeito (botão, cartão, campo, menu, transição, rolagem, texto, fundo, cursor, carregamento) tem propósito, parâmetros e referência aprovados em `docs/refs/mapa-efeitos.md`. Em cada categoria, o agente mostra ao usuário o painel "Onde procurar" (seção 4.2.1) com as bibliotecas e links, para ele escolher algo que goste; depois decompõe o componente real (duração, easing, distância, dependências, peso, licença, acessibilidade), constrói um **protótipo dos efeitos-chave** e só então espalha. Fallback e `prefers-reduced-motion` são obrigatórios; o `P-13` tem camada própria para efeitos.

---


## 3. Estratégia de instalação: global x projeto

**Princípio (editorial):** instale **globalmente** o que é *leve, sem opinião de estilo e útil em todo projeto*. Instale **por projeto** tudo que tem *opinião visual*, *muda o fluxo do agente* ou *ocupa contexto*. Assim você evita deriva de estilo entre clientes e conflitos entre skills.

| Critério | Global | Projeto |
|---|---|---|
| Opinião de estilo (Hallmark, Taste, Tastemaker, Garden) | Não | **Sim** (uma por projeto) |
| Sistema de processo pesado (Superpowers, GSD, gstack, ECC, Ruflo, Designpowers) | Não | **Sim**, só se o projeto pedir |
| Skills leves de método (briefing, anti-preguiça) | **Sim** | Opcional |
| Auditorias (segurança, a11y, performance, SEO) | **Sim** (rodam sob demanda) | Opcional |
| Revisão de acabamento (Impeccable, Jakub, Emil) | Possível | **Preferível** por projeto, para versionar com o repositório |
| MCPs (Inspo, 21st.dev, Canvas UI, UI Skills) | Só Inspo, se você usa em todo projeto | Demais: **por projeto** |
| Bibliotecas de código (shadcn, coss ui, Paper Shaders, React Bits, Canvas UI, ObsidianUI, OriginKit, Bencho, Beautiful UI, AICSS) | n/a (vão no `package.json`) | **Projeto** |

**Kit global recomendado (instale uma vez, mantenha pequeno, ideal de 5 a 8 itens):**
`grill-me` (+ `grill-with-docs` se quiser), `vibe-security`, `no-ai-slop`, `unlazy`, `ui-skills-root`, e as skills de acessibilidade/performance/SEO que você mais usa. Opcional, sob demanda: `watch` (K24), se você recebe vídeos de referência.

**Por quê manter o global pequeno:** em geral as descrições das skills instaladas ficam disponíveis ao agente o tempo todo; muitas skills globais aumentam ruído e a chance de o agente escolher a errada. Reavalie a cada trimestre.

**Como instalar em cada escopo**
- **`npx skills add ...`**: por padrão instala no **projeto**. Para global use a flag `-g` / `--global` (**⚠ confirmar com `npx skills add --help`**, pois a CLI pode mudar).
- **Claude Code, à mão:** projeto = `.claude/skills/<nome>/` · global = `~/.claude/skills/<nome>/`.
- **Plugins do Claude Code** (`/plugin marketplace add ...` e `/plugin install ...`): escolha o escopo na instalação (usuário ou projeto), conforme o menu atual do Claude Code.
- **MCP no Claude Code:** `claude mcp add ...` (confira a opção de escopo local/projeto/usuário em `claude mcp add --help`).
- **Claude.ai (web):** Configurações > Capacidades > Skills.

**Prompt de decisão de escopo:** em `02-prompts-criacao.md`, Parte D (D-1).


---


## 4. Catálogo de links, comandos e escopo

Legenda de escopo: **G** = global recomendado · **P** = por projeto · **P*** = por projeto, só se o cenário exigir.
Todos os comandos vêm do guia original; **reconfirme no README oficial**.

### 4.1 Skills, plugins e sistemas

| ID | Ferramenta | Link | Comando de instalação (do guia) | Escopo |
|---|---|---|---|---|
| K01 | **grill-me** / grill-with-docs (Matt Pocock) | https://github.com/mattpocock/skills | `npx skills@latest add mattpocock/skills` e depois `/setup-matt-pocock-skills` uma vez por repositório | **G** |
| K02 | **Hallmark** (Nutlope) | https://github.com/nutlope/hallmark | `npx skills add nutlope/hallmark` | **P** (mestre) |
| K03 | **Taste Skill** (Leonxlnx) | https://github.com/Leonxlnx/taste-skill | `npx skills add https://github.com/Leonxlnx/taste-skill --skill "design-taste-frontend"` (ou outra variante) | **P** (mestre) |
| K04 | **Tastemaker** (codeswithroh) | https://github.com/codeswithroh/tastemaker | `/plugin marketplace add codeswithroh/tastemaker` e `/plugin install tastemaker@codeswithroh` | **P** (mestre; não junto com Hallmark) |
| K05 | **Impeccable** (pbakaus) | https://github.com/pbakaus/impeccable | `npx skills add pbakaus/impeccable` | **P** (revisão) |
| K06 | **Emil Kowalski skills** | https://github.com/emilkowalski/skills | `npx skills@latest add emilkowalski/skills` | **P** |
| K07 | **Jakub Krehel skills** | https://github.com/jakubkrehel/skills | `npx skills add jakubkrehel/skills` (ou plugin `interfaces@interfaces`) | **P** |
| K08 | **MengTo Skills** | https://github.com/MengTo/Skills | `npx skills add https://github.com/MengTo/Skills --skill <nome>` (**uma por vez**) | **P*** |
| K09 | **GSAP oficial** (GreenSock) | https://github.com/greensock/gsap-skills | `npx skills add greensock/gsap-skills` (**⚠ confirmar forma do comando**) | **P*** |
| K10 | **vibe-security** (Chris Raroque) | https://github.com/raroque/vibe-security-skill | `npx skills add https://github.com/raroque/vibe-security-skill --skill vibe-security` | **G** |
| K11 | **no-ai-slop** (Peter Yang) | https://ui-skills.com (buscar `no-ai-slop`) · **⚠ confirmar repositório** | comando na página do catálogo ou no repositório do autor | **G** |
| K12 | **unlazy** (Leonxlnx) | https://ui-skills.com (buscar `unlazy`) · **⚠ confirmar repositório** | comando na página do catálogo | **G** |
| K13 | **ui-skills-root** (ibelick; roteador de skills) | https://ui-skills.com e https://github.com/ibelick/ui-skills | ver página `ibelick/ui-skills-root` no catálogo | **G** |
| K14 | **Garden Skills** (`web-design-engineer`) | https://github.com/ConardLi/garden-skills | `npx skills add ConardLi/garden-skills -s web-design-engineer` | **P** (mestre alternativa) |
| K15 | **elayadesign/ai-design-skills** (`landing-page-design`) | busca no catálogo https://ui-skills.com · **⚠ confirmar repositório** | copiar `skills/<nome>` para `.claude/skills/` | **P*** (só intake/estrutura/copy) |
| K16 | **Superpowers** (obra) | https://github.com/obra/superpowers-marketplace | `/plugin marketplace add obra/superpowers-marketplace` e `/plugin install superpowers@superpowers-marketplace` | **P*** (lógica) |
| K17 | **ponytail** (DietrichGebert) | https://github.com/DietrichGebert/ponytail | `/plugin marketplace add DietrichGebert/ponytail` e `/plugin install ponytail@ponytail` | **P*** |
| K18 | **Designer Skills** (Owl-Listener) | https://github.com/Owl-Listener/designer-skills | `/plugin marketplace add Owl-Listener/designer-skills` | **P*** (estúdio) |
| K19 | **Obsidian-CLI-skill** (pablo-mano) | https://github.com/pablo-mano/obsidian-cli-skill | `npx skills add pablo-mano/obsidian-cli-skill` | **P*** |
| K20 | **HyperFrames** (HeyGen) | https://github.com/heygen-com/hyperframes | `npx skills add heygen-com/hyperframes` | **P*** (vídeo) |
| K21 | **GSD** | confirmar repositório ativo (guia §13) | `npx get-shit-done-cc` (**⚠ confirmar fork ativo**) | **P*** (projeto grande) |
| K22 | **Skills de a11y/perf/SEO** (`addyosmani/accessibility`, `core-web-vitals`, `seo`; `AccessLint/accessibility-scan`; `ibelick/fixing-motion-performance`; `ibelick/fixing-metadata`) | https://ui-skills.com (buscar pelo ID) · **⚠ confirmar repositório e comando de cada uma** | comando exibido na página de cada skill | **G** |
| K23 | **Estilos e extras** (`ibelick/baseline-ui`, `ibelick/create-design-md`, `0xdesign/design-lab`, `jakubkrehel/variant`, `petergyang/human-review`, `zarazhangrui/frontend-slides`, `emilkowalski/mobile-native`, `joe-bell/apple-web-app`) | https://ui-skills.com (buscar pelo ID) · **⚠ confirmar** | comando exibido na página de cada skill | **P*** |
| K24 | **watch** (claude-video, bradautomates): analisa vídeo e entrega quadros com timestamp e transcrição | https://github.com/bradautomates/claude-video | Claude Code: `/plugin marketplace add bradautomates/claude-video` e `/plugin install watch@claude-video` · outros agentes: `npx skills add bradautomates/claude-video -g --skill watch` (do README de 02/10/2026; **reconfirmar**) | **G** (sob demanda; ver 4.4) |

### 4.2 MCPs, bibliotecas, catálogos e apps

| ID | Item | Link | Instalação / uso | Escopo |
|---|---|---|---|---|
| M01 | **Inspo** (MCP, somente leitura) | https://inspomcp.dev | `npx -y inspo-mcp install` (use `--dry-run` antes) ou `claude mcp add --transport http inspo https://inspomcp.dev/api/mcp` | **P** (ou G se usar sempre) |
| M02 | **21st.dev** (marketplace de componentes da comunidade: *Marketing Blocks* como heroes, features, depoimentos, preços, rodapés e CTAs, e *UI Components* como botões, campos, cartões, modais, tabelas e formulários; Magic MCP, **exige chave**) | https://21st.dev | Cada componente tem página própria com `npx shadcn@latest add "https://21st.dev/r/<autor>/<componente>?api_key=$API_KEY_21ST"`. A chave vai em variável de ambiente; contas gratuitas têm limite diário de instalações. **A licença é por componente** (ex.: MIT): confira na página dele | **P** |
| M03 | **Canvas UI** (efeitos de canvas como Liquid, Glass, Shatter, Particle Reveal e VHS; MIT + Commons Clause) | https://canvasui.dev | `npx shadcn@latest add @canvas-ui/particle-reveal-react`. A maioria usa a API experimental *html-in-canvas* (Chrome ou Edge 140+ com flag; nos demais navegadores cai para uma sobreposição WebGL): **só para momentos "uau", com fallback e teste em celular real** | **P*** |
| M04 | **Paper Shaders** (shaders WebGL como mesh gradient, dithering, vidro canelado e água, para fundos, texturas e filtros de imagem) | https://shaders.paper.design | `npm i @paper-design/shaders-react`. Versões 0.0.x podem quebrar: **fixe a versão**. **⚠ Licença diverge entre as fontes** (PolyForm Shield no GitHub, MIT no npm): confirme no repositório antes de usar | **P*** |
| M05 | **React Bits** (componentes animados em 4 categorias: *text animations*, *animations*, *components* e *backgrounds*) | https://reactbits.dev | via shadcn ou jsrepo, conforme a página do componente | **P*** |
| M06 | **shadcn/ui** (base de componentes) | https://ui.shadcn.com | `npx shadcn@latest add <componente>` | **P** |
| M07 | **Open Design** (app desktop + daemon + MCP, Apache-2.0) | https://github.com/nexu-io/open-design | app desktop (Electron); BYOK | **P*** (estúdio) |
| M08 | **UI Skills** (catálogo, CLI e MCP) | https://ui-skills.com | descoberta de skills (use `ui-skills-root`) | **G** |
| M09 | **Ruflo** (MCP pesado) | https://github.com/ruvnet/ruflo | `claude mcp add ruflo -- npx ruflo@latest mcp start` | **Evite** em design |
| B01 | **ObsidianUI** (React + Tailwind + TypeScript; efeitos de hover, galeria, texto animado, marquee arrastável e templates; MIT segundo o GitHub) | https://www.obsidianui.dev | Registro no `components.json`: `"@obsidian": "https://www.obsidianui.dev/r/{name}.json"`; MCP do shadcn: `npx shadcn@latest mcp init`. Docs falam em Next.js (App Router) | **P*** |
| B02 | **Beautiful UI** (componentes copy-paste para **interfaces de agente e chat**: carregando, raciocínio, streaming, aprovação, chips de ferramenta, tabelas, barra lateral, bloco de código; MIT segundo o rodapé do site) | https://www.beautifului.dev | copiar do site; confirmar o passo a passo na página do componente | **P*** (só se o produto tiver agente ou chat) |
| B03 | **OriginKit** (biblioteca gratuita de componentes **animados**; copiar código, usar no Framer ou via MCP; variáveis editáveis como cor, tempo e easing) | https://www.originkit.dev | CLI: `npx originkit@latest add <id>`; MCP: `claude mcp add originkit https://mcp.originkit.dev/mcp --transport http --header "Authorization: Bearer <chave>" --scope user` (detalhes em https://www.originkit.dev/integrations). A chave é gratuita, na conta do site; use variável de ambiente (`ORIGINKIT_API_KEY`), nunca cole no chat nem versione | **P*** |
| B04 | **coss ui** (design system oficial da Cal.com; antigo Origin UI; React + Tailwind sobre **Base UI**, não Radix; primitivos, "particles" e "atoms") | https://coss.com/ui | Projeto novo: `pnpm dlx shadcn@latest init @coss/style`; projeto existente: `pnpm dlx shadcn@latest add @coss/ui`. O Origin UI antigo segue disponível, com suporte limitado | **P** (base de componentes) |
| B05 | **Bencho** (blocos React **interativos** e microinterações: arrastar, segurar, deslizar; menu radial, "slide to confirm", comparador de imagem, cartão que inclina, carrossel) | https://bencho.dev | a página lida não mostra instalação nem licença: **⚠ confirmar** antes de usar | **P*** |
| B06 | **AICSS** (componentes para **interfaces de agente**, em React, Vue e Svelte; gratuitos e CLI em MIT; os componentes **Pro** exigem licença comercial e o código Pro não é público) | https://www.aicss.dev | confirmar em https://www.aicss.dev/license e https://www.aicss.dev/pricing; use só o que a licença cobre | **P*** (só se o produto tiver agente) |

**Mapa de bibliotecas de elementos** (use no `P-16`, Bloco 4, para sugerir candidatos por tipo de item). Páginas lidas em 02/10/2026; contagens, planos e licenças mudam: confirme na página oficial.

| Tipo | Bibliotecas | Quando considerar | Cuidado de "cara de IA" |
|---|---|---|---|
| **Base de componentes** (formulários, diálogos, tabelas, navegação) | shadcn/ui (M06), coss ui (B04), 21st.dev (M02) | Todo projeto com interface; escolha **uma** base | Tema padrão sem ajuste aos tokens é sinal clássico (P-13) |
| **Efeitos e animação** (texto, fundo, cursor, hover, scroll) | OriginKit (B03), ObsidianUI (B01), React Bits (M05), Paper Shaders (M04), Canvas UI (M03) | Só nos momentos de impacto que o `DESIGN.md` permitir (no máximo 3 por página) | Efeito em todo bloco, brilho e 3D sem função; orçamento de peso e fallback para movimento reduzido |
| **Microinterações** (gestos, confirmação, menus especiais) | Bencho (B05) | Apps e painéis com interação própria; peça vídeo de referência (P-14) | Gesto decorativo sem tarefa; conferir teclado e foco |
| **Interfaces de agente e chat** | Beautiful UI (B02), AICSS (B06) | **Somente** quando o produto tem agente, chat ou fluxo de aprovação (S6 demo, S7, S8) | Em site institucional ou de negócio local, não cabem |

**Regras de uso de biblioteca:** (1) uma base de componentes por projeto (Radix, no shadcn/ui, e Base UI, no coss ui, não se misturam no mesmo conjunto sem decisão registrada); (2) biblioteca de efeito nunca é base; (3) o agente abre a página ou o código real do componente antes de usar, nunca de memória; (4) licença, dependências, peso, teclado, foco e `prefers-reduced-motion` conferidos; (5) componente pago ou Pro só com licença, e nunca se recria código pago a partir de prévia, DOM ou CSS do site; (6) chaves de MCP em variável de ambiente, nunca no chat nem no repositório; (7) adaptar aos tokens do `DESIGN.md`, sem copiar identidade ou assets.

### 4.2.1 Onde procurar cada elemento e cada efeito (painel para o usuário)

> **Para que serve:** em todo ponto do fluxo em que aparece um elemento típico (navbar, hero, botão, cartão, formulário, rodapé) ou um **efeito** (hover, pressionar, transição, rolagem, texto animado, fundo, cursor), o agente **mostra ao usuário** em quais bibliotecas ele pode olhar para escolher algo que goste, e pede o resultado (link, nome do componente, print ou gravação de tela). Isso vale para `P-16`, `P-17` e `P-18` e para os módulos de efeito. O mapa abaixo indica **onde há mais chance de achar**; as categorias exatas mudam, então confira o catálogo.

**Links rápidos:** [21st.dev](https://21st.dev) · [shadcn/ui](https://ui.shadcn.com) · [coss ui](https://coss.com/ui) · [React Bits](https://reactbits.dev) · [ObsidianUI](https://www.obsidianui.dev) · [OriginKit](https://www.originkit.dev) · [Bencho](https://bencho.dev) · [Paper Shaders](https://shaders.paper.design) · [Canvas UI](https://canvasui.dev) · [Beautiful UI](https://www.beautifului.dev) · [AICSS](https://www.aicss.dev)

| Elemento ou efeito | Abrir primeiro | Depois | Cuidado |
|---|---|---|---|
| **Navbar e menus** (barra fixa, item ativo, menu no celular) | 21st.dev (navigation menus) · shadcn/ui | coss ui · Bencho (menu radial) | Barra que encolhe ao rolar e menu com efeito: peça vídeo de referência (`P-14`) |
| **Hero** | 21st.dev (heroes) | ObsidianUI (templates) · OriginKit · React Bits (backgrounds e texto) | Hero com gradiente animado ou shader sem propósito é sinal do `P-13` |
| **Botões** (hover, pressionar, foco, carregando, sucesso) | 21st.dev (buttons) · ObsidianUI (efeitos de hover) · OriginKit | React Bits · Bencho (segurar, *slide to confirm*) | Uma família de botão por projeto; foco visível por teclado |
| **Cartões e itens** (hover, inclinar, expandir) | Bencho (cartão que inclina) · ObsidianUI (efeitos de hover) | 21st.dev (cards) · OriginKit | Um estilo de cartão por página; "levitar" em todo cartão é sinal de IA |
| **Texto animado** (títulos, contadores, marquee) | React Bits (*text animations*) · ObsidianUI (texto animado, marquee arrastável) | OriginKit | *Fade-up* em todo bloco é sinal; um efeito de entrada não se repete em tudo |
| **Fundos e atmosfera** (shader, partículas, ruído) | Paper Shaders · React Bits (*backgrounds*) | 21st.dev (efeitos de shader) · Canvas UI (só momentos "uau") | Peso e FPS no celular; fallback estático e `prefers-reduced-motion` |
| **Galeria, carrossel, comparador de imagem** | ObsidianUI (galeria) · Bencho (carrossel, comparador) | 21st.dev | Teclado, foco e rótulos nos controles |
| **Formulários e campos** (foco, validação, erro) | shadcn/ui · coss ui | 21st.dev (forms) | Estados de erro e vazio nunca ficam sem tratamento |
| **Modais, gavetas, popovers, abas, accordion** | shadcn/ui · coss ui | 21st.dev | Definido no `P-16` (modal, gaveta ou na página); foco preso no modal |
| **Transição de página e de seção** | Vídeo de referência (`P-14`) + skill `animate` | Canvas UI (transições de efeito, momentos "uau") | As bibliotecas do mapa são de componentes: a transição de página depende da stack; o agente propõe e você aprova o protótipo |
| **Rolagem** (revelar, parallax, fixar, progresso) | React Bits (*animations*) · OriginKit | GSAP e skills do Guia 1, seção 12.1 (E2 e E3) | Versão empilhada como fallback; parallax sem propósito é sinal |
| **Cursor e gestos** (arrastar, segurar, deslizar) | Bencho | ObsidianUI (marquee arrastável) | Gesto decorativo sem tarefa; alternativa por teclado |
| **Carregamento e feedback** (skeleton, spinner, toast, vazio) | shadcn/ui · coss ui | 21st.dev (loaders) | Texto de estado específico, não "Algo deu errado" |
| **Tabelas, painéis e gráficos** | shadcn/ui · coss ui | 21st.dev | Dados reais ou rotulados como exemplo |
| **Interface de agente ou chat** | Beautiful UI · AICSS | n/a | **Somente** se o produto tem agente ou chat |

**Painel padrão (texto que o agente mostra ao usuário, uma categoria por vez):**

```text
Onde ver exemplos para {{elemento ou efeito}}: abra {{Biblioteca A}} ({{URL}}) e {{Biblioteca B}} ({{URL}}), escolha algo que você goste e me mande o link, o nome do componente, um print ou uma gravação de tela de 5 a 15 segundos, dizendo o que gostou (estrutura, proporção, cor ou movimento). Se preferir, diga "sugira" e eu trago 3 candidatos que abri de verdade. Dizer "livre" costuma deixar o resultado genérico.
```

### 4.3 Ferramentas de teste no navegador (dão "mãos" ao agente)
`microsoft/playwright-cli`, `vercel-labs/agent-browser` (links via catálogo https://ui-skills.com, **⚠ confirmar**). Escolha **uma**.

### 4.4 Análise de vídeo de referência: `watch` (claude-video)

> Acrescentado depois da pesquisa original, a partir do README oficial lido em 02/10/2026. **Reconfirme comandos e requisitos no dia da instalação.**

Usada pelo prompt **`P-14`** (Guia 2A, Parte A), que **mostra ao usuário a escolha** de usar um vídeo de referência (gravação de tela, arquivo ou link com o trecho) para a IA entender melhor um efeito, transição, modal, menu ou microinteração. A skill entrega **quadros com timestamp e a transcrição**; interpretar o efeito e planejar a implementação é trabalho do agente.

| Ponto | O que saber (do README) |
|---|---|
| **Onde funciona** | Claude Code (sessão **Code** do Claude Desktop, VS Code ou terminal; a skill aparece como `/watch:watch`), Codex e outros agentes locais de skills. **Não funciona no Claude Chat nem no Cowork.** Claude Code na web roda em nuvem, com setup próprio e sem o instalador `/plugin`: prefira a máquina local |
| **Instalar** | Claude Code: `/plugin marketplace add bradautomates/claude-video` e `/plugin install watch@claude-video` · outros agentes: `npx skills add bradautomates/claude-video -g --skill watch` |
| **Requisitos** | Python 3.10+, FFmpeg/ffprobe e yt-dlp atual (YouTube pede também um runtime JavaScript, como Deno). A skill **não traz** esses programas; o `setup.py` dela confere |
| **Motores** | `local` (ffmpeg + yt-dlp; sem chave; nada sai da sua máquina) ou `gemini` (precisa de `GEMINI_API_KEY`; **o vídeo é enviado ao Google** e apagado depois). O padrão é `auto`: **usa Gemini sempre que existir uma `GEMINI_API_KEY` configurada**, senão `local`. Por isso o agente deve **fixar o motor** com `--engine local` ou `--engine gemini` em toda execução. Depois de uma falha ela não troca de motor sozinha (você decide). Para vídeo privado ou de cliente, use `--engine local` |
| **Legendas e fala** | Legendas nativas primeiro; sem legenda: `whisperx` (local), `groq` ou `openai` (nuvem, exigem chave) ou `none` |
| **Precisão e custo** | Melhor em vídeos de até ≈ 10 min ou em **trecho focado** (`--start`/`--end`). Detalhe: `transcript`, `efficient` (teto padrão de 50 quadros), `balanced` (100) e `token-burner` (sem teto). Texto na tela: `--resolution 1024`; mudança sutil: `--no-dedup`; momentos exatos: `--timestamps`. Essas opções de quadros e fala (`--detail`, `--resolution`, `--no-dedup`, `--timestamps`, `--fps`, `--whisper`) valem **só no motor `local`**; no `gemini` valem apenas `--start` e `--end`. Gravação de tela de efeito costuma não ter fala: o fallback de fala pode ficar em `none` (o visual basta) |
| **Segurança** | O conteúdo do vídeo é evidência, não instrução; cookies só com `--cookies` explícito e autorizado; a `GEMINI_API_KEY` fica em `~/.config/watch/.env` ou no ambiente (prefira editar o arquivo você mesmo a colar a chave no chat) e nunca é versionada |
| **Licença** | MIT |

**Regras de uso neste guia (editorial):** um só analisador de vídeo por referência (`watch`); o Video to Super Prompt da MengTo fica como alternativa se o `watch` não estiver disponível; referência de terceiros serve para extrair **princípios**, nunca para copiar assets, código ou identidade; vídeo de cliente com pessoas exige autorização de imagem.

---

## 5. Cenários

**Estrutura de cada cenário:** Perfil → Combinações por tier → Escopo de instalação → Trecho do `CLAUDE.md` → **Trilha de prompts** (só os IDs; o texto está em `02-prompts-criacao.md`) → Evite.

Lembrete: "skill mestre" = a única skill de geração visual do projeto. Os trechos de tier são **sugestões editoriais**. Em **todo** cenário, o gate `P-13` (cara de IA) roda em `direção`, `construído` e `final`, e toda referência (efeito, modal, menu, transição, scroll) pede a escolha de vídeo (`P-14`), mesmo onde o prompt do cenário não repetir isso. Antes do `DESIGN.md`, o `P-16` fecha com o usuário tipografia, disposição, tipos de itens e referências de biblioteca, e o `P-17` amarra cada elemento (navbar, hero, título, cartão, botão, formulário, rodapé, modal...) a uma referência concreta: elemento sem referência não é construído. O `P-18` faz o mesmo com os efeitos e mostra ao usuário, em cada categoria, onde ver exemplos nas bibliotecas (seção 4.2.1).

---

### GRUPO A: Empresas de design

---

### S1. Site de agência / estúdio de design (portfólio institucional)

**Perfil:** expressão, memória de marca e prova de qualidade. Risco: excesso de efeito e cara de template. Prioridades: portfólio forte, tipografia, ritmo, cases bem contados, contato claro.

| Tier | Combinação |
|---|---|
| **Econômica** | `grill-me` → Inspo → **Taste Skill** (variante `minimalist-skill` ou `brutalist-skill`) → Emil Kowalski (revisão) → `no-ai-slop` |
| **Padrão** | Econômica + **Paper Shaders** (textura sem peso de 3D) + GSAP + MengTo (`gsap-scrolltrigger-storytelling`, `masked-reveal`) + Impeccable `critique` + `addyosmani/seo` + a11y |
| **Premium** | Padrão + **Canvas UI** (hero de impacto, com fallback) + `img2threejs` + Taste `image-to-code-skill` + `design-lab`/`variant` (mostrar opções) + Jakub + HyperFrames (reel de 15 s) |

*Alternativa de skill mestre:* **Hallmark** se a diferenciação vier de exploração; use `study` nos prints do moodboard.

**Escopo:** **Global:** K01 grill-me, K10 vibe-security (se houver formulário/backend), K11 no-ai-slop, K12 unlazy, K22. **Projeto:** K03 Taste (ou K02 Hallmark), K06 Emil, K05 Impeccable, K08 MengTo (por skill), K09 GSAP, M01 Inspo, M04 Paper Shaders; Premium: M03 Canvas UI, K07 Jakub, K20 HyperFrames.

**`CLAUDE.md` (trecho):** skill mestre = Taste `{{variante}}`; motion principal = GSAP; revisão = Emil + Impeccable; WebGL só no hero, com fallback; **uma animação por intenção**; nenhum sistema pesado de processo.


**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S1):  
`S1-I` instalação → `S1-1` briefing e posicionamento → `S1-2` referências e direção → `S1-3` estrutura e cases → `S1-4` construção do hero e do ritmo → `S1-5` revisão e qualidade → `P-13` → `P-12` (handoff)

**Evite:** Canvas UI em várias seções; skills de conversão estrita (elaya) como mestre; `ponytail` em modo estrito dentro de cenas 3D; duas skills de motion instruindo o mesmo movimento.

---

### S2. Operação de estúdio com vários clientes (processo, consistência, handoff)

**Perfil:** consistência entre telas e clientes, entrega organizada, aprovação de opções. Risco: deriva de estilo e mistura de ferramentas entre projetos.

| Tier | Combinação |
|---|---|
| **Econômica** | Repositório-modelo com `CLAUDE.md` + `DESIGN.md` + `grill-me` + Hallmark (log em `.hallmark/log.json`) + Jakub |
| **Padrão** | **Tastemaker** (style lock) **ou** Hallmark + **Designer Skills** (processo) + Jakub + `design-lab`/`variant` + Impeccable `normalize` + `DESIGN.md` central |
| **Premium** | Padrão + **Open Design** (bancada de protótipos e exportação) + Obsidian-CLI-skill (briefings e moodboards) + `/design-ops:handoff` + `create-design-md` |

**Escopo:** **Global (conta do estúdio):** K01, K10, K11, K12, K13 (roteador), K22. **Por repositório de cliente:** a skill mestre (K04 Tastemaker **ou** K02 Hallmark, nunca as duas), K07 Jakub, K05 Impeccable, K18 Designer Skills (ou Designpowers), K23 `design-lab`. **Em máquina de design:** M07 Open Design, K19 Obsidian-CLI-skill (precisa do Obsidian aberto).

**`CLAUDE.md` (trecho):** um `DESIGN.md` por cliente; skill mestre fixa por cliente (registrar qual); modo **Direct** do Designpowers no início (você aprova cada passagem); não misturar GSD/Superpowers/gstack.


**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S2):  
`S2-I` instalação do kit do estúdio → `S2-1` criar o repositório-modelo do estúdio → `S2-2` onboarding de novo cliente → `S2-3` travar o estilo e produzir telas → `S2-4` revisão e handoff → `P-13` → `P-12` (handoff)

**Evite:** Tastemaker + Hallmark no mesmo projeto; vários sistemas pesados; instalar skill de estilo em escopo global (vaza estilo entre clientes).

---

### GRUPO B: Negócios locais e de serviços

---

### S3. Estúdio de Pilates / fitness / bem-estar

**Perfil:** acolhimento, confiança e conversão em **aula experimental** (via WhatsApp ou formulário). Público inclui pessoas mais velhas e iniciantes. Risco: site pesado no celular, texto pequeno, formulário que coleta dados demais. Prioridades: mobile primeiro, fotos reais do espaço e dos instrutores, planos e horários claros, SEO local.

| Tier | Combinação |
|---|---|
| **Econômica** | `grill-me` → Inspo → **Hallmark** (HTML+CSS autocontidos, leve) → `no-ai-slop` → `addyosmani/seo` + `fixing-metadata` + a11y |
| **Padrão** | Econômica + **21st.dev** (planos/pricing, depoimentos, FAQ) + **Paper Shaders** (textura suave de fundo) + Jakub (`better-typography`, `better-colors`) + `core-web-vitals` + Impeccable `audit` |
| **Premium** | Padrão + `design-lab` (2 a 3 direções para o dono escolher) + HyperFrames (vídeo curto de 10 a 15 s do espaço) + `emilkowalski/mobile-native` e `joe-bell/apple-web-app` (se houver PWA de agenda) + `vibe-security` (se houver backend de agendamento) |

*Alternativa de skill mestre:* **Taste `soft-skill`** (tom suave), se você já sabe que quer esse estilo. **Não use as duas.**

**Escopo:** **Global:** K01, K10, K11, K12, K22. **Projeto:** K02 Hallmark (ou K03 Taste `soft-skill`), M01 Inspo, M06/M02 shadcn + 21st.dev (Padrão+), M04 Paper Shaders, K07 Jakub, K05 Impeccable; Premium: K20 HyperFrames, K23 `design-lab`, `mobile-native`, `apple-web-app`.

**`CLAUDE.md` (trecho):** oferta = aula experimental; ação principal = botão de WhatsApp fixo no mobile; tom = acolhedor, claro, sem jargão fitness agressivo; contraste e tamanho de fonte acima do mínimo; coletar **o mínimo** de dados no formulário (nome, telefone, horário de preferência); **não** pedir condições de saúde no site.

**Estrutura sugerida de páginas:** Home · Aulas e modalidades · Planos e valores · Professores · O espaço · Depoimentos · Agendar aula experimental · Localização e contato · FAQ.


**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S3):  
`S3-I` instalação → `S3-1` briefing do estúdio → `S3-2` referências e direção → `S3-3` copy → `S3-4` construção mobile first → `S3-5` SEO local e formulário → `S3-6` revisão e qualidade → `S3-7` opcional: Premium → `P-13` → `P-12` (handoff)

**Evite:** Canvas UI/WebGL; hero em vídeo pesado no mobile; sistemas pesados (GSD/Ruflo); Hallmark e Taste juntos; formulário que pede histórico de saúde; promessas médicas no copy.

---

### S4. Clínica, advocacia, consultoria (institucional de confiança)

**Perfil:** credibilidade e clareza. Risco: parecer template; excesso de motion; regras de publicidade profissional. Prioridades: contraste, legibilidade, equipe, áreas de atuação, prova social ética, contato.

| Tier | Combinação |
|---|---|
| **Econômica** | `grill-me` → Inspo → **Impeccable** (revisão e vocabulário) + Hallmark (mestre) → `no-ai-slop` |
| **Padrão** | Econômica + 21st.dev (seções sóbrias) + Jakub (`better-typography`, `better-colors`) + `addyosmani/seo` + `accessibility` + `fixing-metadata` |
| **Premium** | Padrão + `design-lab` (opções) + `core-web-vitals` + `playwright-cli` (testar formulário) + `vibe-security` (formulário com dados pessoais) + `human-review` (ciclo de feedback com o sócio/cliente) |

**Escopo:** **Global:** K01, K10, K11, K12, K22. **Projeto:** K02 Hallmark, K05 Impeccable, K07 Jakub, M01 Inspo, M06/M02; Premium: K23 (`design-lab`, `human-review`), `playwright-cli`.

**`CLAUDE.md` (trecho):** motion decorativo proibido; contraste e legibilidade vêm antes do estilo; sem promessas de resultado; confirmar com o cliente as regras de publicidade do conselho profissional da área (OAB, CRM, CRO etc.); formulário coleta o mínimo.


**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S4):  
`S4-I` instalação → `S4-1` briefing e restrições → `S4-2` referências e direção → `S4-3` copy e construção → `S4-4` qualidade → `P-13` → `P-12` (handoff)

**Evite:** motion decorativo; estoque genérico de "pessoas apertando mãos"; alegações que o conselho profissional possa restringir.

---
### S5. Restaurante, cafeteria, salão, barbearia (negócio local)

**Perfil:** apetite visual e informação prática (cardápio, horários, endereço, reserva/WhatsApp). Risco: peso no celular, cardápio ilegível, efeitos de GPU em aparelhos fracos.

| Tier | Combinação |
|---|---|
| **Econômica** | Inspo → **Hallmark** → `no-ai-slop` → `addyosmani/seo` + `fixing-metadata` |
| **Padrão** | Econômica + **Paper Shaders** (texturas) + 21st.dev (galeria, depoimentos) + `emilkowalski/mobile-native` + `joe-bell/apple-web-app` + `core-web-vitals` |
| **Premium** | Padrão + HyperFrames (vídeo curto do ambiente/pratos) + `design-lab` (opções) + Jakub (`better-typography`) + `accessibility` |

**Escopo:** **Global:** K01, K11, K12, K22. **Projeto:** K02 Hallmark, M01 Inspo, M04 Paper Shaders, M06/M02; Padrão+: K23 `mobile-native`/`apple-web-app`; Premium: K20 HyperFrames, K07 Jakub.

**`CLAUDE.md` (trecho):** mobile primeiro; cardápio e horários legíveis **sem interação**; ação principal = reservar/pedir/WhatsApp; fotos reais de alimento/serviço; sem efeitos de GPU além de textura estática.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S5):  
`S5-I` instalação → `S5-1` briefing e direção → `S5-2` construção → `S5-3` SEO local e qualidade → `P-13` → `P-12` (handoff)

**Evite:** hero em vídeo pesado; PDF de cardápio; sistemas pesados; efeitos de GPU.

---

### GRUPO C: Desenvolvimento de app

---

### S6. Landing page de app ou SaaS (conversão)

**Perfil:** converter (download, cadastro, lista de espera, teste grátis). Risco: aparência genérica de "página de IA". Princípio: **uma oferta, um público, uma ação principal.** Elementos: demo/mockup do produto, prova social, preços, FAQ, selos de loja (quando for app).

| Tier | Combinação |
|---|---|
| **Econômica** | `grill-me` → Inspo → **Hallmark** → Emil Kowalski (revisão de motion) → `no-ai-slop` |
| **Padrão** | Econômica + `elayadesign/landing-page-design` (**só** intake, estrutura, copy e SEO) + 21st.dev (pricing, navbar, hero, depoimentos) + React Bits (micro-interações) + GSAP + `mengto/landing-page` e `pricing-page` + `addyosmani/seo` + `core-web-vitals` + Impeccable `audit` |
| **Premium** | Padrão + `design-lab` (testar 2 a 3 heros) + Paper Shaders (fundo) + HyperFrames (vídeo de demo) + `human-review` (feedback do time) |

**Escopo:** **Global:** K01, K10 (se houver cadastro/lista de espera), K11, K12, K22. **Projeto:** K02 Hallmark, K06 Emil, K05 Impeccable, K09 GSAP, K15 elaya (parcial), K08 MengTo (`landing-page`, `pricing-page`), M01 Inspo, M02/M06, M05 React Bits; Premium: K23, K20.

**`CLAUDE.md` (trecho):** skill mestre = Hallmark; a skill da elaya **só** contribui com intake, estrutura, copy e SEO (**suas regras visuais são ignoradas**); Canvas UI e WebGL **fora da primeira dobra** (performance de conversão); CTA único por seção.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S6):  
`S6-I` instalação → `S6-1` briefing de conversão → `S6-2` referências e direção → `S6-3` estrutura e copy → `S6-4` construção e motion → `S6-5` SEO, performance e revisão → `P-13` → `P-12` (handoff)

**Evite:** Canvas UI/WebGL acima da dobra; GSD/Ruflo; duas skills de landing com regras visuais conflitantes.

---

### S7. Web app / dashboard / SaaS (interface de produto)

**Perfil:** clareza, estados, velocidade, segurança. Risco: efeito decorativo, estados esquecidos (vazio, erro, carregando), regras de acesso fracas.

| Tier | Combinação |
|---|---|
| **Econômica** | **shadcn** (base) + Jakub (`better-interface`, `break`) + Impeccable `audit` + `vibe-security` |
| **Padrão** | Econômica + **Superpowers** (lógica e TDD) + `baseline-ui` + `react-best-practices`/`react-doctor`/`improve-react` + `agent-browser` **ou** `playwright-cli` + `accessibility-scan` + `create-design-md` |
| **Premium** | Padrão + `tailwind-token-consolidation` + `core-web-vitals` + `ponytail` (código enxuto) + Designer Skills (`/ui-design:design-screen`, `/design-ops:handoff`) para times |

**Escopo:** **Global:** K01, K10, K12, K22 (a11y). **Projeto:** M06 shadcn, K07 Jakub, K05 Impeccable, K16 Superpowers, K17 ponytail, K23 (`baseline-ui`, `create-design-md`), testes (um dos de 4.3). **Evite global** em Superpowers/ponytail (mudam o fluxo).

**`CLAUDE.md` (trecho):** sem efeitos decorativos; transições curtas e **interrompíveis**; números tabulares; todos os estados desenhados (vazio, carregando, erro, sucesso, desabilitado); regras de acesso ao banco revisadas por `vibe-security` antes de cada release; TDD nas partes com lógica.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S7):  
`S7-I` instalação → `S7-1` briefing de produto → `S7-2` arquitetura e tokens → `S7-3` construção por fatias → `S7-4` segurança e qualidade → `P-13` → `P-12` (handoff)

**Evite:** efeitos decorativos; motion longo; Canvas UI; dois sistemas de processo.

---

### S8. App mobile (Expo / React Native) e PWA

**Perfil:** experiência de app (toque, gestos, área segura, desempenho). **Atenção — lacuna do guia:** a maioria das skills do guia gera **web** (HTML/CSS/React DOM). Para **React Native/Expo nativo**, o guia só cita as skills de Emil Kowalski para **Expo/Swift** (via catálogo) e as skills oficiais do **Figma**. Trate este cenário como **PWA bem coberto** e **nativo parcialmente coberto**.

| Tier | Combinação (PWA/mobile-first web) |
|---|---|
| **Econômica** | `emilkowalski/mobile-native` + `joe-bell/apple-web-app` + Jakub `better-layout` |
| **Padrão** | Econômica + `emilkowalski/apple-design` (ou `dickwu/apple-design`) + `flornkm/prefer-container-queries` + shadcn + `accessibility-scan` |
| **Premium** | Padrão + Superpowers (lógica) + `vibe-security` (Firebase/Supabase) + `figma-design-to-code` (se o fluxo passa pelo Figma) |

| Tier | Combinação (nativo Expo/React Native) |
|---|---|
| **Econômica** | Skills de Expo da Emil Kowalski (**⚠ confirmar nomes no catálogo**) + Jakub (princípios) + `vibe-security` |
| **Padrão** | + Superpowers (TDD) + `react-best-practices` (princípios; confira aplicabilidade a RN) + Figma oficiais (`figma-design-to-code`) |
| **Premium** | + `ponytail` + Designer Skills (handoff) + `create-design-md` para tokens compartilhados |

**Escopo:** **Global:** K01, K10 (backend Firebase/Supabase), K12. **Projeto:** skills de mobile/Expo/Figma, K16 Superpowers (só se houver lógica), K07 Jakub.

**`CLAUDE.md` (trecho):** toque mínimo de 44 px; respeitar área segura; gestos interrompíveis; dark mode; regras de acesso do backend sob `vibe-security`; testar em aparelho real; tokens em um único `DESIGN.md` espelhado no tema do app.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S8):  
`S8-I` instalação → `S8-1` decisão de plataforma → `S8-2` tokens e componentes → `S8-3` construção e testes → `S8-4` segurança e publicação → `P-13` → `P-12` (handoff)

**Evite:** supor que Hallmark/Taste geram React Native (eles geram web); instalar skills de Swift em projeto RN; vários sistemas de processo.

---

### S9. E-commerce / catálogo

**Perfil:** conversão e confiabilidade. Risco: falhas de segurança em pagamento e lentidão. Prioridade: performance, clareza de produto, checkout seguro, acessibilidade.

| Tier | Combinação |
|---|---|
| **Econômica** | Inspo → componentes sóbrios (**shadcn/21st.dev**) → Impeccable `audit` → `vibe-security` |
| **Padrão** | Econômica + **Superpowers** (carrinho/checkout) + `core-web-vitals` + `performance` + `accessibility` + `seo` + Jakub `break` + `playwright-cli` + `no-ai-slop` (descrições) |
| **Premium** | Padrão + **GSD** (se houver várias fases, **em vez de** Superpowers) + `design-lab` (opções) + `ponytail` + `fixing-metadata` |

**Escopo:** **Global:** K01, K10, K11, K12, K22. **Projeto:** M06/M02, K05, K07, K16 **ou** K21 (um só), K17, testes (`playwright-cli`).

**`CLAUDE.md` (trecho):** nada de shaders/WebGL em página de produto e checkout; `vibe-security` obrigatório antes de qualquer release; preços e estoque sempre validados no servidor; acessibilidade em formulários; `caveman` proibido em decisões.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S9):  
`S9-I` instalação → `S9-1` briefing e catálogo → `S9-2` direção sóbria → `S9-3` construção com testes → `S9-4` segurança e performance → `P-13` → `P-12` (handoff)

**Evite:** WebGL em produto/checkout; `caveman`; misturar GSD e Superpowers.

---
### GRUPO D: Conteúdo, impacto, vídeo e evolução

---

### S10. Blog, documentação, curso online / infoproduto

**Perfil:** leitura confortável, SEO, confiança. Risco: efeito demais, metadados ruins, texto com cara de IA.

| Tier | Combinação |
|---|---|
| **Econômica** | `addyosmani/seo` (ou `iannuttall/seo`) + `no-ai-slop` + `performance` + `human-review` |
| **Padrão** | Econômica + Impeccable (tipografia) + Jakub (`better-typography`, `better-writing`) + `accessibility` + `fixing-metadata` |
| **Premium** | Padrão + Hallmark (página de vendas do curso) + `elayadesign/landing-page-design` (só estrutura/copy da página de vendas) + `HyperFrames` (vídeo de apresentação) |

**Escopo:** **Global:** K11, K12, K22 (SEO/a11y/perf), `human-review` (opcional). **Projeto:** K05, K07; Premium: K02, K15, K20.

**`CLAUDE.md` (trecho):** medida de linha confortável (≈ 60 a 75 caracteres), contraste AA, sem motion pesado nem efeitos de GPU; metadados e Open Graph em todo post; microcopy de interface revisada.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S10):  
`S10-I` instalação → `S10-1` estrutura de conteúdo → `S10-2` tipografia de leitura → `S10-3` texto e revisão humana → `S10-4` publicação → `P-13` → `P-12` (handoff)

**Evite:** motion pesado; efeitos de GPU; múltiplos humanizers.

---

### S11. Experiência de impacto: portfólio criativo, produto 3D, scroll cinematográfico

**Perfil:** impressionar e explicar. Risco: performance, acessibilidade, "tudo é efeito". Cada efeito precisa de **justificativa de marca**.

| Tier | Combinação |
|---|---|
| **Econômica** | Inspo → Taste Skill → GSAP → **Paper Shaders** (no lugar de 3D) |
| **Padrão** | Econômica + `img2threejs` + Taste `image-to-code-skill` + MengTo (`cinematic-scroll-storytelling`, `gsap-scrolltrigger-storytelling`) + Emil (`review-animations`) |
| **Premium** | Padrão + Canvas UI + `cloudai-x/threejs-*` + `mengto/threejs` + `webgl-landing-steering` + `oso95/scroll-world` + `flornkm/webgl-components` + `60fps-animation` + `fixing-motion-performance` + `accessible-animation` |

**Escopo:** **Global:** K01, K12, K22. **Projeto:** K03 Taste, K09 GSAP, K08 MengTo (por skill), K06 Emil, M04, M03; 3D: `img2threejs` (sua), `cloudai-x/threejs-*`, `flornkm/webgl-components`.

**`CLAUDE.md` (trecho):** cena 3D só onde explica ou emociona; fallback estático e `prefers-reduced-motion` obrigatórios; orçamento de performance definido (peso e FPS); **não** usar o recurso "vídeo para prompt" para reproduzir design de terceiros.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S11):  
`S11-I` instalação → `S11-1` conceito e storyboard → `S11-2` conceito 3D em imagem → `S11-3` scroll → `S11-4` performance, acessibilidade, revisão → `P-13` → `P-12` (handoff)

**Evite:** 3D em toda seção; Canvas UI sem fallback; duas skills de motion sem hierarquia.

---

### S12. Lançamento de produto com vídeo, campanha e apresentações (pitch)

**Perfil:** coerência entre página, vídeo e slides com a mesma identidade.

| Tier | Combinação |
|---|---|
| **Econômica** | HyperFrames (vídeo curto) + Hallmark (página) + GSAP |
| **Padrão** | Econômica + `general-video`, `motion-graphics` (HyperFrames) + `danny/motion-ad` + `zarazhangrui/frontend-slides` (**ou** `arifszn/slide-wright` **ou** `nextlevelbuilder/slides`; escolha 1) |
| **Premium** | Padrão + `latent-spaces/brag` (URL → vídeo curto) + `rieranthony/product-film` + `memex-lab/product-launch-video` + Open Design (exporta PPTX/PDF/MP4) + `remotion-to-hyperframes` (se vier de Remotion) |

**Escopo:** **Global:** K01. **Projeto:** K20 HyperFrames, K02 Hallmark, K09 GSAP, K23 (slides), M07 Open Design (Premium).

**`CLAUDE.md` (trecho):** **identidade única** em `DESIGN.md` reutilizada por página, vídeo e slides; HyperFrames como único motor de vídeo (escolha 1: HyperFrames **ou** Remotion; Remotion tem licença paga acima de certo porte); cortes para redes derivados do vídeo mestre.

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S12):  
`S12-I` instalação → `S12-1` identidade e roteiro → `S12-2` página e vídeo → `S12-3` pitch/slides → `P-13` → `P-12` (handoff)

**Evite:** dois motores de vídeo; identidade diferente em cada peça; reproduzir vídeos de terceiros com "vídeo para prompt".

---

### S13. Redesign de site existente

> **Para qualquer outra melhoria em projeto existente** (performance, acessibilidade, SEO, segurança, conteúdo, responsivo, adicionar efeito/mídia/dados, refatoração, hotfix), use o **Guia 4** (`04-melhorar-e-editar.md`). O S13 cobre o redesign visual; o Guia 4 traz o fluxo seguro (snapshot, baseline, camadas, regressão).

**Perfil:** melhorar sem quebrar. Risco: refazer tudo quando o problema era só acabamento.

| Tier | Combinação |
|---|---|
| **Econômica** | `Impeccable audit` + `critique` → `Jakub` (acabamento) → `baseline-ui` |
| **Padrão** | Econômica + `Hallmark audit` (segunda opinião) + `Impeccable document` (gera `DESIGN.md` do que existe) + `pbakaus/optimize` |
| **Premium** | Padrão + `Hallmark redesign` **ou** Taste `redesign-skill` (se a estrutura não salva) + `design-lab` (opções) + `playwright-cli` (regressão visual manual) |

**Escopo:** **Global:** K01, K10, K12, K22. **Projeto:** K05, K07, K02 (ou K03 para `redesign-skill`), K23 (`baseline-ui`, `design-lab`).

**Regra de decisão (editorial):** se o problema é **acabamento** (espaço, tipografia, estados), use Jakub + Impeccable. Se é **estrutura** (hierarquia errada, jornada confusa), use `redesign` da skill mestre. Se é **marca**, comece por P-02/P-04.

**Trilha de prompts** (texto em `02-prompts-edicao.md`, Parte S13):  
`S13-I` instalação → `S13-1` diagnóstico, sem alterar nada → `S13-2` registrar o que existe → `S13-3` aplicar em camadas → `P-13` → `P-12` (handoff)

**Evite:** redesign completo quando o problema é acabamento; duas skills de redesign.

---

### S14. Protótipo rápido / MVP em um dia

**Perfil:** velocidade com qualidade mínima aceitável. Risco: sobrecarga de ferramentas.

| Tier | Combinação |
|---|---|
| **Econômica** | Inspo → **Hallmark** ou Taste → 21st.dev/React Bits → Emil (revisão) |
| **Padrão** | Econômica + `unlazy` + `vibe-security` (se houver dados) |
| **Premium** | Padrão + `ui-skills-root` (achar a skill certa se travar) |

**Escopo:** só o **kit global mínimo** + **uma** skill mestre no projeto. **Qualquer sistema pesado está proibido neste cenário.**

---

**Trilha de prompts** (texto em `02-prompts-criacao.md`, Parte B, S14):  
`S14-I` instalação mínima → `S14-1` protótipo em um dia → `P-13` → `P-12` (handoff)

## 6. Combinações por situação de trabalho

Cada situação tem **receita** (ordem) e **prompt**. Elas se combinam com qualquer cenário da seção 5.

| Situação | Receita (ordem) | Evite |
|---|---|---|
| **A. Do zero, sem direção** | `grill-me` → Inspo `recommend(brief)` → `ui-ux-pro-max` (banco de estilos/paletas) **ou** Hallmark → `DESIGN.md` | Escolher o estilo antes de ver referências |
| **B. Tenho uma referência (print/URL/vídeo)** | `Hallmark study` (print/URL) → `design.md`; vídeo: mostrar a escolha e analisar com `watch` (K24, `P-14`); HTML: MengTo HTML to Interaction Prompts → construir com a skill mestre | Copiar a referência |
| **C. Site existente** | Cenário S13 | Redesign total sem diagnóstico |
| **D. Cliente vago** | `grill-me` → Inspo → `design-lab` (2 a 3 direções) | Construir antes de aprovar |
| **E. Mostrar opções ao cliente** | `design-lab`/`variant`/`prototype`/Open Design → registrar a escolhida | Variantes em skills diferentes |
| **F. Projeto longo com fases** | **Um** sistema: GSD **ou** Superpowers **ou** gstack + `unlazy` | Misturar sistemas |
| **G. Consistência entre telas** | Tastemaker (style lock) **ou** Hallmark (log) + `DESIGN.md` + Impeccable `normalize` | Duas skills de geração |
| **H. Fluxo passa pelo Figma** | Skills oficiais do Figma (`figma-design-to-code`, `figma-generate-design`, `figma-generate-library`, `figma-implement-motion`, `figma-shaders`) | Redigitar tokens |
| **I. Estudar um efeito que vi** | Jakub `explain-interface` (URL → como foi construído); vídeo: `watch` (`P-14`) | Reproduzir design de terceiros |
| **J. Achar skill para um problema** | `ibelick/ui-skills-root` | Instalar o catálogo inteiro |
| **K. Revisar um PR de UI** | Jakub `interface-review` → `vercel-labs/web-design-guidelines` | Revisão só "no olho" |
| **L. Animação com jank** | `fixing-motion-performance` → `60fps-animation` → Emil `review-animations` | Mais efeitos para "compensar" |
| **M. Preparar para publicar** | Seção 10 | Pular segurança e a11y |
| **N. Manter briefings em notas** | Obsidian-CLI-skill + `DESIGN.md` | Duplicar decisões |


**Prompts das situações (SIT-A, SIT-B, SIT-D, SIT-F, SIT-H, SIT-K):** texto em `02-prompts-criacao.md`, Parte C.

---


## 7. Combinações por restrição

| Restrição | Recomendação | Prompt-chave |
|---|---|---|
| **Pouco contexto / poucos tokens** | Perfil mínimo: `grill-me` + 1 skill mestre + Inspo; **uma** variante do Taste; **uma** skill MengTo por vez; ECC só no perfil `minimal`; desligar MCPs ociosos; `caveman` só em tarefas mecânicas; vídeo: `watch` com `--detail efficient` e trecho curto | "Liste os MCPs e skills ativos, estime o que cada um ocupa de contexto e proponha o que desligar nesta tarefa." |
| **Claude Code** | Plugins por marketplace (Superpowers, ponytail, Tastemaker, Designer Skills) e `npx skills add` (Hallmark, Taste, Impeccable) | P-00 |
| **Claude.ai (web)** | Skills por Configurações > Capacidades > Skills (testado para Garden Skills); MCPs e plugins conforme o plano; a skill `watch` (análise de vídeo) **não funciona no Claude Chat nem no Cowork**: use Claude Code ou Codex para isso | "Gere o pacote de skills em formato de upload e liste o que o plano permite." |
| **Cursor** | `pstack` (plugin para Cursor); skill da elaya pode virar regra do Cursor; o instalador do Inspo detecta Cursor | "Converta as regras de CLAUDE.md para o formato de regras do Cursor." |
| **Codex, Copilot, outros** | `npx skills add` detecta o agente; Open Design funciona com 20+ CLIs; ECC tem adaptadores limitados fora do Claude Code | "Detecte o agente atual e adapte os comandos de instalação." |
| **React + Tailwind + shadcn** | Cenário mais coberto: 21st.dev, React Bits, Canvas UI, Paper Shaders, `react-best-practices`, `tailwind-token-consolidation` | P-07 |
| **Vue / Nuxt** | `antfu/*` e `vuejs-ai/*`; Canvas UI tem versão Vue | "Liste as skills Vue/Nuxt do catálogo (https://ui-skills.com) e confirme compatibilidade." |
| **HTML + CSS puro** | Hallmark (gera HTML+CSS autocontidos) + `ponytail` | P-07 sem frameworks |
| **Vite + React** | Garden `web-design-engineer` assume familiaridade com essa stack | Skill mestre = K14 |
| **Sem chaves de API** | Evite `gpt-image-2` (modo local, exige chave OpenAI) Magic MCP do 21st.dev (exige chave) e o MCP do OriginKit (chave gratuita da conta). Inspo, Hallmark, Taste e Impeccable não pedem chave; o `watch` roda sem chave no motor `local` (o motor `gemini` pede `GEMINI_API_KEY` e envia o vídeo ao Google; com a chave configurada, o padrão `auto` escolhe Gemini, então fixe `--engine local`) | "Marque toda ferramenta que exija chave e proponha alternativa sem chave." |
| **Performance crítica** | Paper Shaders em vez de Three.js; evitar Canvas UI; `ponytail`; `core-web-vitals`; `fixing-motion-performance` | P-10 (performance primeiro) |
| **Acessibilidade crítica** | `accessibility`, `accessibility-scan`/`diff`, `wcag-audit-patterns`, `accessible-animation`, Jakub `better-accessibility` | P-10 (a11y primeiro) |
| **Trabalho em equipe** | ECC (memória compartilhada, AgentShield) **ou** gstack/Superpowers como "sistema operacional" único; `DESIGN.md` versionado | "Escreva as regras de colaboração em CLAUDE.md e defina quem aprova mudanças em DESIGN.md." |
| **Solo e rápido** | Perfil mínimo + `unlazy` | S14 |
| **Direitos e licenças** | Ver seção 11 | "Liste licenças e restrições de cada dependência e asset usados." |

---


## 8. Matriz de incompatibilidades

| Se você já tem… | Não adicione… | Motivo |
|---|---|---|
| Hallmark | Taste, Tastemaker, Garden como skill mestre | Duas skills de geração com regras visuais diferentes |
| Tastemaker | Hallmark | Sobreposição (ambos têm `study`/`audit`) |
| Superpowers | GSD, gstack, ECC, Ruflo, Designpowers | Um sistema pesado por projeto |
| GSD | Superpowers, gstack, ECC, Ruflo | Idem |
| gstack | Superpowers, GSD, ECC, Ruflo | Idem |
| `ponytail` | `andrej-karpathy-skills` | Sobrepõem-se; escolha 1 |
| `no-ai-slop` | `humanizer`, `stop-slop`, `unslop`, `deslop` | Humanizer de texto: escolha 1 |
| GSAP oficial (construção) | MengTo/`iart-ai`/`transitions-dev` como base de motion | Só por skill específica, nunca a biblioteca inteira |
| Emil (revisão de motion) | `iart-ai`/`raphaelsalaja` como revisor principal | Escolha 1 revisor |
| HyperFrames | Remotion | Um motor de vídeo |
| `playwright-cli` | `agent-browser`, gstack `/browse` | Um executor de testes |
| shadcn/21st.dev | daisyUI como segunda base | Uma base de componentes |
| coss ui (Base UI) | shadcn/ui (Radix) ou daisyUI como segunda base no mesmo conjunto | Duas bases de primitivos no mesmo projeto; escolha uma e registre |
| Bibliotecas de efeito (OriginKit, ObsidianUI, Bencho, React Bits, Canvas UI) | Usá-las como base ou em todas as seções | Passa de 3 momentos de impacto, pesa no celular e vira sinal de "cara de IA" |
| Site institucional ou de negócio local | Beautiful UI, AICSS (interfaces de agente) | São para produtos com agente ou chat |
| Skill mestre + elaya | Usar as **regras visuais** da elaya | Use só intake, estrutura, copy e SEO |
| `design-lab` | `variant`, `prototype`, `explore-design` | Escolha 1 gerador de variantes |
| Qualquer cenário de performance crítica | Canvas UI, 3D em várias seções | Custo alto no site |
| `watch` (análise de vídeo) | MengTo Video to Super Prompt como segunda análise do mesmo vídeo | Um analisador de vídeo por referência; o da MengTo só se o `watch` não estiver disponível |

---

### 9.1 Tabela de roteamento (YAML para o agente consultar)

```yaml
# docs/playbook.routing.yaml  (curadoria editorial; valide em projeto de teste)
global_kit: [grill-me, vibe-security, no-ai-slop, unlazy, ui-skills-root, a11y-perf-seo]   # + watch (claude-video), sob demanda, se houver vídeo de referência
gates:
  anti_ia: {prompt: P-13, criacao: [direcao, construido, final], edicao: [diagnostico, pos_camada, final], veredito_nao_passa_bloqueia_entrega: true}
  ajuste_visual: {prompt: P-15, classes: [A_dentro_da_direcao, B_mudanca_de_direcao, C_backlog, D_conflito_qualidade], b_exige_confirmacao_e_impacto: true, limite_rodadas_por_fase_editorial: 3, registro: docs/ajustes.md, tag_por_rodada: true, proibido_durante_ajuste: [trocar_skill_mestre, reinstalar_ferramentas, reescrever_design_md, mexer_no_que_nao_foi_citado]}
  escolhas_exatas: {prompt: P-16, blocos: [tipografia, disposicao, tipos_de_itens, referencias_de_biblioteca], arquivos: [docs/escolhas.md, docs/refs/componentes.md], aprovacao_do_usuario: true, criacao: antes_de_P-04_e_P-07, edicao: [M-3_ficha_atual, M-5_ajustar, M-6_trocar, M-12_so_disposicao], mudanca_depois_do_ok: P-15, conferido_por: P-13}
  referencia_por_elemento: {prompt: P-17, arquivos: [docs/refs/mapa-elementos.md, docs/refs/fidelidade.md], status: [com_referencia, pedir_material, livre_aprovado, mantido], elemento_sem_referencia_nao_e_construido: true, material_aceito: [video, imagem, print, link_com_ponto_exato, elemento_de_biblioteca], livre_avisa_uma_vez: true, criacao: antes_de_P-04_e_P-07, edicao: [Parte0_passo6, M-5, M-6, M-13, M-14, M-A], conferido_por: P-13}
  efeitos: {prompt: P-18, arquivo: docs/refs/mapa-efeitos.md, onde_procurar: {secao: 4.2.1, painel_obrigatorio_por_categoria: true}, efeito_sem_proposito_e_referencia_nao_entra: true, prototipo_dos_efeitos_chave_antes_de_espalhar: true, fallback_e_reduced_motion: true, criacao: [P-08, P-07, E-4, E-7, E-8, E-10, S11-1, S11-3, S14-1], edicao: [Parte0_passo6, M-5, M-6, M-13, M-A], conferido_por: P-13}
bibliotecas_de_elementos:
  base_de_componentes: [shadcn-ui, coss-ui, 21st-dev]        # escolher UMA por projeto
  efeitos_e_animacao: [originkit, obsidianui, react-bits, paper-shaders, canvas-ui]   # só nos momentos de impacto do DESIGN.md
  microinteracoes: [bencho]                                  # pedir vídeo de referência (P-14)
  interface_de_agente: [beautiful-ui, aicss]                 # só se o produto tem agente ou chat
  regras: {abrir_o_codigo_real_antes_de_usar: true, licenca_conferida: true, pro_ou_pago_so_com_licenca: true, nunca_recriar_codigo_pago_a_partir_de_previa: true, chave_em_variavel_de_ambiente: true, adaptar_aos_tokens: true}
referencia_em_video: {prompt: P-14, skill: watch-claude-video, escolha_do_usuario_obrigatoria: true, motor_para_video_privado: local, fixar_motor_com_engine: true, opcoes_de_quadros_so_no_motor_local: true, funciona_em: [claude-code, codex, agentes-locais], nao_funciona_em: [claude-chat, cowork]}
cenarios:
  S1_agencia_design:
    sinais: [agência, estúdio de design, portfólio, cases, branding]
    mestre: {padrao: taste, variantes: [minimalist-skill, brutalist-skill], alternativa: hallmark}
    processo: nenhum
    motion: [gsap, emil, mengto-scroll-por-skill]
    efeitos: {padrao: paper-shaders, premium: [canvas-ui, img2threejs]}
    qualidade: [a11y, cwv, seo]
    evitar: [elaya-como-mestre, sistemas-pesados]
  S2_estudio_multicliente:
    sinais: [vários clientes, handoff, design system, consistência]
    mestre: {padrao: tastemaker, alternativa: hallmark}   # nunca os dois
    processo: designer-skills   # ou designpowers (um só)
    extras: [jakub, impeccable-normalize, design-lab, open-design, obsidian-cli-skill]
    evitar: [gsd, superpowers, gstack]
  S3_pilates_bemestar:
    sinais: [pilates, yoga, academia, studio, clínica de bem-estar, aula experimental]
    mestre: {padrao: hallmark, alternativa: taste-soft-skill}
    processo: nenhum
    componentes: [21st.dev, paper-shaders]
    qualidade: [a11y-forte, cwv-mobile, seo-local, lgpd-formulario, vibe-security-se-backend]
    evitar: [canvas-ui, video-pesado-no-hero, formulario-de-saude]
  S4_servicos_confianca:
    sinais: [advocacia, clínica, consultoria, contabilidade]
    mestre: hallmark
    revisao: [impeccable, jakub-typography-colors]
    qualidade: [a11y, seo, vibe-security-formulario]
    evitar: [motion-decorativo, canvas-ui]
  S5_negocio_local:
    sinais: [restaurante, cafeteria, salão, barbearia, cardápio]
    mestre: hallmark
    extras: [paper-shaders, mobile-native, apple-web-app]
    qualidade: [cwv-mobile, seo-local]
    evitar: [canvas-ui, pdf-cardapio]
  S6_landing_app_saas:
    sinais: [landing, saas, waitlist, app store, pricing]
    mestre: hallmark
    estrutura: elaya-landing-page-design   # só intake/estrutura/copy/SEO
    componentes: [21st.dev, react-bits, mengto-landing-page, mengto-pricing-page]
    qualidade: [seo, cwv, impeccable-audit]
    evitar: [canvas-ui-acima-da-dobra, gsd, ruflo]
  S7_web_app_dashboard:
    sinais: [dashboard, painel, app web, crud, login]
    base: shadcn
    revisao: [jakub-better-interface, jakub-break, impeccable-audit]
    processo: superpowers
    extras: [ponytail, baseline-ui, react-doctor, playwright-cli-ou-agent-browser]
    qualidade: [vibe-security-obrigatorio, a11y-scan]
    evitar: [efeitos-decorativos, canvas-ui]
  S8_app_mobile_pwa:
    sinais: [expo, react native, pwa, app mobile]
    pwa: [mobile-native, apple-web-app, apple-design, prefer-container-queries]
    nativo: {lacuna_do_guia: true, acao: "listar skills RN/Expo no catálogo e pedir aprovação antes de instalar"}
    processo: superpowers-se-houver-logica
    qualidade: [vibe-security-backend, a11y]
    evitar: [assumir-que-hallmark-gera-rn]
  S9_ecommerce:
    sinais: [loja, carrinho, checkout, produto, catálogo]
    base: [shadcn, 21st.dev]
    processo: {padrao: superpowers, alternativa: gsd}   # nunca os dois
    qualidade: [vibe-security-obrigatorio, cwv, a11y, seo-produto]
    evitar: [webgl-em-produto, caveman]
  S10_conteudo_curso:
    sinais: [blog, documentação, curso, infoproduto, newsletter]
    foco: [seo, no-ai-slop, performance, human-review, tipografia-de-leitura]
    evitar: [motion-pesado, efeitos-gpu]
  S11_impacto_3d_scroll:
    sinais: [3d, webgl, scroll cinematográfico, awwwards, produto tech]
    mestre: taste
    motion: [gsap, mengto-scroll-por-skill, emil-review]
    efeitos: [paper-shaders, img2threejs, canvas-ui-premium, threejs-skills]
    qualidade: [accessible-animation, 60fps, fallback-estatico]
    evitar: [3d-em-toda-secao, duas-skills-de-motion]
  S12_video_lancamento_pitch:
    sinais: [vídeo, lançamento, reel, pitch, slides]
    video: hyperframes   # nunca junto com remotion
    mestre: hallmark
    slides: escolher-1-de [frontend-slides, slide-wright, nextlevelbuilder-slides]
  S13_redesign:
    sinais: [site existente, melhorar, refazer, auditoria]
    fluxo: [impeccable-audit-critique, hallmark-audit, impeccable-document, jakub, redesign-se-estrutura]
    evitar: [redesign-total-sem-diagnostico]
  S14_prototipo_rapido:
    sinais: [protótipo, mvp, em um dia, demo]
    mestre: {padrao: hallmark, alternativa: taste}
    extras: [unlazy]
    proibido: [qualquer-sistema-pesado]
```

### 9.2 Mapa-resumo: cenário × camada (para consulta rápida)

Legenda: ● usar · ○ opcional · ✕ evitar · — não se aplica.

| Cenário | Briefing | Referência (Inspo) | Skill mestre | Componentes | Motion | 3D/WebGL | Revisão | Segurança | Processo pesado | Vídeo |
|---|---|---|---|---|---|---|---|---|---|---|
| S1 Agência | ● | ● | Taste (ou Hallmark) | ○ Paper Shaders | ● GSAP + Emil | ○ Premium | ● | ○ | ✕ | ○ reel |
| S2 Estúdio multicliente | ● | ● | Tastemaker (ou Hallmark) | ○ | ○ | ○ | ● Jakub + Impeccable | ○ | Designer Skills | ○ |
| S3 Pilates/bem-estar | ● | ● | Hallmark (ou Taste soft) | ● 21st.dev, Paper Shaders | ○ mínimo | ✕ | ● | ● se backend | ✕ | ○ |
| S4 Serviços de confiança | ● | ● | Hallmark | ○ 21st.dev | ✕ decorativo | ✕ | ● Impeccable | ● formulário | ✕ | — |
| S5 Negócio local | ● | ● | Hallmark | ○ | ○ | ✕ | ○ | ○ | ✕ | ○ |
| S6 Landing app/SaaS | ● | ● | Hallmark | ● 21st.dev, React Bits | ● GSAP | ✕ acima da dobra | ● | ○ | ✕ | ○ demo |
| S7 Web app/dashboard | ● | ○ | shadcn + Jakub | ● shadcn | ○ curto | ✕ | ● | ● | Superpowers | — |
| S8 App mobile/PWA | ● | ○ | (lacuna RN) | ○ | ○ | ✕ | ● | ● | ○ Superpowers | — |
| S9 E-commerce | ● | ● | shadcn/21st.dev | ● | ✕ | ✕ | ● | ● | Superpowers **ou** GSD | — |
| S10 Conteúdo/curso | ● | ○ | Impeccable (tipografia) | — | ✕ | ✕ | ● | ○ | ✕ | ○ |
| S11 Impacto 3D | ● | ● | Taste | ○ | ● | ● | ● | ○ | ✕ | ○ |
| S12 Vídeo/pitch | ● | ○ | Hallmark | — | ● | ○ | ○ | — | ✕ | ● |
| S13 Redesign | ● | ○ | existente (Hallmark/Taste `redesign`) | — | ○ | ✕ | ● | ● | ✕ | — |
| S14 Protótipo | ○ curto | ● | Hallmark/Taste | ○ | ○ | ✕ | ○ Emil | ○ | ✕ | — |

---


## 10. Checklist pré-publicação

| Área | O que verificar | Ferramentas | Obrigatório quando |
|---|---|---|---|
| **Segurança** | Regras de acesso (Supabase RLS, Firebase, Convex), chaves expostas, webhooks e preços de pagamento, cabeçalhos, deploy | `vibe-security` | Login, banco, formulário com dados pessoais ou pagamento |
| **Acessibilidade** | Contraste, foco, rótulos, WCAG | `addyosmani/accessibility`, `accessibility-scan`/`diff`, `wcag-audit-patterns`, `fixing-accessibility`, Jakub `better-accessibility` | Sempre |
| **Movimento** | `prefers-reduced-motion`, 60 fps, fallback de WebGL/shader | `accessible-animation`, `60fps-animation`, `fixing-motion-performance` | Qualquer animação ou efeito de GPU |
| **Mídia** | Inventário e licenças, posters, fallbacks por seção, áudio sob comando, peso por tipo, legendas | `docs/midia.md`, prompt `E-11` | Qualquer foto, vídeo ou áudio |
| **Performance** | Core Web Vitals, peso, imagens | `core-web-vitals`, `performance`, `web-quality-audit`, `web-perf`, `pbakaus/optimize` | Sempre; crítico em e-commerce, landing e local |
| **SEO e metadados** | Títulos, descrições, Open Graph, dados estruturados | `addyosmani/seo`, `iannuttall/seo`, `fixing-metadata` | Sites públicos |
| **Revisão visual** | Hierarquia, consistência com `DESIGN.md` | Impeccable `audit`, Hallmark `audit`, Jakub `better-interface`, `web-design-guidelines` | Sempre |
| **Estados e responsivo** | Hover, foco, erro, vazio, carregando; celular | Jakub `break`, Impeccable `adapt`, `playwright-cli` | Sempre |
| **Texto** | Padrões de IA, microcopy, clareza | `no-ai-slop`, `better-writing`, `clarify` | Sempre |
| **Cara de IA** | Sinais visuais, de estrutura, de texto e de código; teste de troca; veredito do gate (`docs/anti-ia.md`) | `P-13`, `no-ai-slop`, Impeccable `critique`/`audit`, Hallmark `audit`, `playwright-cli` ou `agent-browser` (capturas) | **Sempre** |
| **Referência em vídeo** | Escolha registrada; análise guardada em `docs/refs/`; nada copiado; fonte e direitos em `docs/features.md` e `docs/midia.md` | `watch` (K24), prompt `P-14` | Houve vídeo de referência |
| **Código** | Dependências desnecessárias, dívida | `ponytail-review`, `react-doctor` | Projetos com código próprio |
| **Privacidade** | Dados coletados, consentimento, aviso | Revisão com o cliente/jurídico | Formulários e cadastros |
| **Direitos e licenças** | Referências, imagens, componentes, vídeo | Seção 11 | Sempre |

**Prompt de checklist final:** em `02-prompts-criacao.md`, Parte D (D-2).

---


## 11. Pendências e cuidados

**Pendências (do guia original e deste documento)**
- **animation-skills:** nome genérico; as coleções de Emil Kowalski, MengTo, GreenSock e `iart-ai` cobrem o tema. Se você tiver o link exato, envie.
- **andrej-karpathy-skills (multica-ai):** o README não foi lido na pesquisa; há repositórios parecidos (`forrestchang`, `learnprompt`). Confirme qual é o seu.
- **GSD:** há fork original, forks e uma versão nova independente; verifique qual está ativa.
- **Comandos do Impeccable:** nomes mudaram entre versões; consulte o README atual.
- **Links marcados com ⚠ confirmar:** `no-ai-slop`, `unlazy`, `elayadesign/landing-page-design`, as skills de a11y/performance/SEO e os extras do catálogo (K11, K12, K15, K22, K23). O guia apontava o catálogo, não o repositório exato.
- **Flag global (`-g`) do `npx skills add`:** confirmar em `--help`; não consta no guia original.
- **S8 (nativo Expo/React Native):** cobertura limitada no guia; o cenário traz um passo de descoberta no catálogo antes de instalar.
- **Peso, tiers e escopo global x projeto:** curadoria editorial, não medição.
- **Modelos TS, níveis E e orçamentos de peso/mídia (seções 12 a 14):** curadoria editorial; valide por medição no projeto.
- **Técnicas de tratamento de mídia (seção 13):** usam ferramentas comuns fora do guia original (conversão de imagem e vídeo); confirme comandos e instalação.
- **Suporte a animações CSS dirigidas por scroll e a View Transitions:** confirmar nos navegadores no dia (caniuse).
- **`oso95/scroll-world`:** repositório e comandos a confirmar no catálogo.
- **Rolagem suave (biblioteca):** não consta no guia original; avaliar acessibilidade antes de adotar.
- **`watch` (K24) e `P-14`:** comandos e requisitos conferidos no README oficial em 02/10/2026 (incluindo o motor `auto`); reconfirme no dia. Funciona em Claude Code, Codex e agentes locais, **não** no Claude Chat nem no Cowork. A análise do vídeo não revela valores exatos de CSS ou JavaScript: o agente deve marcar como estimativa.
- **Sinais do `P-13` (gate anti-"cara de IA"):** curadoria editorial; ajuste com o seu repertório e valide em projetos reais.
- **Bibliotecas B01 a B06 (ObsidianUI, Beautiful UI, OriginKit, coss ui, Bencho, AICSS):** páginas oficiais lidas em 02/10/2026. Contagem de componentes (o OriginKit aparece com números diferentes conforme a fonte), planos, limites de uso e licenças mudam: reconfirme na página oficial. A página lida do Bencho não mostra instalação nem licença. No AICSS, a licença MIT cobre os componentes gratuitos e o CLI; os Pro exigem licença comercial.
- **Escala do `P-17` por tier:** mínimo ou protótipo só nos elementos-chave (hero, navbar, botão, cartão, rodapé); padrão e completo em todos os elementos aplicáveis. A divisão é curadoria editorial; ajuste ao tamanho do projeto.
- **Valores da ficha de escolhas (`P-16`):** razão da escala, base em px, medida de linha, número de pesos, um estilo de cartão por página e demais números são curadoria editorial; ajuste ao seu repertório. Licença de fonte e de componente: confirme na página oficial.
- **Limite de 3 rodadas de ajuste visual por fase (`P-15`):** curadoria editorial; ajuste ao seu projeto e ao combinado com o cliente.

**Cuidados gerais**
1. **Não instale tudo.** Várias skills disputam a mesma função; escolha uma por camada.
2. **Teste em projeto descartável** e leia o `SKILL.md` antes de adotar.
3. **Segurança:** skills e MCPs executam comandos e podem tocar em credenciais; instale de fontes conferidas; para sistemas pesados, só de fontes oficiais e leia `curl | bash` antes (o README do ECC avisa sobre espelhos não oficiais com malware).
4. **Versões mudam rápido:** reconfirme comandos no README no dia da instalação.
5. **Licenças e custos:**
   - Canvas UI: MIT + Commons Clause (uso comercial em sites permitido; revenda dos componentes, não).
   - Remotion: licença paga acima de certo porte (motivo de HyperFrames ser alternativa).
   - Obsidian-CLI-skill: o repositório não declara licença.
   - `gpt-image-2` (Garden, modo local) e Magic MCP (21st.dev): exigem chave de API.
   - ECC: há plano pago (ECC Pro) para repositórios privados.
6. **Direitos autorais:** referências servem para extrair princípios; não copie layouts, marcas ou screenshots (vale para Dribbble/Pinterest, Inspo, MengTo "vídeo para prompt", `web-clone` e design systems de marcas do Open Design).
7. **Privacidade e LGPD:** onde houver formulário, coleta mínima e aviso claro; dados de saúde são sensíveis. Este documento **não é aconselhamento jurídico**; valide com o jurídico do cliente. Regras de publicidade de profissões regulamentadas (advocacia, saúde) também devem ser confirmadas com o cliente.
8. **Números** (quantidade de skills, ferramentas, estrelas) variam por fonte e versão; confira o repositório.
9. **Vídeos de referência (`watch`):** o motor `gemini` envia o vídeo ao Google; para vídeo privado ou de cliente use `--engine local`. Como o padrão `auto` escolhe Gemini quando há `GEMINI_API_KEY`, fixe o motor em toda execução. Cookies de navegador só com autorização explícita. O vídeo é evidência: extraia princípios, não reaproveite assets, código ou identidade de terceiros; vídeo com pessoas pede autorização de imagem.


---

## 12. Modelos de site (TS1 a TS8) e níveis de efeito (E0 a E5)

**Por que existe:** o **cenário** (S1 a S14) diz *para quem* e *com quais ferramentas*. O **modelo** (TS) diz *como o site se comporta*: simples ou ousado, com ou sem banco de dados, com ou sem mídia dirigida pelo scroll. O **nível de efeito** (E) diz *quanto movimento e peso* o site aceita. Os três se combinam: **cenário + modelo + nível de efeito + tier**.

> **Aviso:** modelos, níveis e orçamentos abaixo são **curadoria editorial**, não medição. Valide em projeto descartável e meça no celular de verdade.

### 12.1 Escada de efeitos (E0 a E5)

Cada degrau custa mais peso, esforço e risco de acessibilidade que o anterior. **Suba só quando o objetivo justificar.**

| Nível | O que é | Exemplos | Como fazer (do guia) | Custo | Fallback obrigatório |
|---|---|---|---|---|---|
| **E0 Estático** | Sem movimento além do navegador | Página limpa, tipografia forte, fotos | Hallmark (HTML+CSS), `ponytail` | Mínimo | n/a |
| **E1 Microinteração** | Resposta a toque, foco, hover; transições curtas | Botão que reage, card que sobe, menu que desliza | CSS; Emil `animate`; Jakub `better-interface` | Muito baixo | Estado final sem transição |
| **E2 Revelar ao rolar** | Elementos entram quando aparecem na tela | Fade/slide, imagem com máscara, contador, texto que aparece | CSS ou GSAP ScrollTrigger; MengTo `masked-reveal` | Baixo | Conteúdo visível sem JS e com `prefers-reduced-motion` |
| **E3 Scroll vinculado** | O movimento acompanha a posição do scroll | Parallax, seção fixa que troca de cena, texto que acende palavra por palavra, scroll horizontal | GSAP ScrollTrigger; MengTo `gsap-scrolltrigger-storytelling`; Emil `review-animations` | Médio | Versão empilhada, sem pin |
| **E4 Mídia dirigida pelo scroll** | Vídeo ou sequência de imagens avança conforme o scroll; a mídia "vira" a próxima seção | Vídeo que se reproduz ao rolar, produto que gira, vídeo que expande e revela a seção seguinte | MengTo `cinematic-scroll-storytelling`; `oso95/scroll-world` (**⚠ confirmar**); HyperFrames para produzir a fonte; técnicas da seção 13.4 | Alto | Poster/imagem estática por seção |
| **E5 3D, WebGL, shader** | Cena renderizada em GPU | Produto 3D, partículas, fundo líquido | `img2threejs`, Canvas UI, `cloudai-x/threejs-*`, `flornkm/webgl-components`; **versão leve:** Paper Shaders | Muito alto | Imagem/CSS estático + `prefers-reduced-motion` |

**Regras da escada**
1. O **modelo** define o nível **máximo**; o **cliente** pode pedir menos, nunca mais sem registrar a decisão (seção 14).
2. No máximo **3 momentos "uau"** (E4 ou E5) por página; o restante fica em E0 a E2.
3. Objetivo de conversão: efeito **fora da primeira dobra**.
4. Todo E3 ou superior tem fallback estático e respeita `prefers-reduced-motion`.
5. Se o orçamento de peso estourar, **desça um degrau** (E5 → Paper Shaders; E4 → sequência curta; E3 → empilhado).
6. Todo efeito acima de E0 passa pelo `P-18`: propósito, parâmetros e referência aprovados (componente de biblioteca escolhido pelo usuário ou material dele), com o painel "Onde procurar" da seção 4.2.1 mostrado em cada categoria.

### 12.2 Os oito modelos

| ID | Modelo | Em uma frase | Nível máx. | Cenários naturais | Skill mestre sugerida | Mídia típica |
|---|---|---|---|---|---|---|
| **TS1** | **Direto ao ponto** | Uma página, uma ação, nada sobrando | E1 | S3, S4, S5, S14 | Hallmark | Fotos tratadas |
| **TS2** | **Simples com efeitos** | A estrutura do TS1 com 1 a 3 efeitos escolhidos | E3 | S3, S5, S1, S6 | Hallmark (ou Taste `soft-skill`) | Fotos, texturas |
| **TS3** | **Landing de conversão** | Uma oferta, um CTA, prova, preço, FAQ | E3 (E4 só abaixo da dobra) | S6, S3, S12 | Hallmark + estrutura da elaya | Mockup, demo, vídeo curto |
| **TS4** | **Editorial** | Texto longo, leitura confortável, SEO | E2 | S10, S1 (cases), S4 (artigos) | Impeccable (tipografia) + Hallmark | Fotos com legenda, ilustrações |
| **TS5** | **Cinematográfico** | História contada com scroll, vídeo, áudio e foto | E5 | S11, S12, S1 premium | Taste | Vídeo, sequência, áudio, foto |
| **TS6** | **Institucional multipágina** | Várias páginas, equipe, serviços, contato | E2 | S4, S1, S5 | Hallmark | Fotos de equipe e espaço |
| **TS7** | **Com dados e banco** | Login, conteúdo que muda, agendamento, catálogo, painel | E1 | S7, S9, S8, S3 (agenda) | shadcn + Jakub | Fotos de produto, avatares |
| **TS8** | **Galeria / portfólio visual** | As imagens são a estrela | E3 | S1, S11, S5 | Taste (ou Hallmark) | Fotos em alta, case studies |

**O que cada modelo exige**

| Modelo | Estrutura | O que evitar | Orçamento de primeira carga (editorial) | Critério de saída |
|---|---|---|---|---|
| **TS1** | Hero + 3 a 5 blocos + CTA + contato, em uma página | GSAP, shaders, vídeo, carrossel | até ≈ 1 MB | Ação principal visível sem rolar e funcional |
| **TS2** | Igual ao TS1 + lista fechada de efeitos em `DESIGN.md` | Mais de 3 efeitos; efeito sem motivo | até ≈ 1,5 MB | Cada efeito tem motivo, fallback e custo registrados |
| **TS3** | Hero → problema → solução → prova → preço → FAQ → CTA | Navegação longa; CTA concorrente; 3D acima da dobra | até ≈ 2 MB | Um CTA por seção; LCP medido |
| **TS4** | Home com listagem + modelo de artigo + páginas de apoio | Motion pesado; medida de linha larga | até ≈ 1,5 MB por página | Medida de ≈ 60 a 75 caracteres; metadados por artigo |
| **TS5** | Storyboard de 5 a 8 momentos; no máx. 3 de impacto | 3D em toda seção; vídeo sem fallback; áudio automático | ≈ 3 a 4 MB iniciais + mídia carregada progressivamente | Storyboard aprovado; orçamento de FPS e peso definido; versão estática |
| **TS6** | Navegação clara, página por serviço, página de equipe, contato | Motion decorativo; páginas "iguais" sem conteúdo próprio | até ≈ 1,5 MB por página | SEO por página; menu funciona no celular |
| **TS7** | Telas por tarefa; todos os estados; regras de acesso ao banco | Efeito decorativo; regra de acesso fraca | até ≈ 2 MB + dados | `vibe-security` aprovado; todos os estados desenhados |
| **TS8** | Grade/lista, página de case, lightbox, filtros | Imagens sem tamanho declarado; carregar tudo de uma vez | ≈ 2 a 2,5 MB com imagens sob demanda | Imagens responsivas; navegação por teclado na galeria |

### 12.3 O que o cliente diz → o modelo

| O cliente diz… | Modelo provável | Pergunta de confirmação |
|---|---|---|
| "Quero algo simples" | **TS1** | Simples de **ver**, de **manter** ou de **fazer**? |
| "Simples, mas com vida, com uns efeitos" | **TS2** | Quais 2 ou 3 momentos merecem efeito? |
| "Direto ao ponto, para as pessoas me chamarem" | **TS1** ou **TS3** | Há uma oferta com preço e prova, ou só contato? |
| "Quero vender meu app/curso/serviço" | **TS3** | Qual a ação: cadastro, compra, agendamento? |
| "Quero algo tipo revista, blog, artigos" | **TS4** | Quem escreve? Com que frequência? Quem edita? |
| "Quero algo cinematográfico, que impressione" | **TS5** | O que os visitantes devem sentir? Que mídia existe? |
| "Quero mostrar meus trabalhos/fotos" | **TS8** | Quantos projetos? Cada um terá página própria? |
| "Quero login, área de clientes, agendamento, loja" | **TS7** | Quem usa? Onde ficam os dados? Quem administra? |
| "Várias páginas, equipe, serviços" | **TS6** | Quem mantém o conteúdo depois? |
| "Quero igual àquele site" | Ver **seção 14** | O que exatamente nele encanta? |

**Híbridos:** são comuns (ex.: TS3 com uma seção TS5 de demo; TS6 com um blog TS4). Regra: declare um **modelo base** e liste a **seção híbrida** com o seu nível de efeito. O orçamento do **modelo mais leve** vale para a página inteira, exceto na seção declarada.

### 12.4 Matriz cenário × modelo

Legenda: ● natural · ○ possível · ✕ evitar.

| Cenário | TS1 | TS2 | TS3 | TS4 | TS5 | TS6 | TS7 | TS8 |
|---|---|---|---|---|---|---|---|---|
| S1 Agência | ○ | ● | ○ | ○ | ● | ○ | ✕ | ● |
| S3 Pilates/bem-estar | ● | ● | ● | ○ | ✕ | ○ | ○ agenda | ○ |
| S4 Serviços de confiança | ● | ○ | ○ | ○ artigos | ✕ | ● | ○ | ✕ |
| S5 Negócio local | ● | ● | ○ | ✕ | ○ | ○ | ○ | ○ |
| S6 Landing app/SaaS | ○ | ○ | ● | ✕ | ○ demo | ✕ | ✕ | ✕ |
| S7 Web app/dashboard | ✕ | ✕ | ✕ | ✕ | ✕ | ✕ | ● | ✕ |
| S9 E-commerce | ✕ | ✕ | ○ | ○ | ✕ | ○ | ● | ○ |
| S10 Conteúdo/curso | ✕ | ○ | ○ vendas | ● | ✕ | ○ | ○ | ✕ |
| S11 Impacto 3D | ✕ | ✕ | ○ | ✕ | ● | ✕ | ✕ | ● |
| S12 Vídeo/pitch | ✕ | ○ | ● | ✕ | ● | ✕ | ✕ | ○ |
| S14 Protótipo | ● | ○ | ○ | ✕ | ✕ | ✕ | ✕ | ✕ |

### 12.5 Como combinar modelo, cenário, nível e tier

1. **Cenário** escolhe as ferramentas e a trilha (seção 5).
2. **Modelo** escolhe estrutura, orçamento e nível máximo (esta seção).
3. **Prazo** escolhe o tier (seção 1). Tier curto + modelo ambicioso = **corte efeitos, não verificações**.
4. **Conflito:** vale o **menor orçamento** e a **maior exigência de qualidade** (segurança e acessibilidade vencem a estética).
5. Registre no `CLAUDE.md`: `modelo: TSx`, `nivel_efeito_max: Ex`, `secoes_hibridas: [...]`, `features_aprovadas: [...]`.

### 12.6 Trechos de `CLAUDE.md` por modelo

- **TS1:** uma página; nenhuma biblioteca de motion; só transições de hover e foco; sem vídeo; ação principal visível sem rolar.
- **TS2:** lista fechada de efeitos em `DESIGN.md` (máx. 3); cada efeito com motivo, custo e fallback; nada de efeito na primeira dobra se a meta é conversão.
- **TS3:** CTA único por seção; prova social real; preços claros; efeito de impacto só abaixo da dobra.
- **TS4:** medida de linha ≈ 60 a 75 caracteres; hierarquia tipográfica documentada; sem motion pesado; metadados e Open Graph por artigo; quem edita e como (arquivos, CMS) definido antes da construção.
- **TS5:** storyboard aprovado antes de codar; orçamento de peso e FPS escrito; máx. 3 momentos de impacto; áudio **nunca** automático; versão estática e `prefers-reduced-motion` obrigatórios.
- **TS6:** SEO e título por página; navegação testada no celular; conteúdo próprio em cada página.
- **TS7:** todos os estados desenhados; regras de acesso revisadas por `vibe-security` antes de cada release; preços e permissões validados no servidor; escolha de backend registrada.
- **TS8:** imagens com largura e altura declaradas, `srcset` e carregamento sob demanda (exceto a imagem principal); lightbox acessível por teclado; direitos de cada imagem registrados.

### 12.7 Módulos que se acrescentam às trilhas S#

Depois do passo de **referências e direção** de qualquer cenário, acrescente conforme o modelo:

| Se o modelo é… | Acrescente (texto em `02-prompts-criacao.md`, Parte E) |
|---|---|
| Qualquer um | `E-0` (modelo e nível de efeito) logo após o briefing |
| TS2 | `E-7` (simples com efeitos) |
| TS4 | `E-8` (editorial) |
| TS5 | `E-10` (cinematográfico) + `E-1`, `E-4`, `E-5`, `E-11` |
| TS7 | `E-9` (dados e banco) |
| TS8 | `E-2` (fotos) + `E-11` |
| Há fotos, vídeo ou áudio | `E-1` a `E-5` e `E-11` conforme o tipo |
| Cliente trouxe referência com efeito | `E-6` (feature de referência) e `P-14` (vídeo de referência) |

---

## 13. Mídia: fotos, vídeo, áudio e scroll com mídia

> **Aviso:** ferramentas de tratamento de mídia citadas (ffmpeg, sharp, etc.) são **ferramentas comuns fora do guia original**; confirme instalação e comandos no dia. As skills nomeadas vêm do guia; onde há **⚠ confirmar**, valide o repositório.

### 13.1 Inventário e direitos (sempre primeiro)

Antes de qualquer tratamento, registre cada arquivo em `docs/midia.md`:

| Arquivo | Tipo | Origem | Licença/autorização | Papel no site | Versões geradas | Peso final |
|---|---|---|---|---|---|---|
| hero.mp4 | vídeo | cliente | própria | atmosfera do hero | mp4, webm, poster | ... |

- **Fotos de pessoas:** autorização de uso de imagem; atenção redobrada com crianças e com negócios de saúde.
- **Música e voz:** licença de uso online; trilha comprada para vídeo **não** vale automaticamente para o site.
- **Banco de imagens/vídeo:** guarde a licença e o crédito exigido.
- **Referências:** servem para extrair princípios, não para copiar assets de terceiros.

### 13.2 Papel de cada mídia

Cada mídia deve ter **um papel**: *contar a história*, *dar prova*, *criar atmosfera*, *demonstrar o produto* ou *orientar a ação*. Mídia sem papel sai.

### 13.3 Regras por tipo de mídia

| Tipo | Regras | Observações |
|---|---|---|
| **Fotos** | Formatos modernos (AVIF/WebP) com JPEG de reserva; `srcset` e `sizes`; largura e altura declaradas; `alt` útil; carregamento sob demanda, exceto a imagem principal; placeholder leve | Recorte diferente para celular quando o enquadramento exigir (art direction); fotos reais valem mais que banco genérico |
| **Vídeo em loop (fundo)** | Curto (≈ 5 a 15 s), **mudo**, `playsinline`, `poster`, versões MP4 e WebM, versão menor para celular, pausar fora da tela | Em `prefers-reduced-motion` ou conexão econômica, mostrar só o poster |
| **Vídeo com som** | Início pelo usuário, controles, legendas e transcrição | Nunca autoplay com som |
| **Áudio ambiente/trilha** | **Desligado por padrão**; botão visível de ligar/mudo; lembrar a escolha; volume baixo; pausar ao sair da aba; ligado só por ação do usuário | Navegadores bloqueiam autoplay com som; trate isso como regra de produto, não como bug |
| **Efeitos sonoros de interface** | Opcionais, desligados por padrão, curtos | Só em experiências onde o som é parte do conceito |
| **Vídeo para scroll (E4)** | Ver 13.4 | Sempre com fallback |
| **Imagem-conceito → 3D** | `img2threejs` + Taste `image-to-code-skill`; entregar também a versão estática | Seção 12.1, nível E5 |

### 13.4 Técnicas de mídia dirigida pelo scroll (E4)

| Técnica | Como funciona | Quando usar | Cuidados |
|---|---|---|---|
| **A. Vídeo "scrub"** | O scroll controla a posição de reprodução (`currentTime`) de um vídeo | Cena curta, contínua, desktop forte | O vídeo precisa ser **re-codificado com quadros-chave frequentes** (senão trava ao rolar para trás); sem áudio; arquivo pequeno; testar no iPhone real, pois o controle de reprodução é mais restrito no celular |
| **B. Sequência de imagens em canvas** | Extrai-se o vídeo em quadros e o scroll escolhe qual quadro desenhar | Produto girando, animação precisa, **funciona melhor no celular** | Muitos arquivos: reduza resolução e quantidade de quadros; carregue em etapas; poster enquanto carrega |
| **C. Animações CSS dirigidas por scroll** | Linha do tempo do scroll aplicada via CSS, sem JavaScript | E3 simples: reveal, parallax, barra de progresso | **⚠ confirmar suporte atual dos navegadores** (caniuse) e prever fallback |
| **D. Seção fixa com troca de cenas** | A seção "gruda" e o conteúdo muda conforme o scroll (GSAP ScrollTrigger com pin) | Contar história em etapas com fotos ou vídeos curtos | Altura de rolagem controlada; versão empilhada para celular e `prefers-reduced-motion` |
| **E. Vídeo que vira a próxima seção** | Um vídeo fixo cresce ou é revelado por máscara até preencher a tela, e a seção seguinte surge por cima | Transição de impacto entre seções | Um por página; fonte curta; o texto da próxima seção deve ser legível sem o efeito |

**Como escolher:**

| Situação | Técnica |
|---|---|
| Funciona só no desktop, vídeo curto, impacto alto | **A** |
| Precisa funcionar bem no celular | **B** ou **D** |
| Efeito leve sem JavaScript | **C** |
| Contar uma história por etapas | **D** |
| Transição de uma cena para a seção seguinte | **E** (feita com **D** + máscara) |
| Orçamento de peso baixo | **C**, **D** com imagens, ou desça para E3 |

**Skills do guia para essas técnicas:** MengTo `cinematic-scroll-storytelling`, `gsap-scrolltrigger-storytelling` e `masked-reveal` (**uma por vez**); GSAP oficial; Emil `review-animations`; `oso95/scroll-world` (**⚠ confirmar**); HyperFrames para produzir ou editar o vídeo-fonte (16:9, 9:16, 1:1) e `iart-ai/accessible-animation`, `60fps-animation`, `fixing-motion-performance` para qualidade.

### 13.5 Fluxo: do material bruto ao site

1. **Receber e inventariar** (13.1).
2. **Decidir o papel** de cada mídia (13.2) e **o nível de efeito** (12.1).
3. **Tratar:** fotos (recorte, formatos, tamanhos), vídeo (cortar, remover áudio se for fundo, re-codificar para a técnica escolhida), áudio (normalizar volume, cortar silêncio, loop sem estalo).
4. **Gerar fallbacks:** poster, imagem estática por seção, versão sem som, versão mobile.
5. **Integrar** seguindo a skill mestre e o `DESIGN.md`.
6. **Medir:** peso, LCP, FPS em celular mediano, comportamento com `prefers-reduced-motion` e com conexão lenta.
7. **Registrar** versões e pesos em `docs/midia.md`.

**Estrutura de pastas sugerida:** `media/originais/` (nunca publicada) · `media/processados/` (publicada) · `docs/midia.md`.

### 13.6 Fallbacks (resumo)

| Condição | O que o site faz |
|---|---|
| `prefers-reduced-motion` | Poster ou imagem estática; sem scrub, sem parallax, sem pin |
| Conexão lenta ou economia de dados | Imagem em vez de vídeo; sequência reduzida |
| Aparelho fraco ou celular | Versão menor, técnica B ou D, ou nível de efeito reduzido |
| Sem JavaScript | Conteúdo legível, imagens e textos presentes |
| Áudio negado ou bloqueado | Site funciona igual; botão continua disponível |

### 13.7 Orçamentos de mídia (sugestão editorial; ajuste com medição)

| Item | Referência |
|---|---|
| Foto de seção | ≈ 100 a 250 KB por imagem, em formato moderno |
| Imagem principal (hero) | ≈ até 300 KB; prioridade de carregamento |
| Vídeo de fundo | ≈ 1 a 3 MB (celular menor); sem áudio |
| Sequência de imagens | Definir total em MB antes de extrair; carregar em etapas |
| Áudio ambiente | Curto, em loop; comprimido; só carrega depois do clique |

---

## 14. Features de referência: quando o cliente escolhe "simples", mas vê algo em outro site

**Situação típica:** o cliente escolhe um modelo simples (TS1 ou TS2) e, olhando uma referência, diz: *"gostei daquele vídeo que vai tocando enquanto rola e vira a próxima seção"*. Isso **muda o modelo**, o prazo e o orçamento. Este protocolo evita duas falhas: **dizer sim sem medir** e **dizer não sem oferecer alternativa**.

### 14.1 Protocolo FR (feature de referência)

| Passo | O que fazer | Ferramenta |
|---|---|---|
| **1. Capturar** | URL, print ou **vídeo** (mostre a escolha de enviar um vídeo ou gravação de tela com o trecho em mm:ss, `P-14`); **qual parte** encanta; onde entraria no seu site; qual **objetivo** serve; mostre o painel "Onde procurar" (seção 4.2.1) para o tipo da feature | `docs/features.md` (modelo em 14.5) |
| **2. Entender** | Descobrir como funciona, extraindo **princípios** (estrutura, ritmo, técnica), sem copiar assets, código ou identidade | **Vídeo:** `watch` (K24, `P-14`) · URL: Jakub `explain-interface` (como foi construído) · HTML: MengTo HTML to Interaction Prompts · print: Hallmark `study` · MengTo Video to Super Prompt só se o `watch` não estiver disponível |
| **3. Classificar** | Nível de efeito (E0 a E5), custo (peso, esforço, acessibilidade), mídia necessária | Seção 12.1 e catálogo 14.2 |
| **4. Decidir** | **Adotar**, **Simplificar** (versão leve), **Trocar** (equivalente mais barato), **Adiar** (fase 2) ou **Recusar** | Matriz 14.4; conversa com o cliente (14.6) |
| **5. Ajustar o modelo** | Se a feature excede o nível do modelo, **suba de modelo** (TS1 → TS2 → TS5 ou seção híbrida) e **registre o impacto em prazo e custo** | Seção 12.5 |
| **6. Implementar** | Skill indicada no catálogo + mídia tratada (seção 13) + fallback | Parte E de `02-prompts-criacao.md` |
| **7. Validar** | `prefers-reduced-motion`, celular real, peso, FPS, leitura sem o efeito | Seção 10 |

### 14.2 Catálogo de features (o que existe, o que custa, como fazer)

| # | Feature | Nível | Técnica / skill do guia | Custo | Versão leve | Fallback |
|---|---|---|---|---|---|---|
| 1 | **Vídeo que avança com o scroll** | E4 | Técnica A; MengTo `cinematic-scroll-storytelling` | Alto | Técnica B com poucos quadros, ou 3 imagens trocando (D) | Poster |
| 2 | **Vídeo que vira a próxima seção** | E4 | Técnica E (D + máscara); GSAP + MengTo `masked-reveal` | Alto | Imagem que expande por máscara | Imagem fixa + seção normal |
| 3 | **Produto girando com o scroll** | E4 | Técnica B (sequência em canvas) | Alto | Carrossel de 4 a 6 ângulos | Imagem principal |
| 4 | **Seção fixa com troca de cenas** | E3 | Técnica D; MengTo `gsap-scrolltrigger-storytelling` | Médio | Blocos empilhados com reveal (E2) | Empilhado |
| 5 | **Parallax em camadas** | E3 | GSAP ou Técnica C | Médio | Parallax em 1 camada | Camadas estáticas |
| 6 | **Texto que acende palavra por palavra** | E3 | GSAP ScrollTrigger | Baixo a médio | Fade do bloco inteiro | Texto visível |
| 7 | **Imagem revelada por máscara** | E2 | MengTo `masked-reveal` | Baixo | Fade simples | Imagem visível |
| 8 | **Scroll horizontal dentro da página** | E3 | GSAP com pin | Médio | Carrossel nativo (scroll-snap) | Lista vertical |
| 9 | **Faixa de logos em movimento (marquee)** | E1 | CSS | Baixo | Grade estática | Grade estática |
| 10 | **Cursor personalizado / efeito magnético** | E1 | JS leve (só desktop) | Baixo | Hover comum | Cursor padrão |
| 11 | **Vídeo de fundo em loop (hero)** | Mídia | 13.3 (loop) | Médio | Foto com leve zoom (CSS) | Poster |
| 12 | **Áudio ambiente com botão mudo** | Mídia | 13.3 (áudio) | Baixo a médio | Sem áudio | Botão some se não houver áudio |
| 13 | **Antes e depois (slider)** | E1 | JS leve ou nativo | Baixo | Duas imagens lado a lado | Duas imagens |
| 14 | **Contadores animados** | E2 | GSAP ou CSS | Baixo | Números estáticos | Números finais |
| 15 | **Transição entre páginas** | E3 | View Transitions (**⚠ confirmar suporte**) | Médio | Navegação padrão | Navegação padrão |
| 16 | **Fundo com textura/shader animado** | E5 leve | Paper Shaders | Médio | Textura estática (CSS/imagem) | Imagem |
| 17 | **Cena 3D de produto** | E5 | `img2threejs`, Canvas UI | Muito alto | Sequência de imagens (B) ou Paper Shaders | Imagem |
| 18 | **Galeria com lightbox e zoom** | E1 | Componente 21st.dev/shadcn | Baixo | Grade com link para a imagem | Grade |
| 19 | **Rolagem suave (smooth scroll)** | E3 | Biblioteca comum, **fora do guia ⚠ confirmar** | Médio | Rolagem nativa | Nativa |

> **Cuidado com a rolagem suave e com "scroll hijack" (travar o scroll):** costumam confundir quem usa teclado, leitor de tela ou celular. Só adote com justificativa e teste.

### 14.3 Substituições leves (quando a feature não cabe)

| Se o cliente quer… | Mas o modelo/orçamento não comporta | Ofereça |
|---|---|---|
| Vídeo scrub | TS1, TS2, peso baixo | 3 a 5 imagens que trocam numa seção fixa (D) ou reveal por máscara |
| 3D de produto | Performance crítica | Sequência curta de imagens (B) ou Paper Shaders no fundo |
| Hero em vídeo | Celular fraco, S3/S5 | Foto forte com zoom lento em CSS; vídeo só no desktop |
| Transição cinematográfica | Prazo curto | Uma única seção híbrida (TS5) no meio da página |
| Áudio ambiente | Público que acessa em locais públicos | Som desligado por padrão com botão discreto, ou sem som |

### 14.4 Matriz modelo × feature

Legenda: ● cabe · ○ condicionado (justificar e medir) · ✕ não cabe sem subir de modelo.

| Feature | TS1 | TS2 | TS3 | TS4 | TS5 | TS6 | TS7 | TS8 |
|---|---|---|---|---|---|---|---|---|
| E1 (hover, marquee, lightbox) | ● | ● | ● | ○ | ● | ● | ● | ● |
| E2 (reveal, contador) | ○ | ● | ● | ○ | ● | ○ | ✕ | ● |
| E3 (pin, parallax, scroll horizontal) | ✕ | ○ | ○ | ✕ | ● | ✕ | ✕ | ○ |
| E4 (vídeo/sequência com scroll) | ✕ | ✕ | ○ abaixo da dobra | ✕ | ● | ✕ | ✕ | ○ |
| E5 (3D, shader pesado) | ✕ | ✕ | ✕ | ✕ | ● | ✕ | ✕ | ○ |
| Vídeo de fundo | ✕ | ○ | ○ | ✕ | ● | ✕ | ✕ | ○ |
| Áudio ambiente | ✕ | ✕ | ✕ | ✕ | ○ | ✕ | ✕ | ✕ |

### 14.5 Modelo de `docs/features.md`

```text
# Features de referência

## F-01: {{nome da feature}}
- Referência: {{URL/print/vídeo}} (apenas inspiração; não copiar assets nem código)
- Vídeo de referência: {{arquivo | URL + trecho mm:ss a mm:ss | nenhum (escolha registrada)}} · Análise: docs/refs/video-{{F-01}}.md
- O que encanta: {{descrição do cliente com as palavras dele}}
- Onde entra: {{seção}}
- Objetivo que serve: {{ex.: mostrar o produto em uso}}
- Nível de efeito: {{E0 a E5}} · Custo: {{baixo/médio/alto}} · Mídia necessária: {{lista}}
- Decisão: {{adotar | simplificar | trocar | adiar | recusar}} · Motivo: {{...}}
- Impacto no modelo, prazo e orçamento: {{...}}
- Fallback: {{...}}
- Aprovado por: {{cliente}} em {{data}}
```

### 14.6 Conversa com o cliente (6 perguntas)

1. O que exatamente nessa referência te chamou atenção: o movimento, a mídia, a história ou a sensação?
2. Qual seria o ganho para o seu objetivo? (mais contatos, mais tempo na página, percepção de marca)
3. Você tem (ou aceita produzir) o vídeo, as fotos ou o áudio que esse efeito exige?
4. Prefere a versão completa (mais prazo e orçamento) ou uma versão leve que passa a mesma ideia?
5. Se houver conflito entre efeito e velocidade no celular, o que pesa mais?
6. Você consegue gravar a tela (ou enviar o link com o minuto e o segundo) do trecho em que o efeito aparece? Com vídeo, a IA analisa o movimento e a ordem das etapas, o que um print não mostra.

**Como comunicar o custo:** mostre **duas opções** lado a lado (completa e leve), com impacto em prazo, orçamento, peso e manutenção, e registre a escolha em `docs/features.md`.

---

## 15. Roteamento adicional (YAML) para modelo, efeito e mídia

```yaml
# docs/playbook.models.yaml  (curadoria editorial; valide em projeto de teste)
niveis_de_efeito:
  E0: {nome: estatico}
  E1: {nome: microinteracao, ferramentas: [css, emil-animate, jakub-better-interface]}
  E2: {nome: revelar_ao_rolar, ferramentas: [css, gsap-scrolltrigger, mengto-masked-reveal]}
  E3: {nome: scroll_vinculado, ferramentas: [gsap, mengto-gsap-scrolltrigger-storytelling, emil-review-animations]}
  E4: {nome: midia_dirigida_pelo_scroll, ferramentas: [mengto-cinematic-scroll-storytelling, oso95-scroll-world-confirmar, hyperframes], tecnicas: [A_video_scrub, B_sequencia_canvas, C_css_scroll_timeline, D_pin_troca_de_cenas, E_video_vira_secao]}
  E5: {nome: 3d_webgl_shader, ferramentas: [img2threejs, canvas-ui, threejs-skills, paper-shaders-leve]}
modelos:
  TS1_direto:        {nivel_max: E1, mestre: hallmark, evitar: [gsap, shaders, video]}
  TS2_simples_efeitos: {nivel_max: E3, regra: "ate 3 efeitos listados em DESIGN.md", fora_da_primeira_dobra_se_conversao: true}
  TS3_landing:       {nivel_max: E3, e4_somente: abaixo_da_dobra, estrutura: elaya-so-intake-estrutura-copy}
  TS4_editorial:     {nivel_max: E2, revisao: [impeccable-tipografia, jakub-better-typography], conteudo: [no-ai-slop, human-review]}
  TS5_cinematografico: {nivel_max: E5, mestre: taste, exige: [storyboard, orcamento_peso_fps, fallback_estatico, reduced_motion, audio_sob_comando], max_momentos_uau: 3}
  TS6_institucional: {nivel_max: E2, qualidade: [seo-por-pagina, a11y]}
  TS7_dados_banco:   {nivel_max: E1, base: shadcn, qualidade: [vibe-security-obrigatorio, estados-completos], decisao: backend-e-quem-administra}
  TS8_galeria:       {nivel_max: E3, exige: [imagens-responsivas, direitos-registrados, lightbox-acessivel]}
midia:
  inventario: docs/midia.md
  pastas: [media/originais, media/processados]
  regras: [audio-nunca-automatico, fallback-por-secao, poster-em-todo-video, reduced-motion-respeitado]
feature_de_referencia:
  video: {prompt: P-14, skill: watch-claude-video, escolha_do_usuario: obrigatoria}
  protocolo: [capturar, entender, classificar, decidir, ajustar-modelo, implementar, validar]
  decisoes: [adotar, simplificar, trocar, adiar, recusar]
  registro: docs/features.md
  regra: "extrair principios; nao copiar assets, codigo ou identidade"
```

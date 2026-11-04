# Guia 4 de 4: Melhorar e Editar (sites e projetos que já existem)

**Como mexer em algo que já está no ar sem quebrar o que funciona: diagnóstico, tipos de melhoria, fluxo seguro, prompts, perguntas ao cliente, checklist de regressão**

Complementa os guias de criação: `01-mapa-e-caminhos.md` (decidir), `02-prompts-criacao.md` (executar), `03-perguntas-para-clientes.md` (perguntar). O **texto dos prompts deste guia** (`M-*` e `S13-*`) está em `02-prompts-edicao.md` (Guia 2B). O cenário **S13 (redesign)** do Guia 1 cobre a melhoria **visual**; este guia cobre **qualquer** melhoria ou edição em projeto existente: performance, acessibilidade, SEO, segurança, conteúdo, responsivo, adicionar efeito ou mídia, adicionar funcionalidade com dados, refatoração, migração e correções pequenas.

> **Aviso de honestidade**
> - **Fatos** sobre as ferramentas (o que cada skill faz) vêm dos guias 1 e 2, que partem da pesquisa de 01/10/2026. Nomes de comandos mudam; **reconfirme no README no dia**.
> - **Fluxo, tipos de intervenção (M1 a M12), matrizes, métricas e prazos** são **curadoria editorial**, não medição. Valide em um projeto descartável.
> - Onde houver **⚠ confirmar**, o repositório ou o comando exato não constava no guia original.
> - **WordPress e outros CMS não são cobertos** pelo guia original: se o projeto usa um, o agente deve avisar e não improvisar.
> - Este documento **não é aconselhamento jurídico** (LGPD, publicidade profissional): valide com o cliente.

---

## Sumário

1. Quando usar este guia (e quando usar o S13)
2. Regras de ouro para mexer em projeto existente
3. Intake de melhoria
4. Fluxo seguro em 8 passos
5. Tipos de intervenção (M1 a M12)
6. Sintoma → intervenção
7. Priorização: impacto, esforço, risco
8. Baseline: medir antes e depois
9. Mapa de risco e checklist de regressão
10. Trilhas por tipo e índice dos prompts (texto em `02-prompts-edicao.md`)
11. Perguntas ao cliente para melhorias
12. Comunicação: plano em camadas e relatório antes/depois
13. Roteamento do agente (YAML)
14. Pendências e cuidados

---

## 1. Quando usar este guia

| Situação | Use |
|---|---|
| Site/app existente, objetivo é **melhorar** algo específico (lento, feio, não converte, quebra no celular) | **Este guia** |
| Redesign visual do site inteiro com diagnóstico | **S13** (Guia 1) + este guia para as camadas de apoio |
| Adicionar um efeito ou mídia (ex.: vídeo que avança com o scroll) | **M10** + seções 12 a 14 do Guia 1 + prompts `E-x` |
| Adicionar login, agenda, loja, formulário com banco | **M11** + `E-9` |
| Correção pequena e urgente | **Hotfix** (`M-16`) |
| Projeto novo do zero | Guias 1 a 3 |
| Projeto que já existe ou **está em andamento** e você quer **um prompt inicial único** que conduza tudo | **Parte 0 do Guia 2B** (`02-prompts-edicao.md`) |
| Projeto em andamento **sem os `.md` do playbook** (sem `CLAUDE.md`, `DESIGN.md` ou `docs/`) | **Parte 0 do Guia 2B**: ela chama o `M-A`, que cria esses arquivos a partir do código (Parte 0-A de `02-prompts-edicao.md`) |

**Regra de ouro de roteamento:** se o pedido é "melhorar X", classifique **primeiro** o tipo de intervenção (seção 5) e só depois escolha ferramentas. Nunca comece pelo redesign.

---

## 2. Regras de ouro para mexer em projeto existente

1. **Entender antes de mudar.** Primeiro mapeie o que existe e **meça**; só então proponha. Diagnóstico **não altera código**.
2. **Proteger o que funciona.** Liste o que **não pode mudar** (textos aprovados, URLs, integrações, formulários, rastreamento, posições no Google) antes de qualquer edição.
3. **Snapshot e ramificação.** Antes de tocar: cópia ou *tag* do estado atual e um *branch* de trabalho. Nada de editar direto em produção; use ambiente de teste ou *preview* quando existir.
4. **Medir antes e depois.** Sem *baseline* não há como provar melhoria nem detectar regressão (seção 8).
5. **Uma camada por vez, com aprovação.** Acabamento → estrutura → qualidade técnica, mostrando antes/depois entre uma camada e outra. Nada de "refazer tudo de uma vez".
6. **Mudanças pequenas e reversíveis.** *Commits* pequenos, um assunto por vez; cada mudança pode ser desfeita.
7. **Manter as URLs.** Se mudar endereço, crie o mapa de redirecionamentos (301) e teste. Mudar URL sem mapa derruba SEO.
8. **Dados são sagrados.** Antes de mudar banco, formulários ou integrações: *export*/backup e plano de reversão. Nunca teste com dados reais de clientes sem autorização.
9. **Uma skill mestre, um sistema de processo, um `DESIGN.md`.** As regras de precedência dos guias 1 e 2 valem aqui. Se o projeto já tiver uma convenção (arquivo de regras, design system), **ela vence** a skill nova: registre-a em `CLAUDE.md`.
10. **Segurança e acessibilidade vencem a estética.** Se uma correção contradizer o `DESIGN.md`, aplique a correção e atualize o `DESIGN.md`.
11. **Não declare "pronto" sem evidência.** Resultado de teste, métrica ou *screenshot* antes/depois.
12. **Falha de ferramenta = parar e relatar.** Não substituir por busca na web ou memória sem autorização; nunca apresentar como obtido o que não foi obtido.
13. **Nada de publicar sem aprovação explícita** do responsável (cliente ou você).
14. **Registrar tudo** em `docs/melhorias.md` (o que mudou, por quê, impacto) e atualizar `DESIGN.md`, `CLAUDE.md` e `docs/handoff.md`.
15. **Verificar a "cara de IA" sempre.** Todo diagnóstico inclui o `P-13` (momento `diagnóstico`); depois de cada camada que mexe em visual, texto, mídia, efeito ou tela nova (M-5 a M-9 e M-11 a M-16, conforme o caso), `P-13` (`pós-camada`); na verificação, `P-13` (`final`), comparando com o diagnóstico. Veredito "não passa" bloqueia a entrega. Correções que mudem a direção, textos aprovados ou área regulada vão para aprovação.
16. **Referência pede a escolha de vídeo.** Sempre que a melhoria envolver uma referência (efeito, transição, modal, menu, scroll), mostre ao usuário a opção de usar vídeo (`P-14`). A análise é feita com a skill `watch` (Guia 1, K24), nunca de memória; se ela falhar, relate e pare. O motor é fixado com `--engine` (o padrão `auto` usa o Gemini, e envia o vídeo ao Google, quando existe `GEMINI_API_KEY`).
17. **Ajuste visual dentro da rota.** Quando o usuário quiser mudar algo visualmente durante a melhoria, aplique o `P-15` (Guia 2A): classifique cada pedido, aplique em lote dentro da camada atual, registre em `docs/ajustes.md` e não toque no que está em "não pode mudar". Mudança de direção ou de camada exige confirmação explícita e novo plano (`M-4`). Pedido repetido, ajuste desfeito ou mais de 3 rodadas na mesma camada param o loop: mostre as versões lado a lado e ofereça reverter pela tag, gerar opções ou replanejar.
18. **Escolhas exatas antes de mexer.** Quando a melhoria tocar tipografia, disposição dos itens, tipo de item ou componente, aplique o `P-16` em modo edição (Guia 2A): extraia a ficha atual no diagnóstico (`M-3`) em `docs/escolhas.md`, marque cada item como mantido, ajustar ou trocar, e pergunte ao usuário só sobre o que for ajustar ou trocar, com opções e valores exatos. Ajustar valores é acabamento (`M-5`); trocar família, grade, tipo de item ou componente-base é estrutura (`M-6`, camada 3, com aprovação). Referências em bibliotecas de elementos (21st.dev, shadcn/ui etc.) vão para `docs/refs/componentes.md` e são adaptadas ao design system existente.
19. **Referência por elemento.** Para cada elemento visual que será criado ou alterado (navbar, hero, título, cartão, botão, formulário, rodapé, modal...), aplique o `P-17` em modo edição: a referência é o próprio existente ("mantido") ou um material novo (vídeo, imagem, print ou link com o ponto exato), com o que pegar e o que não pegar. Sem referência aprovada, o elemento não é criado nem alterado: peça material. Ao fazer algo específico, peça um exemplo antes. Depois, compare com a referência e registre a fidelidade em `docs/refs/fidelidade.md`.
20. **Efeitos.** Efeito novo ou alterado (hover, foco, pressionar, transição, rolagem, texto animado, fundo, cursor, carregamento) passa pelo `P-18`: propósito, parâmetros e referência aprovados em `docs/refs/mapa-efeitos.md`. Em cada categoria, mostre ao usuário o painel "Onde procurar" (Guia 1, seção 4.2.1) para ele escolher na biblioteca algo que goste. Protótipo dos efeitos-chave antes de espalhar; fallback e `prefers-reduced-motion` obrigatórios; efeito existente que não será alterado fica "mantido".

**Precedência quando há conflito** (igual aos guias 1 e 2, com um acréscimo no topo):
1. restrições do cliente e o que **não pode mudar**
2. pedido atual e objetivo da melhoria
3. `DESIGN.md` / convenções já existentes do projeto
4. skill mestre
5. skills de revisão (Impeccable, Jakub): sugerem, não reescrevem a direção
6. qualidade (a11y, performance, SEO, segurança): **vencem a estética**
7. economia (`ponytail`, `caveman`): nunca sobrepõem decisão de design

---

## 3. Intake de melhoria

Faça estas perguntas **nesta ordem** (uma por vez com `grill-me`). O agente que usa a Parte 0 do Guia 2B já conduz este intake sozinho e só pergunta o que não descobrir lendo o projeto:

| Ordem | Dado | O que descobrir |
|---|---|---|
| 1 | **Objetivo da melhoria** | O que precisa mudar e por quê? Qual resultado (mais contatos, menos erro, mais velocidade)? |
| 2 | **Estado atual** | URL/pasta; stack; quem fez; há repositório, hospedagem, domínio, CMS, banco? |
| 3 | **Acessos e ambientes** | Há ambiente de teste? Como publicar? Quem tem acesso a quê? Há backup? |
| 4 | **O que não pode mudar** | Textos aprovados, URLs, integrações, rastreamento, identidade, posições no Google |
| 5 | **Números atuais** | Visitas, origem, conversões, páginas mais acessadas, velocidade, erros |
| 6 | **Prazo, orçamento e aprovação** | Quando? Quanto? Quem aprova cada camada? |

**Modelo de intake (cole para o agente):**

```text
Objetivo da melhoria: {{o que e por quê}}
Tipo de intervenção (M1 a M12, se souber): {{...ou "não sei"}}
Site/projeto: {{URL ou pasta}} · Stack: {{...}} · Quem mantém: {{...}}
Acessos: {{repositório | hospedagem | domínio | CMS | banco | analytics}}
Ambiente de teste: {{sim/não}} · Backup existente: {{sim/não}}
Não pode mudar: {{textos, URLs, integrações, rastreamento, identidade}}
Números atuais: {{visitas, conversões, velocidade, erros}}
Prazo: {{...}} · Orçamento: {{...}} · Aprova: {{nome}}
Escolhas visuais (tipografia, disposição, tipos de itens, biblioteca de componentes): {{o que manter | o que ajustar | o que trocar, com links ou prints}} (P-16, modo edição)
Referência por elemento (navbar, hero, cartão, botão, rodapé, efeito, modal, menu, transição): {{elemento → URL | print | vídeo | "nenhuma"}} · Vídeo de referência: {{arquivo ou link + trecho mm:ss | "nenhum"}} (mostre a escolha: P-14)
Restrições legais/privacidade: {{regras do conselho, LGPD, dados sensíveis}}
```

---

## 4. Fluxo seguro em 8 passos

| Passo | O que fazer | Saída | Prompt |
|---|---|---|---|
| **0. Preparar** | Snapshot, *branch*, acessos, ambiente de teste, o que não pode mudar | `docs/estado-inicial.md` | `M-0` |
| **0b. Adotar** (só se faltarem os `.md` do playbook) | Criar, a partir do código e sem alterar o projeto, `CLAUDE.md`, `DESIGN.md`, `docs/escolhas.md`, `docs/briefing.md` (hipótese) e os arquivos de registro, tudo marcado `[inferido]` ou `[confirmar]` | `CLAUDE.md`, `DESIGN.md`, `docs/…` | `M-A` |
| **1. Mapear** | Estrutura, páginas, URLs, dependências, integrações, formulários, rastreamento | `docs/mapa-do-projeto.md` | `M-1` |
| **2. Medir** | *Baseline*: performance, acessibilidade, SEO, erros, *screenshots* | `docs/baseline.md` | `M-2` |
| **3. Diagnosticar** | Auditorias com **duas fontes** (Impeccable + Hallmark/Jakub) e análise anti-"cara de IA" (`P-13`), **sem alterar nada** | `docs/diagnostico.md` | `M-3` |
| **4. Priorizar e planejar** | Classificar achados, impacto × esforço × risco, plano em camadas | `docs/plano-melhorias.md` | `M-4` |
| **5. Aplicar em camadas** | Executar o tipo de intervenção (seção 5) com aprovação por camada | *commits* pequenos | `M-5` a `M-16` |
| **6. Verificar** | Comparar com o *baseline*, regressão, testes de formulário e integrações, e reanálise anti-"cara de IA" (`P-13`, final) | `docs/antes-depois.md` | `M-17` |
| **7. Entregar e registrar** | Relatório ao cliente, `handoff`, atualizar documentos, orientar manutenção | `docs/handoff.md` | `M-18` |

**Critério de saída global:** nada crítico pendente, nada do "não pode mudar" alterado sem aprovação, métricas iguais ou melhores que o *baseline*, documentação atualizada.

---

## 5. Tipos de intervenção (M1 a M12)

Cada tipo traz: quando usar, ferramentas do guia, risco e trilha de prompts. Ferramentas citadas vêm do guia original; confirme nomes no README. Em **todos**, o gate `P-13` (cara de IA) roda no diagnóstico, depois de cada camada que mexa em visual, texto, mídia, efeito ou tela nova e na verificação final, e toda referência pede a escolha de vídeo (`P-14`). Quando a intervenção mexer em tipografia, disposição, tipo de item ou componente, entra o `P-16` (escolhas exatas com valores).

### M1. Diagnóstico geral (auditoria sem mexer)
- **Quando:** cliente diz "o site não está bom" sem saber por quê; antes de qualquer outro tipo.
- **Ferramentas:** Impeccable `critique` e `audit`; Hallmark `audit` (segunda opinião); Jakub `better-interface` e `break`; `unlazy`; `P-13` (análise anti-"cara de IA", Guia 2A).
- **Risco:** baixo (não altera nada).
- **Trilha:** `M-0` → `M-1` → `M-2` → `M-3` → `M-4`.

### M2. Polimento visual (acabamento)
- **Quando:** a estrutura está boa, mas tipografia, cor, espaçamento, estados e consistência estão fracos.
- **Ferramentas:** Jakub (`better-interface`, `better-typography`, `better-colors`, `break`); Impeccable (`normalize`, `adapt`, `document`); `baseline-ui`.
- **Risco:** baixo a médio (cuidar de contraste e consistência).
- **Trilha:** `M-0` a `M-4` → `M-5` → `M-17`.

### M3. Redesign por camadas (estrutura e marca)
- **Quando:** o diagnóstico mostra problemas de estrutura ou de percepção de marca.
- **Ferramentas:** skill mestre `redesign` (Hallmark ou Taste `redesign-skill`, **escolha 1**); `design-lab` para opções ao cliente; Impeccable `document` para registrar o que existe. Referência do cliente (site, print, efeito): mostre a escolha de vídeo (`P-14`).
- **Risco:** alto (mudança de URLs, textos e SEO). **Mantenha texto, arquitetura e marca**, a menos que o cliente aprove.
- **Trilha:** `M-0` a `M-4` → `M-5` → `M-6` → `M-17`. Veja também S13 (Guia 1).

### M4. Performance
- **Quando:** site lento, imagens pesadas, rolagem travando, nota baixa em Core Web Vitals.
- **Ferramentas:** `core-web-vitals`, `performance`, `web-quality-audit`/`web-perf` (⚠ confirmar IDs no catálogo https://ui-skills.com); `pbakaus/optimize`; `ponytail-audit`/`optimize` (remover dependências); `fixing-motion-performance` e `60fps-animation` se houver animação.
- **Risco:** médio (compressão pode degradar imagem; *lazy load* pode quebrar layout).
- **Trilha:** `M-0` a `M-4` → `M-7` → `M-17`.

### M5. Acessibilidade
- **Quando:** contraste ruim, sem foco visível, formulários sem rótulo, uso por teclado impossível, exigência legal ou de cliente.
- **Ferramentas:** `addyosmani/accessibility`, `accessibility-scan`/`diff`, `wcag-audit-patterns`, `fixing-accessibility`, Jakub `better-accessibility`, `accessible-animation`.
- **Risco:** baixo, mas pode alterar cores do `DESIGN.md`.
- **Trilha:** `M-0` a `M-4` → `M-8` → `M-17`.

### M6. SEO e metadados
- **Quando:** o site não aparece no Google, títulos repetidos, sem Open Graph, negócio local sem dados estruturados.
- **Ferramentas:** `addyosmani/seo`, `iannuttall/seo`, `fixing-metadata`.
- **Risco:** médio. **Nunca** mude URLs sem mapa de redirecionamento.
- **Trilha:** `M-0` a `M-4` → `M-9` → `M-17`.

### M7. Segurança e privacidade (LGPD)
- **Quando:** há login, banco, formulário com dados pessoais ou pagamento; ou o projeto foi feito às pressas.
- **Ferramentas:** `vibe-security` (regras de acesso do banco, chaves expostas, webhooks e preços de pagamento, cabeçalhos, deploy).
- **Risco:** alto (descobertas críticas). **Dados sensíveis** (saúde, documentos): coleta mínima e revisão jurídica do cliente.
- **Trilha:** `M-0` a `M-4` → `M-10` → `M-17`.

### M8. Conteúdo e copy
- **Quando:** textos com cara de IA, genéricos, desatualizados ou que não convertem.
- **Ferramentas:** `no-ai-slop`; Jakub `better-writing`; `clarify`; `human-review`; `P-13` (camada texto).
- **Risco:** médio em áreas reguladas: **a restrição legal vence o tom**.
- **Trilha:** `M-0` a `M-4` → `M-11` → `M-17`.

### M9. Mobile e responsivo
- **Quando:** quebra no celular, texto pequeno, botões difíceis, menu ruim, rolagem horizontal indesejada.
- **Ferramentas:** Impeccable `adapt`; Emil `mobile-native`; `apple-web-app`; `prefer-container-queries`; `playwright-cli` ou `agent-browser` (**escolha 1**) para testar em vários tamanhos.
- **Risco:** baixo a médio. **Teste em aparelho real**.
- **Trilha:** `M-0` a `M-4` → `M-12` → `M-17`.

### M10. Adicionar efeito, mídia ou feature de referência
- **Quando:** o cliente quer "um vídeo que avança com o scroll", fundo em vídeo, áudio ambiente, galeria, parallax, ou algo que viu em outro site.
- **Ferramentas:** protocolo **FR** e catálogo de features (Guia 1, seção 14); níveis E0 a E5 (seção 12); mídia (seção 13); prompts `E-1` a `E-6` e `E-11` (Guia 2A, Parte E); vídeo de referência: `P-14` com a skill `watch` (Guia 1, K24 e seção 4.4).
- **Risco:** alto (peso, acessibilidade, manutenção). O **modelo** do site define o nível máximo; efeito acima dele exige decisão registrada.
- **Trilha:** `M-0` a `M-4` → `M-13` (que chama `E-6`, `E-1` a `E-5`) → `E-11` → `M-17`.

### M11. Adicionar funcionalidade com dados (formulário, login, agenda, loja)
- **Quando:** o site estático precisa guardar ou mostrar dados.
- **Ferramentas:** prompt `E-9` (Guia 2A); shadcn (base); Superpowers (lógica e TDD, **só se houver lógica**); `vibe-security`; `playwright-cli`.
- **Risco:** muito alto (dados pessoais, pagamento, regras de acesso). Escolha de backend e quem administra **antes** de desenhar telas.
- **Trilha:** `M-0` a `M-4` → `M-14` → `M-10` → `M-17`.

### M12. Refatoração, limpeza e design system
- **Quando:** CSS duplicado, tokens espalhados, dependências demais, componentes inconsistentes; projeto difícil de manter.
- **Ferramentas:** Impeccable `document` (gera `DESIGN.md` a partir do código) e `normalize`; `create-design-md`; `tailwind-token-consolidation` (projeto com Tailwind); `react-doctor`/`improve-react` (projeto React); `ponytail-audit`/`optimize`/`review`.
- **Risco:** médio (regressão visual). Faça por **fatias** e compare *screenshots*.
- **Trilha:** `M-0` a `M-4` → `M-15` → `M-17`.

> **Hotfix (`M-16`):** correção pequena e urgente (link quebrado, texto errado, bug de formulário). Use `M-16`: reproduzir, corrigir o mínimo, testar, publicar com aprovação, registrar.
> **Migração (stack, hospedagem, CMS):** o guia original não cobre; trate como projeto novo para a parte visual (Guias 1 e 2) e use `M-0` a `M-2` e `M-17` para proteger URLs, dados e SEO. Avise que a migração em si exige validação fora destes guias.

---

## 6. Sintoma → intervenção

| O cliente (ou você) diz… | Intervenção provável | Primeiro passo |
|---|---|---|
| "O site está lento" | **M4** | `M-2` baseline de performance |
| "Não aparece no Google" | **M6** | Checar metadados, indexação e estrutura |
| "Parece antigo" | **M2** ou **M3** | `M-3` diagnóstico com as duas fontes |
| "Parece feito por IA", genérico ou de template | **M1** → **M2**/**M3**/**M8** | `P-13` (momento diagnóstico) |
| "Ninguém clica no botão / ninguém chama" | **M1** → **M3**/**M8** | Diagnóstico: ação principal visível? copy? |
| "Quebra no celular" | **M9** | Teste em vários tamanhos e aparelho real |
| "Não consigo editar sozinho" | **M12** + conversa | Mapear como o conteúdo é editado; definir ferramenta |
| "Quero um efeito igual ao daquele site" | **M10** | Protocolo FR (`E-6`) |
| "Preciso de login, agenda ou loja" | **M11** | `E-9` (decisões de dados antes de telas) |
| "O formulário não chega" | **Hotfix** (`M-16`) | Reproduzir e testar o envio real |
| "Receio de segurança / LGPD" | **M7** | `vibe-security` + revisão jurídica do cliente |
| "Acessibilidade exigida" | **M5** | `accessibility-scan` + teclado |
| "O código está uma bagunça" | **M12** | `ponytail-audit`, Impeccable `document` |
| "Quero mudar tudo" | **M1** primeiro | Diagnóstico antes de decidir; evitar redesign total sem evidência |

---

## 7. Priorização: impacto, esforço, risco

**Classifique cada achado** (de `M-3`) em uma categoria e uma severidade:

| Categoria | Exemplos |
|---|---|
| **ACABAMENTO** | espaçamento, tipografia, estados, consistência |
| **ESTRUTURA** | hierarquia de página, navegação, ordem das seções |
| **MARCA** | tom, identidade, percepção |
| **CONTEÚDO** | textos, imagens, clareza |
| **TÉCNICO** | performance, dependências, código |
| **QUALIDADE** | acessibilidade, SEO |
| **SEGURANÇA/PRIVACIDADE** | acessos, dados, LGPD |
| **CARA DE IA** | visual, estrutura, texto ou código genéricos, de template ou de IA (ver `P-13`) |

| Severidade | Significado |
|---|---|
| **Crítico** | quebra a função principal, expõe dados ou barra o usuário |
| **Alto** | prejudica claramente o objetivo (conversão, leitura, acesso) |
| **Médio** | incomoda, mas não impede |
| **Baixo** | refinamento |

**Matriz de ordem de ataque** (editorial):

| Impacto | Esforço | Risco | Decisão |
|---|---|---|---|
| Alto | Baixo | Baixo | **Fazer primeiro** |
| Alto | Alto | Baixo/Médio | Planejar em camadas |
| Alto | Qualquer | Alto | Só com plano de reversão e aprovação |
| Baixo | Baixo | Baixo | Agrupar em um lote |
| Baixo | Alto | Qualquer | **Adiar ou recusar** |

**Regra:** críticos de **segurança, dados e acessibilidade** vão primeiro, mesmo que o cliente peça estética.

---

## 8. Baseline: medir antes e depois

Registre em `docs/baseline.md` **antes** de alterar, e repita depois. Use as ferramentas que o projeto tiver (skills de performance/a11y/SEO e testes no navegador); diga **quais** usou e a data. Os números abaixo são **exemplos de campos**, não metas.

| Área | O que medir | Como (ferramentas do guia) |
|---|---|---|
| **Performance** | LCP, CLS, INP (Core Web Vitals), peso total, nº de requisições, maiores imagens | `core-web-vitals`, `web-perf`, `performance` |
| **Acessibilidade** | Erros automáticos, contraste, foco por teclado, rótulos | `accessibility-scan`, `addyosmani/accessibility` |
| **SEO** | Título/descrição por página, Open Graph, dados estruturados, páginas indexáveis | `addyosmani/seo`, `fixing-metadata` |
| **Funcional** | Formulários enviam? Links quebrados? Integrações funcionam? | `playwright-cli`/`agent-browser` |
| **Visual** | *Screenshots* de cada página em desktop e celular | `playwright-cli`/`agent-browser` |
| **Negócio** | Visitas, conversões, origem do tráfego (se houver analytics) | Dados do cliente |
| **Rastreamento** | Quais *tags*/pixels existem e onde | Mapeamento (`M-1`) |

**Modelo de tabela antes/depois:**

| Métrica | Antes (data) | Depois (data) | Meta acordada | Resultado |
|---|---|---|---|---|
| LCP (celular) | | | | |
| Peso da página inicial | | | | |
| Erros de acessibilidade | | | | |
| Formulário envia | | | | |
| Sinais de "cara de IA" (`P-13`: alta/média) | | | | |

> Se uma medição falhar ou não puder ser feita, **registre isso**; não preencha com estimativa e não declare melhoria sem medir.

---

## 9. Mapa de risco e checklist de regressão

### 9.1 O que costuma quebrar (e como prevenir)

| Risco | Como acontece | Prevenção |
|---|---|---|
| **Perder posição no Google** | URLs mudam, títulos mudam sem critério, páginas somem | Mapa de URLs e redirecionamentos 301; manter títulos e textos que ranqueiam |
| **Formulário para de enviar** | Mudança de campos, de rota ou de integração | Teste de envio real antes e depois |
| **Rastreamento some** | Troca de *template* remove *tags* | Inventário de *tags* em `M-1`; conferir depois |
| **Integrações quebram** | Agenda, pagamento, WhatsApp, e-mail marketing | Lista de integrações e teste de cada uma |
| **Layout quebra em páginas que ninguém olhou** | Mudança global de CSS | *Screenshots* de todas as páginas antes e depois |
| **Acessibilidade regride** | Troca de cores, remoção de foco, animações | Rodar a11y antes e depois; `prefers-reduced-motion` |
| **Peso aumenta** | Novos efeitos, mídia, bibliotecas | Orçamento (Guia 1, seções 12 e 13); medir |
| **Dados perdidos ou expostos** | Mudança de banco ou de regras de acesso | Backup e plano de reversão; `vibe-security` |
| **Cache mostra versão antiga** | Hospedagem ou CDN | Limpar cache e conferir em janela anônima |
| **Conteúdo editável deixa de ser editável** | Mudança de estrutura | Documentar como editar; testar com o responsável |
| **A mudança introduz "cara de IA"** | Efeito, texto ou componente padrão acrescentado sem especificidade do negócio | `P-13` depois de cada camada; teste de troca |
| **Loop de ajustes visuais** | Cliente repete ou desfaz pedidos e a camada nunca fecha; a edição escorrega para um redesign | `P-15`: classificar, agrupar em lote, registrar em `docs/ajustes.md`, reverter por tag; mudança de direção vira decisão e replanejamento |
| **Escolhas vagas geram retrabalho** | "Mais moderno", fonte, disposição e tipo de item escolhidos pelo agente sem o usuário ver | `P-16`: ficha de escolhas com valores exatos, aprovada antes de mexer |
| **Entrega genérica mesmo com referência** | Referência tratada como inspiração geral; o agente preenche cada elemento com o padrão da biblioteca ou do modelo | `P-17`: referência obrigatória por elemento, com o que pegar; sem referência, o elemento não é feito; fidelidade conferida depois |
| **Efeito escolhido por padrão** | *Fade-up* em tudo, hover que "levita", fundo animado sem propósito, sem fallback e sem o usuário ter visto alternativas | `P-18`: painel "Onde procurar" em cada categoria, propósito e referência aprovados, protótipo antes de espalhar, `prefers-reduced-motion` |

### 9.2 Checklist de regressão (rodar em `M-17`)

| Área | Verificar | Obrigatório quando |
|---|---|---|
| **URLs** | Todas as URLs antigas respondem ou redirecionam; sem 404 novos | Qualquer mudança de estrutura |
| **Formulários** | Envio real, mensagem de sucesso/erro, e-mail chega | Há formulário |
| **Integrações** | Agenda, pagamento, WhatsApp, e-mail marketing | Há integração |
| **Rastreamento** | *Tags* e eventos continuam disparando | Há analytics/pixel |
| **Visual** | *Screenshots* antes/depois, desktop e celular, todas as páginas | Sempre |
| **Responsivo** | Menu, botões, texto, rolagem horizontal | Sempre |
| **Acessibilidade** | Contraste, foco, rótulos, teclado, reduced-motion | Sempre |
| **Performance** | Igual ou melhor que o baseline | Sempre; crítico em e-commerce e landing |
| **SEO** | Títulos, descrições, Open Graph, canonical, dados estruturados | Sites públicos |
| **Segurança** | `vibe-security` | Login, banco, dados pessoais, pagamento |
| **Mídia e direitos** | `docs/midia.md` atualizado; licenças e créditos | Houve foto, vídeo ou áudio novo |
| **Cara de IA** | `P-13` (final) igual ou melhor que o diagnóstico; nada genérico novo; `docs/anti-ia.md` atualizado | Sempre |
| **Conteúdo editável** | O responsável consegue editar o que combinamos | Sempre |
| **Documentação** | `DESIGN.md`, `CLAUDE.md`, `docs/handoff.md`, `docs/melhorias.md` | Sempre |

---

## 10. Prompts (Parte M): trilhas e índice

O **texto** de cada prompt está em `02-prompts-edicao.md` (Guia 2B, Parte M). Aqui ficam só as **trilhas** (ordem) e o **índice**, para decidir sem carregar o texto. As convenções dos prompts (variáveis `{...}`, P-00, diagnóstico sem alterar código, aprovação por camada, falha de ferramenta) estão no cabeçalho do Guia 2B.

### Trilhas por tipo (resumo)

| Tipo | Trilha |
|---|---|
| M1 diagnóstico | `M-0` → `M-1` → `M-2` → `M-3` → `M-4` |
| M2 polimento | base (`M-0` a `M-4`) → `M-5` → `M-17` → `M-18` |
| M3 redesign | base → `M-5` → `M-6` → `M-17` → `M-18` |
| M4 performance | base → `M-7` → `M-17` → `M-18` |
| M5 acessibilidade | base → `M-8` → `M-17` → `M-18` |
| M6 SEO | base → `M-9` → `M-17` → `M-18` |
| M7 segurança | base → `M-10` → `M-17` → `M-18` |
| M8 conteúdo | base → `M-11` → `M-17` → `M-18` |
| M9 responsivo | base → `M-12` → `M-17` → `M-18` |
| M10 efeito/mídia | base → `M-13` (→ `E-6`, `E-1` a `E-5`) → `E-11` → `M-17` → `M-18` |
| M11 dados | base → `M-14` (→ `E-9`) → `M-10` → `M-17` → `M-18` |
| M12 refatoração | base → `M-15` → `M-17` → `M-18` |
| Hotfix | `M-0` (rápido) → `M-16` → `M-17` (parcial) |

Projeto **sem os `.md` do playbook**: insira `M-A` (adoção) logo depois de `M-0` em qualquer trilha (no hotfix, só o kit mínimo).

### Índice dos prompts

| ID | Prompt | Passo do fluxo (seção 4) |
|---|---|---|
| `M-I` | Instalação do kit de melhoria | Antes do passo 0 |
| `M-0` | Preparar (snapshot, acessos, o que não pode mudar) | 0. Preparar |
| `M-A` | Adoção: criar os `.md` do playbook a partir do código (texto na Parte 0-A de `02-prompts-edicao.md`) | 0b. Adotar (só se faltarem os `.md`) |
| `M-1` | Mapear o projeto | 1. Mapear |
| `M-2` | Baseline | 2. Medir |
| `M-3` | Diagnóstico (duas fontes, sem alterar nada) | 3. Diagnosticar |
| `M-4` | Priorizar e planejar em camadas | 4. Priorizar e planejar |
| `M-5` | Acabamento visual (M2/M3, camada 2) | 5. Aplicar em camadas |
| `M-6` | Estrutura e marca (M3, camada 3) | 5. Aplicar em camadas |
| `M-7` | Performance (M4) | 5. Aplicar em camadas |
| `M-8` | Acessibilidade (M5) | 5. Aplicar em camadas |
| `M-9` | SEO, metadados e URLs (M6) | 5. Aplicar em camadas |
| `M-10` | Segurança e privacidade (M7) | 5. Aplicar em camadas |
| `M-11` | Conteúdo e copy (M8) | 5. Aplicar em camadas |
| `M-12` | Responsivo e mobile (M9) | 5. Aplicar em camadas |
| `M-13` | Adicionar efeito, mídia ou feature de referência (M10) | 5. Aplicar em camadas |
| `M-14` | Adicionar funcionalidade com dados (M11) | 5. Aplicar em camadas |
| `M-15` | Refatoração, limpeza e design system (M12) | 5. Aplicar em camadas |
| `M-16` | Hotfix (correção pequena e urgente) | 5. Aplicar em camadas |
| `M-17` | Verificação, regressão e antes/depois | 6. Verificar |
| `M-18` | Entrega, relatório e manutenção | 7. Entregar e registrar |

Prompts do Guia 2A usados na edição: `P-13` (gate anti-"cara de IA"), chamado dentro de `M-3` (diagnóstico), `M-5`, `M-6`, `M-7` (se mexer em imagem, fonte ou vídeo), `M-8`, `M-9`, `M-11`, `M-12`, `M-13`, `M-14`, `M-15`, `M-16` (se tocar visual ou texto) (pós-camada), `M-17` (final) e `S13-*`; e `P-14` (referência em vídeo), chamado dentro de `M-0` (regra), `M-6`, `M-13` e `S13-3`; e `P-15` (ajuste visual dentro da rota), chamado dentro de `M-0` (regra), `M-5`, `M-6` e `S13-3`; e `P-16` (escolhas exatas), chamado dentro de `M-0` (regra), `M-3` (ficha atual), `M-5`, `M-6` e `M-12` (só disposição); e `P-17` (referência por elemento), chamado dentro de `M-0` (regra), `M-5`, `M-6`, `M-13`, `M-14` e `M-A`; e `P-18` (efeitos e interações), chamado dentro de `M-0` (regra), `M-5`, `M-6`, `M-13` e `M-A`.

**Redesign de site existente (S13):** `S13-I` → `S13-1` → `S13-2` → `S13-3`, texto em `02-prompts-edicao.md`, Parte S13.

---

## 11. Perguntas ao cliente para melhorias

> Faça uma por vez. Serve para o intake e para a conversa de plano. As perguntas de briefing do Guia 3 continuam valendo quando a melhoria mexer em oferta, público ou marca.

### 11.1 Base (todo projeto existente)
1. O que **exatamente** incomoda no site hoje? Pode mostrar exemplos (páginas, prints, reclamações de clientes)?
2. Qual resultado você espera com a melhoria? Como saberemos que deu certo?
3. O que **funciona bem** e **não pode mudar**? (textos, estrutura, endereços, integrações, identidade)
4. Quem fez o site, quem mantém e quem tem acesso (domínio, hospedagem, painel, código, analytics)?
5. Existe **backup** e **ambiente de teste**? Quem publica?
6. Você tem números? (visitas, origem, contatos, vendas, páginas mais vistas, velocidade)
7. Há **prazo** e **orçamento**? Quem aprova cada etapa?
8. Existe alguma **regra legal ou de privacidade** (publicidade profissional, LGPD, dados sensíveis)?
9. Há **eventos próximos** (campanha, lançamento, temporada) que não podem ser prejudicados?
10. Quer **mudar tudo** ou melhorar por etapas, mantendo o que já traz resultado?

### 11.2 Por tipo de intervenção

**M2/M3, visual e redesign**
- O que no visual parece "antigo", "fora da marca" ou "genérico, com cara de feito por IA"? Mostre sites que representam o que você quer. Se tiver um vídeo (gravação de tela ou link com minuto e segundo) de um efeito, menu ou modal que gostou, envie (`P-14`). Qual letra, qual disposição dos blocos e qual tipo de item (cartão, lista, tabela, galeria) você quer manter e qual quer trocar? Tem algum elemento de biblioteca de componentes (21st.dev, shadcn/ui, coss ui, OriginKit, ObsidianUI, Bencho etc.) que quer como referência? (`P-16`) Para cada elemento que quer mudar (navbar, hero, cartão, botão, rodapé...), qual exemplo você quer como referência? Mande vídeo, print ou link com o ponto exato e diga o que gostou nele (`P-17`). Quais efeitos (botão, menu, transição entre páginas, rolagem, texto animado) você viu e gostou? Abra as bibliotecas que indicarmos e escolha algo que goste, ou mande uma gravação de tela (`P-18`).
- A marca (logo, cores, tipografia) pode mudar ou fica?
- Os textos podem ser reescritos ou são aprovados por alguém (sócio, jurídico)?
- Aceita ver 2 ou 3 direções antes de decidir?

**M4, performance**
- O site é lento em que situações? (celular, 4G, páginas específicas, horários)
- O público acessa mais por celular ou por aparelhos simples?
- Há vídeos, imagens grandes ou scripts de terceiros (chat, pixels, mapas) que são indispensáveis?

**M5, acessibilidade**
- Há exigência legal ou de cliente? Algum usuário relatou dificuldade?
- Há vídeos ou áudios que precisam de legenda e transcrição?

**M6, SEO**
- Quais buscas você quer aparecer? Onde aparece hoje?
- Existe Google Meu Negócio e Search Console? Quem controla?
- Posso mudar títulos e textos, ou há páginas que já ranqueiam e precisam ficar iguais?

**M7, segurança e privacidade**
- Que dados o site coleta e guarda? Quais são sensíveis?
- Já houve incidente, spam intenso ou acesso indevido?
- Existe política de privacidade e quem a revisa?

**M8, conteúdo**
- Quem escreve e aprova os textos? Há regras de tom e de publicidade?
- Existem depoimentos, números ou resultados que **podem** ser publicados?

**M9, mobile**
- Quais páginas ou ações mais quebram no celular? Em quais aparelhos?
- A maior parte do tráfego vem do celular?

**M10, efeito, mídia e features de referência**
- Mostre a referência e diga o que te encanta (movimento, mídia, história ou sensação).
- Consegue gravar a tela (ou enviar o link com o minuto e o segundo) do trecho em que o efeito aparece? Com vídeo, a IA analisa o movimento e a ordem das etapas (`P-14`, skill `watch`).
- Você **tem** o vídeo, as fotos ou o áudio que esse efeito exige? Há autorização e licença?
- Prefere a versão **completa** (mais prazo e orçamento) ou uma versão **leve**?
- Se o efeito deixar o site mais lento no celular, você prefere cortar ou manter?
- O site precisa funcionar bem para quem prefere menos movimento ou tem internet lenta? (versão simples de reserva)

**M11, dados e funcionalidades novas**
- Quem usa o novo recurso e o que ele guarda? Há dados sensíveis?
- Onde ficam os dados e **quem administra** depois?
- Há sistema, planilha ou ferramenta atual que precisa se conectar?
- O que acontece se o sistema falhar? Precisa de backup e plano de reversão?

**M12, manutenção e código**
- Quem vai mexer no site depois? Com que frequência?
- Existe alguma tecnologia que **deve** ser mantida (por contrato, equipe ou custo)?
- Quer que o cliente consiga editar sozinho? O quê?

### 11.3 Alertas na conversa

| Sinal | O que fazer |
|---|---|
| Cliente quer "mudar tudo" sem diagnóstico | Propor **M1** primeiro (diagnóstico) e plano em camadas |
| Ninguém sabe quem tem acesso a domínio, hospedagem ou código | Resolver acessos antes de qualquer promessa de prazo |
| Não há backup nem ambiente de teste | Criar snapshot e *branch* antes; sem isso, **não** mexer em produção |
| Pede efeito pesado em site já lento ou antigo | Corrigir performance (**M4**) antes de acrescentar efeito (**M10**) |
| Quer trocar URLs ou estrutura sem lembrar de SEO | Exigir mapa de redirecionamentos e medir indexação |
| Dados sensíveis sem aviso de privacidade | **M7** e revisão jurídica do cliente |
| Cliente pede promessas de resultado em área regulada | A restrição legal vence o tom |
| Quer copiar um site concorrente | Extrair princípios; não copiar layout, marca, textos ou assets |

---

## 12. Comunicação: plano em camadas e relatório antes/depois

### 12.1 Modelo de proposta de plano ao cliente

```text
# Plano de melhorias: {{projeto}}

Objetivo: {{...}}
O que não vamos mudar: {{lista}}

| Camada | O que será feito | Benefício esperado | Risco | Prazo | Custo | Aprovação |
|---|---|---|---|---|---|---|
| 1. Crítico (segurança, dados, acessibilidade) | | | | | | |
| 2. Acabamento e responsivo | | | | | | |
| 3. Estrutura e conteúdo (se necessário) | | | | | | |
| 4. Efeitos, mídia ou novas funções (opcional) | | | | | | |

Fica para depois: {{lista}}
Recusado e por quê: {{lista}}
Como reverter: {{...}}
```

### 12.2 Modelo de relatório antes/depois ao cliente

```text
# Relatório de melhorias: {{projeto}} ({{data}})

1. O que fizemos (em linguagem simples).
2. Por que fizemos (o problema que resolvia).
3. Números antes/depois (velocidade, erros, contatos, quando houver).
4. O que ficou como estava, a pedido.
5. O que ficou para uma próxima etapa.
6. O que você precisa fazer (ex.: atualizar Google Meu Negócio, revisar política de privacidade).
7. Como editar o que combinamos e quem chamar em caso de problema.
```

### 12.3 Como falar de risco e de custo
- Apresente **duas opções** (completa e leve) com impacto em prazo, orçamento, peso do site e manutenção.
- Diga o que **pode dar errado** e como será revertido.
- Registre a decisão por escrito antes de aplicar.

---

## 13. Roteamento do agente (YAML)

```yaml
# docs/playbook.melhorias.yaml  (curadoria editorial; valide em projeto de teste)
prompt_inicial: {arquivo: 02-prompts-edicao.md, parte: 0, usar_quando: projeto_existente_ou_em_andamento, se_faltarem_md: {prompt: M-A, parte: 0-A, somente_leitura_no_projeto: true, cria: [CLAUDE.md, DESIGN.md, docs/escolhas.md, docs/briefing.md, docs/decisoes.md, docs/ajustes.md, docs/backlog.md, docs/melhorias.md, docs/refs/componentes.md], marca: [inferido, confirmar], nunca_sobrescreve_existentes: true, nunca_le_segredos: true}}
regras_globais:
  - gate_anti_ia_P13_no_diagnostico_pos_camada_e_final
  - referencia_pede_escolha_de_video_P14
  - ajuste_visual_dentro_da_rota_P15
  - escolhas_exatas_P16_tipografia_disposicao_itens_biblioteca
  - referencia_por_elemento_P17
  - efeitos_P18_painel_onde_procurar
  - diagnostico_nao_altera_codigo
  - snapshot_e_branch_antes_de_qualquer_mudanca
  - medir_antes_e_depois
  - uma_camada_por_vez_com_aprovacao
  - nao_mudar_urls_sem_mapa_301
  - nao_publicar_sem_aprovacao_explicita
  - falha_de_ferramenta_para_e_relata
  - seguranca_e_a11y_vencem_estetica
fluxo: [preparar, mapear, medir, diagnosticar, priorizar, aplicar_em_camadas, verificar, entregar]
tipos:
  M1_diagnostico:  {sinais: [nao_sei_o_que_esta_ruim, auditoria], ferramentas: [impeccable-critique-audit, hallmark-audit, jakub-better-interface-break, unlazy, P-13], prompts: [M-0, M-1, M-2, M-3, M-4]}
  M2_polimento:    {sinais: [parece_antigo, inconsistente], ferramentas: [jakub, impeccable-normalize-adapt-document, baseline-ui], prompts: [M-5]}
  M3_redesign:     {sinais: [refazer_estrutura, marca], mestre: {escolher_um: [hallmark, taste-redesign]}, opcoes: design-lab, risco: alto, prompts: [M-5, M-6, P-14]}
  M4_performance:  {sinais: [lento, imagens_pesadas], ferramentas: [core-web-vitals, performance, optimize, ponytail-audit, fixing-motion-performance], prompts: [M-7]}
  M5_acessibilidade: {sinais: [contraste, teclado, exigencia_legal], ferramentas: [accessibility, accessibility-scan, wcag-audit-patterns, accessible-animation], prompts: [M-8]}
  M6_seo:          {sinais: [nao_aparece_no_google], ferramentas: [seo, fixing-metadata], regra: redirecionamento_301_obrigatorio_se_mudar_url, prompts: [M-9]}
  M7_seguranca:    {sinais: [login, banco, dados_pessoais, pagamento], ferramentas: [vibe-security], regra: revisao_juridica_do_cliente, prompts: [M-10]}
  M8_conteudo:     {sinais: [texto_generico, cara_de_ia], ferramentas: [no-ai-slop, jakub-better-writing, clarify, human-review], regra: restricao_legal_vence_tom, prompts: [M-11]}
  M9_responsivo:   {sinais: [quebra_no_celular], ferramentas: [impeccable-adapt, mobile-native, apple-web-app, prefer-container-queries], executor_de_testes: {escolher_um: [playwright-cli, agent-browser]}, prompts: [M-12]}
  M10_efeito_midia: {sinais: [quero_efeito, video_com_scroll, audio, referencia_de_outro_site], base: guia1_secoes_12_13_14, prompts: [M-13, E-6, P-14, E-1, E-2, E-3, E-4, E-5, E-11], ferramentas: [watch-claude-video], regra: modelo_define_nivel_maximo}
  M11_dados:       {sinais: [login, agenda, loja, formulario_com_banco], base: E-9, ferramentas: [shadcn, vibe-security, superpowers-se-logica], prompts: [M-14, M-10], regra: backend_e_quem_administra_antes_das_telas}
  M12_refatoracao: {sinais: [codigo_desorganizado, tokens_espalhados], ferramentas: [impeccable-document-normalize, create-design-md, tailwind-token-consolidation, react-doctor, ponytail], prompts: [M-15]}
  hotfix:          {sinais: [bug_urgente, link_quebrado], prompts: [M-16], regra: menor_correcao_possivel}
sempre_no_fim: [M-17, M-18]
evitar: [redesign_total_sem_diagnostico, mudar_urls_sem_mapa, duas_skills_mestras, sistema_pesado_sem_necessidade, publicar_sem_aprovacao, declarar_pronto_sem_evidencia]
```

---

## 14. Pendências e cuidados

**Pendências**
- **Nomes de comandos** do Impeccable, Jakub, Hallmark e skills de qualidade mudam entre versões: confirmar no README antes de rodar.
- **IDs do catálogo** (https://ui-skills.com) de skills de performance, acessibilidade, SEO e `baseline-ui`/`optimize`: confirmar repositório e comando.
- **Migração de stack/hospedagem/CMS** e **WordPress**: não cobertos pelo guia original.
- **Métricas, metas e lotes:** curadoria editorial; ajuste com medição.
- **`watch` (claude-video) e `P-14`:** comandos e requisitos conferidos no README oficial em 02/10/2026; reconfirmar no dia (Guia 1, seção 4.4). Não funciona no Claude Chat nem no Cowork; o motor `gemini` envia o vídeo ao Google, e o padrão `auto` o escolhe quando há `GEMINI_API_KEY`: fixe o motor com `--engine`.
- **Sinais do `P-13` ("cara de IA"):** curadoria editorial; ajuste e valide em projetos reais.
- **Ferramentas de conversão de imagem/vídeo e de testes visuais** citadas indiretamente ficam fora do guia original; confirmar instalação e comandos.

**Cuidados gerais**
1. **Nunca edite produção diretamente.** Snapshot, branch e teste primeiro.
2. **Não instale tudo.** Uma skill mestre, um executor de testes, um sistema de processo (só se necessário).
3. **Segredos:** se aparecer chave, token ou senha no código ou no histórico, avise, recomende rotacionar e não a repita em respostas ou documentos.
4. **Dados reais:** não use dados reais de clientes em testes sem autorização.
5. **Licenças e direitos:** referências servem para extrair princípios; confirme direitos de imagens, vídeo, áudio, fontes e componentes (ver Guia 1, seção 11).
6. **LGPD:** coleta mínima e aviso claro; dados de saúde são sensíveis; este documento não é aconselhamento jurídico.
7. **Mudou algo, documentou:** `docs/melhorias.md`, `DESIGN.md`, `CLAUDE.md`, `docs/handoff.md`.

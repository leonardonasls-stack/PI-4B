# Gate Anti-"Cara de IA" (`P-13`) — Vacina Alagoas

## Momento: `diagnóstico` (2026-11-12)
**Alvo:** `frontend/public/index.html` e `frontend/public/admin.html` (análise por varredura de código autorizada pelo usuário após falha do `chrome_devtools`).

| Sinal | Camada | Onde | Evidência | Severidade | Correção | Status |
|---|---|---|---|---|---|---|
| Descolamento visual entre Portal e Admin (cores `slate-900`/`emerald` no Admin vs `#002530`/`surface` no Portal) | VISUAL | `admin.html` (L69-158, L753+) | `152` classes `slate-*` e `71` `emerald-*` contra apenas `16` `primary` | **Alta** | Unificar header, rodapé, botões e superfícies com tokens `#002530` / `surface` / `secondary` | Pendente |
| Ícones em excesso / duas bibliotecas misturadas (`Material Symbols` carregada 2x + 30 SVGs inline) | VISUAL | `admin.html` (L3-4, corpo), `index.html` (56 SVGs) | 2 `<link>` para Material Symbols em `admin.html:3-4`, uso de apenas 4 ícones | **Média** | Remover Material Symbols duplicado/não usado, padronizar em um único conjunto limpo e reduzir ícones decorativos | Pendente |
| Valores soltos fora dos tokens (`text-[*px]`, `slate-*`, `borderRadius.full: 0.75rem`) | CÓDIGO | `index.html` (L118, 21 `text-[*px]`), `admin.html` (L67, 17 `text-[*px]`) | `borderRadius.full` sobrescrito para `0.75rem` quebra círculos (`L1343`); `text-[10px]`/`text-[11px]` soltos | **Média** | Consolidar escala tipográfica e de raios em `DESIGN.md` e remover valores arbitrários | Pendente |
| Indicador `animate-pulse` decorativo e animações sem `prefers-reduced-motion` | COMPORTAMENTO | `admin.html` (L108), `index.html` (L23) | `animate-pulse` no botão "Ver Portal" (`admin.html:108`); `0` ocorrências de `prefers-reduced-motion` | **Média** | Remover `animate-pulse` decorativo e adicionar fallback `@media (prefers-reduced-motion: reduce)` | Pendente |
| Tag `<html> lang="pt-BR">` malformada | CÓDIGO | `index.html` (L3) | Fechamento `>` antes de `lang="pt-BR">` | **Alta** | Corrigir para `<html lang="pt-BR">` | Pendente |
| Onda SVG decorativa no fundo do Hero | VISUAL | `index.html` (L354-366) | `<svg>` de onda com `opacity-10` atrás do título | **Baixa** | Avaliar remoção ou simplificação para visual institucional mais limpo | Listado |

**Teste de troca:** Os textos, nomes de bairros/municípios (Maceió, Arapiraca), catálogo de vacinas do SUS e integração OSM/ViaCEP são específicos de Alagoas (passa no conteúdo). Porém, a camada visual do Admin parece um "template dark-header + emerald" genérico desconectado do Portal.

**Veredito (`diagnóstico`):** **NÃO PASSA** (2 sinais de severidade **Alta** e 3 de **Média** pendentes).

---

## Momento: `pós-camada` — Camada 1 (2026-11-12)
**Alvo:** `frontend/public/index.html` e `frontend/public/admin.html`

| Sinal | Camada | Onde | Evidência | Severidade | Correção | Status |
|---|---|---|---|---|---|---|
| Tag `<html> lang="pt-BR">` malformada | CÓDIGO | `index.html:3` | Corrigida para `<html lang="pt-BR">` | **Alta** | Corrigido na Camada 1 | **Resolvido** |
| Ausência de `prefers-reduced-motion` | COMPORTAMENTO | `index.html`, `admin.html` | Regra `@media (prefers-reduced-motion: reduce)` adicionada em ambos | **Média** | Corrigido na Camada 1 (resta remover `animate-pulse` na Camada 2) | **Parcial** |
| Descolamento visual Portal vs. Admin | VISUAL | `admin.html` | `slate-900`/`emerald` ainda presentes até a Camada 2 | **Alta** | Programado para Camada 2 | Pendente (Camada 2) |
| Ícones duplicados e valores soltos (`text-[*px]`, `borderRadius.full`) | VISUAL / CÓDIGO | `index.html`, `admin.html` | Programado para Camada 2 | **Média** | Programado para Camada 2 | Pendente (Camada 2) |

**Veredito (`pós-camada 1`):** **NÃO PASSA** (itens de coesão visual programados para a Camada 2).



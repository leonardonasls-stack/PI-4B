# Baseline (`M-2`) — Vacina Alagoas

**Data:** 2026-11-12
**Alvo:** `frontend/public/index.html` e `frontend/public/admin.html` (`http://localhost:3005`)

## 1. Medições de Navegador / Screenshots
- **Status:** **Falha na captura automática (`chrome_devtools`)** — autorizado pelo usuário prosseguir via varredura estática do código (opção 2).
- **Erro registrado:** `Could not find DevToolsActivePort for chrome at C:\Users\Luiz\AppData\Local\Google\Chrome\User Data\DevToolsActivePort` (`ENOENT`).
- **Performance (LCP, CLS, INP), Acessibilidade automática em runtime e Screenshots desktop/mobile:** `não medido (falha de conexão com Chrome DevTools)`.

## 2. Métricas Estáticas Observadas no Código (Pré-Melhoria)

| Métrica | `index.html` (Portal) | `admin.html` (Admin) |
|---|---|---|
| Tamanho do arquivo | `169.276 bytes` (`2.933` linhas) | `84.510 bytes` (`1.479` linhas) |
| Erros de sintaxe HTML críticos | **1** (`<html> lang="pt-BR">` na L3) | `0` detectados na abertura |
| Classes `focus-visible:` | `23` | **`0`** |
| Classes `outline-none` | `6` | **`10`** |
| Suporte `prefers-reduced-motion` | **`0`** | **`0`** |
| Menu mobile (`< 768px`) | Visível | **Oculto (`hidden md:flex` na L92)** |
| Hierarquia de títulos (`<h1>`) | Presente (`L375`) | **Ausente (`0` `<h1>`, começa em `<h2>`)** |
| Tokens MD3 (`bg-primary`/`text-primary`) vs. `slate-*`/`emerald-*` | `62` primary vs `237` slate / `147` emerald | `16` primary vs `152` slate / `71` emerald |
| Tamanhos fora da escala (`text-[*px]`) | `21` | `17` |
| Bibliotecas de ícones | `56` SVGs inline (`0` Material Symbols) | `30` SVGs inline + `4` Material Symbols (fonte carregada **2x**) |


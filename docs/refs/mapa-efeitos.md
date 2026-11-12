# Mapa de Efeitos e Interações (`P-18` — Modo Edição)

Efeitos observados no código em 2026-11-12. Status inicial: `mantido`.

| Efeito / Interação | Onde está | Nível | Status | Fallback / `prefers-reduced-motion` |
|---|---|---|---|---|
| **Scroll suave (`scroll-behavior: smooth`)** | `index.html` (L23), `admin.html` (L6) | E1 | `mantido` | Não verificado explicitamente para `prefers-reduced-motion` |
| **Transições de hover/foco em botões e links (`transition-*`)** | `index.html` (~104 ocorrências), `admin.html` (~38 ocorrências) | E1 | `mantido` | Estado padrão sem transição |
| **Scale no logo do Admin (`group-hover:scale-105`)** | `admin.html` (L74) | E1 | `mantido` | Estado estático |
| **Pulse no indicador "Ver Portal" (`animate-pulse`)** | `admin.html` (L108) | E1 | `mantido` | Sem `motion-reduce:animate-none` observado |
| **Spinner de carregamento (`animate-spin`)** | `admin.html` (L159) e loading states | E1 | `mantido` | Indicador funcional de carregamento |

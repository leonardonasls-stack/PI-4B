# Guia de Handoff e Manutenção — Vacina Alagoas

**Versão da Entrega:** 1.0-melhorias  
**Data:** 04/11/2026  
**Ambiente:** Local / Docker Compose (Nginx :3005, FastAPI :8085, Postgres :5435)  

---

## 1. Visão Geral das Melhorias Entregues

O portal público do **Vacina Alagoas** passou por uma intervenção completa de polimento visual (M2) e reestruturação de layout (M3), mantendo integralmente todas as regras de negócio e integrações existentes:

1. **Eliminação do Aspecto de IA:**
   - Remoção de todas as tags de *Material Symbols* decorativas no frontend do cidadão (`frontend/public/index.html`).
   - Substituição por SVGs inline minimalistas (1.75px stroke) com atributos de acessibilidade (`aria-hidden="true"`).
   - Eliminação de fontes externas de ícones do Google Fonts, reduzindo o tempo de carregamento e eliminando oscilações de layout (CLS / FOIT).
   - Remoção de badges de autoridade artificiais e animações de pulso.

2. **Reorganização Estrutural da Experiência do Usuário (UX):**
   - **Hero Unificado:** Título e subtítulo institucionais claros, integrando a campanha de Influenza de forma editorial discreta.
   - **Barra de Pesquisa Ancorada:** Fim das margens negativas sobrepostas. A barra agora integra Município, Bairro/UBS, botão "Meu GPS" e "Buscar Postos" em um fluxo natural e responsivo.
   - **Guia do Cidadão:** Bento grid substituído por 3 cartões equilibrados e legíveis com informações de documentação, Disque 136 e campanhas.

---

## 2. Como Manter o Padrão Visual

- **Novos Ícones:** Nunca utilizar fontes de ícones pesadas ou de terceiros (`material-symbols` ou `font-awesome`). Utilizar sempre SVGs inline de contorno linear (`fill="none" stroke="currentColor" stroke-width="1.75"`) com `aria-hidden="true"`.
- **Cores e Contrastes:** Manter a paleta de alto contraste baseada em Azul Petróleo (`#002530`) e Container Primário (`#0e3b4a`), em conformidade estrita com a WCAG 2.1 AA/AAA.
- **Estrutura Semântica:** Todo elemento interativo deve ter rótulo acessível (`aria-label`, `for` vinculado ao `id` em formulários) e foco visível (`focus-visible:ring-4`).

---

## 3. Comandos de Operação

```bash
# Iniciar ambiente completo com Docker
docker compose up -d --build

# Parar serviços
docker compose down

# Rodar Frontend isolado para testes rápidos
cd frontend/public && python -m http.server 3005

# Rodar Backend FastAPI localmente
cd backend && uvicorn src.app.main:app --reload --port 8085
```

---

## 4. Reversão de Emergência

Caso seja necessário restaurar qualquer estado anterior:
- Voltar para o fim da Camada 2: `git checkout camada-2-concluida`
- Voltar para o fim da Camada 1: `git checkout camada-1-concluida`
- Voltar para o estado original intocado: `git checkout snapshot-pre-melhoria-m2`


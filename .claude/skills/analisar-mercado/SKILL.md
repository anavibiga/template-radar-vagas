---
name: analisar-mercado
description: Resume o que as vagas registradas pedem (stack, área, senioridade, salário), compara com meu perfil e sugere o que estudar e que projetos fazer. Usar quando eu perguntar "o que as vagas pedem", "quais meus gaps", "que projeto fazer" ou similar.
---

# Analisar mercado e gaps

1. Rodar `python3 scripts/stack.py --saida analises/stack.md` (com `--area` ou `--senioridade` se eu pedir um recorte) e ler o resultado.
2. Com menos de ~10 vagas, avisar que a amostra é pequena antes de concluir.
3. Ler também as descrições em `vagas/descricoes/` para captar o que não é stack: tipo de produto e problema, domínio, soft skills recorrentes, formato do processo seletivo (take-home, live coding, system design).
4. Responder com:
   - **O que a maioria pede:** as 5–8 competências mais frequentes, separando obrigatório × desejável.
   - **Meus maiores gaps**, por frequência.
   - **Onde estou forte** (frequente e já tenho): o que destacar nos CVs.
   - **Salário:** faixa das vagas que informam e das `expectativa_salarial`, comparada com o piso do config.
   - **Projetos sugeridos** (2–3): cada um cobrindo vários gaps de uma vez, com entregável concreto (repo, deploy, artigo) e por que responde às vagas registradas. Priorizar o que aparece nas vagas de maior `aderencia`.
5. Se eu pedir, salvar em `analises/AAAA-MM-DD-mercado.md`.

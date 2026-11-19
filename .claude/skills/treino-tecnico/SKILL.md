---
name: treino-tecnico
description: Monta uma lista de exercícios para a etapa técnica de acordo com a área e a vaga, e corrige minhas respostas no estilo entrevistador, com follow-ups "e se…". Usar quando eu passar para uma etapa técnica, pedir "exercícios para treinar", "me corrige", "simula um live coding".
---

# Treino técnico

## 1. Entender a etapa
- Ler a vaga (`vagas/descricoes/<id>.md`), as `notas` dela (o RH costuma dizer o formato), `perfil/config.md` e `entrevistas/aprendizados.md`.
- Se o formato não estiver claro, perguntar: live coding, take-home, system design, teste em plataforma (HackerRank, CoderPad, Codility…), quanto tempo, qual linguagem/dialeto, quem avalia.
- Perguntar quanto tempo tenho até a etapa e por dia, e montar um plano que caiba.

## 2. Montar a lista → `treino/<id>-exercicios.md`
Escolher pela área e pelo formato. Referência de plataformas (nomes de memória: se algum exercício não aparecer com esse nome, buscar pelo tema):

| área / formato | onde treinar |
|---|---|
| **Algoritmos e estruturas de dados** (qualquer área de engenharia) | LeetCode (listas "Top Interview 150", "LeetCode 75"), NeetCode, HackerRank |
| **Frontend: JavaScript/TypeScript** | GreatFrontEnd, BFE.dev, LeetCode "30 Days of JavaScript", Codewars (fundamentos), javascript.info (teoria) |
| **Frontend: componentes e UI** | GreatFrontEnd (componentes: accordion, tabs, autocomplete, modal), Frontend Mentor (layout e take-home) |
| **System design** | frontend: GreatFrontEnd; backend: "System Design Primer" (GitHub), ByteByteGo |
| **SQL** (dados, backend, fullstack) | DataLemur, LeetCode "SQL 50", StrataScratch |
| **Dados / analytics / engenharia de dados** | DataLemur, StrataScratch; para engenharia de dados, também modelagem dimensional, Spark e orquestração (exercícios em base local com DuckDB) |
| **Ciência de dados / ML** | StrataScratch (Python e estatística), casos de A/B, perguntas de modelagem com trade-offs |
| **Mobile, DevOps, QA, outras** | pesquisar as plataformas mais usadas para a stack da vaga e confirmar comigo antes de montar a lista |

Organizar em blocos de 30–45 min, do fundamento ao mais difícil, com ⭐ no que tem mais chance de cair, e um checklist `- [ ]` por exercício. No fim, o ritual (abaixo).

## 3. Corrigir no estilo entrevistador
Quando eu mandar uma resposta:
1. **Ler o enunciado de novo antes de corrigir** (nomes de saída, formato, filtros). Se eu não tiver mandado o enunciado e a correção depender dele, pedir. Não corrigir nome de coluna, função ou formato de cabeça.
2. Começar pelo que está certo, depois os erros em ordem de gravidade, com o porquê de cada um e uma regra curta para lembrar.
3. Mostrar a versão corrigida mexendo **só** no necessário.
4. Fazer um **"e se…"** (agora por mês, com duplicata, com NULL, com 10x mais dados, com erro na API, em outro navegador…), porque é isso que o entrevistador faz.
5. Se eu travar, dar o **esqueleto com lacunas** antes da resposta pronta.
6. Registrar o padrão aprendido e a pegadinha em `entrevistas/aprendizados.md` (seção da área), sem duplicar.
7. Marcar o exercício como feito na lista, com o tempo se eu disser.

Quizzes de múltipla escolha: alternativas com tamanho parecido (a certa não pode ser sempre a mais longa).

## 4. Ritual (vale para qualquer área)
1. Repetir o problema com as minhas palavras e tirar dúvidas (entradas, formato da saída, casos de borda).
2. Dizer o plano antes de codar.
3. Escrever o esqueleto (funções, CTEs, componentes) com comentários e só depois preencher.
4. Testar com um exemplo pequeno e com um caso de borda.
5. Começar pela solução mais simples que resolve; otimizar só se pedirem.
6. Receber feedback com "boa, faz sentido, vou ajustar aqui" e mexer só no trecho necessário.

## 5. Véspera e dia
- Na véspera, nada de assunto novo depois do meio da tarde. Dormir vale mais que um exercício a mais.
- No dia: no máximo 2 exercícios já feitos, refeitos de memória, e uma revisão leve de `entrevistas/<id>/cola.md`.
- Testar compartilhamento de tela antes (no Mac: Ajustes → Privacidade e Segurança → Gravação de Tela, e reiniciar o navegador). Compartilhar só a janela do editor.

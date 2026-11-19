---
name: montar-perfil
description: Entrevista guiada para montar (ou completar) o currículo mestre, a configuração da busca, os contatos e as histórias de entrevista. Usar no primeiro uso do repositório, quando eu pedir "montar meu perfil", "atualizar meu CV mestre", ou quando perfil/config.md não existir.
---

# Montar o perfil

O objetivo é conhecer a pessoa a fundo e fazê-la **brilhar** nos CVs e nas entrevistas. Vale gastar tempo: é a base de tudo no repositório.

## Como conduzir

- **Um bloco por vez**, com 3 a 5 perguntas por mensagem. Nunca despejar o questionário inteiro.
- **Salvar ao fim de cada bloco** (em `perfil/cv_mestre.md`, `perfil/config.md`, `perfil/contatos.md` ou `entrevistas/historias.md`). A entrevista pode parar e continuar em outro dia.
- No topo de `perfil/cv_mestre.md`, manter um checklist `## Progresso do onboarding` com os blocos feitos e os pendentes. Ao retomar, ler esse checklist e continuar de onde parou.
- **Cavar os números e o impacto.** Respostas como "melhorei a performance" pedem um "quanto? como você mediu? o que mudou para o usuário/negócio?". Se a pessoa não souber o número, registrar o impacto qualitativo e marcar `[confirmar número]`.
- **Nunca inventar.** O que for dedução minha fica `[confirmar]` até a pessoa confirmar.
- Tom de conversa, não de formulário. Elogiar o que for forte, e dizer com franqueza quando uma história ainda está fraca e precisa de mais detalhe.
- Antes de começar, perguntar quanto tempo a pessoa tem hoje e propor quais blocos cabem.

## Blocos

### 0. Documentos (começar por aqui)
- Pedir o CV atual (PDF ou texto), o **PDF do LinkedIn** (Perfil → Mais → Salvar em PDF), o link do GitHub e do portfólio, e o que mais existir (cartas de recomendação, avaliações de desempenho).
- PDFs vão para `perfil/originais/` (gitignored). Ler tudo e montar um **rascunho** de `perfil/cv_mestre.md` antes das perguntas, para que elas sirvam para aprofundar e não para recopiar.
- Se tiver GitHub, olhar os repositórios públicos e anotar os que valem destaque (com o porquê).

### 1. Busca e preferências → `perfil/config.md`
Copiar `perfil/config.exemplo.md` e preencher: áreas, senioridade-alvo, cidade, modelo de trabalho, exterior (cidadania, visto), idiomas, piso salarial, pretensão, formato do CV (LaTeX ou PDF; modelo próprio ou o do repositório; 1 ou 2 páginas), plataformas de treino que já usa.

### 2. Contatos e LGPD → `perfil/contatos.md` + `perfil/config.md`
- Perguntar **uma vez** e-mail, telefone, cidade, LinkedIn, GitHub e portfólio. Salvar em `perfil/contatos.md` (gitignored).
- Perguntar quais desses entram no CV e marcar em `perfil/config.md`. Explicar que o telefone pode ficar de fora do arquivo e ser colocado à mão na hora de enviar.

### 3. Formação
Graduação, pós, mestrado, doutorado (instituição, curso, ano, tema do TCC/dissertação), cursos e certificações relevantes (carga horária, ano), bootcamps.

### 4. Experiências (uma empresa por vez, da mais recente para a mais antiga)
Para cada uma: empresa, o que a empresa faz, cargo(s) e datas, tamanho do time, a quem respondia. Depois, para cada projeto ou responsabilidade relevante:
- **Contexto:** qual era o problema? para quem?
- **O que você fez** (e o que foi do time): decisões técnicas, stack, trade-offs.
- **Resultado:** número, prazo, adoção, economia, performance, qualidade. Como foi medido?
- **O que deu errado no caminho** e como resolveu (vira história de entrevista).

### 5. Projetos pessoais, open source, freelas
O que é, stack, link, quantos usuários ou estrelas, o que aprendeu.

### 6. Fora da área
Voluntariado, trabalhos anteriores em outras áreas, liderança em comunidades, ensino, eventos, palestras. Muitas vezes é aí que estão as melhores histórias de comunicação, liderança e resiliência.

### 7. Idiomas e skills → `perfil/minhas_skills.txt`
- Idiomas com nível real (já fez entrevista nesse idioma? trabalha nele?).
- Stack com nível honesto: **uso no dia a dia** · **já usei em produção** · **só estudei**. Em `minhas_skills.txt` entram só as duas primeiras, em nomes canônicos (ver `scripts/stack.py`).

### 8. Histórias de entrevista → `entrevistas/historias.md`
Montar com a pessoa, em formato **STAR** (situação, tarefa, ação, resultado) e com até 1 minuto falado cada:
1. **Pitch "fale sobre você"** (1 min), em português e, se for o caso, em inglês.
2. **Projeto principal** (o que mais orgulha), com o detalhe técnico pronto para quem quiser aprofundar.
3. **Algo que deu errado** (e o que aprendeu, sem culpar ninguém).
4. **Conflito ou discordância** com colega, gestor ou stakeholder.
5. **Prazo apertado ou escopo mudando.**
6. **Decisão técnica com trade-off** (o que escolheu, o que descartou, por quê).
7. **Liderança ou mentoria** (mesmo sem cargo de liderança).
8. **Feedback negativo recebido** e o que mudou.
9. **Por que quer sair do emprego atual** (versão positiva, sem falar mal da empresa) e a versão para quando pressionarem.
10. **Onde se vê em 3 anos.**
11. **Pretensão salarial:** como responder (perguntar a faixa primeiro; se pressionarem, dar uma faixa baseada no mercado, olhando o pacote todo).

Depois de escrever cada história, ler em voz alta para a pessoa (em texto) e perguntar: "soa como você? falta algum número?".

## Ao terminar
- Resumo curto: o que ficou forte, o que ficou `[confirmar]` e os blocos pendentes.
- Sugerir o próximo passo: `/buscar-vagas`.

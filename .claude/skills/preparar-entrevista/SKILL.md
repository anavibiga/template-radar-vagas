---
name: preparar-entrevista
description: Prepara uma entrevista (RH, técnica, comportamental, gestor, final): pesquisa a empresa e a banca, monta a cola, simula perguntas uma a uma e faz o debrief depois. Usar quando eu disser que tenho entrevista, pedir "me prepara para X", "simula a entrevista", "me testa", ou contar como foi.
---

# Preparar entrevista

## 1. Contexto
- Ler a vaga, as `notas` (formato, quem entrevista, o que o RH já disse), `perfil/cv_mestre.md`, `entrevistas/historias.md` e `entrevistas/aprendizados.md`.
- Perguntar o que faltar: data e hora, formato, duração, quem está na banca. Se eu colar o LinkedIn dos entrevistadores, usar para achar ganchos (formação, empresas anteriores, o que cada um deve avaliar).
- Pesquisar a empresa: produto, modelo de negócio, notícias recentes, relatos de processo seletivo (Glassdoor e afins). Dizer quando não achar nada específico, sem inventar.
- Atualizar `proximo_passo` da vaga em `vagas/vagas.csv`.

## 2. Cola → `entrevistas/<id>/cola.md`
- Checklist de antes de entrar (link, câmera, microfone, compartilhamento de tela, água, notificações em silêncio).
- Banca: quem é quem, o que deve avaliar e o gancho com o meu perfil.
- Formato e tempo de cada parte.
- Pitch de 1 min (e em inglês, se a vaga pedir).
- As histórias de `entrevistas/historias.md` que mais servem para essa vaga, adaptadas (cada uma em até 1 min).
- **Gaps com resposta honesta:** o que a vaga pede e eu não tenho, com a ponte para o que tenho de parecido. Nunca fingir experiência.
- Perguntas prováveis e **pegadinhas de RH** (por que sair, pretensão, outros processos, ponto fraco, onde se vê em 3 anos).
- **Minhas perguntas** (3–4, uma por entrevistador se der), sem repetir o que o RH já respondeu.
- Salário: o que dizer conforme a etapa (e o que não reabrir).
- Lembretes pessoais de `entrevistas/aprendizados.md`.

Se eu pedir uma página para consultar durante a entrevista (abas, celular), gerar um artifact com a cola.

## 3. Simulação
- **Uma pergunta por vez**, no tom da etapa. Esperar a minha resposta.
- Avaliar cada resposta: o que funcionou, o que faltou (número, resultado, concisão, clareza) e uma versão melhorada **usando só fatos meus**. Se eu disser algo novo, perguntar se pode entrar no CV mestre.
- Fazer a pergunta de pressão quando fizer sentido ("mas por que você, e não alguém com mais experiência em X?").
- No fim, listar as 3 respostas que mais precisam de treino.

## 4. Debrief (depois da entrevista)
Quando eu contar como foi:
- Registrar em `vagas/vagas.csv` (`status`, `data_status`, `proximo_passo` e um resumo datado em `notas`): quem estava, o que perguntaram, como respondi, o que disseram da vaga.
- Acrescentar em `entrevistas/<id>/cola.md` uma seção "Debrief" e preparar o gancho para a próxima etapa.
- Lições gerais (perguntas novas, pegadinhas, o que funcionou) vão para `entrevistas/aprendizados.md`.
- Se esqueci algo na entrevista, escrever a frase pronta para a próxima vez.
- Reprovação com feedback: registrar o feedback e, se for padrão, em "Aprendizado registrado" do `CLAUDE.md`.

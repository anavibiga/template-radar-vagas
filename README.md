# Radar de vagas

Um assistente de busca de emprego que roda no **Claude Code**: monta o seu currículo mestre numa entrevista guiada, busca e organiza vagas numa planilha, gera um CV adaptado para cada vaga e treina você para as etapas técnicas e as entrevistas.

Serve para qualquer área (frontend, backend, dados, mobile, produto…). A área e as preferências são definidas no primeiro uso.

> 🇬🇧 **In English:** a job-search assistant that runs on Claude Code. It interviews you to build a master résumé, finds and tracks job postings in a CSV, tailors a résumé to each posting (never inventing experience), drills you for technical rounds and prepares each interview, keeping a running file of lessons learned. Area-agnostic; the docs and prompts are in Brazilian Portuguese.

## Por que existe

Comecei este projeto como um experimento de agente com Claude Code aplicado a carreira: uma planilha de vagas e um currículo mestre que foram virando um assistente completo. Ele registra as vagas com a descrição inteira (elas saem do ar), calcula a aderência ao perfil, gera o CV de cada vaga sem inventar nada e, nas etapas técnicas, corrige no estilo entrevistador e guarda cada pegadinha num arquivo de aprendizados.

Este repositório é a versão genérica, para qualquer pessoa usar: sem dados pessoais e com o que era específico de uma área transformado em configuração.

O que está por trás do desenho:
- **Contexto estruturado:** o currículo mestre é a única fonte da verdade, e as skills dizem ao agente o que ler antes de agir.
- **Nunca inventar:** todo CV e toda resposta de entrevista sai de fatos confirmados; o que é incerto fica marcado `[confirmar]`.
- **Loop de aprendizado:** cada treino e cada entrevista real alimenta `entrevistas/aprendizados.md`, que é lido antes da próxima.
- **Privacidade (LGPD):** dados pessoais ficam fora do git e nunca vão para buscas externas.

## Instalação (5 min)

1. **Crie o seu repositório a partir deste template** (botão "Use this template" no GitHub) e deixe-o **privado**: ele vai guardar o seu CV e as suas notas de entrevista.
2. Clone e abra a pasta no terminal (ou no Cursor / VS Code).
3. Precisa só de **Python 3** (os scripts não têm dependências) e do **Claude Code**.
4. Opcional, para gerar o PDF do CV aqui mesmo: `brew install tectonic`. Sem isso, o CV sai em LaTeX e você compila no [Overleaf](https://www.overleaf.com).
5. Rode `claude` na pasta e digite **`/montar-perfil`**.

## O fluxo

```
/montar-perfil  →  /buscar-vagas  →  /nova-vaga  →  /gerar-cv  →  /treino-tecnico  →  /preparar-entrevista
   (1 vez)          (toda semana)     (registra)     (por vaga)    (etapa técnica)      (cada entrevista)
```

| comando | o que faz |
|---|---|
| `/montar-perfil` | Entrevista guiada, em blocos: documentos (CV, PDF do LinkedIn, GitHub), preferências, contatos, formação, cada experiência a fundo, projetos, trabalhos fora da área, idiomas, skills e as **histórias para entrevista** (pitch, projeto principal, algo que deu errado, conflito…). Dá para parar e continuar outro dia. |
| `/buscar-vagas` | Busca vagas na web de acordo com o seu perfil e coloca os links em `vagas/entrada.md`. |
| `/nova-vaga` | Registra uma vaga (link ou texto colado) com a descrição completa, a stack, a **aderência ao seu perfil** e a expectativa salarial. Sem argumento, processa a fila de `vagas/entrada.md`. Também atualiza o status ("passei para a técnica", "ficou para terça 10h"). |
| `/gerar-cv` | CV adaptado à vaga, só com fatos do seu currículo mestre. LaTeX ou PDF. |
| `/analisar-mercado` | O que as vagas pedem, os seus gaps e projetos que cobrem vários gaps de uma vez. |
| `/treino-tecnico` | Lista de exercícios para a etapa técnica (pela área e pelo formato) e correção no estilo entrevistador, com "e se…". |
| `/preparar-entrevista` | Pesquisa a empresa e a banca, monta a cola, simula as perguntas uma a uma e faz o debrief depois. |

Para ver o andamento: `python3 scripts/painel.py` (status das vagas, próximos passos e o que está parado sem retorno).

## Empilhar vagas

Viu uma vaga? Cole o link (ou o texto) em **`vagas/entrada.md`**. Quando tiver um tempo, rode `/nova-vaga` e ele registra a fila inteira.

## De onde vêm as vagas

| fonte | como entra |
|---|---|
| Páginas de carreira no **Greenhouse, Lever, Ashby, Gupy, inhire** | O `/buscar-vagas` acha e o `/nova-vaga` lê sozinho. São as melhores fontes. |
| Sites de vaga remota (Remotar, Himalayas, Built In e afins) | Em geral, a busca acha e lê. |
| **LinkedIn** | Às vezes dá para ler a vaga pelo link; quando não der, cole o texto. |
| **Indeed, Glassdoor** | Bloqueiam leitura automática: cole o texto, ou procure a vaga no site da empresa. |
| Indicação e vaga sem anúncio | Cole o que souber (mensagem do recrutador, cargo) em `vagas/entrada.md`. |
| Sites pagos (assinatura para ver vagas) | Não são necessários. Se usar algum, cole o texto da vaga. |

## Renda extra

Trabalho por hora ou projeto (freela, avaliar e treinar IA, dar aula, mentoria) vai para `vagas/renda_extra.csv`, separado das vagas de emprego e fora da análise de mercado. É só registrar com `/nova-vaga` normalmente: ele identifica e pergunta na dúvida.

## Seus dados (LGPD)

- Contatos (e-mail, telefone…) ficam em `perfil/contatos.md` e preferências em `perfil/config.md`. Os dois estão no `.gitignore` e não sobem para o GitHub. Os PDFs também não.
- O `/montar-perfil` pergunta **uma vez** quais contatos entram no CV. O telefone pode ficar de fora e ser colocado à mão na hora de enviar.
- As buscas na web nunca levam o seu nome, e-mail ou CV.
- Mesmo assim, mantenha o repositório **privado**: o currículo mestre e as notas de entrevista são pessoais.

## Estrutura

```
perfil/        currículo mestre, skills, config e contatos (os dois últimos não vão para o git)
vagas/         entrada.md (fila), vagas.csv, arquivo.csv, renda_extra.csv, descricoes/
cv/            template/cv.tex e gerados/<id>/cv.tex
entrevistas/   historias.md, aprendizados.md e <id>/cola.md
treino/        listas de exercícios e progresso
analises/      relatórios (stack, mercado)
scripts/       stack.py e painel.py
```

As regras que o Claude segue (nunca inventar experiência, colunas da planilha, critérios) estão no `CLAUDE.md`. Edite à vontade.

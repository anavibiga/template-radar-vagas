# Radar de vagas

Repositório pessoal para:
1. montar um **currículo mestre** completo a partir de conversas e documentos;
2. buscar e registrar vagas numa planilha (`vagas/vagas.csv`), com a descrição completa, a aderência ao perfil e o status de cada uma;
3. gerar um currículo adaptado a cada vaga (LaTeX, com opção de PDF);
4. treinar para as etapas técnicas e preparar as entrevistas, acumulando os aprendizados.

O template não é de nenhuma área específica. Área, senioridade, cidade, piso salarial e o que entra no CV vêm de `perfil/config.md`.

**Primeiro uso:** se `perfil/config.md` não existir, sugerir rodar `/montar-perfil` antes de qualquer outra coisa.

## Skills

| comando | quando usar |
|---|---|
| `/montar-perfil` | primeiro uso, ou para completar o perfil (entrevista guiada) |
| `/buscar-vagas` | procurar vagas novas na web e jogar os links em `vagas/entrada.md` |
| `/nova-vaga` | registrar uma vaga (link ou texto colado) ou processar a fila de `vagas/entrada.md` |
| `/gerar-cv` | CV adaptado para uma vaga registrada |
| `/analisar-mercado` | o que as vagas pedem, gaps e projetos sugeridos |
| `/treino-tecnico` | exercícios para a etapa técnica, com correção no estilo entrevistador |
| `/preparar-entrevista` | cola, simulação, perguntas para fazer e debrief depois da entrevista |

## Arquivos

- `perfil/config.md`: preferências da busca (área, senioridade, cidade, modelo, piso, idiomas, contatos no CV). **Gitignored.**
- `perfil/contatos.md`: e-mail, telefone, LinkedIn, GitHub, portfólio. **Gitignored.**
- `perfil/cv_mestre.md`: inventário completo de experiências, projetos, formação e skills. **Fonte da verdade** para qualquer CV.
- `perfil/minhas_skills.txt`: skills que tenho, uma por linha, em nomes canônicos (ver `scripts/stack.py`).
- `perfil/originais/`: CVs e PDFs enviados no onboarding. **Gitignored.**
- `vagas/entrada.md`: fila de links e textos de vagas a registrar.
- `vagas/vagas.csv`: a planilha. Uma linha por vaga.
- `vagas/arquivo.csv`: vagas fora do foco (aderência < 50, descartadas, duplicadas). Continuam contando na análise de mercado.
- `vagas/renda_extra.csv`: renda extra em paralelo ao emprego (trabalho por hora ou projeto, freela, avaliar/treinar IA, dar aula, mentoria). Mesmas colunas, com `area` = o tipo (`freela`, `ia-por-hora`, `aulas`, `mentoria`…). Fica fora da análise de mercado.
- `vagas/descricoes/<id>.md`: texto integral da vaga (as vagas saem do ar).
- `cv/template/cv.tex`: template LaTeX base. `cv/gerados/<id>/cv.tex`: CV adaptado.
- `entrevistas/historias.md`: histórias no formato STAR e o pitch, construídos no `/montar-perfil`.
- `entrevistas/aprendizados.md`: pegadinhas e lições acumuladas em treinos e entrevistas reais.
- `entrevistas/<id>/`: cola e debrief de cada processo.
- `treino/`: listas de exercícios e o progresso.
- `analises/`: relatórios gerados.
- `scripts/stack.py`: frequência de stack e gaps. `scripts/painel.py`: status das vagas e próximos passos.

## Colunas de `vagas.csv`

| coluna | valores |
|---|---|
| `id` | `AAAA-MM-DD-empresa-cargo` em slug (minúsculas, hífens) |
| `data_coleta` | `AAAA-MM-DD` |
| `empresa`, `cargo`, `local`, `link`, `fonte` | texto livre. `fonte` é o site em slug (`linkedin`, `greenhouse`, `gupy`, `indicacao`…) |
| `area` | um dos valores listados em `perfil/config.md` (ex.: `frontend`, `fullstack`, `engenharia-de-dados`, `analytics`) |
| `senioridade` | `estagio` · `junior` · `pleno` · `senior` · `especialista` · `lideranca` |
| `modelo` | `remoto` · `hibrido` · `presencial` |
| `pais` | país da empresa/contratação em slug. Remoto para empresa de fora → país da empresa |
| `stack_obrigatoria`, `stack_desejavel` | nomes canônicos separados por `; ` |
| `idiomas` | ex.: `ingles-avancado` |
| `salario` | como aparece na vaga, vazio se não informado |
| `expectativa_salarial` | faixa sugerida com base em pesquisa (Glassdoor, levels.fyi, guias salariais), com moeda, período e regime (ex.: `R$ 11–14k/mês CLT`). Fontes em `notas`. Não sobrescrever se já preenchido |
| `aderencia` | 0–100, quanto o perfil atende |
| `status` | `interesse` · `aplicada` · `triagem` · `tecnica` · `final` · `oferta` · `recusada` · `descartada` |
| `data_status` | data da última mudança de status |
| `proximo_passo` | o que vem e quando (ex.: `2026-11-24 10h: técnica com o time`). Vazio se nada pendente |
| `cv` | caminho do CV usado |
| `notas` | observações, feedback recebido, resumo de cada etapa (com data) |

Editar o CSV sempre com o módulo `csv` do Python, nunca à mão (aspas em campos com vírgula).

## Regras

- **Nunca inventar** experiência, ferramenta, número ou resultado no CV ou nas respostas de entrevista. Só reorganizar, reescrever e dar ênfase ao que está em `perfil/cv_mestre.md`. O que a vaga pede e não tenho vai para a análise de gaps. Informação incerta fica marcada `[confirmar]` até eu confirmar.
- **Dados pessoais (LGPD):** contatos só em `perfil/contatos.md`. No CV entram só os contatos marcados em `perfil/config.md`. Nunca mandar dados pessoais para sites externos (buscas, APIs). Recomendado manter este repositório **privado**.
- **Antes de apagar ou sobrescrever** qualquer arquivo, olhar o conteúdo e confirmar comigo. Nunca encadear uma checagem com `rm` no mesmo comando.
- Stack sempre em nomes canônicos (minúsculas). Tecnologia nova → acrescentar o alias em `ALIASES` de `scripts/stack.py`.
- CVs e textos em pt-BR, exceto quando a vaga for em outro idioma (aí o CV acompanha a vaga).
- Commits só quando eu pedir. O push é feito por mim.

## Critérios de busca

Estão em `perfil/config.md` (área, senioridade, cidade, modelo de trabalho, piso salarial). Renda extra (por hora ou projeto) tem critério próprio: valor por hora, horas por semana e se é compatível com o emprego atual (contrato, conflito de interesse). O piso é referência, não filtro: abaixo dele, avisar e mostrar a conta (CLT × PJ × exterior), sem descartar se houver outro atrativo. Inelegível de verdade (presencial fora da cidade, exige visto que não tenho, vaga encerrada, fora da área) → `descartada`, com o motivo nas notas, e mover para `arquivo.csv`.

## Aprendizado registrado

(Preencher com o tempo: feedbacks de processos, o que funcionou, o que reprovou e por quê. Detalhes de entrevista ficam em `entrevistas/aprendizados.md`.)

---
name: nova-vaga
description: Registra vagas na planilha vagas/vagas.csv, com o texto integral em vagas/descricoes. Sem argumentos, processa a fila de vagas/entrada.md. Usar quando eu colar um link ou a descrição de uma vaga, pedir para "registrar/adicionar vaga" ou "processar a fila". Também atualiza status e próximos passos ("passei para a técnica", "a entrevista ficou para terça").
---

# Registrar vaga

## Com argumento (link ou texto) ou sem argumento (fila)
Sem argumento: ler a seção "Pendentes" de `vagas/entrada.md` e registrar cada item. Ao final, tirar da fila **só** os itens registrados (ou marcados como duplicados) e deixar os que falharam, com o motivo ao lado.

## Passos para cada vaga
1. **Obter o texto integral.** Se for link, buscar a página. Se não der para ler (login, bloqueio), pedir o texto colado. Nunca registrar a partir de resumo.
   - Caminhos que costumam funcionar: dados estruturados `JobPosting` (JSON-LD) na página; APIs do Greenhouse (`boards-api.greenhouse.io/v1/boards/<empresa>/jobs/<id>`), Lever (`api.lever.co/v0/postings/<empresa>/<id>`) e Ashby (`api.ashbyhq.com/posting-api/job-board/<empresa>`); LinkedIn guest (`linkedin.com/jobs-guest/jobs/api/jobPosting/<id>`).
   - Indeed costuma bloquear: pedir o link do site da empresa ou o texto. Agregador que só mostra resumo: buscar o anúncio original.
2. **Duplicada?** Comparar link, e empresa + cargo, com `vagas/vagas.csv` e `vagas/arquivo.csv`. Se já existir, avisar e perguntar se é atualização.
3. **`id`:** `AAAA-MM-DD-empresa-cargo` em slug, com a data de hoje.
4. **Salvar `vagas/descricoes/<id>.md`** com o cabeçalho abaixo e o texto da vaga sem cortes:
   ```
   ---
   id: <id>
   empresa: ...
   cargo: ...
   link: ...
   data_coleta: AAAA-MM-DD
   ---
   ```
5. **Preencher as colunas** (definições no `CLAUDE.md`):
   - `stack_obrigatoria` × `stack_desejavel`: pelo que a vaga diz ("requisitos" × "diferenciais/nice to have"). Nomes canônicos de `ALIASES` em `scripts/stack.py`; acrescentar alias novo se aparecer. Incluir competências não técnicas que a vaga cobra explicitamente (ex.: `ingles`, `lideranca-tecnica`, `comunicacao`).
   - `area`: um dos valores de `perfil/config.md`, pelo peso real da vaga e não só pelo título. Se nenhum servir, usar o mais próximo e dizer.
   - `modelo`, `local`, `pais`: vaga remota de empresa estrangeira fica com o país da empresa; anotar em `notas` "aceita Brasil", "contractor/PJ", fuso.
   - `aderencia` (0–100): comparar com `perfil/cv_mestre.md` e `perfil/minhas_skills.txt`, com peso maior para os obrigatórios.
   - `salario`: só o que a vaga informa.
   - `expectativa_salarial`: pesquisar na web (Glassdoor, levels.fyi, guias salariais) para cargo + senioridade + país. Fontes em `notas`. Sem fonte confiável, deixar vazio e dizer.
   - `status`: `interesse`. `data_status`: hoje.
6. **Gravar** a linha com o módulo `csv` do Python. Aderência < 50 ou inelegível → vai direto para `vagas/arquivo.csv`, com o motivo.
   - **Renda extra** (por hora, por projeto, freela, avaliar/treinar IA, aulas, mentoria) → `vagas/renda_extra.csv`, com `area` = o tipo, o valor por hora ou projeto em `salario` e, em `notas`, horas por semana, forma de pagamento (PJ, plataforma, dólar) e se conflita com o emprego atual. Na dúvida se é emprego ou renda extra, perguntar.
7. **Responder** em poucas linhas por vaga: área, aderência, o que já cubro, o que falta, se é elegível e como fica em relação ao piso (mostrar a conta se for PJ ou exterior).

## Atualizar uma vaga existente
Quando eu contar novidades ("apliquei", "me chamaram", "ficou para terça 10h", "reprovei"):
- Atualizar `status` e `data_status` (só se o status mudou), `proximo_passo` (com data e hora) e acrescentar um resumo datado em `notas`, sem apagar o que já existe.
- Feedback recebido vai em `notas` e, se for lição geral, também em `entrevistas/aprendizados.md`.
- Se mudou para `tecnica` ou `final`, sugerir `/treino-tecnico` ou `/preparar-entrevista`.

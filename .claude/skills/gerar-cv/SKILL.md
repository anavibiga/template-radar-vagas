---
name: gerar-cv
description: Gera um currículo adaptado a uma vaga registrada, a partir do currículo mestre, em LaTeX (e PDF, se configurado). Usar quando eu pedir "CV para a vaga X", "adaptar currículo" ou similar.
---

# Gerar CV adaptado

Entrada: o `id` da vaga (ou empresa/cargo para achar o `id` em `vagas/vagas.csv`).

1. **Ler** `vagas/descricoes/<id>.md`, a linha da vaga em `vagas/vagas.csv`, `perfil/cv_mestre.md`, `perfil/config.md` (formato, páginas, contatos no CV), `perfil/contatos.md` e `cv/template/cv.tex`.
   - Se `perfil/config.md` não disser o formato, perguntar **uma vez** (LaTeX ou PDF? modelo do repositório ou o próprio?) e salvar a resposta lá.
2. **Mapear** cada requisito da vaga para evidências no CV mestre: requisito → evidência (ou "sem evidência").
3. **Escolher o ângulo** pela vaga: o que ela mais pesa (profundidade técnica, produto e impacto, liderança, comunicação com negócio). Abrir o resumo e os bullets por esse ângulo.
4. **Escrever `cv/gerados/<id>/cv.tex`** a partir do template:
   - Páginas conforme o config. O que mais vende fica na primeira página.
   - Usar o vocabulário da vaga quando ele descreve com honestidade algo do CV mestre.
   - **Proibido** incluir ferramenta, experiência, número ou resultado que não esteja no CV mestre. Requisito sem evidência fica de fora.
   - **Contatos:** só os marcados em `perfil/config.md`, com os dados de `perfil/contatos.md`. Os não marcados ficam comentados no `.tex`.
   - Idioma do CV = idioma da vaga.
   - Escapar caracteres especiais do LaTeX (`& % $ # _ { }`).
5. **PDF**, se o config pedir: compilar com `tectonic cv.tex` (ou `latexmk -pdf`) dentro de `cv/gerados/<id>/`. Sem compilador, sugerir `brew install tectonic` ou o Overleaf. Corrigir erros e conferir o número de páginas. O PDF é gitignored (tem dados pessoais).
6. **Atualizar** a coluna `cv` da vaga com o caminho do `.tex` (módulo `csv`).
7. **Responder** com o ângulo escolhido, os requisitos sem evidência (para eu decidir se vale um projeto ou estudo) e o caminho do arquivo.

---
name: buscar-vagas
description: Procura vagas novas na web de acordo com perfil/config.md e coloca os links encontrados em vagas/entrada.md, sem duplicar o que já está registrado. Usar quando eu pedir "buscar vagas", "achar vagas de X", "o que tem de vaga nova".
---

# Buscar vagas

1. **Ler** `perfil/config.md` (áreas, senioridade, cidade, modelo, exterior), `perfil/minhas_skills.txt` e os links já existentes em `vagas/vagas.csv`, `vagas/arquivo.csv` e `vagas/entrada.md`, para não sugerir duplicada.
   - Se eu passar um recorte ("só remoto", "só empresas de fora", "React sênior"), ele vale por cima do config.
2. **Montar as buscas.** Termos em português e em inglês (o cargo, os sinônimos e as stacks principais), combinados com:
   - **Sites de vaga que deixam ler a página:** `site:job-boards.greenhouse.io`, `site:boards.greenhouse.io`, `site:jobs.lever.co`, `site:jobs.ashbyhq.com`, `site:gupy.io`, `site:inhire.app`, sites de vaga remota (Remotar, Himalayas, Built In e afins).
   - **Empresas-alvo**, se eu tiver uma lista em `vagas/empresas-alvo.md`: buscar direto no quadro de vagas delas (APIs abaixo).
   - Filtro de data quando o buscador permitir (últimos 7–14 dias). Vaga antiga quase sempre já fechou.
3. **APIs públicas de quadros de vagas** (devolvem a lista inteira de uma empresa):
   - Greenhouse: `https://boards-api.greenhouse.io/v1/boards/<empresa>/jobs?content=true`
   - Lever: `https://api.lever.co/v0/postings/<empresa>?mode=json`
   - Ashby: `https://api.ashbyhq.com/posting-api/job-board/<empresa>`
   - Se uma delas parar de responder, avisar e seguir pelas buscas.
4. **Filtrar** pelo config: área, senioridade (± um nível), modelo e cidade. Descartar na hora o que é claramente inelegível (presencial em outra cidade, exige visto que não tenho), mas listar quantos foram descartados e por quê.
5. **Acrescentar** os links que sobraram em `vagas/entrada.md`, na seção "Pendentes", um por linha, com um comentário curto: `- <link> <!-- empresa · cargo · modelo -->`.
6. **Responder** com uma tabela curta (empresa · cargo · modelo · por que parece boa), quantas foram para a fila e quantas descartei. Perguntar se quero rodar `/nova-vaga` para registrar a fila agora.

## Onde a busca não chega (dizer isso quando fizer sentido)
- **LinkedIn, Indeed e Glassdoor** pedem login ou bloqueiam leitura automática. Vaga vista lá: colar o **texto** (ou o link da página de carreira da empresa) em `vagas/entrada.md`.
- **Indicações e vagas sem anúncio:** colar o que se sabe (mensagem do recrutador, nome do cargo) direto em `vagas/entrada.md`.
- Nunca enviar dados pessoais (nome, e-mail, CV) nas buscas.

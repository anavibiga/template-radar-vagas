"""Frequência de stack nas vagas e gaps em relação ao meu perfil.

Uso:
    python3 scripts/stack.py                       # todas as vagas
    python3 scripts/stack.py --area frontend
    python3 scripts/stack.py --senioridade pleno --saida analises/stack.md

Conta vagas.csv + arquivo.csv. renda_extra.csv fica de fora.
"""

import argparse
import csv
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
VAGAS = RAIZ / "vagas" / "vagas.csv"
ARQUIVO = RAIZ / "vagas" / "arquivo.csv"  # fora do foco, mas continua contando para o mercado
MINHAS_SKILLS = RAIZ / "perfil" / "minhas_skills.txt"

# alias -> nome canônico. Acrescentar aqui quando aparecer variação nova.
ALIASES = {
    # linguagens
    "js": "javascript",
    "ecmascript": "javascript",
    "ts": "typescript",
    "py": "python",
    "python3": "python",
    "golang": "go",
    "c#": "csharp",
    "c++": "cpp",
    # frontend
    "react.js": "react",
    "reactjs": "react",
    "next.js": "nextjs",
    "next": "nextjs",
    "vue.js": "vue",
    "vuejs": "vue",
    "angularjs": "angular",
    "svelte.js": "svelte",
    "tailwind css": "tailwind",
    "tailwindcss": "tailwind",
    "styled components": "styled-components",
    "html5": "html",
    "css3": "css",
    "sass": "scss",
    "redux toolkit": "redux",
    "react query": "tanstack-query",
    "tanstack query": "tanstack-query",
    "react native": "react-native",
    "web accessibility": "acessibilidade",
    "a11y": "acessibilidade",
    "accessibility": "acessibilidade",
    "core web vitals": "web-performance",
    "web performance": "web-performance",
    "design system": "design-system",
    "storybook.js": "storybook",
    "micro frontends": "micro-frontends",
    "microfrontends": "micro-frontends",
    # testes
    "react testing library": "testing-library",
    "testing library": "testing-library",
    "vitest": "vitest",
    "cypress.io": "cypress",
    "unit tests": "testes-unitarios",
    "testes unitários": "testes-unitarios",
    "e2e": "testes-e2e",
    "end-to-end tests": "testes-e2e",
    # backend
    "node": "nodejs",
    "node.js": "nodejs",
    "express.js": "express",
    "nest.js": "nestjs",
    "spring boot": "spring",
    "fast api": "fastapi",
    "rest api": "rest",
    "restful": "rest",
    "graph ql": "graphql",
    "microservices": "microsservicos",
    "microsserviços": "microsservicos",
    # dados
    "postgres": "postgresql",
    "sql server": "sql-server",
    "mongo": "mongodb",
    "pyspark": "spark",
    "apache spark": "spark",
    "apache airflow": "airflow",
    "apache kafka": "kafka",
    "data modeling": "data-modeling",
    "modelagem de dados": "data-modeling",
    "power bi": "powerbi",
    "big query": "bigquery",
    "scikit-learn": "sklearn",
    "machine learning": "ml",
    "a/b testing": "ab-testing",
    "teste a/b": "ab-testing",
    "statistics": "estatistica",
    "estatística": "estatistica",
    # IA
    "llms": "llm",
    "large language models": "llm",
    "genai": "ia-generativa",
    "generative ai": "ia-generativa",
    "retrieval augmented generation": "rag",
    "ai agents": "agentes-ia",
    "agentes de ia": "agentes-ia",
    "prompt engineering": "prompt-engineering",
    # cloud e devops
    "amazon web services": "aws",
    "google cloud": "gcp",
    "google cloud platform": "gcp",
    "microsoft azure": "azure",
    "k8s": "kubernetes",
    "ci/cd": "ci-cd",
    "cicd": "ci-cd",
    "github actions": "github-actions",
    "infrastructure as code": "iac",
    # outros
    "english": "ingles",
    "inglês": "ingles",
    "scrum": "agil",
    "kanban": "agil",
    "agile": "agil",
    "system design": "system-design",
}


def normaliza(item: str) -> str:
    item = item.strip().lower()
    return ALIASES.get(item, item)


def separa(celula: str) -> set[str]:
    return {normaliza(i) for i in (celula or "").split(";") if i.strip()}


def carrega_vagas(area: str | None, senioridade: str | None) -> list[dict]:
    vagas = []
    for arq in (VAGAS, ARQUIVO):
        if arq.exists():
            with arq.open(encoding="utf-8") as f:
                vagas += [v for v in csv.DictReader(f) if (v.get("id") or "").strip()]
    if area:
        vagas = [v for v in vagas if v["area"] == area]
    if senioridade:
        vagas = [v for v in vagas if v["senioridade"] == senioridade]
    return vagas


def carrega_skills() -> set[str]:
    if not MINHAS_SKILLS.exists():
        return set()
    linhas = MINHAS_SKILLS.read_text(encoding="utf-8").splitlines()
    return {normaliza(l) for l in linhas if l.strip() and not l.startswith("#")}


def relatorio(vagas: list[dict], minhas: set[str], filtros: str) -> str:
    n = len(vagas)
    if n == 0:
        return "Nenhuma vaga com esses filtros.\n"

    obrig = Counter(s for v in vagas for s in separa(v["stack_obrigatoria"]))
    desej = Counter(s for v in vagas for s in separa(v["stack_desejavel"]))
    total = obrig + desej

    linhas = [f"# Stack pedida nas vagas{filtros}", "", f"{n} vagas analisadas.", ""]
    linhas += ["## Tecnologias", "",
               "| stack | obrigatória | desejável | % das vagas | tenho? |",
               "|---|---:|---:|---:|:---:|"]
    for s, qtd in total.most_common():
        tenho = "✅" if s in minhas else "❌"
        linhas.append(f"| {s} | {obrig[s]} | {desej[s]} | {qtd / n:.0%} | {tenho} |")

    gaps = [(s, q) for s, q in total.most_common() if s not in minhas]
    linhas += ["", "## Maiores gaps (o que mais aparece e eu não tenho)", ""]
    linhas += [f"- **{s}**: {q / n:.0%} das vagas" for s, q in gaps[:10]] or ["- nenhum"]

    for titulo, col in [("Área", "area"), ("Senioridade", "senioridade"),
                        ("Modelo", "modelo"), ("País", "pais")]:
        cont = Counter(v.get(col) or "?" for v in vagas)
        linhas += ["", f"## {titulo}", ""] + [f"- {k}: {q}" for k, q in cont.most_common()]
    return "\n".join(linhas) + "\n"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--area")
    p.add_argument("--senioridade")
    p.add_argument("--saida", help="arquivo .md para salvar o relatório")
    args = p.parse_args()

    filtros = "".join(f" ({k}: {v})" for k, v in
                      [("área", args.area), ("senioridade", args.senioridade)] if v)
    texto = relatorio(carrega_vagas(args.area, args.senioridade), carrega_skills(), filtros)

    if args.saida:
        Path(args.saida).write_text(texto, encoding="utf-8")
        print(f"salvo em {args.saida}")
    else:
        print(texto)


if __name__ == "__main__":
    main()

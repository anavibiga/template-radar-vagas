"""Painel rápido: quantas vagas em cada status e os próximos passos com data.

Uso:
    python3 scripts/painel.py
"""

import csv
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ARQUIVOS = {
    "vagas": RAIZ / "vagas" / "vagas.csv",
    "renda extra": RAIZ / "vagas" / "renda_extra.csv",
}
ORDEM = ["interesse", "aplicada", "triagem", "tecnica", "final", "oferta", "recusada", "descartada"]
ATIVOS = {"aplicada", "triagem", "tecnica", "final", "oferta"}


def carrega(arq: Path) -> list[dict]:
    if not arq.exists():
        return []
    with arq.open(encoding="utf-8") as f:
        return [v for v in csv.DictReader(f) if (v.get("id") or "").strip()]


def main() -> None:
    for nome, arq in ARQUIVOS.items():
        vagas = carrega(arq)
        print(f"\n## {nome} ({len(vagas)})")
        if not vagas:
            continue
        cont = Counter(v["status"] or "?" for v in vagas)
        chaves = [s for s in ORDEM if s in cont] + [s for s in cont if s not in ORDEM]
        print("  " + " · ".join(f"{s}: {cont[s]}" for s in chaves))

        passos = sorted((v for v in vagas if v.get("proximo_passo")), key=lambda v: v["proximo_passo"])
        if passos:
            print("\n  Próximos passos:")
            for v in passos:
                print(f"  - {v['proximo_passo']}  |  {v['empresa']} · {v['cargo']}")

        sem_passo = [v for v in vagas if v["status"] in ATIVOS and not v.get("proximo_passo")]
        if sem_passo:
            print("\n  Em andamento sem próximo passo (cobrar retorno?):")
            for v in sorted(sem_passo, key=lambda v: v["data_status"]):
                print(f"  - {v['empresa']} · {v['cargo']} ({v['status']} desde {v['data_status']})")


if __name__ == "__main__":
    main()

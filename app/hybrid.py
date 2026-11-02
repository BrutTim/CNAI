"""Kennungen exakt im Text suchen, andere Fragen per RAG beantworten."""

import re
import time

import rag
from wissen import Treffer, dokumente


def kennungen(frage: str) -> list[str]:
    """Erkennt Raum-/Formularnummern und normalisiert Paragraph-Angaben."""
    begriffe = re.findall(r"\b[A-Z]+-\d+\b", frage, flags=re.IGNORECASE)
    for nummer in re.findall(r"(?:§\s*|\bParagraph\s+)(\d+)\b", frage, flags=re.IGNORECASE):
        begriffe.append(f"§ {nummer}")
    return begriffe


def abrufen(frage: str, k: int = rag.K) -> tuple[list[Treffer], float]:
    start = time.perf_counter()
    begriffe = kennungen(frage)
    treffer = []
    if begriffe:
        muster = [
            re.compile(r"(?<!\w)" + re.escape(begriff).replace(r"\ ", r"\s*") + r"(?!\w)", re.IGNORECASE)
            for begriff in begriffe
        ]
        for datei, text in dokumente().items():
            for abschnitt in rag.zerlege(datei, text):
                wert = sum(len(m.findall(abschnitt.text)) for m in muster)
                if wert:
                    treffer.append(Treffer(datei, abschnitt.text, wert))
        treffer.sort(key=lambda t: t.wert, reverse=True)
        treffer = treffer[:k]

    if not treffer:
        treffer = rag.suche(frage, k)
    return treffer, time.perf_counter() - start

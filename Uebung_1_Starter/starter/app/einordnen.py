"""Teil D: Anfragen an den Campus-Assistenten strukturiert einordnen.

Das Modell soll aus einer Mail drei Dinge herauslesen: das Anliegen,
den Studiengang und eine Frist. Das Ergebnis verarbeitet ein Programm
weiter, es muss also immer die gleiche Form haben.

Aufruf:
    docker compose run --rm app einordnen.py
    docker compose run --rm app einordnen.py "Eure eigene Mail"

Eure Aufgaben stehen bei den TODO-Kommentaren.
"""

import json
import sys
from typing import Literal
import warnings

from pydantic import BaseModel, ValidationError, field_validator


from llm import MODEL, client

SYSTEM_PROMPT = (
    "Du ordnest Mails von Studierenden an die HTWG Konstanz ein. "
    "Antworte ausschließlich mit JSON. "
    "anliegen ist pruefung, mensa, bibliothek oder sonstiges. "
    "studiengang ist das Kürzel (z. B. AIN, WIN, MSI) oder null. "
    "frist ist die Frist aus der Mail, so wie sie dort steht, oder null."
)


class Anfrage(BaseModel):
    anliegen: Literal["pruefung", "mensa", "bibliothek", "sonstiges"]
    studiengang: Literal["AIN", "WIN", "MSI"] | None
    frist: str | None

    @field_validator("studiengang", "frist", mode="after")
    @classmethod
    def null_Strings_to_None(cls,value: str):
        if (value == "null" or value == "None"):
            return None
        return value



def schema_von(modell: type[BaseModel]) -> dict:
    """Verpackt das JSON-Schema einer Pydantic-Klasse für response_format."""
    return {
        "type": "json_schema",
        "json_schema": {
            "name": modell.__name__.lower(),
            "schema": modell.model_json_schema(),
        },
    }

def frist_prüfen(frist: str|None, mail: str):
    if frist is None:
        return None
    
    if frist.strip().casefold() not in mail.casefold():
        warnings.warn(f"Frist '{frist}' nicht in Mail gefunden: {mail}")
        return None
    
    return frist

def einordnen(mail: str, versuche: int = 3) -> Anfrage:
    """Fragt das Modell und gibt eine geprüfte Anfrage zurück."""
    nachricht = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": mail},
    ]


    for versuch in range(1, 4):
        response = client.chat.completions.create(
            model=MODEL,
            messages=nachricht,
            temperature=0.0,                #2.5 liefert zu ausführliche Frist, 1.2 und 0.0 beide mehrmals 7/8, wähle 1.2 da 0.0 bei wiederhoöung gleichbleibt
            response_format=schema_von(Anfrage),
        )

        json_string = response.choices[0].message.content
        try:
            ergebnis = Anfrage.model_validate_json(json_string)
            ergebnis.frist = frist_prüfen(ergebnis.frist, mail)
            return ergebnis
        except ValidationError as e:
            print(f"Fehler bei der Validierung (Versuch {versuch}): {e}")
            if versuch == versuche:
                raise RuntimeError("Maximale Anzahl an Versuchen erreicht.")



def auswerten() -> None:
    """Ordnet alle Test-Mails ein und vergleicht mit dem Erwarteten."""
    with open("mails.json", encoding="utf-8") as f:
        faelle = json.load(f)
    richtig = 0
    for fall in faelle:
        ergebnis = einordnen(fall["mail"])
        erwartet = fall["erwartet"]

        passt = ergebnis.anliegen == erwartet["anliegen"]

        if passt:
            richtig += 1
            print("✓ Anliegen stimmt überein.")
        else:
            print("✗ Anliegen stimmt nicht überein.")

        print(f"\nMail: {fall['mail']}")
        print(f"Ergebnis: {ergebnis.model_dump_json(indent=2)}")
        print(f"Erwartet: {json.dumps(erwartet, indent=2)}")
        print(ergebnis.frist is None)        # in Json wird Python None zu null, bei anschliessendem print kommt also null raus -> dieser vergleich zeigt ist

    print(f"\n{richtig} von {len(faelle)} Anliegen richtig ({MODEL})")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(einordnen(" ".join(sys.argv[1:])).model_dump_json(indent=2))
    else:
        auswerten()

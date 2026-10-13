# CNAI

## Teil 1 · Modellaufruf

Bei dem starte mit dem Command, "docker compose run --rm app hallo_llm.py "Wie melde ich mich zu einer Prüfung an?", passiert folgendes.
Der Container starter-ollama-1 wird gestartet.  Darauf folgt Der Container starter-modell-laden-1, der jedoch nur schaut ob die modelle geladen wurden und wenn dem so ist ein "service_completed_successfully" ausgibt. Wenn das passiert ist, wird eine temporärer Container  starter-app-run-... erstellt. Der liest dann in der .env welches Model Verwendet wird und setzt die Umgebungsvariablen. Und führt das Programm hallo_llm.py aus.




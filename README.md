# CNAI

## Teil 1 · Modellaufruf

Bei dem starte mit dem Command, "docker compose run --rm app hallo_llm.py "Wie melde ich mich zu einer Prüfung an?", passiert folgendes.
Der Container starter-ollama-1 wird gestartet.  Darauf folgt Der Container starter-modell-laden-1, der jedoch nur schaut ob die modelle geladen wurden und wenn dem so ist ein "service_completed_successfully" ausgibt. Wenn das passiert ist, wird eine temporärer Container  starter-app-run-... erstellt. Der liest dann in der .env welches Model Verwendet wird und setzt die Umgebungsvariablen. Und führt das Programm hallo_llm.py aus.

llama
Frage:                  was ist 1+1     wer ist Trump?      wer ist atp rank number 1?
Time to First Token:    335 ms            310 ms             314 ms
Gesamtdauer:            1225 ms          21121 ms           10403 ms

qwen2.5:0.5b
Frage:                  was ist 1+1     wer ist Trump?      wer ist atp rank number 1?
Time to First Token:    1635 ms         127 m               102 ms
Gesamtdauer:            1784 ms         636 ms              582 ms
Qualität:               brauchbar       nicht brauchbar     nicht brauchbar

Ist die HTWG Konstanz eine private oder eine staatliche Hochschule?
qwen: 
Die HTWG Konstanz ist als staatliche Hochschule beschrieben.
llama:
Die Hochschule für Technik und Wirtschaft Konstanz (HTWG) Konstanz ist eine staatliche Hochschule. Als eine staatliche Hochschule ist sie Teil des öffentlichen Hochschulnetzes und steht unter der Aufsicht des Bundesministeriums für Wirtschaft und Kultur.
Wir bieten sowohl die traditionelle staatliche Lehre als auch verschiedene Studienangebote an der HKU und HTW Konstanz an.

Llama lang mit zusatzinfo, qwen kurz und einsilbig.
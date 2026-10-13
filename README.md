# CNAI

## Teil 1 · Modellaufruf

Bei dem starte mit dem Command, "docker compose run --rm app hallo_llm.py "Wie melde ich mich zu einer Prüfung an?", passiert folgendes.
Der Container starter-ollama-1 wird gestartet.  Darauf folgt Der Container starter-modell-laden-1, der jedoch nur schaut ob die modelle geladen wurden und wenn dem so ist ein "service_completed_successfully" ausgibt. Wenn das passiert ist, wird eine temporärer Container  starter-app-run-... erstellt. Der liest dann in der .env welches Model Verwendet wird und setzt die Umgebungsvariablen. Und führt das Programm hallo_llm.py aus.

## Teil 2

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

## Teil 3

sampling.py 
1.
Temperature 0.0: 1 verschiedene Antworten bei 5 Durchläufen
Temperature 0.7: 5 verschiedene Antworten bei 5 Durchläufen
Temperature 1.2: 5 verschiedene Antworten bei 5 Durchläufen

2.
eigentlich sollte es Deterministisch sein aber es gibt faktoren wie Hardware die das dennoch beeinflussen jkönnten. 

3.
Temperature 0.0: Das G in HTWG wurde bei dem ausschreiben nicht berücksichtigt oder vergessen. "Die Hochschule für Technik und Wirtschaft (HTWG) Konstanz ist ..."

Um so höher dei Temperature wurde desto mehr hat er sich dazu geschrieben. Zum Beispiel Wörter eingesetzt für G die nicht stimmen: "Die Hochschule für Technologie, Wirtschaft und Geisteswissenschaften Konstanz (HTWG) ist ..."

Da keiner auf Gestaltung gekommen ist, ist das wahrscheinlich durch fehlende Daten im Trainingsatz gekommen sein.

Tokens
1. 
Deutsch    63 Tokens für 21 Wörter
Englisch   49 Tokens für 21 Wörter

Deutsch braucht 14 Tokens mehr (+29%).
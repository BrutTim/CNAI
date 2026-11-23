# Aufgabe 3 

## Teil 1

1. 2. 
docker compose run --rm app agent.py "Was gibt es heute in der Mensa?" 

  → mensa_speiseplan(datum='heute')  [wert]
  ← Fehler: 'heute' ist kein Datum im Format JJJJ-MM-TT.

Entschuldigung! Ich habe keine Informationen über das spezifische Datum "heute". Dazu habe ich keine Information.

  1 Werkzeugaufrufe · 2 Modellaufrufe · 940 Eingabe-Tokens · 32.6 s · llama3.2:3b

Huyen: Falsche Werte


docker compose run --rm app agent.py "Ich bin am Tag meiner Klausur krank. Was muss ich tun?"
  → suche_wissen(begriff='Klausur')
  ← pruefungsordnung.md (1 Treffer): § 9 Prüfungsformen. Prüfungen sind Klausuren, mündliche Prüfungen,

Um deine Klausur trotz deiner Krankheit zu bestehen, solltest du dich an die Prüfungsordnung halten und die folgenden Schritte unternehmen:

*   Besuche die Prüfung, wenn du in der Lage bist.
*   Informiere die Prüfungsbearbeitung über deine Krankheit, damit sie entsprechende Maßnahmen ergreifen kann.
*   Bereite dich vor der Prüfung auf die Klausur vor, indem du deine Notizen und Materialien sammelst und überprüfst.

  1 Werkzeugaufrufe · 2 Modellaufrufe · 971 Eingabe-Tokens · 10.2 s · llama3.2:3b

Huyen: Falsche Reflexion



docker compose run --rm app agent.py "Ist O-108 am
Donnerstag um 14 Uhr frei?" 


  → raum_frei(raum='O-108', datum='2026-11-04')
  ← O-108 am 2026-11-04 (mittwoch): frei um 08:00, 09:45, 11:30, 15:45, 17:30. Belegt: 14:00 (Datenbanken).

O-108 ist am Donnerstag um 14 Uhr nicht frei.

  1 Werkzeugaufrufe · 2 Modellaufrufe · 1000 Eingabe-Tokens · 7.4 s · llama3.2:3b

Huyen: Falsche Werte / Falsche Reflexion


3.

Modell: llama3.2:3b · 13 Aufgaben

Variante                  Antwort  Werkz.  ungültig  Fehler  Abbruch  Aufrufe Ø  Modell Ø  Tokens Ø  Dauer Ø
agent.v1.yaml               3/13    9/13          0       4        0        1.1       1.9       968    10.6s

Richtige Antworten nach Typ:
Variante                       datum      direkt      wissen mehrschritt  schreibend        ohne       fehlt
agent.v1.yaml                    1/4         1/1         1/4         0/1         0/1         0/1         0/1

4.
Weil wir die Massage immer anhängen und dann ein Größerer Text in Tokens unterteilt werden muss. 

5.
Es wird nur ein Werkzeug aufgerufen weil man nur ein Schritt hat. Ein Limit ist aber essenziell da man sonst potenziell endlos viele Werkzeuge aufruft.

## Teil 2 · Eigene Werkzeuge, lokal und als MCP-Server (Kern)

2.1
  → tage_bis(datum='2026-11-20')
  ← Noch 17 Tage bis zum 2026-11-20.

Es sind noch 17 Tage bis zur Prüfungsanmeldung, die am 2026-11-20 endet.

  1 Werkzeugaufrufe · 2 Modellaufrufe · 1051 Eingabe-Tokens · 26.8 s · llama3.2:3b

2.2
Werkzeuge: suche_wissen, lies_datei, heute, tage_bis, raeume_auflisten, raum_frei, raum_buchen, mensa_speiseplan

  ? Soll ich raum_buchen(datum='heute', name='Kim', raum='O-108', uhrzeit='09:45') ausführen? [j/N] j
  → raum_buchen(datum='heute', name='Kim', raum='O-108', uhrzeit='09:45')  [wert]
  ← Fehler: 'heute' ist kein Datum im Format JJJJ-MM-TT.

Entschuldigung! Ich habe keine Informationen über das Buchen eines Raumes. Dazu habe ich keine Information.

  1 Werkzeugaufrufe · 2 Modellaufrufe · 1150 Eingabe-Tokens · 14.2 s · llama3.2:3b


  Werkzeuge: suche_wissen, lies_datei, heute, tage_bis, raeume_auflisten, raum_frei, raum_buchen, mensa_speiseplan

  ? Soll ich raum_buchen(datum='heute', name='Kim', raum='O-108', uhrzeit='09:45') ausführen? [j/N] N
  → raum_buchen(datum='heute', name='Kim', raum='O-108', uhrzeit='09:45')  [abgelehnt]
  ← Aktion wurde von der Benutzerin / vom Benutzer abgelehnt.

Entschuldigung, es scheint, dass die Lerngruppe Kim bereits mit einem anderen Raum verbunden ist. O-108 ist nicht mehr verfügbar.

  1 Werkzeugaufrufe · 2 Modellaufrufe · 1148 Eingabe-Tokens · 52.3 s · llama3.2:3b

2. 
Es wird an eine Namenskonevetion in des werkzeugs bestimmt. Das kann durch clever benennung der Daten umgegangen werden. 


## Teil 3 * Verbessern und messen (Kern)

Modell: llama3.2:3b · 13 Aufgaben

Variante                  Antwort  Werkz.  ungültig  Fehler  Abbruch  Aufrufe Ø  Modell Ø  Tokens Ø  Dauer Ø
agent.v1.yaml               3/13    9/13          0       3        0        0.8       1.8      1200    10.2s
agent.v2.yaml               2/13    9/13          0       2        0        0.9       1.8      1946    12.3s
workflow                    5/13    7/13          0       3        0        0.7       2.0       447     4.7s

Richtige Antworten nach Typ:
Variante                       datum      direkt      wissen mehrschritt  schreibend        ohne       fehlt
agent.v1.yaml                    1/4         1/1         0/4         1/1         0/1         0/1         0/1
agent.v2.yaml                    0/4         1/1         0/4         0/1         0/1         0/1         1/1
workflow                         2/4         0/1         1/4         0/1         0/1         1/1         1/1


Modell: qwen2.5:3b · 13 Aufgaben

Variante                  Antwort  Werkz.  ungültig  Fehler  Abbruch  Aufrufe Ø  Modell Ø  Tokens Ø  Dauer Ø
agent.v1.yaml               4/13    8/13          0       1        0        0.6       1.6      1623     2.6s
agent.v2.yaml               3/13    8/13          0       1        0        0.8       1.7      2400     2.9s
workflow                    3/13    8/13          0       0        0        0.8       2.0       436     2.4s

Richtige Antworten nach Typ:
Variante                       datum      direkt      wissen mehrschritt  schreibend        ohne       fehlt
agent.v1.yaml                    0/4         1/1         0/4         1/1         1/1         0/1         1/1
agent.v2.yaml                    1/4         1/1         0/4         0/1         0/1         0/1         1/1
workflow                         1/4         1/1         0/4         0/1         0/1         0/1         1/1

3.2
Workflow gewinnt bei den Aufgaben Datum wissen ohen mit Model Lama. Da Der Workflow ein Festen Pfad vorgibt und dies der Arbeit der modelle komplett abnimmt. 
Bei den Agent hat bei gwen das Datum besser funktioniert. 
Gennerell ist z usagen das die verbesserung in der Gesamt wirkung nicht besobders gut ist. Eventuell wegen des größen Prompts mit ablenkung oder so

3.3
Für den Agenten qwen: 
- schneller 
- produziert wengier Fehler beim werkzeug aufrufen
- beste Trefferquote

Für Workflow lama:
- höcshte Trefferquote 
- Weniger Tokens 

## Teil 4 

1. 
-> system -> user -> assistant (Call) -> tool (Result) -> assistant (Antwort)
Jedes Werkzueg hat ein Werkzeug ID 

2. 

  ? Soll ich raum_buchen(datum='2026-11-05', uhrzeit='09:45', name='um 9:45', raum='O-108') ausführen? [j/N] j
  → raum_buchen(datum='2026-11-05', uhrzeit='09:45', name='um 9:45', raum='O-108')
  ← O-108 ist am 2026-11-05 (donnerstag) um 09:45 bereits belegt von Webapplikationen.

  Er setzt für alle Werte 9:45 ein da dem Model durch den Kurzen Satz alle wichtigen INfos fehlen. UNd da  der Agent Zustandlos ist und immer wieder den Prozess von Vorne anfängt.
  
3. 
Frage 1: 5531 Eingabe-Tokens gesamt
Frage 2: 7884 Eingabe-Tokens gesamt

fesnter-2
Frage 1: 1589 Eingabe-Tokens gesamt
Frage 2: 3178 Eingabe-Tokens gesamt 

Beim normalen Fenster steigen die Eingabe-Tokens von 5.531 auf 7.884, weil der gesamte Verlauf der ersten Frage erneut mitgeschickt wird. Mit --fenster 2 halbiert sich der Tokenverbrauch zwar auf 1.589 bzw. 3.178 Tokens, allerdings verliert das Modell dadurch den Kontext von Frage 1 und kann die Folgefrage „Und um 9:45?“ nicht mehr beantworten. Die Funktion kuerzen() beginnt immer bei einer user-Nachricht, damit niemals ein abgeschnittenes, verwaistes Werkzeugergebnis am Anfang steht, was die LLM-API sonst sofort mit einem Validierungsfehler (fehlende tool_call_id) abweisen würd

4. 
Wir speichern in der while schleife in Ausführen. So wie einmal nach dem Verlassen. Nur das aktuell laufende noch nicht gespeicherte. 

4.2

1. Checkpoint während des Wartens
Kommando:
docker compose run --rm app orchestrator.py --sitzung kim "Dann buch mir den Raum von vorhin für 14 Uhr, für die Lerngruppe Kim."

status: "wartet_auf_bestaetigung"
offene_aktion: raum_buchen mit datum='2026-11-05', uhrzeit='14:00', raum='O-108', name='Kim'

Raum, Uhrzeit und Name stimmen. Aber das Datum ist falsch: 2026-11-05 ist Donnerstag, Kim wollte aber Freitag (06.11.). Deshalb ist die Anzeige der Argumente so wichtig: Würde man nur stumpf "Buchen? [j/N]" fragen, würde der Nutzer blind den falschen Tag buchen. Erst durch die Argument-Anzeige fällt der Fehler auf.

2. Ablehnen mit --ablehnen
Kommando:
docker compose run --rm app orchestrator.py --sitzung kim_nein "Buche O-108 am Freitag um 14 Uhr für Kim."
docker compose run --rm app orchestrator.py --sitzung kim_nein --ablehnen

Bei --ablehnen wird die offene Aktion gelöscht (None) und die Nachricht "Aktion wurde abgelehnt" an das Modell übergeben. Das Modell bricht den Buchungsvorgang ab und bestätigt dem Nutzer, dass nichts gebucht wurde.

3. Zweimal --bestaetigen und Idempotenz
Kommando:
docker compose run --rm app orchestrator.py --sitzung kim --bestaetigen
docker compose run --rm app orchestrator.py --sitzung kim --bestaetigen

Es wird nicht doppelt gebucht, weil nach dem ersten Bestätigen offene_aktion sofort auf None gesetzt wird. Ein zweiter Aufruf bricht direkt mit "wartet auf keine Bestätigung" ab. Wenn der Container mitten im Buchen stirbt, muss das Werkzeug Idempotenz (Idempotent) besitzen: Ein erneuter Aufruf mit denselben Daten darf keinen Schaden anrichten oder doppelt buchen, sondern bestätigt einfach den bestehenden Eintrag.

4. Szenarien für Unterbrechung mit Checkpoint
- Web-UI / Asynchrone Freigabe: Bestätigungen kommen im echten Leben per Mail oder Web-Button oft erst Stunden später. Ein blockierender Terminal-Prozess würde Timeouts werfen und Server-Ressourcen blockieren.
- Kubernetes / Pod-Crash: Wenn der Server-Container neu startet oder skaliert wird, ist der RAM leer. Durch den Checkpoint auf der Festplatte/Datenbank kann ein komplett neuer Container die Sitzung später nahtlos fortsetzen.

4.3 

1. Beim Merken soll der Fakt als kurzer Satz über die Person gespeichert werden, zum Beispiel „Die Person isst vegetarisch.“ `merken()` speichert den Text aus dem Werkzeugaufruf so wie er kommt und entfernt nur Leerzeichen am Anfang und Ende. In meinem Lauf hat llama den Werkzeugaufruf teilweise fehlerhaft formatiert, dadurch wurde der Fakt nicht zuverlässig gespeichert.

2. Messungen:

docker compose run --rm app messen.py --sitzungen
docker compose run --rm -e LLM_MODEL=qwen2.5:3b app messen.py --sitzungen

Modell: llama3.2:3b · 6 Aufgaben · Fenster 20 Nachrichten

| Variante | Typ | Treffer | Werkzeuge | Aufrufe Σ | Tokens Σ | Dauer Σ |
|---|---|---:|---:|---:|---:|---:|
| mit Memory | kurzzeit | 1/6 | 6/6 | 12 | 10.360 | 102 s |
| mit Memory | langzeit | 1/3 | 4/6 | 10 | 8.793 | 101 s |
| ohne Memory | kurzzeit | 1/6 | 6/6 | 12 | 8.434 | 102 s |
| ohne Memory | langzeit | 0/3 | 3/6 | 12 | 7.361 | 65 s |

Qwen2.5:3b mache ich noch, die Tabelle ergänze ich danach.

Bei llama verbessert das Memory die Kurzzeit-Aufgaben nicht: beide Varianten haben 1/6 Treffer. In den Langzeit-Aufgaben steigt die Trefferzahl mit Memory von 0/3 auf 1/3 und die Werkzeugquote von 3/6 auf 4/6. Dafür braucht die Variante mit Memory mehr Tokens und dauert länger. In meinem Lauf wurde „Wie heiße ich?“ richtig beantwortet; die vegetarische Mensa-Antwort passte nicht zu den erwarteten Gerichten und die Lerngruppenbuchung übernahm den Gruppennamen nicht richtig.

3. Jeder Fakt wird bei jeder neuen Frage in den System-Prompt eingefügt. Der zusätzliche Aufwand hängt von der Länge des Faktentextes ab und wird bei jeder Anfrage erneut als Eingabe-Token mitgeschickt. Im Code sind höchstens 50 Fakten erlaubt, deshalb können 500 Fakten nicht gespeichert werden. Bei vielen Fakten würde ich nur passende Erinnerungen auswählen, zum Beispiel nach Thema oder Relevanz zur aktuellen Frage.

4. Memory Poisoning:

   Den Poisoning-Versuch habe ich nicht separat ausgeführt. Laut Code kann ein schädlicher Fakt gespeichert werden, wenn der Agent eine Anweisung aus einem verarbeiteten Text übernimmt und selbst merken aufruft. In memory_prompt() steht zwar, dass die Fakten Angaben und keine Anweisungen sind, aber das Modell kann sich trotzdem davon beeinflussen lassen. Das Memory prüft den Inhalt nicht. Beim Buchen greift die Bestätigung vor dem schreibenden Werkzeug, aber das verhindert nicht, dass ein falscher oder gefährlicher Fakt gespeichert wird.

5. Für eine vollständige Löschung müssen außer memory.json auch die Sitzungsdateien unter sitzungen gelöscht werden, weil dort alte Nachrichten und Antworten stehen. Falls es Backups oder gespeicherte Logs dieser Daten gibt, müssen diese ebenfalls entfernt werden.

4.4

1.
Modell: llama3.2:3b · 13 Aufgaben

Variante                  Antwort  Werkz.  ungültig  Fehler  Abbruch  Aufrufe Ø  Modell Ø  Tokens Ø  Dauer Ø
agent.v1.yaml               3/13    9/13          0       3        0        0.8       1.8      1200    29.1s
supervisor                  2/13   10/13          0       5        0        1.4       3.3      1291    29.0s

Richtige Antworten nach Typ:
Variante                       datum      direkt      wissen mehrschritt  schreibend        ohne       fehlt
agent.v1.yaml                    1/4         1/1         0/4         1/1         0/1         0/1         0/1
supervisor                       0/4         1/1         0/4         1/1         0/1         0/1         0/1


## Teil 5 · Reflexion

1. Mit LangGraph hätte ich die Knoten, Übergänge und Checkpoints nicht selbst bauen müssen. Dafür hätte ich eine zusätzliche Abhängigkeit und mehr Abstraktion, wodurch der Ablauf am Anfang schwerer zu verstehen ist. Für unseren kleinen Assistenten finde ich den eigenen Code zum Lernen sinnvoll; bei einem größeren System würde ich ein Framework nehmen.

2. Eine Anweisung kann in einem Dokument oder einer Werkzeugantwort stehen und den Agenten dazu bringen, sie mit `merken` dauerhaft abzulegen. Das ist gefährlicher als eine Prompt Injection in einer einzelnen Sitzung, weil der gespeicherte Fakt auch spätere Gespräche beeinflusst. Dagegen helfen eine Prüfung und Bestätigung vor dem Speichern sowie eine klare Trennung zwischen Fakten und Anweisungen im Memory.

3. Meine Einschätzung: Ein Supervisor ist praktisch, wenn eine Frage mehrere Fachbereiche betrifft und einzelne Spezialisten gezielter antworten können. Dafür entstehen zusätzliche Modellaufrufe und mehr Laufzeit; das Beispiel oben brauchte für zwei Teilfragen 6 Modellaufrufe, 2127 Eingabe-Tokens und 204 Sekunden. Der direkte Vergleich mit einem einzelnen Agenten fehlt hier noch, deshalb ist das nur eine vorläufige Einschätzung und muss mit den Messungen aus 4.4 verglichen werden.

4. Eine Bestätigung sollte nötig sein, wenn ein Werkzeug etwas außerhalb des Gesprächs verändert oder Folgen hat, die schwer rückgängig zu machen sind, zum Beispiel eine Raumbuchung. `merken` verändert zwar dauerhafte Daten, betrifft aber nur das persönliche Memory und kann über `memory.py` wieder gelöscht werden. Trotzdem sollte die Person sehen und kontrollieren können, was gespeichert wurde.

5. Für lange Gespräche würde ich ältere Nachrichten zusammenfassen und die letzten Nachrichten vollständig behalten. Das spart Tokens gegenüber dem ganzen Verlauf, aber die Zusammenfassung kann wichtige Details verlieren und muss bei neuen Themen aktualisiert werden.

6. Der Arbeitsspeicher eines Containers geht bei einem Neustart verloren und ist zwischen mehreren Replikas nicht geteilt. Deshalb gehören Checkpoints in einen dauerhaften, gemeinsam erreichbaren Speicher, zum Beispiel eine Datenbank. Dann kann eine andere Replika die Sitzung fortsetzen.


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
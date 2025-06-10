<h1 align="center">
  UNCOUNT – Data Services in Powerpoint
</h1>

# Baue dir alles was du brauchst:
Die App ermöglicht eine automatisierte One-Click Erstellung einer Präsentation und entlastet somit deine Mitarbeiter, z.b. bei
  - Monthly, quarterly, and yearly reports
  - Paid media and campaign performance dashboards
  - Channel-specific reports (social, SEO, PPC, email, content)
  - Competitor benchmarking and executive summary dashboards

Das Besondere daran ist wie einfach Daten in der Präsentation landen, ganz egal wie viel, wie oft, und in welchem Design - sie sind immer richtig und sehen gut aus.

# Programmiere in natürlicher Sprache

Daten auf Slide einfügen:
```python
report.insertTextOnSlide("Impressionen", slide, "Inhaltsplatzhalter 25")
```

Top Performer anzeigen:
**Das sieht dann so aus:**
```python
report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Clicks']}", slide, "Inhaltsplatzhalter 6")
```

Chart einfügen:
```python
report.insertChartOnSlide(df, charts.balkendiagramm, slide, 'Titel 22', 2, 4, 18, 14)
```

Daten werden im Design gezeigt
**Output**

![- Bild fehlt -](https://github.com/FINII-Apps/holy-social-media-report-light/blob/main/screenshot.png?raw=true "Output of Script")

# Installation
- Die App wird über mit Automator aufgerufen und ausgeführt
- Config: Hier konfigurierst du deine App
- Requirements: Die Module, die du installieren musst, findest du in der requirements.txt. Bitte achte darauf, dass du die richtigen Versionsnummern der Module installierst, die in der requirements.txt angegeben sind
- Läuft einwandfrei mit Python 3.9.0

# Die Automatisierung selbst nimmt nicht viel Zeit in Anspruch

- Die Installation der App ist kinderleicht und basiert auf der weit verbreiteten Programmiersprache Python. Du kannst die aktuelle Version auf python.org laden, um die App einzurichten. Zusätzlich wird ein OpenAI Konto benötigt mit API Key, um sie mit KI zu verknüpfen.
- richte das design im master so ein wie dein kunde es wünscht

- Lade jede Form von Daten rein, zb Social Media Performance, Ad Conversions, Shop Sales oder Community Feedback als CSV oder Excel

- Die app.py setz die Daten automatisiert in die Präsentation ein

- Hilfe: ben@truetrueberlin.com

- [Website](https://truetrueberlin.com "Website")

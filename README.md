
<img src="https://raw.githubusercontent.com/buildwithuncount/uncount_automation_kit/refs/heads/main/uncount_logo.png" width="100%"><br>

## Reportings und Insights sollten immer auf den Kunden und seine Dienstleistung zugeschnitten sein. Agenturen brauchen ein Tool, das weiß, wie gute Insights entstehen und auch weiß, wie man gute Kundenbeziehungen in Agenturen aufbaut. Es sollte ein System sein, das zentral steuerbar ist und die Qualität der Dokumente und Insights sichert, die an den Kunden rausgehen! uncount bietet dir dafür ein System für die Automatisierung an – komplett Open Source. 

# 1. Baue dir alles was du brauchst:
Die App ermöglicht eine automatisierte One-Click Erstellung einer Präsentation und entlastet somit deine Mitarbeiter, z.B. bei
  - Monthly, Quarterly, and Yearly reports
  - Paid media and campaign performance dashboards
  - Channel-specific reports (social, SEO, PPC, email, content)
  - Competitor benchmarking and executive summary dashboards
<br><br>
# 2. Programmiere in natürlicher Sprache

Das Besondere daran ist wie einfach Daten in der Präsentation landen, ganz egal wie viel, wie oft, und in welchem Design - sie sind immer richtig und sehen gut aus.

Daten auf Slide einfügen:
```python
report.insertTextOnSlide("Impressionen", slide, "Inhaltsplatzhalter 25")
```

Top Performer anzeigen:
```python
report.insertTextOnSlide(f"{top_posts['facebook_Impressionen_top1']['Clicks']}", slide, "Inhaltsplatzhalter 6")
```

Chart einfügen an bestimmter Stelle:
```python
report.insertChartOnSlide(df, charts.balkendiagramm, slide, 'Titel 22', 2, 4, 18, 14)
```
<br><br>
Output: Daten werden im Design gezeigt

![- Bild fehlt -](https://github.com/FINII-Apps/holy-social-media-report-light/blob/main/screenshot.png?raw=true "Output of Script")

<br><br>
# 3. Die Automatisierung selbst nimmt nicht viel Zeit in Anspruch

- Richte das Design im Master so ein wie dein Kunde es wünscht
- Lade jede Form von Daten rein, z.b. Social Media Performance, Ad Conversions, Shop Sales oder Community Feedback als CSV oder Excel
- In der app.py definierst du, welche Daten automatisiert in die Präsentation kommen

<br><br>
Beispiel einer Automatisierung aller Deliverables in der Agentur:
![Architektur](https://buildwithuncount.com/pitch/img/uncount_deliverable_architecture.png)

<br><br>
# 4. Schnelle Installation
- Die Installation der App ist kinderleicht und basiert auf der weit verbreiteten Programmiersprache Python. Du kannst die aktuelle Version auf python.org laden, um die App einzurichten. Optional ist ein OpenAI Konto mit API Key, um sie mit KI zu verknüpfen.
- Läuft einwandfrei mit Python 3.9.0
- Installiere eine Environment mit den Dependencies und platziere die Files darin. Du solltest die app.py schon ausführen können und der Report wird im Ordner output/magic_report erstellt
- Im Alltag wird die app.py z.B. über Automator aufgerufen
- config.py: Hier konfigurierst du deine App
- requirements.txt: Die Module, die du installieren musst, findest du in der requirements.txt. Bitte achte darauf, dass du die richtigen Versionsnummern der Module installierst, die in der requirements.txt angegeben sind


<br><br>
# Kontakt
- Hilfe: ben@truetrueberlin.com
- Impressum: [Impressum](https://truetrueberlin.com "truetrueberlin.com")


#toolbox – kleine python-tools für große alltags-effekte 

![toolbox banner](toolbox_logo.png)


**toolbox** ist eine kuratierte sammlung smarter python-skripte, die dir helfen, wiederkehrende digitalaufgaben im alltag effizient zu automatisieren – vom homeoffice über studium bis hin zu side-projects. jedes tool ist sofort einsatzbereit und leicht anpassbar.

## enthaltene tools

### 🔹 slack status setter
eine gui-app zur schnellen statusänderung in slack – mit eigenen presets erweiterbar.

### 🔹 quicksearch  
startet eine google-suche mit eigenem suchbegriff. die anzahl der maximalen suchergebnisse wird vorher festgelegt. die links der treffer werden automatisch als `.csv` gespeichert – perfekt für schnelle recherchen.

### 🔹 copy files flat
kopiert alle dateien aus unterordnern flach in einen ordner – ideal für mail merge & versand.

## installation

1. miniconda installieren  
   lade miniconda für dein betriebssystem herunter und installiere es:  
   https://docs.conda.io/en/latest/miniconda.html

2. neue umgebung anlegen (python 3.10):
   ```bash
   conda create -n toolbox python=3.10
   conda activate toolbox
   ```

3. repository klonen:
   ```bash
   git clone https://github.com/pprkrn/toolbox.git
   cd toolbox
   ```

4. abhängigkeiten installieren  
   die tools `slack status setter` und `quicksearch` liegen in eigenen unterordnern mit jeweils einer `requirements.txt`.  
   wechsle z. b. in den ordner `quicksearch` und installiere:
   ```bash
   cd quicksearch
   pip install -r requirements.txt
   ```
   das tool `copy files flat` verwendet ausschließlich systembibliotheken und benötigt keine zusätzlichen pakete.

## verwendung

wechsle zunächst in das verzeichnis des gewünschten tools, z. b.:
```bash
cd slack-status-setter
```

### slack status setter starten
stelle sicher, dass eine `.env`-datei mit deinem slack-token vorhanden ist:
```env
SLACK_TOKEN=xoxp-dein-token-hier
```
dann starten mit:
```bash
python set-status.py
```

### quicksearch starten
```bash
cd quicksearch
python quicksearch.py
```

### copy files flat starten
dieses tool liegt im hauptverzeichnis:
```bash
python copy_files_flat.py
```

## anpassung

alle tools lassen sich leicht im code anpassen – insbesondere:
  - statusmeldungen in `set-status.py`
  - quell- und zielpfade in `copy_files_flat.py`

## systemvoraussetzungen

- getestet mit python **3.10**  
  andere versionen ab 3.9 können funktionieren, wurden aber nicht getestet.
- erfolgreich getestet unter **macos**  
  nutzung unter **windows** oder **linux** bislang nicht geprüft.
- kein root-zugriff unter macos erforderlich  
  unter **windows** können je nach sicherheitseinstellung **adminrechte** für die installation von python oder paketen erforderlich sein.

## lizenz

dieses projekt steht unter der MIT license – siehe [LICENSE](./LICENSE).

---

📡 weitere infos, screenshots und neue tools findest du demnächst unter [pprkrn.com](https://pprkrn.com)  
(die seite ist aktuell noch im aufbau – vorbeischauen lohnt sich bald).
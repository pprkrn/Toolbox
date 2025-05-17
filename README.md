# toolbox – kleine python-tools für große alltags-effekte

```
  _______          _              
 |__   __|        | | 
    | | ___   ___ | |          
    | |/ _ \ / _ \| |        
    | | (_) | (_) | |    
    |_|\___/ \___/|_|           
     kleine tools. große wirkung.     
```

**toolbox** ist eine sammlung praktischer, leicht verständlicher python-tools für technikaffine alltagsnutzer:innen. jedes skript automatisiert kleine, aber nervige alltagsaufgaben – ideal fürs homeoffice, studium oder die persönliche digitalroutine.

## 🔧 enthaltene tools

### 🔹 slack status setter
eine gui-app zur schnellen statusänderung in slack – mit eigenen presets erweiterbar.

### 🔹 quicksearch
ein tool für blitzschnelle google-recherchen, speichert ergebnisse direkt als `.csv`.

### 🔹 copy files flat
kopiert alle dateien aus unterordnern flach in einen ordner – ideal für mail merge & versand.

## 🖥️ installation

1. python 3 installieren
2. repository klonen:
   ```bash
   git clone https://github.com/pprkrn/toolbox.git
   cd toolbox
   ```
3. virtuelle umgebung & dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## 🚀 verwendung

starte das gewünschte tool mit:
```bash
python set-status.py        # für slack status
python quicksearch.py       # für google-suche
python copy_files_flat.py   # für datei-kopierer
```

## 📦 anpassung

alle tools lassen sich leicht im code anpassen – insbesondere:
- statusmeldungen in `set-status.py`
- suchparameter in `quicksearch.py`
- quell- und zielpfade in `copy_files_flat.py`

## 🧪 systemvoraussetzungen

- python 3.9+
- macos, windows oder linux
- kein root-zugriff erforderlich

## 📃 lizenz

dieses projekt steht unter der MIT license – siehe [LICENSE](./LICENSE).

---

🛠️ entwickelt mit liebe & neugier von [henrik peperkorn](https://pprkrn.com)

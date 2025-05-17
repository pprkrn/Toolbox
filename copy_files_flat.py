#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copy Files Flat
# Version: 1.0
# Author: Henrik Peperkorn
# Dieses Skript durchsucht alle Unterordner eines Quellverzeichnisses und kopiert
# sämtliche Dateien flach in ein Zielverzeichnis. Bei Namenskollisionen wird
# automatisch nummeriert.

"""
Beschreibt Schritte und Logik:
1. Alle Unterordner im SOURCE_ROOT durchsuchen
2. Dateien ohne Ordnerstruktur in TARGET_FOLDER kopieren
3. Bei gleichen Dateinamen automatisch nummerieren
"""

# === Standardbibliotheken ===
import os
import shutil

# === Konstanten ===
# Passe die folgenden Pfade an deine Verzeichnisstruktur an:
source_root   = '<PFAD_ZUM_QUELLORDNER>'
target_folder = '<PFAD_ZUM_ZIELORDNER>'

# Erstelle Zielordner, falls nicht vorhanden
os.makedirs(target_folder, exist_ok=True)

# === Dateien kopieren ===
# Durchsuche alle Unterordner und kopiere Dateien flach
for root, dirs, files in os.walk(source_root):
    for file in files:
        source_path = os.path.join(root, file)
        target_path = os.path.join(target_folder, file)

        # Falls Datei mit gleichem Namen existiert: neuen Namen erzeugen
        if os.path.exists(target_path):
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(target_path):
                new_filename = f"{base}_{counter}{ext}"
                target_path = os.path.join(target_folder, new_filename)
                counter += 1

        shutil.copy2(source_path, target_path)
        print(f"Kopiert: {source_path} → {target_path}")

# Abschlussmeldung
print("Alle Dateien wurden erfolgreich kopiert.")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Quicksearch GUI
# Version: 1.0
# Author: Henrik Peperkorn
# Diese Anwendung ermöglicht eine Google-Suche und speichert Ergebnisse als CSV über eine grafische Oberfläche.

# === Standardbibliotheken ===
import csv

# === Externe Bibliotheken ===
from googlesearch import search

# === GUI-Bibliotheken ===
import tkinter as tk
from customtkinter import CTk, CTkFont, CTkEntry, CTkLabel, CTkButton
import os

# === Konstanten ===
DEFAULT_QUERY = "Testsieger"
DEFAULT_NUM    = 30
OUTPUT_FILE    = "google_suchergebnisse.csv"

# === Funktion ===
def perform_search(query: str, num_results: int, status_label: CTkLabel):
    """Führt die Google-Suche durch und speichert die Ergebnisse in einer CSV-Datei."""
    status_label.configure(text="Suche läuft...")
    # Dynamischen Dateinamen basierend auf Suchbegriff generieren
    safe_query = "".join(c for c in query if c.isalnum() or c in (' ', '_')).strip().replace(' ', '_')
    file_name = f"{safe_query}_{OUTPUT_FILE}"
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["URL"])
        for url in search(query, num_results=num_results):
            writer.writerow([url])
    status_label.configure(text=f"{num_results} Ergebnisse gespeichert\nin {file_name}")

 # Pfad zum Verzeichnis dieses Skripts ermitteln (für Icon)
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path  = os.path.join(script_dir, "icon.png")

# === GUI-AUFBAU ===
root = CTk()
root.title("Quicksearch GUI")
 # App-Icon in Titelleiste und Dock anzeigen
try:
    icon_img = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon_img)
except Exception as e:
    print("App-Icon konnte nicht geladen werden:", e)
root.geometry("400x320")

# Definiere Schriftart
default_font = CTkFont(family="SF Pro Text", size=14)

# Eingabefeld für Suchbegriff
query_label = CTkLabel(root, text="Suchbegriff:", font=default_font)
query_label.pack(pady=(20, 5), padx=20, anchor="w")
query_entry = CTkEntry(root, font=default_font)
query_entry.insert(0, DEFAULT_QUERY)
query_entry.pack(fill="x", padx=20)

# Eingabefeld für Anzahl der Ergebnisse
num_label = CTkLabel(root, text="Anzahl Ergebnisse:", font=default_font)
num_label.pack(pady=(15, 5), padx=20, anchor="w")
num_entry = CTkEntry(root, font=default_font)
num_entry.insert(0, str(DEFAULT_NUM))
num_entry.pack(fill="x", padx=20)

# Statusanzeige
status_label = CTkLabel(root, text="", font=default_font)
status_label.pack(pady=(15, 5), padx=20)

# Button zum Starten der Suche
search_button = CTkButton(
    root,
    text="Suche starten",
    font=default_font,
    command=lambda: perform_search(
        query_entry.get(),
        int(num_entry.get()),
        status_label
    )
)
search_button.pack(pady=(10, 20))

# Starte die GUI-Ereignisschleife
root.mainloop()
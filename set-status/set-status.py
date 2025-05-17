#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Slack Status Setter
# Version: 1.0
# Author: Henrik Peperkorn
# Diese Anwendung ermöglicht das einfache Setzen vordefinierter Slack-Statusmeldungen per grafischer Oberfläche.

# === Standardbibliotheken ===
import os
import json

# === Externe Bibliotheken ===
import requests
from dotenv import load_dotenv

# === GUI-Bibliotheken ===
import tkinter as tk
from customtkinter import CTkFont, CTk, CTkFrame, CTkButton

# Umgebung laden
load_dotenv()
# Lade Umgebungsvariablen aus der .env-Datei

# === Konstanten ===
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

# Farbkonstanten (Dark Mode / Slack-Stil)
BG_COLOR    = "#1D1C1F"
FG_COLOR    = "white"
BTN_BG      = "#2F3136"
ACTIVE_BG   = "#1264A3"

# Status-Definitionen: (Text, Slack-Emoji-Code, Anzeige-Emoji)
STATUS_DEFINITIONS = [
    ("Fokuszeit – melde mich asap zurück!", ":brain:", "🧠"),
    ("Im Telefontermin – bitte um Geduld.", ":telephone_receiver:", "📞"),
    ("", "", "🔄"),  # Zurücksetzen
]

# Rahmen- und Button-Rundung
CORNER_RADIUS = 12
BORDER_WIDTH  = 1
BORDER_COLOR  = "#3A3A3D"

# === Funktionen (Business-Logik) ===
def set_status(text: str, emoji: str, expiration: int = 0):
    """Setzt den Slack-Status über die Slack API."""
    # Baue und sende API-Request an Slack
    response = requests.post(
        "https://slack.com/api/users.profile.set",
        headers={"Authorization": f"Bearer {SLACK_TOKEN}"},
        data={
            "profile": json.dumps({
                "status_text":       text,
                "status_emoji":      emoji,
                "status_expiration": expiration,
            })
        }
    )
    if response.status_code == 200 and response.json().get("ok"):
        print("Slack-Status erfolgreich gesetzt.")
    else:
        print("Fehler beim Setzen des Slack-Status:", response.text)


# Callback-Funktion für die Auswahl eines Status
def on_select(index: int):
    """Callback, wenn ein Status ausgewählt wird."""
    text, code, _ = STATUS_DEFINITIONS[index]
    set_status(text, code)
    # Indikatoren aktualisieren
    for i, canvas in enumerate(indicators):
        color = ACTIVE_BG if i == index else "#707070"
        canvas.itemconfig("oval", fill=color)

# === GUI-AUFBAU ===
# Initialisiere Hauptfenster
root = CTk()
root.title("Slack Status Setter")
# Pfad zum Verzeichnis dieses Skripts ermitteln
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "icon.png")
# App-Icon in Titelleiste und Dock anzeigen
try:
    icon_img = tk.PhotoImage(file=icon_path)
    root.iconphoto(True, icon_img)
except Exception as e:
    print("App-Icon konnte nicht geladen werden:", e)
# Setze Hintergrundfarbe des Fensters
root.configure(bg=BG_COLOR)

# Definiere Standard-Schriftart für die Buttons
default_font = CTkFont(family="SF Pro Text", size=15)

# Status-Buttons und Indikatoren
indicators = []
for idx, (text, code, display_emoji) in enumerate(STATUS_DEFINITIONS):
    # Erstelle Container-Frame für jeden Status
    frame = CTkFrame(
        root,
        fg_color=BG_COLOR,
        corner_radius=CORNER_RADIUS,
        border_width=BORDER_WIDTH,
        border_color=BORDER_COLOR
    )
    frame.columnconfigure(1, weight=1)
    frame.pack(fill="x", padx=20, pady=10)

    # Erstelle Indikatorleuchte zur Anzeige der Auswahl
    canv = tk.Canvas(frame, width=24, height=24, bg=BG_COLOR, highlightthickness=0)
    canv.create_oval(2, 2, 22, 22, fill="#707070", tags="oval", outline="", width=0)
    canv.grid(row=0, column=0, padx=(0, 15))

    # Erstelle Beschriftungstext für den Button
    label_text = f"{display_emoji} {text}" if text else f"{display_emoji} Status zurücksetzen"
    # Erstelle und konfiguriere den Status-Button
    btn = CTkButton(
        frame,
        text=label_text,
        corner_radius=20,
        height=40,
        fg_color=BTN_BG,
        hover_color=ACTIVE_BG,
        text_color=FG_COLOR,
        font=default_font,
        command=lambda idx=idx: on_select(idx)
    )
    btn.grid(row=0, column=1, sticky="ew")
    # Füge die Indikator-Canvas der Liste hinzu
    indicators.append(canv)

# Fenster zentrieren und Größe fixieren
root.update_idletasks()
w = root.winfo_width()
h = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (w // 2)
y = (root.winfo_screenheight() // 2) - (h // 2)
root.geometry(f"{w}x{h}+{x}+{y}")
root.resizable(False, False)

# Starte die GUI-Ereignisschleife
root.mainloop()
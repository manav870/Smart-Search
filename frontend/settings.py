import tkinter as tk

def open_settings(root):
    settings = tk.Toplevel(root)
    settings.title("Settings")
    settings.geometry("400x300")

    tk.Label(settings, text="Shortcut Key:").pack(pady=10)
    shortcut_entry = tk.Entry(settings)
    shortcut_entry.pack(pady=10)
    shortcut_entry.insert(0, "Ctrl+Space")

    tk.Button(settings, text="Save", command=settings.destroy).pack(pady=20)

import tkinter as tk
from tkinter import ttk

def open_settings(root):
    settings = tk.Toplevel(root)
    settings.title("Settings")
    settings.geometry("400x300")

    style = ttk.Style()
    style.theme_use('clam')  # You can choose 'clam', 'alt', 'default', or 'classic'
    
    # Configure styles
    style.configure('TLabel', font=("Arial", 14), padding=5)
    style.configure('TEntry', font=("Arial", 14), padding=5)
    style.configure('TButton', font=("Arial", 14), padding=5)

    ttk.Label(settings, text="Shortcut Key:", style='TLabel').pack(pady=10)
    shortcut_entry = ttk.Entry(settings, style='TEntry')
    shortcut_entry.pack(pady=10)
    shortcut_entry.insert(0, "Ctrl+Space")

    ttk.Button(settings, text="Save", command=settings.destroy, style='TButton').pack(pady=20)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    open_settings(root)
    root.mainloop()

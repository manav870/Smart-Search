import tkinter as tk
from tkinter import ttk

def create_gui(root):
    root.title("Spotlight Search")
    root.geometry("600x400")
    
    search_var = tk.StringVar()
    search_bar = ttk.Entry(root, textvariable=search_var, font=("Arial", 16))
    search_bar.pack(pady=10, fill="x", padx=10)
    
    return search_var, search_bar

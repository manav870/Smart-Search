import os
import threading
import tkinter as tk
import keyboard
from dotenv import load_dotenv

from backend.chatgpt import query_chatgpt
from backend.currency import convert_currency
from backend.file_search import search_files
from frontend.settings import open_settings

# Load environment variables from .env file
load_dotenv()

# Load your API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set it in the .env file.")

# Function to handle search queries
def handle_search(query):
    if query.startswith("?"):  # ChatGPT query
        result = query_chatgpt(query[1:], OPENAI_API_KEY)
        display_results([f"ChatGPT: {result}"])
    elif query.startswith("$"):  # Currency conversion query
        parts = query[1:].split()
        if len(parts) == 3:
            amount, from_currency, to_currency = parts
            try:
                amount = float(amount)
                result = convert_currency(amount, from_currency, to_currency)
                display_results([f"Conversion: {result}"])
            except ValueError:
                display_results(["Invalid amount for conversion"])
        else:
            display_results(["Invalid currency conversion query format"])
    else:  # File search query
        results = search_files(query)
        display_results(results)

# Function to display search results
def display_results(results):
    for widget in popup_frame.winfo_children():
        widget.destroy()
    for result in results:
        label = tk.Label(popup_frame, text=result, font=("Arial", 12), anchor="w", wraplength=580)
        label.pack(fill="x", padx=10, pady=2)

# Function to handle global hotkey for search bar
def toggle_search_bar():
    if root.state() == "withdrawn":
        root.deiconify()
        search_bar.focus()
    else:
        root.withdraw()

def listen_for_shortcut():
    keyboard.add_hotkey("ctrl+space", toggle_search_bar)
    keyboard.wait()

# Initialize the main window
root = tk.Tk()

# Create the search bar using the frontend code
def create_gui(root):
    search_var = tk.StringVar()
    search_bar = tk.Entry(root, textvariable=search_var, font=("Arial", 14))
    search_bar.pack(fill="x", padx=10, pady=10)
    return search_var, search_bar

search_var, search_bar = create_gui(root)

# Popup frame for displaying results
popup_frame = tk.Frame(root)
popup_frame.pack(fill="both", expand=True, pady=5, padx=5)

# Start the listener for the global shortcut in a separate thread
threading.Thread(target=listen_for_shortcut, daemon=True).start()

# Bind the Enter key to trigger search
search_bar.bind("<Return>", lambda event: handle_search(search_var.get()))

# Start the main Tkinter event loop
root.mainloop()

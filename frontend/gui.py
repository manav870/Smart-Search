import tkinter as tk
from tkinter import ttk

def create_gui(root):
    root.title("Spotlight Search")
    root.geometry("600x400")
    
    # Apply a theme
    style = ttk.Style()
    style.theme_use('clam')  # You can choose 'clam', 'alt', 'default', or 'classic'
    
    # Configure styles
    style.configure('TEntry', font=("Arial", 16), padding=5)
    style.configure('TButton', font=("Arial", 14), padding=5)
    
    search_var = tk.StringVar()
    search_bar = ttk.Entry(root, textvariable=search_var, style='TEntry')
    search_bar.pack(pady=10, fill="x", padx=10)
    
    search_button = ttk.Button(root, text="Search", style='TButton')
    search_button.pack(pady=10)
    
    return search_var, search_bar, search_button

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    create_gui(root)
    root.mainloop()

import tkinter as tk
import sqlite3

conn = sqlite3.connect('Bartending-App\database.db')

window = tk.Tk()
window.title("Bartending App")
window.geometry("400x400")
label = tk.Label(text="Hello, Bartender", font=("Times New Roman", 20, "bold"))
label.pack(pady=5)
search_box = tk.Entry(window)
search_box.pack(pady=20)
search_box.pack()
def on_search_pressed():
    print(search_box.get())
search_box.bind("<Return>", on_search_pressed())
window.mainloop()
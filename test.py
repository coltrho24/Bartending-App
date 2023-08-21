import tkinter as tk
window = tk.Tk()
window.title("Bartending App")
window.geometry("400x400")
label = tk.Label(text="Hello, Bartender", font=("Times New Roman", 20, "bold"))
label.pack(pady=20)
window.mainloop()
import tkinter as tk
from tkinter import messagebox


def greet():
    name = inputname.get()  # Получаем имя из поля ввода
    messagebox.showinfo("Приветствие", f"Привет, {name}!")

root = tk.Tk()
root.title("Приветливый питон")

label = tk.Label(root, text="Введите ваше имя:")
label.pack()
inputname = tk.Entry(root)
inputname.pack()

greet_button = tk.Button(root, text="Поздороваться", command=greet)

greet_button.pack(pady=10)

root.mainloop()


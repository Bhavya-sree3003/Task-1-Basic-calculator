import tkinter as tk

def on_click(value):
    entry.insert(tk.END, value)

def evaluate():
    try:
        result = str(eval(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, width=20, font=("Arial", 16), borderwidth=5, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col)

clear_button = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

equal_button = tk.Button(root, text="=", width=5, height=2, font=("Arial", 14), command=evaluate)
equal_button.grid(row=5, column=2, columnspan=2)

root.mainloop()

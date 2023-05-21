import tkinter as tk

def evaluate(event=None):
    try:
        result = eval(entry.get())
        label.config(text="Result: " + str(result))
    except:
        label.config(text="Error")

def clear():
    entry.delete(0, tk.END)
    label.config(text="Result:")

window = tk.Tk()
window.title("Calculator")

entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=5)
entry.bind("<Return>", evaluate)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    button = tk.Button(window, text=text, width=5, command=lambda text=text: entry.insert(tk.END, text) if text != 'C' else clear())
    button.grid(row=row, column=col)

equal_button = tk.Button(window, text='=', width=5, command=evaluate)
equal_button.grid(row=4, column=3)

label = tk.Label(window, text="Result:")
label.grid(row=6, column=0, columnspan=4)

window.mainloop()

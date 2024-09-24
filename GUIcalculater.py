from tkinter import*
from tkinter.messagebox import showinfo

root=Tk()

root.title("Calculator")
root.geometry("300x400")

# Entry widget for calculation result
entry = Entry(root, width=16, font=("Arial", 24), borderwidth=2, relief="groove")
entry.grid(row=0, column=0, columnspan=4)

def button_click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, str(result))
    except Exception as e:
        showinfo("Error", "Invalid Input")

# Calculator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == 'C':
        Button(root, text=button, padx=20, pady=20, command=clear_entry).grid(row=row_val, column=col_val)
    elif button == '=':
        Button(root, text=button, padx=20, pady=20, command=calculate).grid(row=row_val, column=col_val)
    else:
        Button(root, text=button, padx=20, pady=20, command=lambda value=button: button_click(value)).grid(row=row_val, column=col_val)
        
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
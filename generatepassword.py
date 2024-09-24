from tkinter import *
import random
import string

def Password():
    window = Toplevel(root)
    window.geometry('400x200')
    window.title('Generator Tab')

    characterlist = ""

    def update_characterlist():
        nonlocal characterlist  
        characterlist = ""  
        if Capitalval.get():
            characterlist += string.ascii_uppercase
        if Smallval.get():
            characterlist += string.ascii_lowercase
        if Numberval.get():
            characterlist += string.digits
        if Symbolval.get():
            characterlist += string.punctuation

    def generate_password():
        update_characterlist()
        length = lengthval.get()  
        password = []
        if characterlist:  
            for i in range(length):
                password.append(random.choice(characterlist))
            result_label.config(text="Generated Password: " + "".join(password))
        else:
            result_label.config(text="Please select at least one character type!")

    Label(window, text='Generate Your Password').pack(pady=10)
    Button(window, text="Generate Password", command=generate_password).pack(pady=10)
    result_label = Label(window, text="")
    result_label.pack(pady=10)

root = Tk()
root.title("Random Password Generator")
root.geometry("455x455")

lengthval = IntVar()  
Capitalval = BooleanVar()
Smallval = BooleanVar()
Numberval = BooleanVar()
Symbolval = BooleanVar()

Label(root, text="Password Length").grid(row=0, column=1)
lengthentry = Entry(root, textvariable=lengthval)
lengthentry.grid(row=0, column=2)

Label(root, text="Select conditions for your password").grid(row=1, column=1)

Capital = Checkbutton(root, text="Capital Alphabet", variable=Capitalval)
Capital.grid(row=2, column=1)

Small = Checkbutton(root, text="Small Alphabet", variable=Smallval)
Small.grid(row=3, column=1)

Number = Checkbutton(root, text="Numbers", variable=Numberval)
Number.grid(row=4, column=1)

Symbol = Checkbutton(root, text="Symbols", variable=Symbolval)
Symbol.grid(row=5, column=1)

Button(root, text="Open Password Generator", command=Password).grid(row=6, column=2)

root.mainloop()

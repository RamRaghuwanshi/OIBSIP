from tkinter import*
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newfile():
    global file
    root.title("Umtitled-Notepad") 
    file=None
    textarea.delete(1.0,END)

def openfile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())
        f.close()

def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitle.txt',defaultextension=".txt",filetypes=[("All files","*.*"),("Text document","*.txt")])
        if file=="":
            file=None
        else:
            #save as a new file
            f=open(file,"w")
            f.write(textarea.get(1.0,END))
            f.close()

            root.title(os.path.basename(file)+"-Notepad")
    else:
        #save the file
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()

def quitapp():
    root.destroy()

def cut():
    textarea.event_generate("<<Cut>>")

def copy():
    textarea.event_generate("<<Copy>>")

def paste():
    textarea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad","Notepad by me")

if __name__=='__main__':
    #basis tkinder setup
    root=Tk()
    root.title("NOTEPAD")
    root.geometry("644x544")

    #add textarea
    textarea=Text(root,font="lucida 13")
    file=None
    textarea.pack(expand=TRUE,fill=BOTH)

    #create a menubar
    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)
    #to open new file
    filemenu.add_command(label="New",command=newfile)
    #to open existing file
    filemenu.add_command(label="Open",command=openfile)
    #to save current file
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitapp)
    menubar.add_cascade(label="File",menu=filemenu)

    #edit menu start
    editmenu=Menu(menubar,tearoff=0)
    #to give features of cut copy paste
    editmenu.add_command(label="Cut",command=cut)
    editmenu.add_command(label="Copy",command=copy)
    editmenu.add_command(label="Paste",command=paste)
    menubar.add_cascade(label="Edit",menu=editmenu)

    #help menu start
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="About notepad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)

    root.config(menu=menubar)

    #adding scrollbar
    Scroll=Scrollbar(textarea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=Scroll.set)

    root.mainloop()
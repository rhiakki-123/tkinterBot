

from tkinter import *
import tkinter.messagebox

root = Tk()

root.title("New way")

label_1 = Label(root, text="Name") #Define Dimention of lable
label_2 = Label(root, text="Password")#Define Dimention of lable
entry_1 = Entry(root) #This is text box used to enter data
entry_2 = Entry(root)

label_1.grid(row=0, sticky=E)  #Grid E,W,N,S
label_2.grid(row=1, sticky=E)

entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me logged in")#Check button is used for tick mark button
c.grid(columnspan=2)

def clickAk(event):
    for widget in root.winfo_children():
        widget.destroy()
    print("Hi der")
    butt1 = Button(root, fg="red", text=x)
    butt1.pack(anchor=NW, expand=1, fill=BOTH)


def clickIn(event):
    for widget in root.winfo_children():
        widget.destroy()
    print("go to new page")
    kd=["kedar","akash","Ketan","Nitin"]
    for x in kd:  # type: str
        abc="abc"
        abc=abc+x
        abc=Button(root, fg="red", text=x)
        abc.pack(anchor=NW, expand=1, fill=BOTH)
        abc.bind("<Button-1>", clickAk)


button_1 = Button(root, text="Login")
button_1.grid(row=4, column=1)
button_1.config(relief=GROOVE, borderwidth=5)
button_1.bind("<Button-1>", clickIn)

















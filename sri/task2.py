from tkinter import*    
window = Tk()
window.geometry('500x500')
window.title("Contact Book")
window.configure(bg="sky blue")
s=Label(window,text="CONTACT BOOK",foreground="brown",font=('Comic Sans Ms',18),bd=15,bg="sky blue")
s.pack()
window.resizable(0, 0)
contactlist = []
Name = StringVar()
Number = StringVar()
frame = Frame(window)
frame.pack(side=RIGHT,padx=130,pady=100,fill=X)
scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=RIGHT)
def Selected():
    return int(select.curselection()[0])

def AddContact():
    contactlist.append([Name.get(), Number.get()])
    Select_set()
def EDIT():
    if select.curselection():
        index = Selected()
        contactlist[index] = [Name.get(), Number.get()]
        Select_set()
def DELETE():
    if select.curselection():
        del contactlist[Selected()]
        Select_set()
def VIEW():
    if select.curselection():
        index = Selected()
        NAME, PHONE = contactlist[index]
        Name.set(NAME)
        Number.set(PHONE)

def EXIT():
    window.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)

Select_set()


Label(window, text='NAME', font='arial 12 bold', bg="sky blue").place(x=60, y=100)
Entry(window, textvariable=Name).place(x=170,y=100)
Label(window,text='PHONE NO',font='arial 12 bold',bg="sky blue").place(x=60,y=140)
Entry(window,textvariable=Number).place(x=170,y=140)
Button(window,text="ADD",font='arial 12 bold',bg="pink",command=AddContact).place(x=100,y=190)
Button(window,text="EDIT",font='arial 12 bold',bg="pink",command=EDIT).place(x=100,y=240)
Button(window,text="DELETE",font='arial 12 bold',bg="pink",command=DELETE).place(x=100,y=290)
Button(window,text="VIEW",font='arial 12 bold',bg="pink",command=VIEW).place(x=100,y=340)
Button(window,text="EXIT",font='arial 12 bold',bg="coral",command=EXIT).place(x=200,y=400)
window.mainloop()


import tkinter

screen  = tkinter.Tk()
screen.geometry("500x500")
screen.title(  "ADDRESS BOOK")

addressbook={}

def open():
    file2 = tkinter.filedialog.askopenfile()
    if file2 != None:
        items = file2.readlines()
        for item in items:
            lb.insert(tkinter.END,item)

def add():
    name = e1.get()
    adress = e1.get()
    mobile = e1.get()
    bday = e1.get()
    name = e1.get()




lb = tkinter.Listbox(screen)
e1 = tkinter.Entry(screen)
e2 = tkinter.Entry(screen)
e3 = tkinter.Entry(screen)
e4 = tkinter.Entry(screen)
e5 = tkinter.Entry(screen)
l1= tkinter.Label(screen,text="my address book")
l2= tkinter.Label(screen,text="name")
l3= tkinter.Label(screen,text = "address")
l4= tkinter.Label(screen,text = "mobile")
l5= tkinter.Label(screen,text="email")
l6= tkinter.Label(screen,text= "birthday")
b1 = tkinter.Button(screen,text="open",command=open)
b2 = tkinter.Button(screen,text = "save")
b3 = tkinter.Button(screen,text = "add/update")
b4 = tkinter.Button(screen,text = "edit")
b5 = tkinter.Button(screen,text= "delete")

lb.grid(row=2,column=1,rowspan=5)
e1.grid(row=2,column=4)
e2.grid(row=3,column=4)
e3.grid(row=4,column=4)
e4.grid(row=5,column=4)
e5.grid(row=6,column=4)
l1.grid(row=1,column=1)
l2.grid(row=2,column=3)
l3.grid(row=3,column=3)
l4.grid(row=4,column=3)
l5.grid(row=6,column=3)
l6.grid(row=5,column=3)
b1.grid(row=1,column=3)
b2.grid(row=7,column=4)
b3.grid(row=7,column=3)
b4.grid(row=7,column=2)
b5.grid(row=7,column=1)

screen.mainloop()
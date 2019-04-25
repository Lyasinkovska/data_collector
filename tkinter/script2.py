from tkinter import *

window = Tk()

def converter():
    gr = float(e1_value.get())*1000
    t1.insert(END, gr)
    p = float(e1_value.get()) * 2.20462
    t2.insert(END, p)
    o = float(e1_value.get()) * 35.274
    t3.insert(END, o)

l1 = Label(window, text='Kg')
l1.grid(row=0, column=0)

l2 = Label(window, text='grams')
l2.grid(row=2, column=0)

l3 = Label(window, text='pounds')
l3.grid(row=2, column=1)

l4 = Label(window, text='ounces')
l4.grid(row=2, column=2)

b1 = Button(window, text = "Convert", command = converter)
b1.grid(row=0, column=2)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row  = 1, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row  = 1, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row  = 1, column = 2)

window.mainloop()


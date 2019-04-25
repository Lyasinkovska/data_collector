from tkinter import *
from datetime import datetime

window = Tk()

def age():
    age = int(datetime.now().year) - int(e1_value.get())
    t1.insert(END, age)


b1 = Button(window, text = "Додати  в список", command = age)
b1.grid(row=0, column=0)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 20)
t1.grid(row  = 0, column = 2)

window.mainloop()


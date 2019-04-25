from tkinter import *
import backend


def get_selected_row(event):
    try:
        global selected_row
        index = lb1.curselection()[0]
        selected_row = lb1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[3])
        e3.delete(0, END)
        e3.insert(END, selected_row[2])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
        print(event)
    except IndexError:
        pass


def view_command():
    lb1.delete(0, END)
    for row in backend.view():
        lb1.insert(END, row)


def search_command():
    lb1.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        lb1.insert(END, row)


def add_command():
    backend.add(title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    lb1.delete(0, END)
    lb1.insert(END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get()))


def delete_command():
    backend.delete(selected_row[0])


def update_command():
    backend.update(selected_row[0], title_value.get(), author_value.get(), year_value.get(), isbn_value.get())


def close_command():
    window.destroy()


window = Tk()


window.wm_title("BookStore")
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Year')
l2.grid(row=1, column=0)

l3 = Label(window, text='Author')
l3.grid(row=0, column=2)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)

title_value = StringVar()
e1 = Entry(window, textvariable=title_value)
e1.grid(row=0, column=1)

year_value = StringVar()
e2 = Entry(window, textvariable=year_value)
e2.grid(row=1, column=1)

author_value = StringVar()
e3 = Entry(window, textvariable=author_value)
e3.grid(row=0, column=3)

isbn_value = StringVar()
e4 = Entry(window, textvariable=isbn_value)
e4.grid(row=1, column=3)

b1 = Button(window, text="View all", width=17, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=17, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=17, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=17, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=17, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=17, command=close_command)
b6.grid(row=7, column=3)

lb1 = Listbox(window, height=10, width=35)
lb1.grid(row=2, column=0, rowspan=6, columnspan=2)

sc = Scrollbar(window)
sc.grid(row=2, column=2, rowspan=10)

lb1.configure(yscrollcommand=sc.set)
sc.configure(command=lb1.yview)

lb1.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()

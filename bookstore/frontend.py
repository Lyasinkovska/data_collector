from tkinter import *
from backend import Database

database = Database("bookstore.db")


class Window(object):

    def __init__(self, window):

        self.window = window
        self.window.wm_title("BookStore")

        l1 = Label(window, text='Title')
        l1.grid(row=0, column=0)

        l2 = Label(window, text='Year')
        l2.grid(row=1, column=0)

        l3 = Label(window, text='Author')
        l3.grid(row=0, column=2)

        l4 = Label(window, text='ISBN')
        l4.grid(row=1, column=2)

        self.title_value = StringVar()
        self.e1 = Entry(window, textvariable=self.title_value)
        self.e1.grid(row=0, column=1)

        self.year_value = StringVar()
        self.e2 = Entry(window, textvariable=self.year_value)
        self.e2.grid(row=1, column=1)

        self.author_value = StringVar()
        self.e3 = Entry(window, textvariable=self.author_value)
        self.e3.grid(row=0, column=3)

        self.isbn_value = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_value)
        self.e4.grid(row=1, column=3)

        b1 = Button(window, text="View all", width=17, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search entry", width=17, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add entry", width=17, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update selected", width=17, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete selected", width=17, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=17, command=self.close_command)
        b6.grid(row=7, column=3)

        self.lb1 = Listbox(window, height=10, width=35)
        self.lb1.grid(row=2, column=0, rowspan=6, columnspan=2)

        sc = Scrollbar(window)
        sc.grid(row=2, column=2, rowspan=10)

        self.lb1.configure(yscrollcommand=sc.set)
        sc.configure(command=self.lb1.yview)

        self.lb1.bind("<<ListboxSelect>>", self.get_selected_row)

    def get_selected_row(self, event):
        try:
            index = self.lb1.curselection()[0]
            self.selected_row = self.lb1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.selected_row[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.selected_row[3])
            self.e3.delete(0, END)
            self.e3.insert(END, self.selected_row[2])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_row[4])
            print(event)
        except IndexError:
            pass

    def view_command(self):
        self.lb1.delete(0, END)
        for row in database.view():
            self.lb1.insert(END, row)

    def search_command(self):
        self.lb1.delete(0, END)
        for row in database.search(self.title_value.get(), self.author_value.get(), self.year_value.get(),
                                   self.isbn_value.get()):
            self.lb1.insert(END, row)

    def add_command(self):
        database.add(self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get())
        self.lb1.delete(0, END)
        self.lb1.insert(END, (self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()))

    def delete_command(self):
        database.delete(self.selected_row[0])

    def update_command(self):
        database.update(self.selected_row[0], self.title_value.get(), self.author_value.get(), self.year_value.get(),
                        self.isbn_value.get())

    def close_command(self):
        window.destroy()


window = Tk()
Window(window)
window.mainloop()

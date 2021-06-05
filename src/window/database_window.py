# New window instance for database mod
from tkinter import Button, Entry, Label, Toplevel

from src.fetchers.json_obj import JsonObj


class DatabaseWindow:

    def __init__(self):
        self.json_obj = JsonObj()
        dat = Toplevel()
        dat.title("Speechy - Database")
        # setting window pos
        screen_width = dat.winfo_screenwidth()
        screen_height = dat.winfo_screenheight()
        x = (screen_width / 2) - (800 / 2)
        y = (screen_height / 2) - (250 / 2)
        dat.geometry('%dx%d+%d+%d' % (800, 400, x, y + 220))
        dat.resizable(height=False, width=False)

        # Text label - Addition
        lab_name = Label(dat, text="Add new author ")
        lab_name.config(font=("Calibri Light", 16))
        lab_name.place(x=25, y=10)

        # Text label - author's name
        text_author_name = Label(dat, text="Name: ")
        text_author_name.config(font=("Calibri Light", 14))
        text_author_name.place(x=25, y=50)

        # Input - author's name
        E1 = Entry(dat, bd=1)
        E1.place(x=25, y=80)

        # Text label - author info
        text_author_info = Label(dat, text="Bio: ")
        text_author_info.config(font=("Calibri Light", 14))
        text_author_info.place(x=25, y=120)

        # Input - author's info
        E2 = Entry(dat, bd=1)
        E2.place(x=25, y=150, height=100, width=200)

        # Text label - Delete
        lab_rem_name = Label(dat, text="Remove author ")
        lab_rem_name.config(font=("Calibri Light", 16))
        lab_rem_name.place(x=500, y=10)

        # Text label - delete author
        text_del_author = Label(dat, text="Name: ")
        text_del_author.config(font=("Calibri Light", 14))
        text_del_author.place(x=500, y=50)

        # Input - author's name to delete
        E3 = Entry(dat, bd=1)
        E3.place(x=500, y=80)

        # Function to get from input
        def del_record():
            # json obj instance
            read_rec = E3.get()
            print("User want to delete" + read_rec)
            print("JSON operation...")
            delete = self.json_obj.del_authors(str(read_rec))

        # Function to get from input
        def add_record_name():
            # Reading input from Name and Bio fields
            read_rec_name = E1.get()
            read_rec_info = E2.get()

            print("User want to add" + read_rec_name)
            print("JSON operation...")

            # Database update
            add = self.json_obj.insert_author_name(str(read_rec_name), str(read_rec_info))

        # Buttons for records addition and removal
        add_name_button = Button(dat, text="Add", command=add_record_name)
        add_name_button.place(x=25, y=280)

        del_button = Button(dat, text="Delete", command=del_record)
        del_button.place(x=500, y=110)

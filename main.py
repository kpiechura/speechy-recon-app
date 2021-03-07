from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3
from PIL import Image, ImageTk
import platform

import webbrowser
import time

# Class with configuration of Txt2S
class Speech:

    def __init__(self, line):
        engine = pyttsx3.init()
        voice = engine.getProperty('voice')
        engine.setProperty(voice, "!v/f1")

        # Saying things...
        engine.say(line)
        engine.runAndWait()


# Main class of a GUI
class MainWindow:

    def __init__(self, master):
        self.master = master
        master.title("Speechy App")
        master.geometry("800x400")

        # Reserve some place for img/test img placement
        load = Image.open("icons/king.png")
        render = ImageTk.PhotoImage(load)
        self.img = Label(master, image=render)
        self.img.image = render
        self.img.place(x=400, y=20)

        # Title screen
        self.label = Label(master, text="Speechy")
        self.label.config(font=("Calibri Light", 24))
        self.label.place(x=25, y=30)

        # Title screen
        say_line = "A database for your favorite writers"
        Speech("Speechy.. " + str(say_line))

        self.label1 = Label(master, text=say_line)
        self.label1.config(font=("Calibri Light italic", 16))
        self.label1.place(x=25, y=70)

        self.pick_label = Label(master, text="Pick writer: ")
        self.pick_label.config(font=("Calibri Light", 14))
        self.pick_label.place(x=25, y=110)
        # End of title screen

        # TO DO: Change to read from file maybe?
        # List of writers to pick...
        write = ('Stephen King', 'Adam Mickiewicz', 'Graham Masterton', 'Katarzyna Grohola',
                 'Juliusz Slowacki KEKW')
        write_var = StringVar(master, value=write)

        self.writers_list = Listbox(master, listvariable=write_var, height=5)

        # Scrollbar - not working for now
        # self.scrollbar = Scrollbar(
        #     master,
        #     orient='vertical',
        #     command=self.writers_list.yview
        # )
        # self.writers_list['yscrollcommand'] = self.scrollbar.set
        #
        # self.scrollbar.grid(
        #     column=1,
        #     row=1,
        #     sticky='ns')

        self.writers_list.place(x=25, y=150)

        # Handle events for list
        def items_selected(event):
            """ handle item selected event
            """
            # get selected indices
            selected_indices = self.writers_list.curselection()
            # get selected items
            selected_langs = ",".join([self.writers_list.get(i) for i in selected_indices])
            msg = f'You selected: {selected_langs}'
            print(selected_langs)
            Speech(selected_langs)

            showinfo(
                title='Information',
                message=msg)
            return selected_langs

        self.writers_list.bind('<<ListboxSelect>>', items_selected)
        # End of listbox

        # Buttons:
        self.greet_button = Button(master, text="Pick", command=self.greet)
        self.greet_button.place(x=25, y=250)

        self.help_button = Button(master, text="About", command=self.help)
        self.help_button.place(x=0, y=0)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x=25, y=350)

    def greet(self):
        print("Writer picked!")
        Speech("Time to throw pogchamp!")

    def help(self):
        showinfo(
            title='About',
            message="App version: 0.1v\n \n"
                    "Authors:\nKamil Piechura\n"
                    "Lukasz Bugajski \n"
                    "Dariusz Kowalczyk"
        )


root = Tk()
my_gui = MainWindow(root)

root.mainloop()



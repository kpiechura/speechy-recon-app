from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3
import json
from PIL import Image, ImageTk
import concurrent.futures
import sys

import webbrowser
import time

# Read info from JSON obj
class JsonObj():

    writer_info = ""
    #path_to_img = ""

    def __init__(self, writer_info):
        with open("writer.json", encoding='utf-8') as jsondata:
            data = json.load(jsondata)

        # Part to show proper info about writer
        print(data[writer_info][0]['info'])
        writer_info = (data[writer_info][0]['info'])
        self.writer_info = writer_info

        # Part for loading proper img
        # print(data[path_to_img][0]['img'])
        # path_to_img = (data[path_to_img][0]['img'])
        # self.path_to_img = path_to_img

    def read_sur(self):
        with open("writer.json", encoding='utf-8') as jsondata:
            data = json.load(jsondata)

        for key in data:
            print (key)

        jsondata.close()


# Class with configuration of Txt2S
class Speech:

    def __init__(self, line):
        engine = pyttsx3.init()
        voice = engine.getProperty('voice')
        engine.setProperty(voice, "!v/f1")

        # Saying things...
        engine.say(line)
        engine.runAndWait()
        del engine

# Class to operate on img files
class Img:

    def __init__(self, master, path_to_img):
        load = Image.open("icons/" + path_to_img + ".png")
        render = ImageTk.PhotoImage(load)
        self.img = Label(master, image=render)
        self.img.image = render
        self.img.place(x=400, y=20)

# Multi-threading needs to be implemented - now t2s is called before displaying output
# def parallel(text):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         future_tasks = {executor.submit(Speech, text), executor.submit(typing, text)}
#         for future in concurrent.futures.as_completed(future_tasks):
#             try:
#                 data = future.result()
#             except Exception as e:
#                 print(e)

# Main class of a GUI
class MainWindow:

    def __init__(self, master):
        self.master = master
        master.title("Speechy App")
        master.geometry("800x600")
        # master.configure(bg='lightgrey')

        # Reserve some place for default img placement
        Img(master, "Stephen King")

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
        self.pick_label.place(x=25, y=130)

        self.info_lab = Label(master,
                              text="About writer:")
        self.info_lab.config(font=("Calibri Light", 14))
        self.info_lab.place(x=25, y=370)
        # End of title screen

        # TO DO: Change to read from file maybe?
        # List of writers to pick...
        write = ('Stephen King', 'Adam Mickiewicz', 'Graham Masterton', 'Katarzyna Grohola',
                 'Juliusz Slowacki KEKW', 'Norman Davies', 'Ken Follett')
        write_var = StringVar(master, value=write)

        self.writers_list = Listbox(master, listvariable=write_var, height=6, font=("Calibri Light", 12))
        # Scrollbar for listbox
        scrollbar = Scrollbar(self.writers_list, orient="vertical")
        scrollbar.config(command=self.writers_list.yview)
        scrollbar.place(x=145, y=0)

        self.writers_list.config(yscrollcommand=scrollbar.set)

        self.writers_list.place(x=25, y=170)

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

            # Text about author
            json_obj = JsonObj(selected_langs)
            self.info_lab = Label(master, text=json_obj.writer_info, wraplength=700, justify='center')
            self.info_lab.config(font=("Calibri Light", 12))
            self.info_lab.place(x=25, y=400)

            # Show author's image
            Img(master, selected_langs)

            # showinfo(
            #     title='Information',
            #     message=msg)
            return selected_langs

        self.writers_list.bind('<<ListboxSelect>>', items_selected)
        # End of listbox

        # Buttons:
        self.greet_button = Button(master, text="Pick", command=self.greet)
        self.greet_button.place(x=25, y=310)

        self.help_button = Button(master, text="About", command=self.help)
        self.help_button.place(x=0, y=0)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x=45, y=0)


    def greet(self):
        print("Writer picked!")
        Speech("Time to throw pogchamp!")

    def help(self):
        message="App version: 0.1v\n\nAuthors:" \
                "\n\nKamil Piechura" \
                "\n\nLukasz Bugajski" \
                "\n\nDariusz Kowalczyk"
        Speech(message)
        showinfo(
            title='About',
            message=message
        )


root = Tk()
my_gui = MainWindow(root)

root.mainloop()

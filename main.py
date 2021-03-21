import json
from tkinter import *
from tkinter.messagebox import showinfo

import pyttsx3
import speech_recognition as sr
from PIL import Image, ImageTk


# Class for speech recognition
class SpeechRecog():

    def __init__(self):

        r = sr.Recognizer()
        # check micro status
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)

                # Debug list of micros
                print(sr.Microphone.list_microphone_names())
                print("Listening...")
                audio = r.listen(source, timeout=2)
        except OSError as ose:
            showinfo(
                title='Error',
                message='Microphone not detected!'
            )
            print("ERROR: Microphone not detected! Aborting sr module!\n" + str(ose))

        try:
            text = r.recognize_google(audio, language="en-in")
            print("You said: {}".format(text))

        except Exception as e:
            showinfo(
                title='Error',
                message='ERROR: Speechy could not understand you!'
            )
            print("ERROR during speech-recon!" + e)


# Read info from JSON obj
class JsonObj():

    writer_info = ""

    # Init with default value
    def __init__(self, writer_info="Adam Mickiewicz"):
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
            authors = []

        for key in data:
            authors.append(key)

        # Tuple for purpose of init of listbox with names from json file
        tuple(authors)
        jsondata.close()

        return tuple(authors)

    # Delete authors - impl for DatabaseWindow class
    def del_authors(self, author_name=" "):

        with open("writer.json", encoding='utf-8') as jsondata:
            data = json.load(jsondata)

            found = False
            for i in data:
                if i == author_name:
                    found = True
                    data.pop(i)
                    showinfo(
                        title='Remove record',
                        message='Record' + author_name + 'has been removed!'
                    )
                    break

            if found == False:
                showinfo(
                    title='Remove record',
                    message='Record cannot be found!'
                )

            # overwrite json
            open("writer.json", "w").write(
                 json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            )
        return author_name


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
        load = load.resize((300, 345), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        self.img = Label(master, image=render)
        self.img.image = render
        self.img.place(x=400, y=40)

# Multi-threading needs to be implemented - now t2s is called before displaying output
# def parallel(text):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         future_tasks = {executor.submit(Speech, text), executor.submit(typing, text)}
#         for future in concurrent.futures.as_completed(future_tasks):
#             try:
#                 data = future.result()
#             except Exception as e:
#                 print(e)


# New window instance for database mod
class DatabaseWindow:

    def __init__(self):
        dat = Toplevel()
        dat.title("Speechy - Database")
        dat.geometry("800x200+275+75")
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
        E2.place(x=25, y=150)

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
            read_rec = E3.get()
            print("User want to delete" + read_rec)
            print("JSON operation...")
            delete = JsonObj.del_authors(str(read_rec))


        del_button = Button(dat, text="Delete", command=del_record)
        del_button.place(x=500, y=110)


# Main class of a GUI
class MainWindow:

    selected_langs = ""

    def __init__(self, master):

        self.master = master
        master.title("Speechy App")
        master.geometry("800x600")
        master.resizable(0, 0)
        # master.configure(bg='lightgrey')

        # Reserve some place for default img placement
        Img(master, "default")

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

        # List of writers to pick...
        # TO DO fix the way the read_sur method is called. Currently temporary object of JsonObj is created
        self.json_temp = JsonObj()
        write = self.json_temp.read_sur()
        write_var = StringVar(master, value=write)

        self.writers_list = Listbox(master, listvariable=write_var, height=6, font=("Calibri Light", 12))

        # Scrollbar for listbox
        scrollbar = Scrollbar(self.writers_list, orient="vertical")
        scrollbar.config(command=self.writers_list.yview)
        scrollbar.place(x=145, y=0)

        self.writers_list.config(yscrollcommand=scrollbar.set)

        self.writers_list.place(x=25, y=170)
        self.json_obj = None

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
            self.json_obj = JsonObj(selected_langs)
            self.info_lab = Label(master, text=self.json_obj.writer_info, wraplength=700, justify='center')
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
        self.greet_button = Button(master, text="Speech", command=self.greet)
        self.greet_button.place(x=25, y=310)

        # Calling sr module - further pass to fun required
        self.listen_button = Button(master, text="Listen", command=SpeechRecog)
        self.listen_button.place(x=150, y=310)

        self.database_button = Button(master, text="Database", command=DatabaseWindow)
        self.database_button.place(x=85, y=0)

        self.help_button = Button(master, text="About", command=self.help)
        self.help_button.place(x=0, y=0)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(x=45, y=0)

    # Pass json value
    def greet(self):
        print("Writer picked!")
        try:
            Speech(self.json_obj.writer_info)
        except Exception as e:
            print(e)
        # Speech(line)

    def help(self):
        message = "App version: 0.1v\n\nAuthors:" \
                "\n\nKamil Piechura" \
                "\n\nLukasz Bugajski" \
                "\n\nDariusz Kowalczyk"
        Speech(message)
        showinfo(
            title='About',
            message=message
        )


if __name__ == '__main__':
    root = Tk()
    my_gui = MainWindow(root)

    root.mainloop()

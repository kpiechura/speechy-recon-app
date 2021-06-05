# Main class of a GUI
from tkinter import Button, Label, Listbox, Scrollbar, StringVar
from src.fetchers.img import Img
from src.speech.speech import Speech
from src.fetchers.json_obj import JsonObj
from src.speech.speech_recog import SpeechRecog
from src.window.database_window import DatabaseWindow
from tkinter.messagebox import showinfo

class MainWindow:
    selected_langs = " "

    def __init__(self, master):

        self.master = master
        master.title("Speechy App")

        # setting window pos
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x = (screen_width / 2) - (800 / 2)
        y = (screen_height / 2) - (600 / 2)
        master.geometry('%dx%d+%d+%d' % (800, 600, x, y))
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

            return selected_langs

        self.writers_list.bind('<<ListboxSelect>>', items_selected)
        # End of listbox

        # Buttons:
        self.greet_button = Button(master, text="Speech", command=self.greet)
        self.greet_button.place(x=25, y=310)

        # Calling sr module - further pass to fun required
        self.listen_button = Button(master, text="Listen", command=self.speech_recog)
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
        message = "App version: 0.6v\n\nAuthors:" \
                  "\n\nKamil Piechura" \
                  "\n\nLukasz Bugajski" \
                  "\n\nDariusz Kowalczyk"
        # Speech(message)
        showinfo(
            title='About',
            message=message
        )

    def speech_recog(self):

        recognizer = SpeechRecog(self.master)
        self.json_obj = recognizer.json_obj

from tkinter import Label
from tkinter.messagebox import showinfo

import speech_recognition as sr

from src.fetchers.img import Img
from src.fetchers.json_obj import JsonObj


# Class for speech recognition
class SpeechRecog:

    def __init__(self, window):

        r = sr.Recognizer()
        text = ''
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
        except Exception as e:
            showinfo(
                title='Error',
                message='ERROR: Speechy could not hear you!'
            )
            print("ERROR during speech-recon!" + str(e))

        try:
            text = r.recognize_google(audio, language="en-in")
            print("You said: {}".format(text))
            # self.json_obj = JsonObj.__init__(text)
            # print(self.json_obj.writer_info)

        except Exception as e:
            showinfo(
                title='Error',
                message='ERROR: Speechy could not understand you!'
            )
            print("ERROR during speech-recon!" + str(e))

        # Text about author
        self.json_obj = JsonObj(text)
        self.info_lab = Label(window, text=self.json_obj.writer_info, wraplength=700, justify='center')
        self.info_lab.config(font=("Calibri Light", 12))
        self.info_lab.place(x=25, y=400)

        # Show author's image
        Img(window, text)

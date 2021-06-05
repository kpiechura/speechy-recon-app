# Class to operate on img files
import re
from tkinter import Image, Label
from tkinter.messagebox import showinfo

from PIL import Image, ImageTk


class Img:

    def __init__(self, master, path_to_img):

        # check var for one word instance
        one_word = False

        if " " not in path_to_img:
            one_word = True

        # split name to make possible to get via catalog path
        split_name = re.findall('.[^A-Z]*', path_to_img)

        # If there is no image for newly created author, call default avatar img
        try:
            load = Image.open("icons/" + path_to_img + ".png")
        except:

            # get image from Google Search engine
            # check if name given is one-word/many-word
            if one_word:
                try:
                    load = Image.open("simple_images/"
                                      + path_to_img
                                      + "/"
                                      + path_to_img + "_1.jpeg")
                except:
                    showinfo(
                        title='Error',
                        message='Speechy could not get your author image from Google! '
                                'Using default avatar!'
                    )
                    load = Image.open("icons/default_avatar.png")
            else:
                try:
                    load = Image.open("simple_images/"
                                      + split_name[0].replace(" ", "")
                                      + "_" + split_name[1] + "/"
                                      + path_to_img + "_1.jpeg")
                except:
                    showinfo(
                        title='Error',
                        message='Speechy could not get your author image from Google! '
                                'Using default avatar!'
                    )
                    load = Image.open("icons/default_avatar.png")

        load = load.resize((300, 345), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        self.img = Label(master, image=render)
        self.img.image = render
        self.img.place(x=400, y=40)

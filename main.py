from tkinter import *

from src.window.main_window import MainWindow

if __name__ == '__main__':
    root = Tk()
    my_gui = MainWindow(root)

    root.mainloop()

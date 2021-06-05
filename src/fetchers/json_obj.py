import json
from src.fetchers.get_google_img import GetGoogleImg
from tkinter.messagebox import showinfo
import wikipedia

# Read info from JSON obj
class JsonObj:
    writer_info = " "

    # Init with default value
    def __init__(self, writer_info=""):

        # Checking if database instance exists
        try:
            with open("writer.json", encoding='utf-8') as jsondata:
                data = json.load(jsondata)
        except:
            showinfo(
                title='Database instance error',
                message='Database instance cannot be found! Aborting!'
            )
            exit(-1)

        # Part to show proper info about writer
        try:
            if writer_info:
                print(data[writer_info][0]['info'])
                writer_info = (data[writer_info][0]['info'])
                self.writer_info = writer_info
        except:
            showinfo(
                title='Database read fault',
                message='Database cannot found that record!'
            )

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
                        message='Record ' + author_name + ' has been removed!'
                    )
                    break

            if not found:
                showinfo(
                    title='Remove record',
                    message='Record cannot be found!'
                )

            # overwrite json file with latest changes
            open("writer.json", "w").write(
                json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            )

        return author_name

    # Adding new key with author's name and info to json
    def insert_author_name(self, author_name=" ", input_author_info=" "):
        with open("writer.json", encoding='utf-8') as jsondata:
            data = json.load(jsondata)

            # get picture from Google
            GetGoogleImg(author_name)

            # if wiki summary is available --> insert that
            # if not --> insert input set by user
            try:
                author_info = (wikipedia.summary(author_name, sentences=4))
            except:
                author_info = input_author_info

            data[author_name] = [{"img": "icons/default_avatar.png", "info": author_info}]
            # overwrite json
            open("writer.json", "w").write(
                json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
            )

            showinfo(
                title='Add record',
                message='Record ' + author_name + ' added to database! Added with found Google image!'
            )
import pyttsx3


# Class with configuration of Txt2S
class Speech:

    # default config for t2s module
    def change_voice(self, engine, language, gender='VoiceGenderFemale'):
        for voice in engine.getProperty('voices'):
            if language in voice.languages and gender == voice.gender:
                engine.setProperty('voice', voice.id)
                return True

        # showinfo(
        #     title='Speechy - language',
        #     message='NOTE: Please, consider installing en_US language pack'
        # )

    def __init__(self, line):
        engine = pyttsx3.init()
        self.change_voice(engine, "en_US", "VoiceGenderFemale")
        # Setting speeching speed
        engine.setProperty('rate', 180)
        voice = engine.getProperty('voice')
        engine.setProperty(voice, "!v/f1")

        # Saying things...
        engine.say(line)
        engine.runAndWait()

        del engine

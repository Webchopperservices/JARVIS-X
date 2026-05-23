import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)


def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
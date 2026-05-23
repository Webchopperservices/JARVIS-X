import os
import webbrowser
import datetime
import pyautogui
import wikipedia
import pywhatkit

from core.speak import speak
from core.utils import get_time, get_date



def execute_command(command):

    # =========================
    # GREETING
    # =========================

    if "hello" in command:
        speak("Hello Sir")

    elif "how are you" in command:
        speak("I am doing great Sir")

    # =========================
    # TIME
    # =========================

    elif "time" in command:
        speak(f"Current time is {get_time()}")

    # =========================
    # DATE
    # =========================

    elif "date" in command:
        speak(f"Today's date is {get_date()}")

    # =========================
    # OPEN WEBSITES
    # =========================

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    # =========================
    # SEARCH GOOGLE
    # =========================

    elif "search" in command:

        query = command.replace("search", "")

        if query:
            speak(f"Searching {query}")
            webbrowser.open(f"https://www.google.com/search?q={query}")

    # =========================
    # PLAY YOUTUBE
    # =========================

    elif "play" in command:

        song = command.replace("play", "")

        if song:
            speak(f"Playing {song}")
            pywhatkit.playonyt(song)

    # =========================
    # WIKIPEDIA
    # =========================

    elif "wikipedia" in command:

        topic = command.replace("wikipedia", "")

        speak("Searching Wikipedia")

        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        except:
            speak("Sorry, I could not find anything")

    # =========================
    # OPEN APPS
    # =========================

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "open command prompt" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    # =========================
    # SCREENSHOT
    # =========================

    elif "take screenshot" in command:

        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"screenshots/screenshot_{now}.png"

        os.makedirs("screenshots", exist_ok=True)

        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

        speak("Screenshot captured")

    # =========================
    # SYSTEM COMMANDS
    # =========================

    elif "shutdown" in command:
        speak("Shutting down the system")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting the system")
        os.system("shutdown /r /t 5")

    # =========================
    # EXIT
    # =========================

    elif "exit" in command or "stop" in command:
        speak("Goodbye Sir")
        return False

    else:
        speak("Command not recognized")

    return True
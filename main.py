import datetime

from core.speak import speak
from core.voice import listen
from core.commands import execute_command



def wish_user():

    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning Sir")

    elif hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("I am Jarvis. How can I help you?")



def main():

    wish_user()

    while True:

        try:

            command = listen()

            if command:
                running = execute_command(command)

                if not running:
                    break

        except KeyboardInterrupt:
            speak("Program terminated")
            break

        except Exception as e:
            print(e)
            speak("An error occurred")



if __name__ == "__main__":
    main()
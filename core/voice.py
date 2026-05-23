import queue
import json
import os
import sounddevice as sd
from vosk import Model, KaldiRecognizer

from config import MODEL_PATH

# =========================
# CHECK MODEL
# =========================

if not os.path.exists(MODEL_PATH):
    print("Model not found")
    exit()

# =========================
# LOAD MODEL
# =========================

model = Model(MODEL_PATH)

# Better recognizer
recognizer = KaldiRecognizer(model, 16000)

# Queue
q = queue.Queue()

# =========================
# AUDIO CALLBACK
# =========================

def callback(indata, frames, time, status):

    if status:
        print(status)

    q.put(bytes(indata))

# =========================
# LISTEN FUNCTION
# =========================

def listen():

    try:

        with sd.RawInputStream(
            samplerate=16000,
            blocksize=4000,
            dtype='int16',
            channels=1,
            callback=callback
        ):

            print("Listening...")

            while True:

                data = q.get()

                # Accept voice
                if recognizer.AcceptWaveform(data):

                    result = json.loads(recognizer.Result())

                    text = result.get("text", "").strip()

                    # Ignore empty noise
                    if text != "":

                        print(f"You Said: {text}")

                        return text.lower()

    except Exception as e:
        print("Microphone Error:", e)
        return ""
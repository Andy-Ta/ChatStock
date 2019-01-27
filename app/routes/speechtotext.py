import time
import socket
import pyttsx
import speech_recognition as sr
from googletrans import Translator

def speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("'recognizer' must be Recognizer instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`'microphone' must be Microphone instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        recognizer.pause_threshold = 0.5
        audio = recognizer.listen(source)
        
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        print("Recognition started...")
        start_time = time.time()
        response["transcription"] = recognizer.recognize_google(audio)
        elapsed_time = time.time() - start_time
        print("Time taken to recognize speech: " + str(elapsed_time))
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    PROMPT_LIMIT = 5

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    translator = Translator()

    instruction = (
        "What do you want to say?\n"
    )

    print(instruction)

    for i in range(PROMPT_LIMIT):
        word = speech_from_mic(recognizer, microphone)
        if word["transcription"]:
            break
        if word["success"]:
            break
        print("I didn't catch that. What did you say?\n")

    if word["error"]:
        print("ERROR: {}".format(word["error"]))

    recorded = "{}".format(word["transcription"])
    print(recorded)

    print("\nTranslation started...")
    start_time = time.time()
    translated = translator.translate(recorded, dest='fr').text
    elapsed_time = time.time() - start_time
    print("Time taken to translate: " + str(elapsed_time))
    print(translated)

    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'french')
    engine.say(translated)
    engine.runAndWait()

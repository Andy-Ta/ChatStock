import time

from googletrans import Translator
import requests
import speech_recognition as sr


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

        translator = Translator()
        print("\nTranslation started...")
        start_time = time.time()
        print(response)
        translated = translator.translate(response['transcription'], dest='fr').text
        elapsed_time = time.time() - start_time
        print("Time taken to translate: " + str(elapsed_time))
        print(translated)

        r = requests.post("http://localhost:5000/translate", json={'message': translated})
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


if __name__ == "__main__":
    PROMPT_LIMIT = 99999

    while True:
        recognizer = sr.Recognizer()
        microphone = sr.Microphone()

        instruction = (
            "What do you want to say?\n"
        )

        print(instruction)

        word = speech_from_mic(recognizer, microphone)

        if word["error"]:
            print("ERROR: {}".format(word["error"]))

        recorded = "{}".format(word["transcription"])
        print(recorded)

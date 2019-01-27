import json
import time

from flask import request
from app import app
import pyttsx3 as pyttsx
from googletrans import Translator


@app.route('/translate', methods=['POST'])
def translate():
    message = request.get_json(force=True)['message']
    translator = Translator()
    print("\nTranslation started...")
    start_time = time.time()
    translated = translator.translate(message, dest='fr').text
    elapsed_time = time.time() - start_time
    print("Time taken to translate: " + str(elapsed_time))
    print(translated)

    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice)
    engine.setProperty('voice', 'french')
    engine.say(translated)
    engine.runAndWait()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}


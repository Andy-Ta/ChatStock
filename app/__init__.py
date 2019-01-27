from flask import Flask

app = Flask(__name__)
app.secret_key = 'gietmamaw'

import json
import time

from flask import request
from app import app
import pyttsx as pyttsx


@app.route('/translate', methods=['POST'])
def translate():
    message = request.get_json(force=True)['message']

    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        print(voice)
    engine.setProperty('voice', 'french')
    engine.say(message)
    engine.runAndWait()
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

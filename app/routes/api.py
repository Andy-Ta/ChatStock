from flask import request, abort, session, jsonify
from app import app
from watson_developer_cloud import ConversationV1
import json

conversation = []
context = []


@app.route('/api/v1.0/start', methods=['GET'])
def start():
    conversation.append(ConversationV1(
        username='87eaf392-180e-4bc8-b4ec-3bad35575a6e',
        password='XHU6f7WvRZ42',
        version='2017-01-27'
    ))
    context.append(None)

    session['id'] = len(conversation) - 1

    return str(session['id'])


@app.route('/api/v1.0/send', methods=['POST'])
def message():

    response = conversation[session['id']].message(
        workspace_id='edbd27fc-5ae5-4a8b-80f0-8ed11e09c23b',
        input={
            'text': request.get_json(force=True)['message']
        },
        context=context[session['id']]
    )
    context[session['id']] = response['context']

    return json.dumps(response)

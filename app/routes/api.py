from flask import request, abort, session, jsonify
from app import app
from watson_developer_cloud import ConversationV1
from twilio.rest import Client
import json

conversation = []
context = []

account_sid = "ACb6cdefc1dec9c4ae8e825bb47ecede5c"
auth_token = "0e27a5f88443ab7c7ef8a0d18ba64c08"


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


@app.route('/api/v1.0/text', methods=['POST'])
def text():
    price = request.get_json(force=True)['price']
    phone = request.get_json(force=True)['phone']
    stock = request.get_json(force=True)['stock']

    if phone[0] != "1":
        phone = "1" + phone

    client = Client(account_sid, auth_token)

    response = client.api.account.messages.create(
        to="+" + phone,
        from_="+15146121818",
        body="Hello, your stock " + stock + " has reached " + price ".")
    return json.dumps(response)

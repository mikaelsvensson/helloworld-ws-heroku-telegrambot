from flask import request, Response
from twx.botapi import Message
from app import application
from app import bot
import json


@application.route('/')
def index():
    return "Hej"


@application.route('/incoming', methods=['POST'])
def incoming():
    j = json.loads(request.get_data())
    m = j['message']
    msg = Message.from_result(m)
    print msg

    try:
        chat_id = msg.chat.id
        print 'Responding to chat %i using token %s' % (chat_id, bot.token)
        resp = bot.send_message(
            chat_id=chat_id,
            text='You said: %s' % msg.text,
            parse_mode=None,
            disable_web_page_preview=None,
            reply_to_message_id=None,
            reply_markup=None,
            disable_notification=False).wait()
    except Exception as e:
        print "ERROR: ", e.message

    print "send_message returned ", resp

    return Response(status=200)

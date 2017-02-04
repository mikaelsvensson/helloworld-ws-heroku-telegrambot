#!/usr/bin/python
import os

from twx.botapi import InputFileInfo, InputFile

from app import application
from app import bot

if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    application.logger.addHandler(stream_handler)
    application.logger.setLevel(logging.DEBUG)

try:
    bot.update_bot_info().wait()
    print 'Starting bot %s' % bot.username

    fp = open('app/helloworld-kikbot-herokuapp-com.pem', 'rb')
    file_info = InputFileInfo(
        file_name='app/helloworld-kikbot-herokuapp-com.pem',
        fp=fp,
        mime_type='text/plain')

    certificate = InputFile('certificate', file_info)

    bot.set_webhook(
        url='https://helloworld-telegrambot.herokuapp.com/incoming',
        certificate=certificate,
    ).wait()

    print 'Certificate: %s' % certificate

except Exception as e:
    print e

application.run(debug=True, threaded=True)

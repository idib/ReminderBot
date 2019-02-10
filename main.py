#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dateutil.parser import parse
import datetime
from setup import *

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

r = re.compile(regexpInput)

rOffset = re.compile(regexpOffset)


def mergeDict(dicts):
    dict = {'date': None, 'time': None, 'offset': None}
    result = []
    i = 0
    l = len(dicts)

    while i < l:
        if dicts[i]['date'] and i + 1 < l and dicts[i + 1]['time']:
            result += [{'date': dicts[i]['date'], 'time': dicts[i + 1]['time'], 'offset': None}]
            i += 1
        else:
            result += [dicts[i]]
        i += 1
    return result


def offsetConvert(str):
    m = rOffset.match(str).groupdict()
    res = {}
    for k, v in m.items():
        if k and v:
            res[k] = int(v)
    return datetime.datetime.now() + datetime.timedelta(**res)


def formatConversion(dDateTime):
    res = None
    today = parse("0:0")
    now = datetime.datetime.now()
    strDate = dDateTime['date']
    strTime = dDateTime['time']
    strOffset = dDateTime['offset']

    if strOffset:
        res = offsetConvert(strOffset)
    elif strDate or strTime:
        date = None
        time = None
        if strDate:
            strDate = re.sub(r"\.- ", "/", strDate.strip())
            if strDate == "today":
                date = today
            elif strDate == "tomorrow":
                date = today + datetime.timedelta(days=1)
            else:
                date = parse(strDate)
        if strTime:
            strTime = strTime.replace(" ", ":")
            if strTime in setupAPP:
                time = today.replace(**setupAPP[strTime])
            else:
                time = parse(strTime)
        if date and time:
            res = datetime.datetime.combine(date.date(), time.time())
        elif time:
            if time < now:
                time += datetime.timedelta(days=1)
            res = time
        elif date:
            if date == today:
                date += datetime.timedelta(**setupAPP['offset'])
            else:
                date = date.replace(**setupAPP['midday'])
            if date < today:
                date = date.replace(year=date.year + 1)
            res = date
    return res


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text("hi")
    update.message.reply_text(message['helloWorld'])


def alarm(bot, job):
    """Send the alarm message."""
    bot.send_message(job.context, text='Beep!')


def setReminder(bot, update, chat_data):
    """Add a job to the queue."""
    update.message.reply_text('Ok! Set time. \nExample: \ntomorrow,\n17 00,\n17:00,\n10m')


def set_timer(bot, update, job_queue, chat_data):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    m = mergeDict([m.groupdict() for m in r.finditer(update.message.text)])

    timeNow = datetime.datetime.today()
    chatDate = update.message.date
    structDatetime = datetime.datetime.today()
    for spls in m:
        try:
            structDatetime = formatConversion(spls)
            update.message.reply_text(f"{structDatetime}")
            update.message.reply_text(f"{chatDate}")
            update.message.reply_text(f"{timeNow}")
        except:
            update.message.reply_text("we can not convert you message")
            update.message.reply_text(f"we problem exp: {spls}")
            update.message.reply_text(f"original message: {t}")

    if structDatetime > timeNow:
        update.message.reply_text("set Timer")
        job = job_queue.run_once(alarm, (structDatetime - chatDate).total_seconds(), context=chat_id)
        chat_data['job'] = job


def unset(bot, update, chat_data):
    """Remove the job if the user changed their mind."""
    if 'job' not in chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Timer successfully unset!')


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Run bot."""
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))

    dp.add_handler(MessageHandler(Filters.forwarded, setReminder, pass_chat_data=True))
    dp.add_handler(MessageHandler(Filters.text, set_timer,
                                  pass_job_queue=True,
                                  pass_chat_data=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    # updater.start_webhook(listen='127.0.0.1', port=5000, url_path=TOKEN)
    # updater.bot.set_webhook(webhook_url=f'https://{DOMAIN}/{TOKEN}', certificate=open('/etc/nginx/cert.pem', 'rb'))

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

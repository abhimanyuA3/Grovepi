import time, datetime
from grovepi import *
import telepot
from telepot.loop import MessageLoop


led = 4
fan = 2
bulb = 3
tube = 7


now = datetime.datetime.now()

pinMode(led,"OUTPUT")
pinMode(fan,"OUTPUT")
pinMode(bulb,"OUTPUT")
pinMode(tube,"OUTPUT")

 

#intially off all devices
digitalWrite(led, 0) #Off initially
digitalWrite(fan, 0) #Off initially
digitalWrite(bulb, 0) #Off initially
digitalWrite(tube, 0) #Off initially




def action(msg):

    chat_id = msg['chat']['id']

    command = msg['text']


    print ('Received: %s' % command)

    if 'on' in command:

        message = "Turned on "

        if 'led' in command:

            message = message + "led "

            digitalWrite(led, 1)

        if 'fan' in command:

            message = message + "fan "

            digitalWrite(fan, 1)

        if 'bulb' in command:

            message = message + "bulb "

            digitalWrite(bulb, 1)

        if 'tube' in command:

            message = message + "tube "

            digitalWrite(tube, 1)

        if 'all' in command:

            message = message + "all "

            digitalWrite(led, 1)

            digitalWrite(fan, 1)

            digitalWrite(bulb, 1)

            digitalWrite(tube, 1)

        message = message + "light(s)"

        telegram_bot.sendMessage (chat_id, message)



    if 'off' in command:

        message = "Turned off "

        if 'led' in command:

            message = message + "led "

            digitalWrite(led, 0)

        if 'fan' in command:

            message = message + "fan "

            digitalWrite(fan, 0)

        if 'bulb' in command:

            message = message + "bulb "

            digitalWrite(bulb, 0)

        if 'tube' in command:

            message = message + "tube "

            digitalWrite(tube, 0)

        if 'all' in command:

            message = message + "all "

            digitalWrite(led, 0)

            digitalWrite(fan, 0)

            digitalWrite(bulb, 0)

            digitalWrite(tube, 0)

        message = message + "light(s)"

        telegram_bot.sendMessage (chat_id, message)


 


telegram_bot = telepot.Bot('5521025255:AAGFFPP_X_iJzi3VC34yIHoNuZw5FEUkElU')

print (telegram_bot.getMe())


MessageLoop(telegram_bot, action).run_as_thread()

print ('Home Automation running')


while 1:

    time.sleep(10)


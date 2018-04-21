# Raspberry Pi LED code
This is a totally pointless Raspberry Pi Project.

## LED lights controller
The LED light could be controlled by a few command via [Telegram bot](#connect-to-telgram-bot)
```
greet = Get a friendly response from the bot
green = Green LED light on
blue = Blue LED light on
red = Red LED light on
off = All the LED lights will be offf
fizzbuzz = Do a fizzbuzz test with the LED, counting to 25
all = All the lights will light up
exit = This really does nothing of importance except the bot will bid you goodbye. But the bot is still active. XP   
```
If you send gibberish to the bot, the cultured bot will return a beautiful random quote :) 

## [Connect to Telegram bot]
Telegram bots are fun! Check out the [Telegram API document](https://core.telegram.org/bots) to get started. My telegram bot API key is stored in a document call api.py as telegram_api. To start the bot after everything is set up, just run python telegram_bot.py.

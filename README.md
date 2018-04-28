# Raspberry Pi LED X Buzzer code
This is a totally pointless Raspberry Pi Project.

Awesome shout out to gumslone's raspi_buzzer_player for the mario buzzer song: https://github.com/gumslone/raspi_buzzer_player

## LED lights X buzzer controller
The LED light could be controlled by a few command via Telegram bot.
```
greet = Get a friendly response from the bot
green = Green LED light on
blue = Blue LED light on
red = Red LED light on
off = All the LED lights will be offf
fizzbuzz = Do a fizzbuzz test with the LED, counting to 25
all = All the lights will light up
beep = Buzzer will beep once
mario = Mario song!
exit = This really does nothing of importance except the bot will bid you goodbye. But the bot is still active. XP   
```
If you send gibberish to the bot, the cultured bot will return a beautiful random quote :)

## Connect to Telegram bot
Telegram bots are fun! Check out the [Telegram API document](https://core.telegram.org/bots) to get started. My telegram bot API key is stored in a document call api.py as telegram_api. To start the bot after everything is set up, just run python telegram_bot.py.

### Breadboard setup
__3 LEDs: 1 blue, 1 green, 1 red__

220 Ohm Resistor: Connects to negative of LED and negative rail of breadboard

M/F jumper wire: Connects to positive of LED and GPIO pins on Raspi

__1 passive buzzer__

M/F jumper wire: Connects to positive of buzzer and GPIO pin of Raspi

M/M jumper wire: Connects to negative of buzzer and negative rail of breadboard

__1 ground wire__

Connects to negative rail of breadboard and Ground pin of Raspi 

#! /usr/bin/python3.5
import json
import os
import requests
import sys
import time
import telepot
import RPi.GPIO as GPIO
import LED_vars
import tele_commands
from api import telegram_api
from tele_map import command_map

def random_quote():
	url = 'https://talaikis.com/api/quotes/random/'
	req = requests.get(url)
	return json.loads(req.text)['quote']

def handle(msg):
	has_valid_function = False
	chat_id = msg['chat']['id']
	command = msg['text'].lower()
	user = msg['from']['username']

	print('Exceuting command: %s by %s' % (command, user))

	if command in command_map:
		function_to_call = command_map[command]
		has_valid_function = True

	if command == 'hello':
		bot.sendMessage(chat_id, tele_commands.greet(user))
	elif has_valid_function:
		has_valid_function = False
		bot.sendMessage(chat_id, function_to_call())
	else:
		bot.sendMessage(chat_id, random_quote())

bot = telepot.Bot(telegram_api)
bot.message_loop(handle)
print('I am listening')

while 1:
	try:
		time.sleep(10)

	except KeyboardInterrupt:
		print('\n Program interrupted')
		GPIO.cleanup()
		exit()

	except:
		print('Other error or exception occured!')
		GPIO.cleanup()

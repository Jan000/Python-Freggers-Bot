import threading
import time
import random
import sys

from freggersbot import BasicFreggersBot, log_error
from freggersbot.utils import format_time

START_DELAY = (4, 25)

start_time = time.time()

bots = [
	BasicFreggersBot('Username', 'Password'),
	BasicFreggersBot('Username2', 'Password2'),
	BasicFreggersBot('Username3', 'Password3'),
]

bots.extend([
	BasicFreggersBot('Username4', 'Password4'),
	BasicFreggersBot('Username5', 'Password5'),
])

bots.append(BasicFreggersBot('Username6', 'Password6'))

try:
	for bot in list(bots):
		if not bot.init():
			bots.remove(bot)
	
	print(len(bots), 'Account(s) running...')
	
	def startup_bot(bot):
		try:
			bot.boot()
			bot.start()
		except Exception as e:
			log_error(e)
	
	threads = []
	
	for index, bot in enumerate(bots):
		t = threading.Thread(target = startup_bot, args = [bot])
		threads.append(t)
		t.start()
		print('Started bot {}/{}.'.format(index + 1, len(bots)))
		if index + 1 < len(bots):
			start_timeout = max(START_DELAY[0], random.randint(*START_DELAY) + random.random() - 1)
			print('Waiting random timeout of {} before starting next...'.format(format_time(start_timeout)))
			time.sleep(start_timeout)
	
	print('Took {} to start.'.format(format_time(time.time() - start_time)))
	
	for t in threads:
		t.join()
except Exception as e:
	log_error(e)
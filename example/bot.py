import threading
import time
import random
import sys

from freggersbot import FreggersBot, Event, log_error
from freggersbot.utils import format_time

START_DELAY = (4, 25)

start_time = time.time()

class BasicFreggersBot(FreggersBot):
	
	def __init__(self, username, password):
		super(BasicFreggersBot, self).__init__(username, password)
		self.register_callback(Event.CHAT_USR, self.__handle_show_chat_usr)
		self.register_callback(Event.CHAT_SRV, self.__handle_show_chat_svr)
		self.chat_show_blocked = True
		self.animation_manager.ignore_animations = True
		self.start = self.run
	
	def __handle_show_chat_usr(self, data):
		if data.type == 0 and (not data.overheard or self.chat_show_blocked):
			sender = self.wob_registry.get_object_by_wobid(data.wob_id)
			if sender == None:
				return
			self.log('[CHAT] {}{}{}: {}'.format(sender.name, ' [denkt]' if data.mode == 2 else (' [schreit]' if data.mode == 3 else (' [flüstert]' if data.mode == 4 else '')), ' [blocked]' if data.overheard else '', data.message))

	def __handle_show_chat_svr(self, data):
		self.log('[CHAT] [SERVER]: {}'.format(data.message))
	
	def run(self):
		try:
			self.daily_routine(skip_first_cycle = False, #Am ersten Tag den Planwagen/Baustelle überspringen
							idle_room = 'plattenbau%2.eigenheim',
							idle_room_alt = 'plattenbau.plattenbau', #'beach.beach2'
							care_pets = True, #True/False | Kümmert sich nach dem Sammeln und Abgeben um die Haustiere im Plattenbau
							care_pompom = True, #True/False | Kümmert sich um das Pompom im Plattenbau
							maintain_amount = 200, #Anzahl an Ameisen, die im Inventar/Warteschlange gehalten werden soll
							overload_amount = 75,
							min_deliver_amount = 3, #Ab welcher Anzahl (XP / AmeisenXP) an Ameisen der Bot abgeben soll
							loop_min_idle_sec = 2.5 * 60 * 60, #Minimale Wartezeit in Sekunden, die der Bot in der Wohnung wartet
							loop_max_idle_sec = 4 * 60 * 60) #Maximale Wartezeit in Sekunden, die der Bot in der Wohnung wartet
		except Exception as e:
			log_error(e)

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
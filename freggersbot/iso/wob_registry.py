from .player import Player
from .item import IsoItem

class WOBRegistry:
	
	def __init__(self):
		self.clear()
	
	def add(self, obj):
		self.world_objects[obj.wob_id] = obj
		if isinstance(obj, Player):
			self.players[obj.name] = obj
			self.players_by_uid[obj.user_id] = obj
			self.player_ids.add(obj)
		elif isinstance(obj, IsoItem):
			self.iso_items.add(obj)
	
	def remove(self, obj):
		del self.world_objects[obj.wob_id]
		if isinstance(obj, Player):
			del self.players[obj.name]
			del self.players_by_uid[obj.user_id]
			self.player_ids.discard(obj.wob_id)
		elif isinstance(obj, IsoItem):
			self.iso_items.discard(obj)
	
	def get_object_by_wobid(self, wob_id):
		return self.world_objects.get(wob_id)
		
	def get_player_by_name(self, username):
		return self.players.get(username)
	
	def get_player_by_uid(self, user_id):
		return self.players_by_uid.get(user_id)
	
	def get_by_iso_object(self, iso_obj):
		for wob in self.world_objects.values():
			if wob.iso_obj == iso_obj:
				return wob
		return None
	
	def get_wob_ids(self):
		return self.world_objects.keys()
	
	def clear(self):
		self.world_objects = {}
		self.players = {}
		self.players_by_uid = {}
		self.iso_items = set()
		self.player_ids = set()	
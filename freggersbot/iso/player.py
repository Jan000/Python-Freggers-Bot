from ..iso.container import IsoObjectContainer

class Player(IsoObjectContainer):
	
	def __init__(self, user_id, wob_id):
		super(Player, self).__init__(wob_id)
		self.user_id = user_id
	
	@staticmethod
	def create_from_data(avatar_data):
		if avatar_data.username == None or avatar_data.user_id <= 0:
			return None
		player = Player(avatar_data.user_id, avatar_data.wob_id)
		player.name = avatar_data.username
		player.rights = avatar_data.rights
		status = avatar_data.status
		if status != None:
			for x in range(len(status)):
				if status.get(x) != None:
					player.set_state(x, True, status[x])
		return player
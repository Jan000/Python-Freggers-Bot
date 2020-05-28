from .avatar import AvatarData

class TrRoomJoin:
	
	def __init__(self, utfmsg):
		self.data = AvatarData(utfmsg, start_index = 1)

class TrRoomLeave:
	
	def __init__(self, utfmsg):
		array = utfmsg.get_int_list_arg(1)
		self.wob_id = array[0]
		self.user_id = array[1]

class TrRoomReject:

	def __init__(self, utfmsg):
		self.reason = utfmsg.get_int_arg(1)
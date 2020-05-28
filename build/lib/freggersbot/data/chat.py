class ChatUsr:
	
	def __init__(self, utfmsg):
		self.wob_id = utfmsg.get_int_arg(1)
		self.message = utfmsg.get_string_arg(2)
		self.type = utfmsg.get_int_list_arg(0)[2]
		self.mode = 0 if utfmsg.get_arg_count() <= 3 else utfmsg.get_int_arg(3)
		self.overheard = False if utfmsg.get_arg_count() <= 4 else utfmsg.get_boolean_arg(4)

class ChatSrv:
	
	def __init__(self, utfmsg):
		self.message = utfmsg.get_string_arg(1)
class EffectData:
	
	def __init__(self, utfmsg):
		self.gui = utfmsg.get_string_arg(0)
		array = utfmsg.get_int_list_arg(1)
		self.duration = array[0]
		self.update_interval = 30 if len(array) < 2 else array[1]
	
	@staticmethod
	def from_utfmsg(utfmsg):
		if utfmsg == None:
			return None
		return EffectData(utfmsg)
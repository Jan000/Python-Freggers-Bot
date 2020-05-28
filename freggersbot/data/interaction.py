class InteractionData:
	
	def __init__(self, utfmsg):
		self.__data = None
		if utfmsg == None:
			return
		arg_len = utfmsg.get_arg_count()
		if arg_len == 0:
			return
		data = []
		for i in range(arg_len):
			msg = utfmsg.get_message_arg(i)
			data.append({
				'label': msg.get_string_arg(0),
				'name': msg.get_string_arg(1),
				'produces': msg.get_string_arg(2)
			})
		if len(data) == 0:
			return
		self.__data = data
	
	def get_data(self):
		return self.__data
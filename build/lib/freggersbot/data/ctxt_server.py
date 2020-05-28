class CtxtServer:
	
	def __init__(self, utfmsg):
		self.port = utfmsg.get_int_arg(1)
		self.host = CtxtServer.get_host(utfmsg.get_int_list_arg(1)[1:])
	
	@staticmethod
	def get_host(arr):
		arr_len = len(arr)
		if arr == None or arr_len != 4 and arr_len != 8:
			return
		if arr_len == 4:
			s = ''
			for i in arr:
				s += str(i) + '.'
			return s[:len(s) - 1]
		s = ''
		for i in arr:
			s += hex(i).replace('0x','') + ':'
		return s[:len(s) - 1]
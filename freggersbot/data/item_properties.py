class ItemProperties:
	
	TYPE_NONE = 0
	TYPE_SHOP = 1
	TYPE_DOORBELL = 2
	FLAG_TYPE = 1
	FLAG_NO_SELECT = 2
	
	def __init__(self, data):
		self.type = 0
		self.selectable = True
		if data != None and len(data) > 0:
			flags = data.pop(0)
			if (flags & ItemProperties.FLAG_TYPE) != 0:
				self.type = data.pop(0)
			if (flags & ItemProperties.FLAG_NO_SELECT) != 0:
				self.selectable = data.pop(0) == 0
class Position:
	
	def __init__(self, u, v, z, direction = 0):
		self.u = u
		self.v = v
		self.z = z
		self.direction = direction
	
	@staticmethod
	def from_array(array):
		if array == None:
			return None
		return Position(array[0], array[1], array[2], direction = array[3])
	
	def __str__(self):
		return 'Position({}, {}, {}, {})'.format(self.u, self.v, self.z, self.direction)
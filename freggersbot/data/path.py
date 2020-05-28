import time

from .position import Position
from .waypoint import Waypoint

class Path:
	
	def __init__(self, start, duration, received_at):
		self.start = start
		self.duration = duration
		self.waypoints = []
		self.received_at = received_at
	
	@staticmethod
	def from_utfmsg(utfmsg):
		if utfmsg == None:
			return None
		array = utfmsg.get_int_list_arg(0)
		if array == None or len(array) < 5:
			return None
		path = Path(Position(array[1], array[2], array[3]), array[4] / 1000, time.time())
		for x in range(array[0]):
			wp = utfmsg.get_int_list_arg(x + 1)
			path.add_waypoint(Waypoint(Position(wp[0], wp[1], wp[2]), wp[3] / 1000))
		return path
	
	def add_waypoint(self, waypoint):
		self.waypoints.append(waypoint)
	
	def age(self):
		return time.time() - self.received_at
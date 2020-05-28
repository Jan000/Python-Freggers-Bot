class ListCmd:
	
	def feed(self, utfmsg):
		pass
	def is_complete(self):
		return False
	def get_data(self):
		return None

class MayVote(ListCmd):
	
	def __init__(self, utfmsg):
		self.may_vote = utfmsg.get_boolean_arg(1)
		self.vote_count = utfmsg.get_int_arg(2)
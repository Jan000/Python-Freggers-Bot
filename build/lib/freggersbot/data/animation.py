class AnimationData:
	
	ANIM_KEYVAL_PLAY = 1
	ANIM_KEYVAL_MODE = 2
	ANIM_KEYVAL_MILLIS = 3
	ANIM_KEY_PLAY = 'play'
	ANIM_KEY_MODE = 'mode'
	ANIM_KEY_MILLIS = 'millis'
	
	def __init__(self, utfmsg):
		self.name = utfmsg.get_string_arg(0)
		self.datapack = utfmsg.get_string_arg(1)
		keyframes = []
		for x in range((utfmsg.get_arg_count() - 2) // 2):
			keyframe = utfmsg.get_int_list_arg(x * 2 + 2)
			if keyframe != None:
				key = keyframe[0]
				if key == AnimationData.ANIM_KEYVAL_PLAY:
					keyframes.append({
						'name': AnimationData.ANIM_KEY_PLAY,
						'data': utfmsg.get_int_list_arg(x * 2 + 3)
					})
				elif key == AnimationData.ANIM_KEYVAL_MODE:
					keyframes.append({
						'name': AnimationData.ANIM_KEY_MODE,
						'modifier': keyframe[1],
						'data': utfmsg.get_int_arg(x * 2 + 3)
					})
				elif key == AnimationData.ANIM_KEYVAL_MILLIS:
					keyframes.append({
						'name': AnimationData.ANIM_KEY_MILLIS,
						'data': utfmsg.get_int_arg(x * 2 + 3)
					})
		self.keyframes = keyframes
	
	@staticmethod
	def from_utfmsg(utfmsg):
		if utfmsg == None:
			return None
		return AnimationData(utfmsg)
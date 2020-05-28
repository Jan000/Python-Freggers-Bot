from ..iso import Status
from ..net.utf_message import UtfMessage
from .path import Path
from .position import Position
from .effect import EffectData
from .item_properties import ItemProperties
from .interaction import InteractionData
from .animation import AnimationData

class ItemData:
	def __init__(self, utfmsg):
		self.name = utfmsg.get_string_arg(0)
		self.wob_id = utfmsg.get_int_arg(1)
		self.gui = utfmsg.get_string_arg(2)
		if utfmsg.get_arg_type(3) == UtfMessage.TYPE_RECORD:
			self.path = Path.from_utfmsg(utfmsg.get_message_arg(3))
		else:
			self.position = Position.from_array(utfmsg.get_int_list_arg(3))
		self.animation = AnimationData.from_utfmsg(utfmsg.get_message_arg(4))
		self.sound = None #SoundBlock.fromUtfMessage(utfmsg.get_message_arg(5))
		self.lightmap = None #LightmapData.fromUtfMessage(utfmsg.get_message_arg(6))
		self.status = Status.get_object_status_data(utfmsg.get_message_arg(7))
		self.effect = EffectData.from_utfmsg(utfmsg.get_message_arg(8))
		self.ghost_trail = None #GhosttrailData.fromUtfMessage(utfmsg.get_message_arg(9))
		self.properties = ItemProperties(utfmsg.get_int_list_arg(10))
		self.interactions = InteractionData(utfmsg.get_message_arg(11))
		self.primary_interaction_label = utfmsg.get_string_arg(12)
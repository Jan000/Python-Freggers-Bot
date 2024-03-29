from .decoder import Decoder, BitMapData

class LevelBackground:

    def __init__(self, area_name, room_name, brightness, level_size):
        self.area_name = area_name
        self.room_name = room_name
        self.brightness = brightness
        self.level_size = level_size
        self.identifier = area_name + '.' + room_name + '.' + str(brightness)

        self.version = None
        self.lightmap = None
        self.offset = None
        self.bitmap_data = None
        self.avg_brightness = 1
        self.loaded = False
        self.use_lightmap = True
    
    def set(self, bg):
        self.area_name = bg.area_name
        self.room_name = bg.room_name
        self.brightness = bg.brightness
        self.level_size = bg.level_size
        self.identifier = bg.area_name + '.' + bg.room_name + '.' + str(bg.brightness)
        self.version = bg.version
        self.lightmap = bg.lightmap
        self.offset = bg.offset
        self.bitmap_data = bg.bitmap_data
        self.avg_brightness = bg.avg_brightness
        self.loaded = bg.loaded
        self.use_lightmap = bg.use_lightmap

    def cleanup(self):
        pass

    def clone(self):
        bg = LevelBackground(self.area_name, self.room_name, self.brightness, self.level_size)
        bg.avg_brightness = self.avg_brightness
        if self.lightmap != None:
            bg.lightmap = self.lightmap.clone()
        bg.offset = self.offset
        bg.bitmap_data = self.bitmap_data
        bg.version = self.version
        return bg
    
    def decode(self, container):
        decoded = Decoder.decode_background(container)
        if decoded == None:
            return False
        self.version = decoded[Decoder.VERSION_NUMBER]
        self.init(decoded[Decoder.BG_IMAGE], decoded.get(Decoder.BG_LIGHTMAP, None), decoded[Decoder.BG_OFFSET], decoded[Decoder.BG_WIDTH], decoded[Decoder.BG_HEIGHT])
    
    def init(self, pixel_data, lightmap, offset, width, height):
        self.bitmap_data = BitMapData(pixel_data, width, height)
        #if pixel_data != None:
        #    self.bitmap_data.save_to('bg/' + self.identifier + '.png', True)
        """
        if lightmap != None:
            #TODO self.lightmap = Lightmap(lightmap)
            pass
        else:
            #TODO self.lightmap = Lightmap(BitMapData(*self.level_size, False, 8421504))
            pass
        """
        self.offset = offset
        #self.avg_brightness = self.lightmap.compute_avg_brightness()
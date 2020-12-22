import sprite
import pygame


class Sprite_of_type(sprite.Sprite_image):
    def __init__(self, sprite_type, x, y, costume_name=None, visible=True):
        self.sprite_type = sprite_type

        #TODO если нет костюма - получить первый костюм типа
        self._active_costume_name = costume_name

        # get costume image from sprite type #TODO временный код
        image = pygame.image.load("sprite_types/type1/costumes/1.png")

        sprite.Sprite_image.__init__(self, image, x, y, visible, 967, 488, 90)

    def _change_costume(self, image, pos_offset, orig_angle, save_moving_angle):
        if save_moving_angle:
            angle_diff = self.get_start_angle() - orig_angle
            angle_modif = self.get_angle_modification()
            self.set_angle_modification(angle_modif+angle_diff)
        self.change_base_image(image, pos_offset, orig_angle)

    def set_costume(self, costume_name):
        # get costume image from sprite type #TODO временный код
        self._active_costume_name = costume_name
        image = pygame.image.load("sprite_types/type1/costumes/"+costume_name+".png")
        if costume_name=="1":
            self._change_costume(image, [967, 488], 90, True)
        else:
            self._change_costume(image, [115, 66], 0, True)

    def get_sprite_costume(self):
        return self._active_costume_name

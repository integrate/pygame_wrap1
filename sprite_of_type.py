import sprite
import pygame


class Sprite_of_type(sprite.Sprite_image):
    def __init__(self, sprite_type, x, y, costume_name=None, visible=True):
        self.sprite_type = sprite_type

        #TODO если нет костюма - получить первый костюм типа
        self._active_costume_name = costume_name

        # get costume image from sprite type #TODO временный код
        image = pygame.image.load("sprite_types/type1/costumes/1.png")

        sprite.Sprite_image.__init__(self, image, x, y, visible, 967, 488)

    def set_costume(self, costume_name):
        # get costume image from sprite type #TODO временный код
        self._active_costume_name = costume_name
        image = pygame.image.load("sprite_types/type1/costumes/"+costume_name+".png")
        self.change_image(image)
        if costume_name=="1":
            self.change_pos_offset(967, 488)
        else:
            self.change_pos_offset(115, 66)

    def get_sprite_costume(self):
        return self._active_costume_name

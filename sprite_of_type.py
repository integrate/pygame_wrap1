import sprite
import pygame


class Sprite_of_type(sprite.Sprite_image):
    def __init__(self, sprite_type, x, y, costume_name=None, visible=True):
        self.sprite_type = sprite_type

        #TODO если нет костюма - получить первый костюм типа
        self._active_costume_name = costume_name

        # get costume image from sprite type #TODO временный код
        image = pygame.image.load("sprite_types/type1/costumes/1.png")

        sprite.Sprite_image.__init__(self, image, x, y, visible)

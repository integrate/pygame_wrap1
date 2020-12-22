import pygame, image_modifier, math_utils


class Sprite_manager():
    def __init__(self, window, bkg):
        object.__init__(self)

        self._window = window
        self._bkg = bkg

        self._group = pygame.sprite.LayeredDirty()
        self._group.clear(None, self._bkg)

    def _set_background(self, bkg):
        if self._bkg is bkg: return

        self._bkg = bkg
        self._group.clear(None, self._bkg)

    def update_sprites(self):
        self._group.draw(self._window)

    def add_image_sprite(self, sprite):
        self._group.add(sprite)


class Sprite_image(pygame.sprite.DirtySprite):
    def __init__(self, image, x, y, visible=True, posx=0, posy=0):
        pygame.sprite.DirtySprite.__init__(self)

        self._pos = [x, y]

        # original image
        self._orig_modifier = image_modifier.ImageSource(None, None, image, [posx, posy])
        self._size_modifier = image_modifier.ImageResizer(self._orig_modifier, None, None, None)
        self._flipper = image_modifier.ImageFlipper(self._size_modifier, None)
        self._rotator = image_modifier.ImageRotator(self._flipper, None)

        self._final_modifier = self._rotator
        self._final_modifier.change_callback(self._update_sprite_data)
        self._final_modifier.update()

        self.visible = visible

    def _update_sprite_data(self):
        if not hasattr(self, '_final_modifier'):
            return

        # get changed image
        self.image = self._final_modifier.get_modified_image()
        self.rect = self.image.get_rect()

        # calc correct pos
        posx, posy = self._final_modifier.get_modified_pos()
        self.rect.topleft = [self._pos[0] - posx, self._pos[1] - posy]

        self.dirty = 1

    def change_image(self, image):
        self._orig_modifier.change_image(image)

    def change_pos_offset(self, posx, posy):
        self._orig_modifier.change_pos([posx, posy])

    def change_size(self, width, height):
        self._size_modifier.change_size(width, height)

    def get_real_width(self):
        return self.image.get_width()

    def get_real_height(self):
        return self.image.get_height()

    def get_width(self):
        return self._size_modifier.get_size()[0]

    def get_height(self):
        return self._size_modifier.get_size()[1]

    def get_flipx(self):
        return self._flipper.get_flips()[0]

    def get_flipy(self):
        return self._flipper.get_flips()[1]

    def set_flipx(self, flipx):
        return self._flipper.set_flipx(flipx)

    def set_flipy(self, flipy):
        return self._flipper.set_flipy(flipy)

    def set_angle(self, angle):
        self._rotator.change_angle(-angle)

    def get_angle(self):
        return -self._rotator.get_angle()

    def move_sprite_by(self, dx, dy):
        self._pos[0] += dx
        self._pos[1] += dy
        self._update_sprite_data()

    def get_visible(self):
        return self.visible

    def set_visible(self, visible):
        self.visible = visible
        self.dirty = 1

    def move_sprite_at_angle(self, angle, distance):
        res = math_utils.get_point_by_angle([*self._pos], -angle, distance)
        self._pos[0] = int(res[0])
        self._pos[1] = int(res[1])

        self._update_sprite_data()

    def move_sprite_to_angle(self, distance):
        res = math_utils.get_point_by_angle([*self._pos], self._rotator.get_angle(), distance)
        self._pos[0] = int(res[0])
        self._pos[1] = int(res[1])

        self._update_sprite_data()

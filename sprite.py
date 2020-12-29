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
    def __init__(self, image, x, y, visible=True, posx=0, posy=0, base_angle=0):
        pygame.sprite.DirtySprite.__init__(self)

        self._pos = [x, y]

        # original image
        self._orig_modifier = image_modifier.ImageSource(None, None, image, [posx, posy], -base_angle)
        self._size_modifier = image_modifier.ImageResizer(self._orig_modifier, None, None, None)
        self._flipper_angle = image_modifier.ImageFlipper(self._size_modifier, None)
        self._rotator = image_modifier.ImageRotator(self._flipper_angle, None)

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

    @staticmethod
    def normalize_angle(angle):
        if angle > 360:
            angle %= 360
        if angle < -360:
            angle %= -360
        if angle > 180:
            angle -= 360
        if angle <= -180:
            angle += 360

        return angle

    def change_image(self, image):
        self._orig_modifier.change_image(image)

    def change_pos_offset(self, posx, posy):
        self._orig_modifier.change_pos([posx, posy])

    def change_base_angle(self, angle):
        self._orig_modifier.change_angle(-angle)

    def change_base_image(self, image=None, pos=None, angle=None):
        if angle is not None:
            angle = -angle
        self._orig_modifier.change_all(image, pos, angle)

    def get_original_width(self):
        oi = self._orig_modifier.get_modified_image()
        return oi.get_width()

    def get_original_height(self):
        oi = self._orig_modifier.get_modified_image()
        return oi.get_height()

    def get_original_sizes(self):
        oi = self._orig_modifier.get_modified_image()
        return oi.get_size()

    def get_real_width(self):
        return self.image.get_width()

    def get_real_height(self):
        return self.image.get_height()

    def get_real_size(self):
        return self.image.get_size()

    def get_width(self):
        return self._size_modifier.get_size()[0]

    def get_height(self):
        return self._size_modifier.get_size()[1]

    def get_size(self):
        return self._size_modifier.get_size()

    def set_original_size(self):
        self._size_modifier.change_size_pix(None, None)

    def change_width(self, width):
        h = self._size_modifier.get_size()[1]
        self._size_modifier.change_size_pix(width, h)

    def change_height(self, height):
        w = self._size_modifier.get_size()[0]
        self._size_modifier.change_size_pix(w, height)

    def change_size_pix(self, width, height):
        self._size_modifier.change_size_pix(width, height)

    def change_width_proportionally(self, width, from_modified=False):
        if from_modified:
            cur_w, cur_h = self._size_modifier.get_size()
        else:
            oi = self._orig_modifier.get_modified_image()
            cur_w, cur_h = oi.get_size()

        width, height = math_utils.get_sizes_proportionally(cur_w, cur_h, width, None)
        self._size_modifier.change_size_pix(width, height)

    def get_flipx_reverse(self):
        return self._flipper_angle.get_flipx()

    def get_flipy_reverse(self):
        return self._flipper_angle.get_flipy()

    def set_flipx_reverse(self, flipx):
        curr_flip = self._flipper_angle.get_flipx()

        self._flipper_angle.set_flipx(flipx, True)

        if curr_flip != flipx:
            self._rotator.reflect_flip_once(True, False)

    def set_flipy_reverse(self, flipy):
        curr_flip_y = self._flipper_angle.get_flipy()

        self._flipper_angle.set_flipy(flipy, True)

        if curr_flip_y != flipy:
            self._rotator.reflect_flip_once(False, True)

    def get_start_angle(self):
        return Sprite_image.normalize_angle(-self._orig_modifier.get_angle())

    def set_angle_modification(self, angle):
        self._rotator.change_angle(-angle)

    def get_angle_modification(self):
        return Sprite_image.normalize_angle(-self._rotator.get_angle())

    def get_final_angle(self):
        return Sprite_image.normalize_angle(-self._final_modifier.get_modified_angle())

    def move_sprite_to(self, x, y):
        self._pos[0] = x
        self._pos[1] = y
        self._update_sprite_data()

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
        an = self._final_modifier.get_modified_angle()
        res = math_utils.get_point_by_angle([*self._pos], an, distance)
        self._pos[0] = int(res[0])
        self._pos[1] = int(res[1])

        self._update_sprite_data()

    def move_sprite_to_point(self, point, distance):
        # can't move to same point
        if point[0] == self._pos[0] and point[1] == self._pos[1]:
            return

        an = math_utils.get_angle_by_point(self._pos, point)

        res = math_utils.get_point_by_angle([*self._pos], an, distance)
        self._pos[0] = int(res[0])
        self._pos[1] = int(res[1])

        self._update_sprite_data()

    def rotate_to_point(self, point):
        # can't move to same point
        if point[0] == self._pos[0] and point[1] == self._pos[1]:
            return

        an = math_utils.get_angle_by_point(self._pos, point)

        orig_angle = self._flipper_angle.get_modified_angle()
        self._rotator.change_angle(an - orig_angle)

import pygame, math_utils, image_utils


class ImageModifier():
    def __init__(self, image_modifier, callback):
        # save parameters
        self._orig_image_modifier = image_modifier
        self._callback = callback

        self._modification_data = None

        # init changed data
        self._changed_image = None
        self._changed_pos = None
        self._changed_angle = None

        # subscribe on source image change
        if self._orig_image_modifier is not None:
            self._orig_image_modifier.change_callback(self.update)

    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        return [orig_image.copy(), [*orig_pos], orig_angle]

    def update(self):
        if self._orig_image_modifier is not None:
            new_source = self._orig_image_modifier.get_modified_image()
            new_pos = self._orig_image_modifier.get_modified_pos()
            new_angle = self._orig_image_modifier.get_modified_angle()
        else:
            new_source = new_pos = new_angle = None

        res = self.__class__._modify(new_source, new_pos, new_angle, self._modification_data)
        self._changed_image = res[0]
        self._changed_pos = res[1]
        self._changed_angle = res[2]

        if callable(self._callback):
            self._callback()

    def change_callback(self, callback):
        self._callback = callback

    def get_modified_image(self):
        return self._changed_image

    def get_modified_pos(self):
        return self._changed_pos

    def get_modified_angle(self):
        return self._changed_angle


class ImageSource(ImageModifier):
    def __init__(self, image_modifier, callback, image, pos, angle):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = [image.copy(), [*pos], angle]

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        return [modification_data[0].copy(), [*modification_data[1]], modification_data[2]]

    def change_image(self, image):
        self._modification_data[0] = image.copy()
        self.update()

    def change_pos(self, pos):
        self._modification_data[1] = [*pos]
        self.update()

    def change_angle(self, angle):
        self._modification_data[2] = angle
        self.update()

    def change_all(self, image=None, pos=None, angle=None):
        if image is not None:
            self._modification_data[0] = image.copy()

        if pos is not None:
            self._modification_data[1] = [*pos]

        if angle is not None:
            self._modification_data[2] = angle

        self.update()

    def get_angle(self):
        return self._modification_data[2]

    def get_pos(self):
        return self._modification_data[1]


class ImageResizer(ImageModifier):
    def __init__(self, image_modifier, callback, to_width, to_height):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = [to_width, to_height]

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        # get origin and final size
        orig_width = orig_image.get_width()
        orig_height = orig_image.get_height()

        width_to = orig_width if type(modification_data[0]) is not int else modification_data[0]
        height_to = orig_height if type(modification_data[1]) is not int else modification_data[1]

        scale_x = width_to / orig_width
        scale_y = height_to / orig_height

        res_image = pygame.transform.scale(orig_image, [width_to, height_to])

        res_pos = [orig_pos[0] * scale_x, orig_pos[1] * scale_y]

        return [res_image, res_pos, orig_angle]

    @staticmethod
    def modify(orig_image, orig_pos, orig_angle, width_to, height_to):
        return ImageResizer._modify(orig_image, orig_pos, orig_angle, [int(width_to), int(height_to)])

    def change_size(self, to_width=None, to_height=None):
        self._modification_data = [to_width, to_height]
        self.update()

    def get_size(self):
        return self._changed_image.get_size()


class ImageRotator(ImageModifier):
    def __init__(self, image_modifier, callback):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = 0

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        angle = modification_data

        orig_center = orig_image.get_rect().center
        orig_dx = orig_pos[0] - orig_center[0]
        orig_dy = orig_pos[1] - orig_center[1]

        dx, dy = math_utils.get_point_on_circle([*orig_center], [*orig_pos], angle)
        res_image = pygame.transform.rotate(orig_image, angle)

        res_center = res_image.get_rect().center
        res_pos = [0, 0]
        res_pos[0] = res_center[0] + orig_dx + dx
        res_pos[1] = res_center[1] + orig_dy + dy

        return [res_image, res_pos, orig_angle + angle]

    def change_angle(self, angle):
        self._modification_data = angle
        self.update()

    def reflect_flip_once(self, flipx, flipy):
        res_angle = self._modification_data
        if flipx:
            res_angle = -res_angle
        if flipy:
            res_angle = -res_angle
        self._modification_data = res_angle
        self.update()

    def get_angle(self):
        return self._modification_data


class ImageFlipper(ImageModifier):
    def __init__(self, image_modifier, callback, flipx=False, flipy=False, reverse_angle_x=False,
                 reverse_angle_y=False):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = {
            'flipx': flipx,
            'flipy': flipy,
            'reverse_angle_x': reverse_angle_x,
            'reverse_angle_y': reverse_angle_y
        }

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        flipx = modification_data['flipx']
        flipy = modification_data['flipy']
        reverse_angle_x = modification_data['reverse_angle_x']
        reverse_angle_y = modification_data['reverse_angle_y']

        orig_center = orig_image.get_rect().center
        orig_dx = orig_pos[0] - orig_center[0]
        orig_dy = orig_pos[1] - orig_center[1]

        res_image = pygame.transform.flip(orig_image, flipx, flipy)

        res_center = res_image.get_rect().center

        mx = -1 if flipx else 1
        my = -1 if flipy else 1

        res_pos = [0, 0]
        res_pos[0] = res_center[0] + mx * orig_dx
        res_pos[1] = res_center[1] + my * orig_dy

        res_angle = orig_angle
        if flipx and reverse_angle_x:
            res_angle = -res_angle
        if flipy and reverse_angle_y:
            res_angle = 180 - res_angle

        return [res_image, res_pos, res_angle]

    def set_flips(self, flipx=False, flipy=False, reverse_angle_x=False,
                  reverse_angle_y=False):
        self._modification_data = {
            'flipx': flipx,
            'flipy': flipy,
            'reverse_angle_x': reverse_angle_x,
            'reverse_angle_y': reverse_angle_y
        }
        self.update()

    def set_flipx(self, flipx, reverse_angle_x=False):
        self._modification_data['flipx'] = flipx
        self._modification_data['reverse_angle_x'] = reverse_angle_x
        self.update()

    def set_flipy(self, flipy, reverse_angle_y=False):
        self._modification_data['flipy'] = flipy
        self._modification_data['reverse_angle_y'] = reverse_angle_y
        self.update()

    def get_flipx(self):
        return self._modification_data['flipx']

    def get_flipx_reverse(self):
        return self._modification_data['reverse_angle_x']

    def get_flipy(self):
        return self._modification_data['flipy']

    def get_flipy_reverse(self):
        return self._modification_data['reverse_angle_y']


class ImageColorRemover(ImageModifier):
    def __init__(self, image_modifier, callback, remove_color, threshold):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = {
            'color': remove_color,
            'threshold': threshold
        }

        # first update
        self.update()


    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        color = modification_data['color']
        threshold = modification_data['threshold']

        m1 = pygame.mask.from_threshold(orig_image, color, [threshold, threshold, threshold])
        m1.invert()
        q2 = orig_image.copy()

        flags = orig_image.get_flags()
        if flags & pygame.SRCALPHA:
            transp_color = [0, 0, 0, 0]
        else:
            transp_color = image_utils.get_not_used_color(orig_image)

        q2.fill(transp_color)
        m1.to_surface(q2, orig_image, None, None, None)
        q2.set_colorkey(transp_color)
        return [q2, orig_pos, orig_angle]

    @staticmethod
    def modify(orig_image, orig_pos, orig_angle, color, threshold):
        mod = {
            'color':color,
            'threshold': threshold
        }
        return ImageColorRemover._modify(orig_image, orig_pos, orig_angle, mod)
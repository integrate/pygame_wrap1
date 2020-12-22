import pygame, math


class ImageModifier():
    def __init__(self, image_modifier, callback):
        # save parameters
        self._orig_image_modifier = image_modifier
        self._callback = callback

        self._modification_data = None

        # init changed data
        self._changed_image = None
        self._changed_pos = None

        # subscribe on source image change
        if self._orig_image_modifier is not None:
            self._orig_image_modifier.change_callback(self.update)

    @staticmethod
    def _modify(orig_image, orig_pos, modification_data):
        return [orig_image, orig_pos]

    def update(self):
        if self._orig_image_modifier is not None:
            new_source = self._orig_image_modifier.get_modified_image()
            new_pos = self._orig_image_modifier.get_modified_pos()
        else:
            new_source = new_pos = None

        res = self.__class__._modify(new_source, new_pos, self._modification_data)
        self._changed_image = res[0]
        self._changed_pos = res[1]

        if callable(self._callback):
            self._callback()

    def change_callback(self, callback):
        self._callback = callback

    def get_modified_image(self):
        return self._changed_image

    def get_modified_pos(self):
        return self._changed_pos


class ImageSource(ImageModifier):
    def __init__(self, image_modifier, callback, image, pos):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = [image.copy(), [*pos]]

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, modification_data):
        return [modification_data[0], modification_data[1]]

    def change_image(self, image):
        self._modification_data[0] = image.copy()
        self.update()

    def change_pos(self, pos):
        self._modification_data[1] = [*pos]
        self.update()


class ImageResizer(ImageModifier):
    def __init__(self, image_modifier, callback, to_width, to_height):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = [to_width, to_height]

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, modification_data):
        # get origin and final size
        orig_width = orig_image.get_width()
        orig_height = orig_image.get_height()

        width_to = orig_width if type(modification_data[0]) is not int else modification_data[0]
        height_to = orig_height if type(modification_data[0]) is not int else modification_data[1]

        scale_x = width_to / orig_width
        scale_y = height_to / orig_height

        res_image = pygame.transform.scale(orig_image, [width_to, height_to])

        res_pos = [orig_pos[0] * scale_x, orig_pos[1] * scale_y]

        return [res_image, res_pos]

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
    def _modify(orig_image, orig_pos, modification_data):
        angle = modification_data

        orig_center = orig_image.get_rect().center
        orig_dx = orig_pos[0] - orig_center[0]
        orig_dy = orig_pos[1] - orig_center[1]

        dx, dy = ImageRotator._get_point_on_circle2(orig_center, orig_pos, angle)
        res_image = pygame.transform.rotate(orig_image, angle)

        res_center = res_image.get_rect().center
        res_pos = [0, 0]
        res_pos[0] = res_center[0] + orig_dx + dx
        res_pos[1] = res_center[1] + orig_dy + dy

        return [res_image, res_pos]

    @staticmethod
    def _get_point_on_circle(center, start_point, angle_degrees):
        dx = start_point[0] - center[0]
        dy = start_point[1] - center[1]

        if dx == 0:
            b_degr = 90
        else:
            tanb = dy / dx
            b_degr = math.degrees(math.atan(tanb))

        c_degr = 90 - b_degr + angle_degrees / 2

        hip = math.hypot(dx, dy)
        l = 2 * hip * math.sin(math.radians(angle_degrees / 2))

        dx = l * math.cos(math.radians(c_degr))
        dy = -l * math.sin(math.radians(c_degr))

        return [dx, dy]

    @staticmethod
    # center - center of circle
    # start point - point on circle
    # angle_degrees - angle between start point and result point
    # result - [dx, dy] - distance between start point and result point
    def _get_point_on_circle2(center, start_point, angle_degrees):

        center_m = [*center]
        start_point_m = [*start_point]

        ym = 1
        xm = 1

        if center_m[0] > start_point_m[0]:
            xm = -1
            ym = -1

        dx, dy = ImageRotator._get_point_on_circle(center_m, start_point_m, angle_degrees)
        return dx * xm, dy * ym

    def change_angle(self, angle):
        self._modification_data = angle
        self.update()

    def get_angle(self):
        return self._modification_data


class ImageFlipper(ImageModifier):
    def __init__(self, image_modifier, callback, flipx=False, flipy=False):
        ImageModifier.__init__(self, image_modifier, callback)

        # save parameters
        self._modification_data = [flipx, flipy]

        # first update
        self.update()

    @staticmethod
    def _modify(orig_image, orig_pos, modification_data):
        flipx = modification_data[0]
        flipy = modification_data[1]

        orig_center = orig_image.get_rect().center
        orig_dx = orig_pos[0] - orig_center[0]
        orig_dy = orig_pos[1] - orig_center[1]

        res_image = pygame.transform.flip(orig_image, flipx, flipy)

        res_center = res_image.get_rect().center

        mx = -1 if flipx else 1
        my = -1 if flipy else 1

        res_pos = [0, 0]
        res_pos[0] = res_center[0] + mx*orig_dx
        res_pos[1] = res_center[1] + my*orig_dy

        return [res_image, res_pos]

    def set_flips(self, flipx=False, flipy=False):
        self._modification_data = [flipx, flipy]
        self.update()

    def set_flipx(self, flipx):
        self._modification_data[0] = flipx
        self.update()

    def set_flipy(self, flipy):
        self._modification_data[1] = flipy
        self.update()

    def get_flips(self):
        return self._modification_data
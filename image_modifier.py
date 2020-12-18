import pygame

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
        #get origin and final size
        orig_width = orig_image.get_width()
        orig_height = orig_image.get_height()

        width_to = orig_width if type(modification_data[0]) is not int else modification_data[0]
        height_to = orig_height if type(modification_data[0]) is not int else modification_data[1]

        scale_x = width_to/orig_width
        scale_y = height_to / orig_height

        res_image = pygame.transform.scale(orig_image, [width_to, height_to])

        res_pos = [orig_pos[0]*scale_x, orig_pos[1]*scale_y]

        return [res_image, res_pos]

    def change_size(self, to_width=None, to_height=None):
        self._modification_data = [to_width, to_height]
        self.update()

    def get_size(self):
        return self._modification_data

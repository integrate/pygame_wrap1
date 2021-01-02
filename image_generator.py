import image_modifier, pygame


class TextImageGenerator(image_modifier.ImageModifier):

    def __init__(self, text, font_name="Arial", font_size=20,
                 bold=False, italic=False, underline=False,
                 text_color=(0, 0, 0),
                 back_color=None, pos=None, angle=None, callback = None):

        image_modifier.ImageModifier.__init__(self, None, callback)

        if pos is not None:
            pos = [*pos]

        # create font
        font_data = {
            'name': font_name,
            'size': font_size,
            'bold': bold,
            'italic': italic,
            'underline': underline
        }
        font = TextImageGenerator._get_font_by_data(font_data)

        self._modification_data = {
            "font_data": font_data,
            'font': font,
            'text': text,
            "text_color": text_color,
            "back_color": back_color,
            "pos": pos,
            "angle": angle
        }

        super().update()

    @staticmethod
    def _get_font_by_data(font_options):
        font = pygame.font.SysFont(font_options["name"], font_options["size"], font_options["bold"], font_options["italic"])
        font.set_underline(font_options["underline"])
        return font

    @staticmethod
    def _modify(orig_image, orig_pos, orig_angle, modification_data):
        if 'font' in modification_data:
            f = modification_data['font']
        else:
            f = TextImageGenerator._get_font_by_data(modification_data['font_data'])

        im = f.render(modification_data['text'], True, modification_data['text_color'], modification_data['back_color'])

        # prepare pos
        pos = modification_data["pos"] if "pos" in modification_data else None
        if pos is None:
            w, h = im.get_size()
            pos = [w / 2, h / 2]
        else:
            pos = [*pos]

        # prepare angle
        if "angle" in modification_data and modification_data['angle'] is not None:
            angle = modification_data["angle"]
        else:
            angle = 90

        return [im, pos, angle]

    def get_font_name(self):
        return self._modification_data['font_data']['name']

    def set_font_name(self, name):
        self._modification_data['font_data']['name'] = name
        self._modification_data['font'] = TextImageGenerator._get_font_by_data(self._modification_data['font_data'])
        self.update()

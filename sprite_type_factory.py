import os, sprite_type_loader, sprite_type as st, sprite_type_costume, math_utils, image_modifier


class Sprite_type_factory():
    @staticmethod
    def _prepare_image(orig_image, orig_pos, orig_angle, prepare_data):
        print(prepare_data)

        # change size
        if ('width' in prepare_data and prepare_data['width'] is not None) or\
                ('height' in prepare_data and prepare_data['height'] is not None):
            w_mod = prepare_data['width'] if 'width' in prepare_data else None
            h_mod = prepare_data['height'] if 'height' in prepare_data else None
            w_orig, h_orig = orig_image.get_size()
            w_mod, h_mod = math_utils.get_sizes_proportionally(w_orig, h_orig, w_mod, h_mod)

            orig_image, orig_pos, orig_angle = image_modifier.ImageResizer.modify(orig_image, orig_pos, orig_angle,
                                                                                  int(w_mod), int(h_mod))

        # remove color
        if 'remove_color' in prepare_data and prepare_data['remove_color']:
            orig_image, orig_pos, orig_angle = image_modifier.ImageColorRemover.modify(orig_image, orig_pos, orig_angle,
                                                                                       prepare_data['remove_color_rgb'],
                                                                                       prepare_data['remove_color_thr'])

        return [orig_image, orig_pos, orig_angle]

    @staticmethod
    def create_sprite_type_from_file(name, path, show_infos=False, show_warnings=True):
        # load data
        path = os.path.join(path, str(name))
        infos = []
        warnings = []
        sprite_type_data = sprite_type_loader.Sprite_type_loader.load_data(path, [], infos, warnings,
                                                                           "SPRITE " + str(name) + ":")

        if not sprite_type_data:
            if show_warnings: print(warnings)
            if show_infos: print(infos)
            return False

        # create sprite and costumes
        sprite_type = st.Sprite_type()
        for cost_data in sprite_type_data['costumes']:
            image = cost_data['image']
            posx = cost_data['posx'] if cost_data['posx'] is not None else image.get_width()/2
            posy = cost_data['posy'] if cost_data['posy'] is not None else image.get_height()/2
            pos = [posx, posy]
            angle = cost_data['angle']

            # prepare image
            if 'process' in cost_data:
                image, pos, angle = Sprite_type_factory._prepare_image(image, pos, angle, cost_data['process'])

            cost = sprite_type_costume.Sprite_type_costume_image(image, pos, angle)
            sprite_type.add_costume(cost_data['name'], cost)

        if show_warnings: print(warnings)
        if show_infos: print(infos)

        return sprite_type

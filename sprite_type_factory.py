import os, sprite_type_loader, sprite_type as st, sprite_type_costume

class Sprite_type_factory():
    @staticmethod
    def create_sprite_type_from_file(name, path, show_infos=False, show_warnings=True):
        #load data
        path = os.path.join(path, str(name))
        infos = []
        warnings = []
        sprite_type_data = sprite_type_loader.Sprite_type_loader.load_data(path, [], infos, warnings, "SPRITE "+str(name)+":")

        if not sprite_type_data:
            if show_warnings: print(warnings)
            if show_infos: print(infos)
            return False

        #create sprite and costumes
        sprite_type = st.Sprite_type()
        for cost_data in sprite_type_data['costumes']:
            pos = [cost_data['posx'], cost_data['posy']]
            cost = sprite_type_costume.Sprite_type_costume_image(cost_data['image'], pos, cost_data['angle'])

            sprite_type.add_costume(cost_data['name'], cost)

        if show_warnings: print(warnings)
        if show_infos: print(infos)

        return sprite_type
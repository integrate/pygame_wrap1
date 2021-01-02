import wrap_base

def _get_sprite_by_id(id):
    sprite = wrap_base.sprite_id_manager.get_obj_by_id(id)
    if not sprite:
        raise Exception()  # TODO временный код
    return sprite

def get_font_name(id):
    pass
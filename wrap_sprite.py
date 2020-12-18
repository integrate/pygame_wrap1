import wrap_base
import sprite_of_type


def _get_sprite_by_id(id):
    sprite = wrap_base.sprite_id_manager.get_obj_by_id(id)
    if not sprite:
        raise Exception()  # TODO временный код
    return sprite


def add_sprite(sprite_type_name, x, y, visible=True):
    # get sprite type
    sprite_type = wrap_base.sprite_type_manager.get_sprite_type_by_name(sprite_type_name)
    if not sprite_type:
        raise Exception()  # TODO временный код

    sprite = sprite_of_type.Sprite_of_type(sprite_type, x, y, "1", visible)

    id = wrap_base.sprite_id_manager.add_object(sprite)
    wrap_base.world.sprite_manager.add_image_sprite(sprite)

    return id

def change_sprite_costume(id, costume_name):
    sprite = _get_sprite_by_id(id)
    sprite.set_costume(costume_name)

def get_sprite_costume(id):
    return _get_sprite_by_id(id).get_sprite_costume()

def move_sprite_by(id, dx, dy):
    _get_sprite_by_id(id).move_sprite_by(dx, dy)


def change_sprite_size(id, width, height):
    _get_sprite_by_id(id).change_size(int(width), int(height))


def get_sprite_width(id):
    return _get_sprite_by_id(id).get_width()


def get_sprite_height(id):
    return _get_sprite_by_id(id).get_height()

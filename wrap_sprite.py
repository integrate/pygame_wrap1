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


def change_sprite_size(id, width, height):
    _get_sprite_by_id(id).change_size(int(width), int(height))


def get_sprite_width(id):
    return _get_sprite_by_id(id).get_width()


def get_sprite_height(id):
    return _get_sprite_by_id(id).get_height()


def get_sprite_flipx_reverse(id):
    return _get_sprite_by_id(id).get_flipx_reverse()


def get_sprite_flipy_reverse(id):
    return _get_sprite_by_id(id).get_flipy_reverse()


def set_sprite_flipx_reverse(id, flipx):
    return _get_sprite_by_id(id).set_flipx_reverse(flipx)

def set_sprite_flipy_reverse(id, flipy):
    return _get_sprite_by_id(id).set_flipy_reverse(flipy)


def set_sprite_angle(id, angle):
    _get_sprite_by_id(id).set_angle_modification(angle)


def get_sprite_angle(id):
    return _get_sprite_by_id(id).get_angle_modification()

def get_sprite_final_angle(id):
    return _get_sprite_by_id(id).get_final_angle()

def move_sprite_to(id, x, y):
    return _get_sprite_by_id(id).move_sprite_to(x, y)

def move_sprite_by(id, dx, dy):
    _get_sprite_by_id(id).move_sprite_by(dx, dy)


def is_sprite_visible(id):
    return _get_sprite_by_id(id).get_visible()


def show_sprite(id):
    _get_sprite_by_id(id).set_visible(True)


def hide_sprite(id):
    _get_sprite_by_id(id).set_visible(False)


def move_sprite_at_angle(id, angle, distance):
    _get_sprite_by_id(id).move_sprite_at_angle(angle, distance)


def move_sprite_to_angle(id, distance):
    _get_sprite_by_id(id).move_sprite_to_angle(distance)

def move_sprite_to_point(id, x, y, distance):
    _get_sprite_by_id(id).move_sprite_to_point([x, y], distance)

def rotate_to_point(id, x, y):
    _get_sprite_by_id(id).rotate_to_point([x, y])
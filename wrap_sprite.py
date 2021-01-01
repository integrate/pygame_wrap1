import settings, wrap_base
import sprite_of_type, sprite_type_factory


def _get_sprite_by_id(id):
    sprite = wrap_base.sprite_id_manager.get_obj_by_id(id)
    if not sprite:
        raise Exception()  # TODO временный код
    return sprite


def add_sprite(sprite_type_name, x, y, visible=True, costume=None):
    # get sprite type
    if not wrap_base.sprite_type_manager.has_sprite_type_name(sprite_type_name):
        st = sprite_type_factory.Sprite_type_factory.create_sprite_type_from_file(sprite_type_name,
                                                                                  settings.SPRITE_TYPES_PATH)
        wrap_base.sprite_type_manager.add_sprite_type(st, sprite_type_name)

    sprite_type = wrap_base.sprite_type_manager.get_sprite_type_by_name(sprite_type_name)
    if not sprite_type:
        raise Exception(str(sprite_type_name) + " loading failed.")

    #make sprite of sprite type
    sprite = sprite_of_type.Sprite_of_type(sprite_type, x, y, costume, visible)

    #register sprite
    id = wrap_base.sprite_id_manager.add_object(sprite)
    wrap_base.world.sprite_manager.add_image_sprite(sprite)

    return id


def change_sprite_costume(id, costume_name, save_moving_angle=False, apply_proc_size=True):
    sprite = _get_sprite_by_id(id)
    sprite.set_costume(costume_name, save_moving_angle, apply_proc_size)

def set_next_costume(id, save_moving_angle=False, apply_proc_size=True):
    sprite = _get_sprite_by_id(id)
    sprite.set_costume_by_offset(1, save_moving_angle, apply_proc_size)

def set_previous_costume(id, save_moving_angle=False, apply_proc_size=True):
    sprite = _get_sprite_by_id(id)
    sprite.set_costume_by_offset(-1, save_moving_angle, apply_proc_size)


def get_sprite_costume(id):
    return _get_sprite_by_id(id).get_sprite_costume()



def get_sprite_width(id):
    return _get_sprite_by_id(id).get_width_pix()

def get_sprite_height(id):
    return _get_sprite_by_id(id).get_height_pix()

def get_sprite_size(id):
    return _get_sprite_by_id(id).get_size_pix()

def set_sprite_original_size(id):
    _get_sprite_by_id(id).set_original_size()

def change_sprite_size(id, width, height):
    _get_sprite_by_id(id).change_size_pix(int(width), int(height))

def change_sprite_width(id, width):
    _get_sprite_by_id(id).change_width_pix(width)

def change_sprite_height(id, height):
    _get_sprite_by_id(id).change_height_pix(height)

def change_width_proportionally(id, width, from_modified=False):
    _get_sprite_by_id(id).change_width_pix_proportionally(width, from_modified)

def change_height_proportionally(id, height, from_modified=False):
    _get_sprite_by_id(id).change_height_pix_proportionally(height, from_modified)

def get_sprite_width_proc(id):
    return _get_sprite_by_id(id).get_width_proc()

def get_sprite_height_proc(id):
    return _get_sprite_by_id(id).get_height_proc()

def get_sprite_size_proc(id):
    return _get_sprite_by_id(id).get_size_proc()

def change_sprite_size_proc(id, width, height):
    _get_sprite_by_id(id).change_size_proc(int(width), int(height))

def change_sprite_width_proc(id, width):
    _get_sprite_by_id(id).change_width_proc(width)

def change_sprite_height_proc(id, height):
    _get_sprite_by_id(id).change_height_proc(height)

def change_sprite_size_by_proc(id, proc):
    _get_sprite_by_id(id).change_size_by_proc(proc)

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

import wrap_base
import sprite_of_type




def add_sprite(sprite_type_name, x, y, visible=True):
    #get sprite type
    sprite_type = wrap_base.sprite_type_manager.get_sprite_type_by_name(sprite_type_name)
    if not sprite_type:
        raise Exception()#TODO временный код

    sprite = sprite_of_type.Sprite_of_type(sprite_type, x, y, None, visible)

    id = wrap_base.sprite_id_manager.add_object(sprite)
    wrap_base.world.sprite_manager.add_image_sprite(sprite)

    return id

def move_sprite_by(id, dx, dy):
    sprite = wrap_base.sprite_id_manager.get_obj_by_id(id)
    if not sprite:
        raise Exception()  # TODO временный код

    # TODO временный код
    sprite.rect.move_ip(dx, dy)
    sprite.dirty = 1
import pygame
from wrap import world, app, event, sprite, text_sprite

app.set_fps(100)

world.create_world(1000, 1000)
world.set_world_background_color([10, 20, 30])

# sp1_id = sprite.add_sprite("type2", 600, 600, True, "1")
sp1_id = sprite.add_text(600, 600, "Ха Ха Ха", text_color=[255, 255, 255])
sp2_id = sprite.add_sprite("type2", 600, 600, False, "man1")
sp_mark_id = sprite.add_sprite("type3", 500, 500, True)


def on_right_clicked(key, unicode):
    sprite.set_bottom_to(sp1_id, 100)


def on_left_clicked(keys):
    sprite.set_top_to(sp1_id, 100)


width = 100


def _show_sprite_size(id):
    x, y = sprite.get_sprite_size(id)
    xpr, ypr = sprite.get_sprite_size_proc(id)

    print('width: ' + str(x) + " pix / " + str(xpr) + "%")
    print('height: ' + str(y) + " pix / " + str(ypr) + "%")


def _check_collision(id1, id2):
    res = sprite.sprites_collide(id1, id2)
    if res:
        sprite.move_sprite_to(sp_mark_id, res[0], res[1])
        sprite.show_sprite(sp_mark_id)
    else:
        sprite.hide_sprite(sp_mark_id)


def _check_collision_any(id1, id_list):
    res = sprite.sprites_collide_any(id1, id_list)
    # print(res)


def _check_collision_all(id1, id_list):
    res = sprite.sprites_collide_all(id1, id_list)
    # print(res)


def on_up_clicked(control_keys):
    global width
    width += 5
    if pygame.KMOD_SHIFT in control_keys:
        sprite.change_sprite_height_proc(sp1_id, width)
    else:
        from_modified = pygame.KMOD_ALT in control_keys
        if from_modified:
            sprite.change_sprite_size_by_proc(sp1_id, 105)
        else:
            sprite.change_sprite_size_proc(sp1_id, width, width)
    _show_sprite_size(sp1_id)


def on_down_clicked(control_keys):
    global width
    width -= 5
    if pygame.KMOD_SHIFT in control_keys:
        sprite.change_sprite_height_proc(sp1_id, width)
    else:
        from_modified = pygame.KMOD_ALT in control_keys
        if from_modified:
            sprite.change_sprite_size_by_proc(sp1_id, 95)
        else:
            sprite.change_sprite_size_proc(sp1_id, width, width)

    _show_sprite_size(sp1_id)


def on_zero_clicked():
    sprite.set_sprite_original_size(sp1_id)


def on_space_clicked(key, unicode, dasfg):
    global sp1_id, sp2_id
    t = sp1_id
    sp1_id = sp2_id
    sp2_id = t


size_diff = 1


def on_one_clicked(control_keys):
    global size_diff
    apply_proc_size = pygame.KMOD_SHIFT not in control_keys
    sprite.set_previous_costume(sp1_id, True, apply_proc_size)

    if text_sprite.is_sprite_text(sp1_id):
        s = text_sprite.get_angle(sp1_id)
        if s==None:
            s=45
        elif s==45:
            s =215
        else:
            s = None

        text_sprite.set_angle(sp1_id, s)
        print(text_sprite.get_angle(sp1_id))

    _show_sprite_size(sp1_id)


def on_two_clicked():
    flipx = sprite.get_sprite_flipx_reverse(sp1_id)
    sprite.set_sprite_flipx_reverse(sp1_id, not flipx)


def on_three_clicked():
    flipy = sprite.get_sprite_flipy_reverse(sp1_id)
    sprite.set_sprite_flipy_reverse(sp1_id, not flipy)


def on_four_clicked():
    if not sprite.is_sprite_visible(sp1_id):
        sprite.show_sprite(sp1_id)
    else:
        sprite.hide_sprite(sp1_id)


def on_five_clicked():
    pass


def on_six_clicked():
    pass


def on_w_clicked():
    a = sprite.get_sprite_angle(sp1_id)
    sprite.set_sprite_angle(sp1_id, a + 5)


def on_s_clicked():
    a = sprite.get_sprite_angle(sp1_id)
    sprite.set_sprite_angle(sp1_id, a - 5)


def on_d_clicked():
    sprite.move_sprite_to_angle(sp1_id, 10)


def on_a_clicked():
    sprite.move_sprite_to_angle(sp1_id, -10)


def on_sec1():
    # print(sprite.get_sprite_final_angle(sp1_id))
    _check_collision_all(sp1_id, [sp2_id, sp_mark_id])


def on_sec2():
    sprite.move_sprite_by(-20, 0)


def on_mouse_pressed(pos):
    # sprite.move_sprite_to_point(sp1_id, pos[0], pos[1], 3)
    sprite.rotate_to_point(sp1_id, pos[0], pos[1])
    sprite.move_sprite_to_angle(sp1_id, 30)


# left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
# left_id = event.on_key_pressed([pygame.K_LEFT, pygame.K_RIGHT], on_left_clicked, 100, [pygame.KMOD_LALT, pygame.KMOD_RSHIFT])
right_id = event.on_key_down(pygame.K_RIGHT, on_right_clicked)
left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
up_id = event.on_key_down(pygame.K_UP, on_up_clicked)
down_id = event.on_key_down(pygame.K_DOWN, on_down_clicked)
space_id = event.on_key_down(pygame.K_SPACE, on_space_clicked)
zero_id = event.on_key_down(pygame.K_0, on_zero_clicked)
one_id = event.on_key_down(pygame.K_1, on_one_clicked)
two_id = event.on_key_down(pygame.K_2, on_two_clicked)
three_id = event.on_key_down(pygame.K_3, on_three_clicked)
four_id = event.on_key_down(pygame.K_4, on_four_clicked)
five_id = event.on_key_down(pygame.K_5, on_five_clicked)
six_id = event.on_key_down(pygame.K_6, on_six_clicked)
w_id = event.on_key_down(pygame.K_w, on_w_clicked)
s_id = event.on_key_down(pygame.K_s, on_s_clicked)
d_id = event.on_key_down(pygame.K_d, on_d_clicked)
a_id = event.on_key_down(pygame.K_a, on_a_clicked)
# close_id = event.on_close(on_close)
sec_id1 = event.on_timeout(50, 0, on_sec1)
# sec_id2 = event.on_timeout(1000, 5, on_sec2)
mouse_pressed_id = event.on_mouse_pressed([0], on_mouse_pressed, 100)

app.start()

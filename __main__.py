import pygame, wrap, time, math
from wrap import world, app, event, sprite

app.set_fps(100)

world.create_world(1000, 1000)

sp1_id = sprite.add_sprite("type1", 600, 600, True)
w = sprite.get_sprite_width(sp1_id)
h = sprite.get_sprite_height(sp1_id)
sprite.change_sprite_size(sp1_id, w * 0.3, h * 0.3)

def on_right_clicked(key, unicode):
    sprite.move_sprite_by(sp1_id, 10, 0)


def on_left_clicked(keys):
    sprite.move_sprite_by(sp1_id, -10, 0)

def on_up_clicked():
    w = sprite.get_sprite_width(sp1_id)
    h = sprite.get_sprite_height(sp1_id)
    sprite.change_sprite_size(sp1_id, w*1.1, h*1.1)

def on_down_clicked():
    w = sprite.get_sprite_width(sp1_id)
    h = sprite.get_sprite_height(sp1_id)
    sprite.change_sprite_size(sp1_id, w * 0.9, h * 0.9)


def on_space_clicked(key, unicode, dasfg):
    sprite.change_sprite_size(sp1_id, 200, 300)

def on_one_clicked(key, unicode, dasfg):
    if sprite.get_sprite_costume(sp1_id)=="1":
        sprite.change_sprite_costume(sp1_id, "2")
    else:
        sprite.change_sprite_costume(sp1_id, "1")

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
    sprite.set_sprite_angle(sp1_id, a+5)

def on_s_clicked():
    a = sprite.get_sprite_angle(sp1_id)
    sprite.set_sprite_angle(sp1_id, a-5)

def on_d_clicked():
    sprite.move_sprite_to_angle(sp1_id, 10)

def on_a_clicked():
    sprite.move_sprite_to_angle(sp1_id, -10)

def on_sec1():
    pass


def on_sec2():
    sprite.move_sprite_by(-20, 0)


def on_mouse_pressed(pos):
    print(pos)


# left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
# left_id = event.on_key_pressed([pygame.K_LEFT, pygame.K_RIGHT], on_left_clicked, 100, [pygame.KMOD_LALT, pygame.KMOD_RSHIFT])
right_id = event.on_key_down(pygame.K_RIGHT, on_right_clicked)
left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
up_id = event.on_key_down(pygame.K_UP, on_up_clicked)
down_id = event.on_key_down(pygame.K_DOWN, on_down_clicked)
space_id = event.on_key_down(pygame.K_SPACE, on_space_clicked)
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
# sec_id1 = event.on_timeout(50, 0, on_sec1)
# sec_id2 = event.on_timeout(1000, 5, on_sec2)
mouse_pressed_id = event.on_mouse_pressed([0], on_mouse_pressed, 100)

app.start()

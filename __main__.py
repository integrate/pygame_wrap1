import pygame, wrap, time, math
from wrap import world, app, event, sprite

app.set_fps(100)

world.create_world(1000, 1000)

sp1_id = sprite.add_sprite("temp_name", 100, 200, True)


w = world.wrap_base.world._window
orig_im = pygame.image.load("sprite_types/type1/costumes/1.png")
orig_im = pygame.transform.scale(orig_im, [300, 200])

orig_rect = orig_im.get_rect()
orig_center = orig_rect.center
orig_point = orig_rect.topright

pygame.draw.circle(orig_im, [255, 0, 0], orig_im.get_rect().topleft, 2)
angle = 0






def on_right_clicked(key, unicode):
    sprite.move_sprite_by(sp1_id, 10, 0)


def on_left_clicked(keys):
    pass


def on_space_clicked(key, unicode, dasfg):
    pass


def on_close():
    print("goodbye")
    event.stop_listening(left_id)
    # exit()


def on_sec1():
    pass


def on_sec2():
    sprite.move_sprite_by(-20, 0)


def restart_rotation(op):
    global orig_im, orig_rect, orig_center, orig_point, angle
    orig_im = pygame.image.load("sprite_types/type1/costumes/1.png")
    orig_im = pygame.transform.scale(orig_im, [300, 200])
    orig_rect = orig_im.get_rect()
    orig_center = orig_rect.center
    orig_point = op

    pygame.draw.circle(orig_im, [255, 0, 0], orig_point, 2)
    angle = 0


def on_mouse_pressed(pos):
    pass


# left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
# left_id = event.on_key_pressed([pygame.K_LEFT, pygame.K_RIGHT], on_left_clicked, 100, [pygame.KMOD_LALT, pygame.KMOD_RSHIFT])
right_id = event.on_key_down(pygame.K_RIGHT, on_right_clicked)
# left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
# space_id = event.on_key_down(pygame.K_SPACE, on_space_clicked)
# close_id = event.on_close(on_close)
# sec_id1 = event.on_timeout(50, 0, on_sec1)
# sec_id2 = event.on_timeout(1000, 5, on_sec2)
# mouse_pressed_id = event.on_mouse_pressed([0], on_mouse_pressed, 1000)

app.start()

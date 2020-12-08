import pygame, wrap, time
from wrap import world, app, event, sprite

app.set_fps(100)

# world.set_world_background_color([100, 200, 200])
world.set_world_background_image("bkgs/1.jpg")
world.create_world(1000, 200)

sprite.add_sprite(100, 200, True, 100, 100)

def on_right_clicked(key, unicode):
    sprite.move_sprite_by(10, 0)

def on_left_clicked(keys):
    print(keys)
    sprite.move_sprite_by(-10, 0)

def on_space_clicked(key, unicode, dasfg):
    event.stop_listening(sec_id2)

def on_close():
    print("goodbye")
    event.stop_listening(left_id)
    # exit()

def on_sec1():
    sprite.move_sprite_by(10, 0)

def on_sec2():
    sprite.move_sprite_by(-20, 0)

def on_mouse_pressed(control_keys, mouse_buttons):
    print(control_keys, "|", mouse_buttons)

# left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
left_id = event.on_key_pressed([pygame.K_LEFT, pygame.K_RIGHT], on_left_clicked, 100, [pygame.KMOD_LALT, pygame.KMOD_RSHIFT])
# right_id = event.on_key_down(pygame.K_RIGHT, on_right_clicked)
space_id = event.on_key_down(pygame.K_SPACE, on_space_clicked)
close_id = event.on_close(on_close)
sec_id1 = event.on_timeout(1000, 0, on_sec1)
time.sleep(0.5)
sec_id2 = event.on_timeout(1000, 5, on_sec2)
mouse_pressed_id = event.on_mouse_pressed([0, 1, 2, 3], on_mouse_pressed, 100, [pygame.KMOD_ALT, pygame.KMOD_SHIFT])

app.start()


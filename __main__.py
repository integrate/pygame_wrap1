import pygame, wrap
from wrap import world, app, event, sprite

app.set_fps(100)

# world.set_world_background_color([100, 200, 200])
world.set_world_background_image("bkgs/1.jpg")
world.create_world(1000, 200)

sprite.add_sprite(100, 200, True, 100, 100)

def on_right_clicked(key, unicode, **kwargs):
    sprite.move_sprite_by(10, 0)

def on_left_clicked(key, unicode, **kwargs):
    sprite.move_sprite_by(-10, 0)

def on_space_clicked(key, unicode, **kwargs):
    pass

def on_close(**kwargs):
    print("goodbye")
    # exit()

def on_sec1(**kwargs):
    sprite.move_sprite_by(10, 0)

def on_sec2(**kwargs):
    sprite.move_sprite_by(-20, 0)

left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
right_id = event.on_key_down(pygame.K_RIGHT, on_right_clicked)
space_id = event.on_key_down(pygame.K_SPACE, on_space_clicked)
close_id = event.on_close(on_close)
sec_id1 = event.on_timout(1000, 0, on_sec1)
sec_id2 = event.on_timout(1000, 5, on_sec2)

app.start()


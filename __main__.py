import pygame, wrap
from wrap import world, app, event, sprite

app.set_fps(100)

# world.set_world_background_color([100, 200, 200])
# world.set_world_background_image("bkgs/1.jpg")
world.create_world(1000, 200)

sprite.add_sprite(100, 200, True, 100, 100)

def on_right_clicked(key, unicode, **kwargs):
    sprite.move_sprite_by(10, 0)

event.on_key_down(pygame.K_RIGHT, on_right_clicked)



app.start()


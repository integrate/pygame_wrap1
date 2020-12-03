import app, world, event_generator, sprite
import pygame

w = world.World()
w.set_world_background_color([100, 200, 200])
w.create_world(200, 200)
w.change_world(1000, 700)
w.set_world_background_image("bkgs/1.jpg")
w.change_world_fullscreen()
w.change_world(1000, 700)

print(w.get_world_size())
print(w.get_world_fullscreen())

im = pygame.image.load("sprite_types/type1/costumes/1.png")
s1 = sprite.Sprite_image(im, 500, 500)
w.sprite_manager.add_sprite(s1)

eg = event_generator.Event_generator()

a = app.App(w, eg)
a.set_fps(100)

a.start()
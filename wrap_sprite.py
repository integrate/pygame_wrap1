import wrap_base
import sprite
import pygame

s1 = 0
def add_sprite(x, y, visible=True, width=None, height=None):
    global s1
    im = pygame.image.load("sprite_types/type1/costumes/1.png")
    s1 = sprite.Sprite_image(im, x, y, visible, width, height)
    wrap_base.world.sprite_manager.add_sprite(s1)

def move_sprite_by(dx, dy):
    s1.rect.move_ip(dx, dy)
    s1.dirty = 1
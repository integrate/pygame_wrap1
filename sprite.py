import pygame
from pygame import sprite

class Sprite():
    def __init__(self):
        object.__init__(self)

        self.__sprite = sprite.DirtySprite()
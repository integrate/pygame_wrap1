import pygame


class Sprite_manager():
    def __init__(self, window, bkg):
        object.__init__(self)

        self._window = window
        self._bkg = bkg

        self._group = pygame.sprite.LayeredDirty()
        self._group.clear(None, self._bkg)

    def _set_background(self, bkg):
        if self._bkg is bkg: return

        self._bkg = bkg
        self._group.clear(None, self._bkg)

    def add_sprite(self, sprite):
        self._group.add(sprite)

    def update_sprites(self):
        self._group.draw(self._window)


class Sprite_image(pygame.sprite.DirtySprite):
    def __init__(self, image, x, y, visible = True, width=None, height=None):
        pygame.sprite.DirtySprite.__init__(self)

        self.dirty = 0

        self.image = image.copy()
        self.rect = self.image.get_rect()

        self.visible = visible
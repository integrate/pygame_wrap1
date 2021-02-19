import pygame
from wrap_engine import sprite


class World:
    def __init__(self):
        object.__init__(self)

        self.sprite_manager = None

        self._window = None

        self._bkg_color = [0, 0, 0]
        self._bkg_pic = None
        self._bkg = pygame.Surface([1000, 1000])

    def _is_world_created(self):
        return self._window is not None

    def _update_bkg(self):
        if self._window is None: return

        w, h = self._window.get_size()
        fon = pygame.Surface([w, h])
        fon.fill(self._bkg_color)

        if self._bkg_pic is not None:
            fon.blit(self._bkg_pic, [0, 0])

        self._bkg = fon
        self._window.blit(self._bkg, [0, 0])

    def _update_sprite_manager(self):
        if self.sprite_manager is None and self._window is not None:
            self.sprite_manager = sprite.Sprite_manager(self._window, self._bkg)

        if self.sprite_manager is not None:
            self.sprite_manager._set_background(self._bkg)


    def create_world(self, width, height):
        self._window = pygame.display.set_mode([width, height], 0)
        self._update_bkg()
        self._update_sprite_manager()

    def change_world(self, width, height):
        self.create_world(width, height)

    def create_world_fullscreen(self):
        self._window = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
        self._update_bkg()
        self._update_sprite_manager()

    def change_world_fullscreen(self):
        self.create_world_fullscreen()

    def get_world_size(self):
        if not self._is_world_created():
            raise Exception()

        return self._window.get_size()

    def get_world_fullscreen(self):
        if not self._is_world_created():
            raise Exception()

        return bool(self._window.get_flags() & pygame.FULLSCREEN)

    def set_world_background_color(self, color):
        self._bkg_color = [*color]
        self._update_bkg()
        self._update_sprite_manager()

    def set_world_background_image(self, path_to_file, fill=False):
        self._bkg_pic = pygame.image.load(path_to_file)
        self._update_bkg()
        self._update_sprite_manager()



    def update(self):
        if not self._is_world_created():
            return

        if self.sprite_manager is not None:
            self.sprite_manager.update_sprites()

        pygame.display.flip()

import pygame

class World:
    def __init__(self):
        object.__init__(self)

        self._window = None

    def _is_world_created(self):
        return self._window is not None

    def create_world(self, width, height):
        self._window = pygame.display.set_mode([width, height], 0)

    def change_world(self, width, height):
        self.create_world(width, height)


    def create_world_fullscreen(self):
        self._window = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
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


    def update(self):
        if not self._is_world_created():
            return

        self._window.fill([100, 200, 120])
        pygame.display.flip()
import pygame

class App:

    def __init__(self, world, event_generator):
        object.__init__(self)

        self.fps = 60
        self._clock = pygame.time.Clock()

        self.world = world
        self.event_generator = event_generator



    def get_fps(self):
        return self.fps
    def set_fps(self, fps):
        self.fps = fps
    def get_real_fps(self):
        return self._clock.get_fps()

    def start(self):
        while True:
            self._clock.tick(self.fps)

            self.event_generator.process_events()

            if self.world._is_world_created():
                self.world.update()
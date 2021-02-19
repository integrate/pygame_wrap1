import pygame, threading


class App:

    def __init__(self, world, event_generator):
        object.__init__(self)

        self.fps = 60
        self._clock = pygame.time.Clock()

        self.world = world
        self.event_generator = event_generator

        self._started = False

    def get_fps(self):
        return self.fps

    def set_fps(self, fps):
        self.fps = fps

    def get_real_fps(self):
        return self._clock.get_fps()

    def _do_cycle(self):
        self.event_generator.process_events()

        if self.world._is_world_created():
            self.world.update()

    def start(self, on_tick = None):
        if self._started:
            return

        self._started = True

        while True:
            self._clock.tick(self.fps)
            self._do_cycle()
            if on_tick is not None:
                on_tick()

    # def _serve_connections(self, timeout_to_all_connections):
    #     if len(self._rpyc_connections)==0:
    #         return
    #
    #     one_timeout = timeout_to_all_connections/len(self._rpyc_connections)
    #     for i in self._rpyc_connections.copy():
    #         if i.closed:
    #             continue
    #         i.poll_all(one_timeout)

    # def start_as_server(self):
    #     while True:
    #         with self._lock:
    #             self._serve_connections(1/self.fps)
    #             self._clock.tick(self.fps)
    #             self._do_cycle()
    #
    # def start_with_connection(self, connection):
    #     while True:
    #         if not connection.closed:
    #             connection.poll_all(1/self.fps)
    #         else:
    #             break
    #
    #         self._clock.tick(self.fps)
    #         self._do_cycle()
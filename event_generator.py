import pygame
import condition_checker, event_id_pool, environ_data, event

PYGAME_EVENT_TYPES_TO_PROCESS = [
    pygame.KEYDOWN, pygame.KEYUP,
    pygame.MOUSEMOTION,
    pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP,
    pygame.QUIT
]


class Event_generator:
    def __init__(self):
        object.__init__(self)

        self._pygame_event_id_pool = event_id_pool.Event_id_pool.get_pygame_pool()

        # debug
        fil = {
            "type": pygame.KEYDOWN,
            "key": [pygame.K_RIGHT, pygame.K_LEFT]
        }
        c = condition_checker.Condition_checker_pygame_event(environ_data.get_data(), fil)
        self.et = event.ConditionalEventType(environ_data.get_data(), [c])

    def process_events(self):

        # process events
        active_event = None
        pygame_events = pygame.event.get()
        for pev in pygame_events:
            # if type not used
            if pev.type not in PYGAME_EVENT_TYPES_TO_PROCESS and \
                    not self._pygame_event_id_pool.is_id_used_free_or_busy(pev.type):
                continue

            # if native pygame event
            if pev.type in PYGAME_EVENT_TYPES_TO_PROCESS:
                environ_data.update_data(pev)

            if self.et.confirms():
                e = self.et.make_event()
                print(e)

import pygame
import condition_checker, event_id_pool, environ_data, event

PYGAME_EVENT_TYPES_TO_PROCESS = [
    pygame.KEYDOWN, pygame.KEYUP,
    pygame.MOUSEMOTION,
    pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP,
    pygame.QUIT
]

pygame.init()
pygame.key.set_repeat(50)

class Event_generator:
    def __init__(self, message_broker):
        object.__init__(self)

        self.message_broker = message_broker

        self._event_types = {}#id->Event_type

        # debug
        # fil = {
        #     "type": pygame.KEYDOWN,
        #     "key": [pygame.K_RIGHT, pygame.K_LEFT]
        # }
        # c = condition_checker.Condition_checker_pygame_event(environ_data.get_data(), fil)
        # self.et = event.ConditionalEventType(self._environ_data, [c])

    def _clean_timers(self):
        pass

    def start_event_notification(self,
                                 delay=None, count=None,
                                 event_filter=None, key_codes=None, control_keys=None, mouse_buttons=None
                                 ):
        checkers = []

        #create filter by pygame event
        if event_filter is not None:
            chkr = condition_checker.Condition_checker_pygame_event(event_filter)
            checkers.append(chkr)

        event_type = event.ConditionalEventType(checkers)

        assert event_type.id not in self._event_types, "Id of EventType must be unique!"
        self._event_types[event_type.id] = event_type

        return event_type.id

    def stop_event_notification(self, event_type_id):
        if event_type_id in self._event_types:
            del self._event_types[event_type_id]

        self._clean_timers()


    def process_events(self):

        pygame_event_id_pool = event_id_pool.Event_id_pool.get_pygame_pool()

        # process events
        active_event = None
        pygame_events = pygame.event.get()
        for pev in pygame_events:
            # if type not used
            if pev.type not in PYGAME_EVENT_TYPES_TO_PROCESS and \
                    not pygame_event_id_pool.is_id_used_free_or_busy(pev.type):
                continue

            #update data about environment
            # if native pygame event
            if pev.type in PYGAME_EVENT_TYPES_TO_PROCESS:
                environ_data.update_data(pev)
            else: #any other event
                environ_data.update_data(None)

            #notify broker
            _event_types = self._event_types.copy()
            for event_id in _event_types:
                event_type = _event_types[event_id]
                if event_type.confirms():
                    event = event_type.make_event()
                    self.message_broker.notify(event)

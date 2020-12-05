import pygame
import condition_checker, event_id_pool, environ_data, event, timer

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

        self._event_types = {}  # id->Event_type

        self._timers = {}  # pygame_event_id -> Timer

    def _get_timer(self, delay, count):
        if count != 0:
            t = timer.Timer(delay, count, True)
            self._timers[t.get_pygame_event_id()] = t
            return t

        for id in self._timers:
            t = self._timers[id]
            if t.delay == delay and t.count == count and t.get_state() == timer.TIMER_STATE_ACTIVE:
                return t

        t = timer.Timer(delay, count, True)
        self._timers[t.get_pygame_event_id()] = t
        return t

    def _clean_timers(self):

        pass#TODO clean timers

    def start_event_notification(self,
                                 delay=None, count=0,
                                 event_filter=None, key_codes=None, control_keys=None, mouse_buttons=None
                                 ):
        checkers = []

        # create filter by pygame event
        if event_filter is not None:
            chkr = condition_checker.Condition_checker_pygame_event(event_filter)
            checkers.append(chkr)

        # create filter by timer
        if delay is not None:
            t = self._get_timer(delay, count)
            checkers.append(t)

        # create and save EventType
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

            # update data about environment
            environ_data.update_data()
            # if native pygame event
            if pev.type in PYGAME_EVENT_TYPES_TO_PROCESS:
                environ_data.set_active_pygame_event(pev)
            else:
                environ_data.set_active_pygame_event(None)

            # turn on timer
            if pev.type in self._timers:
                self._timers[pev.type].on()

            # notify broker
            _event_types = self._event_types.copy()
            for event_id in _event_types:
                event_type = _event_types[event_id]
                if event_type.confirms():
                    event = event_type.make_event()
                    self.message_broker.notify(event)

            # turn off timers
            for t in self._timers:
                self._timers[t].off()
            # turn off pygame event
            environ_data.set_active_pygame_event(None)

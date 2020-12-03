import event_id_pool, condition_checker

class Event():
    def __init__(self, typeid, data):
        object.__init__(self)

        self.type = typeid

        for key in data:
            setattr(self, key, data[key])


class EventType(condition_checker.Condition_checker):
    def __init__(self):
        condition_checker.Condition_checker.__init__(self)

        self.id = event_id_pool.Event_id_pool.get_usual_pool().get_id()

    def confirms(self):
        assert False, "Method confirms() of class EventType is abstract and must be overriden"
        return False

    def make_event(self):
        assert False, "Method make_event() of class EventType is abstract and must be overriden"
        return None


class ConditionalEventType(EventType):
    def __init__(self, environ_data, checkers):
        EventType.__init__(self)
        self._environ_data = environ_data
        self._checkers = [*checkers]

    def confirms(self):
        for ch in self._checkers:
            if not ch.confirms():
                return False

        return True

    def make_event(self):
        assert self.confirms(), "EventType must confirm to generate event"

        event_data = {}

        #collect checkers classes
        types = []
        for ch in self._checkers:
            types.append(ch.__class__)

        if condition_checker.Condition_checker_pygame_event in types:
            #collect pygame event data
            pygame_event = self._environ_data['active_pygame_event']
            pygame_event_data = vars(pygame_event)
            for attr in pygame_event_data:
                event_data[attr] = pygame_event_data[attr]

        return Event(self.id, event_data)
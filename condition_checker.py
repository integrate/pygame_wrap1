import environ_data


class Condition_checker():
    def confirms(self):
        assert False, "Condition_checker class confirms() method is abstract and must be overriden"
        return False


class Condition_checker_pygame_event(Condition_checker):
    def __init__(self, pygame_event_filter):
        Condition_checker.__init__(self)
        self._filter = pygame_event_filter

    def confirms(self):

        if not environ_data.is_active_pygame_event_set():
            return False

        event = environ_data.get_active_pygame_event()
        for attr in self._filter:
            filter_val = self._filter[attr]

            if not hasattr(event, attr): return False

            event_val = getattr(event, attr)

            # check if filter is iterable and val not in sequence
            if hasattr(filter_val, "__iter__") and event_val not in filter_val:
                return False
            # check if filter is simple value and not equal event value
            if (not hasattr(filter_val, "__iter__")) and event_val != filter_val:
                return False

        return True

class Message_broker():
    def __init__(self):
        object.__init__(self)

        self._subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def ubsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify(self, event):
        for sub in self._subscribers:
            if sub.event_type == event.type:
                sub.process_event(event)


class Subscriber():
    def __init__(self, event_type, func):
        object.__init__(self)

        self.event_type = event_type
        self.func = func

    def process_event(self, event):
        assert self.event_type == event.type
        event_data = vars(event)
        self.func(**event_data)

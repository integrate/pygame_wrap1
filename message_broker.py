class Message_broker():
    def __init__(self):
        object.__init__(self)

        self._subscribers = []

    def subscribe(self, subscriber):
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def ubsubscribe(self, subscriber):
        self._subscribers =[el for el in self._subscribers if el is not subscriber]

    def ubsubscribe_by_event_type_id(self, event_type_id):
        self._subscribers =[el for el in self._subscribers if el.event_type_id != event_type_id]

    def notify(self, event):
        for sub in self._subscribers:
            if sub.event_type_id == event.type:
                sub.process_event(event)


class Subscriber():
    def __init__(self, event_type_id, func):
        object.__init__(self)

        self.event_type_id = event_type_id
        self.func = func

    def process_event(self, event):
        assert self.event_type_id == event.type
        event_data = vars(event)
        self.func(**event_data)

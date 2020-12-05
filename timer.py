import condition_checker as cc, event_id_pool

TIMER_STATE_PAUSE = 0
TIMER_STATE_ACTIVE = 1
TIMER_STATE_FINISHED = 2

class Timer(cc.Condition_checker):
    def __init__(self, delay, count, start):
        cc.Condition_checker.__init__(self)

        assert delay>0, "Timer delay must be greater than 0"
        assert count>=0, "Timer count must be 0 or greater"

        self._pygame_event_id = event_id_pool.Event_id_pool.get_pygame_pool().get_id()

        self.delay = delay
        self.count = count
        self._real_count = 0

        self._state=TIMER_STATE_PAUSE
        self._active_is_on=False

        if start:
            self.start()


    def start(self):
        pass
import pygame, time, sched, threading


def _start_queue(event_type, delay_ms, active_event, alive_event):
    # run from sheduler thread
    def sched_thread(event_type, delay_ms, active_event, alive_event):

        # run in sheduler thread on timer
        def _on_action(event_type, active_event, alive_event):
            if not active_event.is_set() or not alive_event.is_set():
                return

            pygame.fastevent.post(pygame.event.Event(event_type))
            # print(event_type)

        sh = sched.scheduler()

        # run until killed
        while alive_event.is_set():

            # wait for activated
            active_event.wait()
            if not alive_event.is_set():  # die if killed when activated
                return

            sh.enter(delay_ms / 1000, 1, _on_action,
                     kwargs={"event_type": event_type, "active_event": active_event, "alive_event": alive_event}
                     )
            sh.run(blocking=True)

    t = threading.Thread(target=sched_thread, args=(event_type, delay_ms, active_event, alive_event),
                         name="event_sheduler")
    t.start()



class Pygame_event_timer():
    def __init__(self, event_type, delay_ms):
        # save settings
        self._event_type = event_type
        self._delay_ms = delay_ms

        # flags
        self._active_event = threading.Event()

        self._alive_event = threading.Event()
        self._alive_event.set()

        _start_queue(self._event_type, self._delay_ms, self._active_event, self._alive_event)


    def start(self):
        assert self._alive_event.is_set()
        self._active_event.set()

    def pause(self):
        assert self._alive_event.is_set()
        self._active_event.clear()

    def kill(self):
        assert self._alive_event.is_set()
        self._alive_event.clear()
        self._active_event.set()

    def is_alive(self):
        return self._alive_event.is_set()

    def is_active(self):
        assert self._alive_event.is_set()
        return self._active_event.is_set()

    def __del__(self):
        self._alive_event.clear()
        self._active_event.set()

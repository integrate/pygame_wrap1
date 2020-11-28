import pygame

class Event_generator:
    def __init__(self):
        object.__init__(self)

    def process_events(self):
        pygame.event.get()
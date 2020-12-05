import pygame

pygame.init()

import app, world, event_generator, message_broker

world = world.World()

broker = message_broker.Message_broker()
event_generator = event_generator.Event_generator(broker)

app = app.App(world, event_generator)






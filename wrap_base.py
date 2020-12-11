import pygame

pygame.init()

import app, world, event_generator, message_broker, object_manager, sprite_type, sprite_of_type

world = world.World()
sprite_manager = world.sprite_manager
sprite_id_manager = object_manager.Object_manager()
sprite_type_manager = sprite_type.Sprite_types_manager()

broker = message_broker.Message_broker()
event_generator = event_generator.Event_generator(broker)


app = app.App(world, event_generator)


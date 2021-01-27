from datetime import timedelta, datetime

now = datetime.now()
last_allowed_day = datetime(2021, 3, 1)
period = last_allowed_day - now
if period.days<0:
    print("Library expired!")
    exit()

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from wrap_engine import app, world, event_generator, message_broker, object_manager, sprite_type, sprite_of_type


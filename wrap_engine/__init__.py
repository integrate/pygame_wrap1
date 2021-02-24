import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

from datetime import datetime

#we can't translate here because user have not chance to set language yet
#from wrap_engine.transl import translator as _

now = datetime.now()
last_allowed_day = datetime(2021, 6, 1)
period = last_allowed_day - now
if period.days<0:
    print("Library expired!")
    exit()



from wrap_engine import app, world, event_generator, message_broker, object_manager, sprite_type, sprite_of_type


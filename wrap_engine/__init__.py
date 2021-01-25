from datetime import timedelta, datetime

now = datetime.now()
last_allowed_day = datetime(2021, 3, 1)
period = last_allowed_day - now
if period.days<0:
    print("Library expired!")
    exit()


from wrap_engine import wrap_world as world, wrap_app as app, wrap_event as event
from wrap_engine import wrap_sprite as sprite
from wrap_engine import wrap_sprite_text as text_sprite
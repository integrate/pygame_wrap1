import app, world, event_generator

w = world.World()
w.create_world(200, 200)
w.change_world_fullscreen()
w.change_world(300, 300)

print(w.get_world_size())
print(w.get_world_fullscreen())

eg = event_generator.Event_generator()

a = app.App(w, eg)
a.set_fps(100)

a.start()
import pygame, wrap, time, math
from wrap import world, app, event, sprite

app.set_fps(100)

# world.set_world_background_color([100, 200, 200])
# world.set_world_background_image("bkgs/1.jpg")
world.create_world(1000, 1000)

# sprite.add_sprite(100, 200, True, 100, 100)


w = world.wrap_base.world._window
orig_im = pygame.image.load("sprite_types/type1/costumes/1.png")
orig_im = pygame.transform.scale(orig_im, [300, 200])

orig_rect = orig_im.get_rect()
orig_center = orig_rect.center
orig_point = orig_rect.topright

pygame.draw.circle(orig_im, [255, 0, 0], orig_im.get_rect().topleft, 2)
angle = 0


def get_point_on_circle(center, start_point, angle_degrees):
    dx = start_point[0] - center[0]
    dy = start_point[1] - center[1]

    if dx == 0:
        b_degr = 90
    else:
        tanb = dy / dx
        b_degr = math.degrees(math.atan(tanb))

    c_degr = 90 - b_degr + angle_degrees / 2

    hip = math.hypot(dx, dy)
    l = 2 * hip * math.sin(math.radians(angle_degrees / 2))

    dx = l * math.cos(math.radians(c_degr))
    dy = -l * math.sin(math.radians(c_degr))

    return [dx, dy]


def get_point_on_circle2(center, start_point, angle_degrees):

    center_m = [*center]
    start_point_m = [*start_point]

    ym = 1
    xm = 1

    if center_m[0] > start_point_m[0]:
        xm = -1
        ym = -1

    dx, dy = get_point_on_circle(center_m, start_point_m, angle_degrees)
    return dx * xm, dy * ym


def rot(an):
    rt_im = pygame.transform.rotate(orig_im, an)

    dx, dy = get_point_on_circle2(orig_center, orig_point, an)

    rt_center = [*orig_center]
    rt_center[0] -= round(dx)
    rt_center[1] -= round(dy)

    rt_rect = pygame.Rect(0, 0, rt_im.get_width(), rt_im.get_height())
    rt_rect.center = rt_center

    # rt_rect.move_ip(500, 500)

    w.fill([0, 0, 0])
    w.blit(orig_im, [0, 0])
    w.blit(rt_im, rt_rect)
    pygame.display.flip()


def make_circle(center, start_point):
    pygame.draw.circle(w, [0, 0, 255], center, 4)
    pygame.draw.circle(w, [0, 255, 0], start_point, 4)
    for i in range(0, 360):
        print(i)
        dx, dy = get_point_on_circle2(center, start_point, i)
        p = [*start_point]
        p[0] += round(dx)
        p[1] += round(dy)
        pygame.draw.circle(w, [255, 0, 0], p, 2)
        pygame.display.flip()


def on_right_clicked(key, unicode):
    # global angle
    # angle += 5
    # rot(angle)

    make_circle([500, 500], [600, 600])
    make_circle([500, 500], [400, 600])
    make_circle([500, 500], [600, 400])
    make_circle([500, 500], [400, 400])


def on_left_clicked(keys):
    global angle
    angle -= 5
    rot(angle)


def on_space_clicked(key, unicode, dasfg):
    event.stop_listening(sec_id2)


def on_close():
    print("goodbye")
    event.stop_listening(left_id)
    # exit()


def on_sec1():
    global angle
    angle -= 5
    rot(angle)


def on_sec2():
    sprite.move_sprite_by(-20, 0)


def restart_rotation(op):
    global orig_im, orig_rect, orig_center, orig_point, angle
    orig_im = pygame.image.load("sprite_types/type1/costumes/1.png")
    orig_im = pygame.transform.scale(orig_im, [300, 200])
    orig_rect = orig_im.get_rect()
    orig_center = orig_rect.center
    orig_point = op

    pygame.draw.circle(orig_im, [255, 0, 0], orig_point, 2)
    angle = 0


def on_mouse_pressed(pos):
    global orig_point
    restart_rotation(pos)
    rot(angle)


# left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
# left_id = event.on_key_pressed([pygame.K_LEFT, pygame.K_RIGHT], on_left_clicked, 100, [pygame.KMOD_LALT, pygame.KMOD_RSHIFT])
right_id = event.on_key_down(pygame.K_RIGHT, on_right_clicked)
left_id = event.on_key_down(pygame.K_LEFT, on_left_clicked)
# space_id = event.on_key_down(pygame.K_SPACE, on_space_clicked)
# close_id = event.on_close(on_close)
sec_id1 = event.on_timeout(50, 0, on_sec1)
# sec_id2 = event.on_timeout(1000, 5, on_sec2)
mouse_pressed_id = event.on_mouse_pressed([0], on_mouse_pressed, 1000)

app.start()

import pygame, math

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


# def rot(an):
#     rt_im = pygame.transform.rotate(orig_im, an)
#
#     dx, dy = get_point_on_circle2(orig_center, orig_point, an)
#
#     rt_center = [*orig_center]
#     rt_center[0] -= round(dx)
#     rt_center[1] -= round(dy)
#
#     rt_rect = pygame.Rect(0, 0, rt_im.get_width(), rt_im.get_height())
#     rt_rect.center = rt_center
#
#     # rt_rect.move_ip(500, 500)
#
#     w.fill([0, 0, 0])
#     w.blit(orig_im, [0, 0])
#     w.blit(rt_im, rt_rect)
#     pygame.display.flip()


# def make_circle(center, start_point):
#     pygame.draw.circle(w, [0, 0, 255], center, 4)
#     pygame.draw.circle(w, [0, 255, 0], start_point, 4)
#     for i in range(0, 360):
#         print(i)
#         dx, dy = get_point_on_circle2(center, start_point, i)
#         p = [*start_point]
#         p[0] += round(dx)
#         p[1] += round(dy)
#         pygame.draw.circle(w, [255, 0, 0], p, 2)
#         pygame.display.flip()
import math

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

    if angle_degrees<0:
        angle_degrees=angle_degrees%-360
        angle_degrees+=360

    center_m = [*center]
    start_point_m = [*start_point]

    ym = 1
    xm = 1

    if center_m[0] > start_point_m[0]:
        xm = -1
        ym = -1
    if center_m[1]>start_point_m[1]:
        xm = -1
        ym = -1

    dx, dy = get_point_on_circle(center_m, start_point_m, angle_degrees)
    return dx * xm, dy * ym


def get_point_by_angle(start_point, angle, distance):
    center = [*start_point]
    start_point[1] -= round(distance) #angle 0

    dx, dy = get_point_on_circle2(center, [*start_point], angle)
    end_point = [0, 0]
    end_point[0] = start_point[0] + dx
    end_point[1] = start_point[1] + dy

    return end_point

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


def make_circle(screen, center, start_point, step):
    import pygame, time, image_modifier
    pygame.draw.circle(screen, [0, 0, 255], center, 4)
    pygame.draw.circle(screen, [0, 255, 0], start_point, 4)
    for i in range(0, 360, step):
        print(i)
        # dx, dy = image_modifier.ImageRotator._get_point_on_circle2(center, start_point, i)
        dx, dy = get_point_on_circle2(center, start_point, i)
        p = [0, 0]
        p[0] = start_point[0] + dx
        p[1] = start_point[1] + dy

        pygame.draw.circle(screen, [255, 0, 0], [round(p[0]), round(p[1])], 2)
        pygame.display.flip()
        time.sleep(0.05)

        # start_point=[*p]

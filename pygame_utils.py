import pygame

PYGAME_KMODS = [pygame.KMOD_LSHIFT,
                pygame.KMOD_RSHIFT,
                pygame.KMOD_SHIFT,
                pygame.KMOD_LCTRL,
                pygame.KMOD_RCTRL,
                pygame.KMOD_CTRL,
                pygame.KMOD_LALT,
                pygame.KMOD_RALT,
                pygame.KMOD_ALT,
                pygame.KMOD_LMETA,
                pygame.KMOD_RMETA,
                pygame.KMOD_META,
                pygame.KMOD_CAPS,
                pygame.KMOD_NUM,
                pygame.KMOD_MODE]


def key_list_of_pressed_keys(keys_pressed):
    res = []
    key_index = 0
    for key_value in keys_pressed:
        if key_value:
            res.append(key_index)
        key_index += 1
    return res

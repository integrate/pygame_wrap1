import wrap_base, pygame

# general subscriber
def _register_event_handler(func, delay=None, count=None, pygame_event_type_filter_data=None, key_codes=None,
                            control_keys=None, mouse_buttons=None):
    # start event notification
    event_type_id = wrap_base.event_generator.start_event_notification(
        delay=delay,
        count=count,
        event_filter=pygame_event_type_filter_data,
        key_codes=key_codes,
        control_keys=control_keys,
        mouse_buttons=mouse_buttons
    )

    subs = wrap_base.message_broker.Subscriber(event_type_id, func)
    wrap_base.broker.subscribe(subs)


def on_key_down(key, func):
    _register_event_handler(
        func=func,
        pygame_event_type_filter_data={
            'type': pygame.KEYDOWN,
            'key': key
        })
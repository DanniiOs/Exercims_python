def handle_error_by_throwing_exception():
    raise Exception("Exception")


def handle_error_by_returning_none(input_data):
    try:
        value = int(input_data)
    except ValueError:
        return None
    else:
        return value


def handle_error_by_returning_tuple(input_data):
    try:
        value = int(input_data)
    except ValueError as e:
        return (False, e)
    else:
        return (True, value)


def filelike_objects_are_closed_on_exception(filelike_object):
    try:
        filelike_object.do_something()
    except Exception as e:
        filelike_object.close()
        raise e
    else:
        filelike_object.close()

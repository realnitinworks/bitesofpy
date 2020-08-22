def flatten(list_of_lists):
    result = []

    def wrapper(items):
        for item in items:
            if isinstance(item, list) or isinstance(item, tuple):
                wrapper(item)
            else:
                result.append(item)

    wrapper(list_of_lists)
    return result

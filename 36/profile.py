def get_profile(name, age, *args, **kwargs):
    if not isinstance(age, int):
        raise ValueError("age must be an int")

    if len(args) > 5:
        raise ValueError("Too many sports")

    profile = {
        "name": name,
        "age": age,
    }

    if args:
        profile["sports"] = sorted(args)

    if kwargs:
        profile["awards"] = kwargs

    return profile

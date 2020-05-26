def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""

    if not all(value >= 0 and value <= 255 for value in rgb):
        raise ValueError("rgb value must a value between 0 and 255")

    return "#" + "".join("{:02x}".format(value).upper() for value in rgb)

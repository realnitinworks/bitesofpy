def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    users_dict = {}

    for line in passwd.strip().splitlines():
        user = line.split(":")[0]
        name = line.split(":")[4]

        if not name:
            name = "unknown"

        name = name.strip(",")
        if "," in name:
            name = name.split(",")
            name = " ".join([name[0], name[-1]])

        users_dict[user] = name

    return users_dict

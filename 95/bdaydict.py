MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        for date in self.values():
            if (date.month, date.day) == (birthday.month, birthday.day):
                print(MSG.format(name))
                break
        self.update({name: birthday})

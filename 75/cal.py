import re

NUM_DAYS_IN_WEEK = 7

def get_weekdays(calendar_output):
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""

    # regex
    # \s\s\d - days like <space><space>1,<space><space>2 etc
    # \d+ - days like 10, 11, 12 etc
    # \s\s - start of month does not always start on a Sunday
    day_regex = re.compile(r"\s\s\d|\d+|\s\s")

    # Pack the spaces|days into 7 weekdays
    return {
       int(day): weekday
       for line in calendar_output.splitlines()[2:]  # consider only the day numbers
       for day, weekday in zip(day_regex.findall(line)[-NUM_DAYS_IN_WEEK:], "Su Mo Tu We Th Fr Sa".split())
       if day != "  "  # ignore the spaces after they map to weekdays
    }

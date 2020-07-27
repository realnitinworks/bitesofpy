from datetime import timedelta
from typing import List
from collections import namedtuple
from dateutil.parser import parse


Section = namedtuple('Section', 'id duration text')

def get_srt_section_ids(text: str) -> List[int]:
    """Parse a caption (srt) text passed in and return a
       list of section numbers ordered descending by
       highest speech speed
       (= ratio of "time past:characters spoken")

       e.g. this section:

       1
       00:00:00,000 --> 00:00:01,000
       let's code

       (10 chars in 1 second)

       has a higher ratio then:

       2
       00:00:00,000 --> 00:00:03,000
       code

       (4 chars in 3 seconds)

       You can ignore milliseconds for this exercise.
    """
    text = text.strip().split("\n\n")
    sections = []

    for line in text:
        id, duration, text = line.split("\n")
        start_time, end_time = duration.split("-->")
        duration = (parse(end_time) - parse(start_time)).total_seconds()
        sections.append(Section(id=id, duration=duration, text=text))

    return [
        int(section.id)
        for section in sorted(
            sections,
            key=lambda s: len(s.text)/s.duration,
            reverse=True
        )
    ]

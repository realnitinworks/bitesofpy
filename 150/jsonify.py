import csv
import json
from collections import namedtuple

members = """
id,first_name,last_name,email
1,Junie,Kybert;jkybert0@army.mil
2,Sid,Churching|schurching1@tumblr.com
3,Cherry;Dudbridge,cdudbridge2@nifty.com
4,Merrilee,Kleiser;mkleiser3@reference.com
5,Umeko,Cray;ucray4@foxnews.com
6,Jenifer,Dale|jdale@hubpages.com
7,Deeanne;Gabbett,dgabbett6@ucoz.com
8,Hymie,Valentin;hvalentin7@blogs.com
9,Alphonso,Berwick|aberwick8@symantec.com
10,Wyn;Serginson,wserginson9@naver.com
"""


Member = namedtuple('Member', 'id first_name last_name email')
DELIMITERS = ";|"


def convert_to_json(members=members):
    for delimiter in DELIMITERS:
        members = members.replace(delimiter, ",")

    reader = csv.DictReader(members.strip().splitlines())
    return json.dumps([
        Member(
            id=row['id'],
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email']
        )._asdict()
        for row in reader
    ])



from csv import DictReader
from os import path
from urllib.request import urlretrieve
from collections import Counter

DATA = path.join('/tmp', 'bite_output_log.txt')
if not path.isfile(DATA):
    urlretrieve('https://bit.ly/2HoFZBd', DATA)


class BiteStats:

    def _load_data(self, data) -> list:
        with open(DATA) as f:
            reader = DictReader(f)
            return list(reader)

    def __init__(self, data=DATA):
        self.rows = self._load_data(data)

    @property
    def number_bites_accessed(self) -> int:
        """Get the number of unique Bites accessed"""
        accessed_bites = {
            row['bite']
            for row in self.rows
        }

        return len(accessed_bites)

    @property
    def number_bites_resolved(self) -> int:
        """Get the number of unique Bites resolved (completed=True)"""
        resolved_bites = {
            row['bite']
            for row in self.rows
            if row['completed'] == 'True'
        }

        return len(resolved_bites)

    @property
    def number_users_active(self) -> int:
        """Get the number of unique users in the data set"""
        unique_users = {
            row['user']
            for row in self.rows
        }

        return len(unique_users)

    @property
    def number_users_solving_bites(self) -> int:
        """Get the number of unique users that resolved
           one or more Bites"""
        users_solving_bites = {
            row['user']
            for row in self.rows
            if row['completed'] == 'True'
        }

        return len(users_solving_bites)

    @property
    def top_bite_by_number_of_clicks(self) -> str:
        """Get the Bite that got accessed the most
           (= in most rows)"""
        top_bites_by_clicks = Counter(
            row['bite']
            for row in self.rows
        )

        top_bite, _ = top_bites_by_clicks.most_common(1)[0]

        return top_bite

    @property
    def top_user_by_bites_completed(self) -> str:
        """Get the user that completed the most Bites"""
        top_users = Counter(
            row['user']
            for row in self.rows
            if row['completed'] == "True"
        )

        top_user, _ = top_users.most_common(1)[0]

        return top_user

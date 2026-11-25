from datetime import datetime
import time
from models.match import Match
from models.player import Player


class Round:
    """A round of a tournament: a name, a list of matches, a start time and an end time."""

    TIME_FORMAT = "%d/%m/%Y %H:%M:%S"

    def __init__(self, name):
        self.name = name
        self.matches = []
        self.start_time = datetime.now().strftime(self.TIME_FORMAT)
        self.end_time = None

    def finish(self):
        """Set the end time of a round."""
        self.end_time = datetime.now().strftime(self.TIME_FORMAT)

    def add_match(self, match):
        """Added match to the round."""
        self.matches.append(match)

    def to_dict(self):
        """Convert round to a dictionary."""
        resultat = []
        for match in self.matches:
            resultat.append(match.to_dict())
        return {
            "name": self.name,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": resultat
        }


if __name__ == "__main__":
    p1 = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    p2 = Player("Petit", "Maurice", "24/08/1994", "AB56789")
    m = Match(p1, p2)
    r = Round("Round 1")
    r.add_match(m)
    for match in r.matches:
        print(match)
    print("start_time:", r.start_time)
    time.sleep(2)
    r.finish()
    print("end_time:", r.end_time)
    print(r.to_dict())

import uuid
from datetime import datetime
import time
from models.match import Match
from models.player import Player


class Round:
    """A round of a tournament: a name, a list of matches, a start time and an end time."""

    TIME_FORMAT = "%d/%m/%Y %H:%M:%S"

    def __init__(self, name, round_id=None, start_time=None, end_time=None):
        self.name = name
        self.id = round_id or str(uuid.uuid4())
        self.matches = []
        self.start_time = start_time or datetime.now().strftime(self.TIME_FORMAT)
        self.end_time = end_time

    def finish(self):
        """Set the end time of a round."""
        self.end_time = datetime.now().strftime(self.TIME_FORMAT)

    def add_match(self, match):
        """Add a match to the round."""
        self.matches.append(match)

    def to_dict(self):
        """Convert round to a dictionary."""
        resultat = []
        for match in self.matches:
            resultat.append(match.to_dict())
        return {
            "name": self.name,
            "id": self.id,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "matches": resultat
        }

    @classmethod
    def from_dict(cls, data):
        """Create a round from a dictionary."""
        round_party = cls(
            data["name"], data["id"],
            data["start_time"], data["end_time"],
        )
        for match_data in data["matches"]:
            match = Match.from_dict(match_data)
            round_party.add_match(match)
        return round_party


if __name__ == "__main__":
    p1 = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    p2 = Player("Petit", "Maurice", "24/08/1994", "AB56789")
    p1.save()
    p2.save()
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
    copie = Round.from_dict(r.to_dict())
    print(copie.id == r.id, copie.end_time == r.end_time)
    for match in copie.matches:
        print(match)

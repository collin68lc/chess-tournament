import uuid
from datetime import datetime
import time
import json
from pathlib import Path
from models.match import Match
from models.player import Player


class Round:
    """A round of a tournament: a name, a list of matches, a start time and an end time."""

    TIME_FORMAT = "%d/%m/%Y %H:%M:%S"
    DATA_FILE = Path("data/rounds.json")

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

    @classmethod
    def load_all(cls):
        """Return the list stored in the file, or an empty list."""
        if not cls.DATA_FILE.exists():
            return []
        with open(cls.DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):
        """Save the round to the JSON file."""
        liste = self.load_all()
        for index, item in enumerate(liste):
            if item["id"] == self.id:
                liste[index] = self.to_dict()
                break
        else:
            liste.append(self.to_dict())
        self.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(self.DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(liste, f, indent=4, ensure_ascii=False)

    @classmethod
    def get_by_id(cls, round_id):
        """Return the round with this id, or None."""
        for item in cls.load_all():
            if item["id"] == round_id:
                return cls.from_dict(item)
        return None


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
    r.save()
    r.save()
    print("end_time:", r.end_time)
    print(r.to_dict())
    copie = Round.from_dict(r.to_dict())
    print(copie.id == r.id, copie.end_time == r.end_time)
    for match in copie.matches:
        print(match)
    retrouve = Round.get_by_id(r.id)
    print(retrouve.end_time == r.end_time)
    for match in retrouve.matches:
        print(match)

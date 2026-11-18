import re
import uuid
import json
from pathlib import Path


class Player:
    """Refers to a chess player who is a registered member of the club."""

    DATA_FILE = Path("data/players.json")

    def __init__(self, last_name, first_name, birth_date, national_id, player_id=None):
        if not self.is_valid_national_id(national_id):
            raise ValueError("L'identifiant national ne correspond pas.")
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.national_id = national_id
        self.id = player_id or str(uuid.uuid4())

    @staticmethod
    def is_valid_national_id(national_id):
        """Check the format: two letters followed by five digits (e.g. AB12345)."""
        return re.fullmatch(r"[A-Z]{2}\d{5}", national_id) is not None

    def __str__(self):
        """Return player."""
        return f"{self.last_name} {self.first_name} ({self.national_id})"

    def to_dict(self):
        """Convert player in dictionary."""
        return {
            "Nom": self.last_name, "Prénom": self.first_name,
            "Date de naissance": self.birth_date, "Identifiant national": self.national_id,
            "player id": self.id
        }

    @classmethod
    def from_dict(cls, data):
        """Create a player from a dictionary."""
        return cls(
            data["Nom"], data["Prénom"], data["Date de naissance"],
            data["Identifiant national"], data["player id"]
        )

    @classmethod
    def load_all(cls):
        """Return the list stored in the file, or an empty list."""
        if not cls.DATA_FILE.exists():
            return []
        with open(cls.DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self):
        """Save the player to the JSON file."""
        liste = self.load_all()
        for index, item in enumerate(liste):
            if item["player id"] == self.id:
                liste[index] = self.to_dict()
                break
        else:
            liste.append(self.to_dict())
        self.DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

        with open(self.DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(liste, f, indent=4, ensure_ascii=False)

    @classmethod
    def get_by_id(cls, player_id):
        """Return the player with this id, or None."""
        liste = cls.load_all()
        for item in liste:
            if item["player id"] == player_id:
                return cls.from_dict(item)
        return None

    @classmethod
    def get_by_national_id(cls, national_id):
        """Return the player with this national ID, or None."""
        liste = cls.load_all()
        for item in liste:
            if item["Identifiant national"] == national_id:
                return cls.from_dict(item)
        return None


if __name__ == "__main__":
    p = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    p.save()
    print(Player.get_by_national_id("AB12345"))
    print(Player.get_by_national_id("ZZ99999"))

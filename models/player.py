import re
import uuid
import json
from pathlib import Path


class Player:
    """Refers to a chess player who is a registered member of the club."""

    FICHIER = Path("data/players.json")

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
        if not cls.FICHIER.exists():
            return []
        with open(cls.FICHIER, "r", encoding="utf-8") as f:
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
        self.FICHIER.parent.mkdir(parents=True, exist_ok=True)

        with open(self.FICHIER, "w", encoding="utf-8") as f:
            json.dump(liste, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    # p1 = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    # p2 = Player("Maurice", "Petit", "23/10/1996", "GF23456")
    # p3 = Player("Peter", "Lang", "16/08/2003", "DG23457")
    # print(p1, p2)

    # try:
    #     Player("Rust", "Ange", "12/08/1989", "J24")
    # except ValueError as error:
    #     print(error)
    # try:
    #     Player("Olaf", "Rufus", "30/12/2000", "ar67891")
    # except ValueError as error:
    #     print(error)

    # data = p1.to_dict()
    # print(data)
    # copie = Player.from_dict(data)
    # print(copie)
    # print(copie is p1, copie.national_id == p1.national_id)
    p = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    p.save()
    p.save()
    print(len(Player.load_all()))

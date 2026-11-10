# models/player.py
import re


class Player:
    """Refers to a chess player who is a registered member of the club."""

    def __init__(self, last_name, first_name, birth_date, national_id):
        if not self.is_valid_national_id(national_id):
            raise ValueError("L'identifiant national ne correspond pas.")
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date      # format "JJ/MM/AAAA" pour l'instant
        self.national_id = national_id

    @staticmethod
    def is_valid_national_id(national_id):
        """Check the format: two letters followed by five digits (e.g. AB12345)."""
        return re.fullmatch(r"[A-Z]{2}\d{5}", national_id) is not None

    def __str__(self):
        """Return player."""
        return f"{self.last_name} {self.first_name} ({self.national_id})"


if __name__ == "__main__":
    p = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    print(p)

    try:
        Player("Rust", "Ange", "12/08/1989", "J24")
    except ValueError as error:
        print(error)
    try:    
        Player("Olaf", "Rufus", "30/12/2000", "ar67891")
    except ValueError as error:
        print(error)

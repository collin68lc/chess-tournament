# models/player.py
import re


class Player:
    """Représente un joueur d'échecs inscrit au club."""

    def __init__(self, last_name, first_name, birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date      # format "JJ/MM/AAAA" pour l'instant
        self.national_id = national_id

    @staticmethod
    def is_valid_national_id(national_id):
        """Vérifie le format : deux lettres puis cinq chiffres (ex : AB12345)."""
        return re.fullmatch(r"[A-Z]{2}\d{5}", national_id) is not None

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.national_id})"


if __name__ == "__main__":
    p = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    print(p)
    print(Player.is_valid_national_id("AB12345"))   # True
    print(Player.is_valid_national_id("A123"))      # False
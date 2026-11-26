from models.player import Player


class Match:
    """result of the match between two players"""

    WIN = 1
    LOSS = 0
    DRAW = 0.5

    def __init__(self, player1, player2):
        self.match_result = ([player1, 0], [player2, 0])

    def set_winner(self, winner):
        """score depending on the winner"""
        if winner == self.match_result[0][0]:
            self.match_result[0][1] = self.WIN
            self.match_result[1][1] = self.LOSS
        elif winner == self.match_result[1][0]:
            self.match_result[0][1] = self.LOSS
            self.match_result[1][1] = self.WIN
        elif winner is None:
            self.match_result[0][1] = self.DRAW
            self.match_result[1][1] = self.DRAW
        else:
            raise ValueError("entrée le nom d'un des deux joueurs ou None")

    def __str__(self):
        """display score players"""
        return (
            f"{self.match_result[0][0]} : {self.match_result[0][1]}, "
            f"{self.match_result[1][0]} : {self.match_result[1][1]}"
        )

    def to_dict(self):
        """Convert match result in dictionary."""
        return {
            "player1":
            {"national_id": self.match_result[0][0].national_id, "score": self.match_result[0][1]},
            "player2":
            {"national_id": self.match_result[1][0].national_id, "score": self.match_result[1][1]}
        }

    @classmethod
    def from_dict(cls, data):
        """Create a match from a dictionary."""
        player1 = Player.get_by_national_id(data["player1"]["national_id"])
        player2 = Player.get_by_national_id(data["player2"]["national_id"])
        new_match = cls(player1, player2)
        new_match.match_result[0][1] = data["player1"]["score"]
        new_match.match_result[1][1] = data["player2"]["score"]
        return new_match


if __name__ == "__main__":
    p1 = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    p2 = Player("Petit", "Maurice", "24/08/1994", "AB56789")
    p1.save()
    p2.save()
    m = Match(p1, p2)
    m.set_winner(p1)
    copie = Match.from_dict(m.to_dict())
    print(copie)

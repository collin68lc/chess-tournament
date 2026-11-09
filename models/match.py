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


if __name__ == "__main__":
    alice = "Alice"
    bob = "Bob"
    for winner in ("Alice", "Bob", None):
        m = Match("Alice", "Bob")
        m.set_winner(winner)
        print(m)

    try:
        m.set_winner("Charles")
    except ValueError as error:
        print(error)

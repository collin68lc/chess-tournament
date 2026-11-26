import uuid
from models.player import Player
from models.round import Round


class Tournament:
    """A chess tournament with a location, dates, rounds and registered players."""

    def __init__(
            self, name, location, start_date, end_date,
              number_of_rounds=4, description="", tournament_id=None
            ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_of_rounds = number_of_rounds
        self.description = description
        self.id = tournament_id or str(uuid.uuid4())
        self.current_round_number = 0
        self.rounds = []
        self.players = []

    def add_player(self, player):
        """Add a player to the tournament."""
        self.players.append(player)

    def add_round(self, round_):
        """Add a round to the tournament."""
        self.rounds.append(round_)


if __name__ == "__main__":
    p1 = Player("Carlsen", "Magnus", "30/11/1990", "AB12345")
    p2 = Player("Petit", "Maurice", "24/08/1994", "AB56789")
    t = Tournament("test", "Lyon", "26/11/2026", "27/11/2026", 1, "essai")
    t.add_player(p1)
    t.add_player(p2)
    t.add_round(Round("round1"))
    print(len(t.players))
    print(len(t.rounds))

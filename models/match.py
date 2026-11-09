class Match:
    """score players"""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score_player1 = 0
        self.score_player2 = 0

    def set_winner(self, winner):
        """score depending on the winner"""
        if winner == self.player1:
            self.score_player1 = 1
            self.score_player2 = 0
        elif winner == self.player2:
            self.score_player1 = 0
            self.score_player2 = 1
        elif winner is None:
            self.score_player1 = 0.5
            self.score_player2 = 0.5
        else:
            raise ValueError("sélectionnez l'option pas de vainqueur")

    def __str__(self):
        return f"{self.player1} : {self.score_player1} , {self.player2} : {self.score_player2}" 


if __name__ == "__main__":
    alice = "Alice"
    bob = "Bob"
    m = Match(alice, bob)
    m.set_winner("Alice")
    #m.set_winner("Bob")
    print(m.player1, m.score_player1, m.player2, m.score_player2)   # avant le résultat
    #try:
    #    m.set_winner("Charlie")
    #except ValueError:
     #   print("nom refusé")
    
    # print(m.player1, m.score_player1, m.player2, m.score_player2)   # après le résultat
    
from views.player import PlayerView
from models.player import Player


class PlayerController:
    """Functionality of player menu."""

    def __init__(self):
        self.view = PlayerView()

    def create_player(self):
        """Ask the data, create player and save it."""
        data = self.view.ask_new_player()
        try:
            player = Player(
                data["last_name"], data["first_name"],
                data["birth_date"], data["national_id"]
            )
        except ValueError as error:
            self.view.show_message(str(error))
            return
        player.save()
        self.view.show_message("Joueur créé.")


if __name__ == "__main__":
    controller = PlayerController()
    controller.create_player()

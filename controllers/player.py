from views.player import PlayerView
from models.player import Player


class PlayerController:
    """Functionality of player menu."""

    def __init__(self):
        self.view = PlayerView()

    def create_player(self):
        """Ask the data, create player and save it."""
        data = self.view.ask_new_player()
        if Player.get_by_national_id(data["national_id"]) is not None:
            self.view.show_message("Ce joueur existe déjà.")
            return
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

    def run(self):
        """Display the player menu until the user goes back."""
        while True:
            choice = self.view.show_menu_player()
            if choice == "1":
                self.create_player()
            elif choice == "4":
                return
            else:
                self.view.show_message("Choix invalide.")

if __name__ == "__main__":
    controller = PlayerController()
    #controller.create_player()
    controller.run()

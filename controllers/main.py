from views.menu import MenuView
from controllers.player import PlayerController


class MainController:
    """Start the program and dispatch to the other controllers."""

    def __init__(self):
        self.menu = MenuView()
        self.player_controller = PlayerController()

    def run(self):
        """Display the main menu until the user quits."""
        while True:
            choice = self.menu.show_main_menu()
            if choice == "2":
                self.player_controller.run()
            elif choice == "4":
                return
            elif choice in ("1", "3"):
                print("bientôt disponible")
            else:
                print("Choix invalide.")

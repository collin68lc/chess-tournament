class MenuView:
    """Display the menu and read the user's choice."""

    def show_main_menu(self):
        """Display the options and return what the user typed."""
        print("1 - Gérer les tournois")
        print("2 - Gérer les joueurs")
        print("3 - Afficher les rapports")
        print("4 - Quitter")
        return input("Votre choix : ")


if __name__ == "__main__":
    view = MenuView()
    choice = view.show_main_menu()
    print(f"Vous avez choisi : {choice}")

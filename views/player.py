class PlayerView:
    """Display the player menus and messages and read the user's input."""

    def show_menu_player(self):
        """Display the different choices in menu player."""
        print("1 - Créer un nouveau joueur")
        print("2 - Trouver un joueur(bientôt disponible)")
        print("3 - Supprimer un joueur(bientôt disponible)")
        print("4 - Retour")
        return input("Votre choix : ")

    def show_message(self, message):
        """Display a message to the user."""
        print(message)

    def ask_new_player(self):
        """Ask the player's data and return them in a dictionary."""
        first_name = input("Prénom : ")
        last_name = input("Nom : ")
        birth_date = input("Date de naissance (jj/mm/aaaa) : ")
        national_id = input("Identifiant national : ")
        return {
            "first_name": first_name, "last_name": last_name,
            "birth_date": birth_date, "national_id": national_id
        }


if __name__ == "__main__":
    view = PlayerView()
    player = view.show_message("Identifiant invalide : format attendu AB12345.")
    print(player)

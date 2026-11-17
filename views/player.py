class PlayerView:
    """Ask the user for the data of a player."""

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
    player = view.ask_new_player()
    print(player)

"""Base view."""


class View:
    """Chess tournament view"""

    def get_player(self):
        """Ask a player informations from the user.
        Return a dict of the infos."""
        player_info = {
            "surname": input("Merci de taper le nom de famille du joueur : "),
            "name": input("Merci de saisir le prénom du joueur : "),
            "birthdate": input("Date de naissance du joueur : "),
            "gender": input("Merci de saisir le sexe du joueur : "),
            "ranking": int(input("Merci de saisir le classement du joueur : "))
        }
        return player_info

    def get_tournament(self):
        """Ask the user for tournament informations.
        Return a dict of the infos."""
        tournament_info = {
            "name": input("Merci de saisir le nom du tournois : "),
            "place": input(
                "Merci de saisir la localisation du tournois : "),
            "date":  input("merci de saisir une date pour le tournois : "),
            "description": input(
                "merci de saisir une description pour le tournois : ")
        }
        return tournament_info

    def get_tournament_time_management(self):
        """ask for the tournament time management type.
        Return the string corresponding to the choice."""
        tournament_time = input(
            " Merci de choisir un contrôle du temps parmis : 'Bullet'"
            ", 'Blitz', 'Coup rapide'")
        if (tournament_time == "Bullet"
                or tournament_time == "Blitz"
                or tournament_time == "Coup rapide"):
            return tournament_time
        print("Choix incorrect.")
        self.get_tournament_time_management()
        return tournament_time

    def get_number_of_rounds(self):
        """Ask for the number of round. Return that number"""
        rounds_choice = input(
            "Le nombre de round par défaut est 4."
            " Souhaitez vous le changer ? Y/N ")
        if rounds_choice == "Y" or rounds_choice == "y":
            round_number = int(input(
                "Saississez le nombre de tours pour le tournois"))
        elif rounds_choice == "N" or rounds_choice == "N":
            print("Le tournois se déroulera sur 4 rounds.")
            round_number = 4
        else:
            print("La réponse saisie est incorrecte.")
            self.get_number_of_rounds()
        return round_number

    def choose_tournament(self, tournaments):
        """Print the list of tournament in memory
        then ask the user for a choice.
        Return the choosen tournament."""
        count = 1
        print("Liste des tournois:")
        for tournament in tournaments:
            tournament_name = tournament.get_name()
            print(f"Tournois {count} : {tournament_name}")
        choice = int(input("Merci de saisir le numéro du tournois choisi."))
        tournament = tournaments[choice-1]
        return tournament

    def ask_player_number(self):
        player_number = int(
            input("combien de joueur souhaitez vous ajouter ?"))
        return player_number

    def choose_option(self):
        option = int(input("Entrez votre choix: "))
        return option

    def set_player_ranking(self, players):
        choice = int(
            input("Numéro du joueur choisi:"))
        player = players[choice-1]
        ranking = int(input("Indiquer le rang du joueur: "))
        player.set_ranking(ranking)

    def post_tournament_ranking(self, players):
        """prompt the user to set a new ranking
        for each player of the input list"""
        for player in players:
            player_name = player.get_name()
            player_surname = player.get_surname()
            old_rank = player.get_ranking()
            print(f"{player_name} {player_surname}"
                  f" ancien classement : {old_rank}")
            ranking = int(input("Indiquer le nouveau rang du joueur: "))
            player.set_ranking(ranking)

    def display_menu(self):
        """Print the app menu"""
        menu = {
            1: "Ajouter des joueurs à la base de données",
            2: "Creer un tournois",
            3: "Lancer un tournois",
            4: "Afficher le classement des joueurs",
            5: "Afficher la liste des joueurs",
            6: "Afficher la liste des tournois",
            7: "Modifier le classement d'un joueur",
            8: "Sauvegarder les joueurs dans la database",
            9: "Charger les joueurs enregistrés dans la database",
            10: "Sauvegarder les tournois dans la database",
            11: "Charger les tournois de la database",
            12: "Afficher la liste des joueurs d'un tournois",
            13: "Afficher le classement des joueurs d'un tournois",
            14: "Afficher les tours d'un tournois",
            15: "Afficher tous les matchs d'un tournois",
            16: "Quitter l'application"
        }
        for key in menu.keys():
            print(key, "--", menu[key])

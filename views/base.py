"""Base view."""


class View:
    """Chess tournament view"""

    # View function regarding model Player
    def get_player(self):
        """Ask a player informations from the user"""
        player_info = {
            "surname": input("Merci de taper le nom de famille du joueur : "),
            "name": input("Merci de saisir le prénom du joueur : "),
            "birthdate": input("Merci de renseigner la date de naissance du joueur : "),
            "gender": input("Merci de saisir le sexe du joueur : "),
            "ranking": input("Merci de saisir le classement du joueur : ")
        }
        return player_info

    # View function regarding model Tournament
    def get_tournament(self):
        tournament_info = {
            "name" : input("Merci de saisir le nom du tournois : "),
            "place" : input(
            "Merci de saisir la localisation du tournois : "),
            "date" :  input("merci de saisir une date pour le tournois : "),
            "description" : input(
            "merci de saisir une description pour le tournois : "),
            "time" : self.get_tournament_time_management,
            "rounds" : self.get_number_of_rounds
        }
        return tournament_info

    def get_tournament_time_management(self):
        """ask for the tournament time management type"""
        tournament_time = input(
            " Merci de choisir un contrôle du temps parmis : 'Bullet', 'Blitz', 'Coup rapide'")
        if tournament_time == "Bullet" or tournament_time == "Blitz" or tournament_time == "Coup rapide":
            return tournament_time
        print("Choix incorrect.")
        View.get_tournament_time_management()

    # View function regarding model Round
    def get_number_of_rounds(self):
        """Ask for the number of round"""
        rounds_choice = input(
            "Le nombre de round par défaut est 4. Souhaitez vous le changer ? Y/N ")
        if rounds_choice == "Y" or rounds_choice == "y":
            round_number = input(
                "Saississez le nombre de tours pour le tournois")

        elif rounds_choice == "N" or rounds_choice == "N":
            print("Le tournois se déroulera sur 4 rounds.")
            round_number = 4
        else:
            print("La réponse saisie est incorrecte.")
            View.get_number_of_rounds()
        return round_number

    def get_round_starttime(self):
        """ask for the tournament start time"""
        start_time = input("Saisissez l'heure de démarrage du round : ")
        return start_time

    def get_round_startdate(self):
        """ask for the tournament start date"""
        start_date = input("Saisissez la date de démarrage du round : ")
        return start_date

    def get_round_endtime(self):
        """ask for the tournament end time"""
        end_time = input("Saisissez l'heure de fin du round : ")
        return end_time

    def get_round_enddate(self):
        """ask for the tournament start date"""
        end_date = input("Saisissez la date de fin du round : ")
        return end_date

    # View function regarding model Match
    def get_player_result(self, player_name):
        """ask for the player's match result"""
        result = input(f"Merci de saisir le resultat de {player_name} : ")
        return result

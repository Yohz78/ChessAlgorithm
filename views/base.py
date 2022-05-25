"""Base view."""

class View:
    """Chess tournament view"""

    def get_player(self):
        """Ask a player informations from the user"""
        player_info = {
            "surname" : input("Merci de taper le nom de famille du joueur : "),
            "name" : input("Merci de saisir le prénom du joueur : "),
            "birthdate" : input("Merci de renseigner la date de naissance du joueur : "),
            "gender" : input("Merci de saisir le sexe du joueur : "),
            "ranking" : input("Merci de saisir le classement du joueur : ")
        }
        return player_info

    def get_tournament_name(self):
        tournament_name = input("Merci de saisir le nom du tournois : ")
        return tournament_name

    def get_tournament_place(self):
        tournament_place = input("Merci de saisir la localisation du tournois : ")    
        return tournament_place    

    def get_tournament_description(self):
        tournament_description = input("merci de saisir une description pour le tournois : ")
        return tournament_description

    def get_tournament_date(self):
        tournament_date = input("merci de saisir une date pour le tournois : ")   
        return tournament_date 

    def get_number_of_rounds(self):
        rounds_choice = input("Le nombre de round par défaut est 4. Souhaitez vous le changer ? Y/N ")
        if rounds_choice == "Y" or rounds_choice == "y":
            tournament_rounds = input("Saississez le nombre de tours pour le tournois")
        elif rounds_choice == "N" or rounds_choice == "N":
            print("Le tournois se déroulera sur 4 rounds.")
        else:
            print("La réponse saisie est incorrecte.")
            View.get_number_of_rounds()        
        return tournament_rounds 

    def get_tournament_time_management(self):
        tournament_time = input(" Merci de choisir un contrôle du temps parmis : 'Bullet', 'Blitz', 'Coup rapide'")
        if tournament_time == "Bullet" or tournament_time == "Blitz" or tournament_time == "Coup rapide":
            return tournament_time
        print("Choix incorrect.")
        View.get_tournament_time_management()    

    def get_round_starttime(self):
        start_time = input("Saisissez l'heure de démarrage du round : ")
        return start_time

    def get_round_startdate(self):
        start_date = input("Saisissez la date de démarrage du round : ")
        return start_date

    def get_round_endtime(self):
        end_time = input("Saisissez l'heure de fin du round : ")
        return end_time

    def get_round_enddate(self):
        end_date = input("Saisissez la date de fin du round : ")
        return end_date    
      
    def get_player_result(self, player_name):
        result = input(f"Merci de saisir le resultat de {player_name} : ")
        return result


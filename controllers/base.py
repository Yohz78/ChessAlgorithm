from operator import attrgetter
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from typing import List
from datetime import datetime


class Controller:
    """main controller"""

    def __init__(self, view):
        """Has a list of players, a list of rounds and the tournament info."""
        # Models
        self.players: List[Player] = []
        self.tournaments: List[Tournament] = []

        # Views
        self.view = view

    def save_players(self):
        """get the tournament players"""
        player_number = int(
            input("combien de joueur souhaitez vous ajouter ?"))
        players = []
        while len(players) < player_number:
            player_info = self.view.get_player()
            player = Player(player_info["surname"], player_info["name"],
                            player_info["birthdate"], player_info["gender"], player_info['ranking'])
            self.players.append(player)
            players.append(player)

    def get_players_ranking(self):
        "print the players sorted by rank"
        print("Voici le classement des joueurs")
        self.players.sort(key=attrgetter("ranking"))
        count = 1
        for player in self.players:
            player_name = player.get_name()
            player_surname = player.get_surname()
            player_ranking = player.get_ranking()
            print(f"{count} -- Rank {player_ranking} : {player_name} {player_surname}") 
            count += 1 

    def get_players(self):
        "print the players in ascending order based on surname"
        print("Vous avez choisi d'afficher la liste des joueurs")
        self.players.sort(key=attrgetter("surname"))
        for player in self.players:
            player_name = player.get_name()
            player_surname = player.get_surname()
            print(f"{player_name} {player_surname}") 

    def get_tournaments(self):
        "print the tournaments in self.tournaments"
        print("Voici la liste des tournois en mémoire.")
        count = 1
        for tournament in self.tournaments:
            tournament_name = tournament.get_name()
            print(f"Tournois {count} : {tournament_name}")
            count += 1        

    def create_tournament(self):
        """Return an object tournament"""
        tournament_info = self.view.get_tournament()
        tournament_info['time'] = self.view.get_tournament_time_management()
        tournament_info['rounds'] = self.view.get_number_of_rounds()
        tournament = Tournament(
            tournament_info["name"], tournament_info["place"], tournament_info['date'],
            tournament_info["time"], tournament_info["description"], self.players, tournament_info['rounds'])
        return tournament

    def run(self):
        """Run the application"""
        while(True):
            self.view.display_menu()
            option = int(input("Entrez votre choix: "))
            if option == 1:
                print("Vous avez choisi d'ajouter des joueurs.")
                players_list = self.save_players()
            elif option == 2:
                print("Vous avez choisi de créer un tournois")
                if len(self.players) < 8:
                    print("Pas assez de joueur pour créer un tournois. Retour au menu")
                else:
                    tournament = self.create_tournament()
                    self.tournaments.append(tournament)
                    print("Tournois créé. Retour au menu principal.")
            elif option == 3:
                print("Vous avez choisis de lancer un tournois.")
                count = 1
                players_list = self.players
                print("Liste des tournois:")
                for tournament in self.tournaments:
                    tournament_name = tournament.get_name()
                    print(f"Tournois {count} : {tournament_name}")
                choice = int(input("Merci de saisir le numéro du tournois à lancer."))
                launched_tournament = self.tournaments[choice-1]
                launched_tournament.choose_players(players_list)
                launched_tournament.run_tournament
            elif option == 4:
                self.get_players_ranking()
            elif option == 5:
                self.get_players()
            elif option == 6:
                self.get_tournaments() 
            elif option == 7:
                print("Vous avez choisi de modifier le classement d'un joueur.")
                self.get_players_ranking()
                players = self.players
                choice = int(input("Choississez un joueur à modifier en tapant son numéro:"))
                player = players[choice-1]
                ranking = input("Indiquer le rang du joueur: ")
                player.set_ranking(ranking)
            elif option == 8:
                print("Vous avez choisi de quitter l'application. Bye bye !")
                quit()
            else:
                print("Choix invalide. Merci de saisir un nombre entre 1 et 8.")





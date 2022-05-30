from operator import attrgetter
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from typing import List
from tinydb import TinyDB


class Controller:
    """main controller"""

    def __init__(self, view):
        """Has a list of players, a list of rounds and the tournament info."""
        # Models
        self.players: List[Player] = []
        self.tournaments: List[Tournament] = []

        # Views
        self.view = view

        self.db = TinyDB('db.json')

    def save_players(self):
        """save the players in the database"""
        self.players.sort(key=attrgetter("surname"))
        serialized_players = [player.serialized() for player in self.players]
        print(serialized_players)
        players_table = self.db.table("players")
        players_table.truncate()
        players_table.insert_multiple(serialized_players)

    def load_players(self):
        """Load the players from the database"""
        players_table = self.db.table("players")
        players = players_table.all()
        for player in players:
            new_player = Player(player["surname"], player["name"],
                                player["birthdate"], player["gender"], player["ranking"])
            self.players.append(new_player)
        self.players.sort(key=attrgetter("surname"))

    def save_tournaments(self):
        self.tournaments.sort(key=attrgetter("name"))
        serialized_tournaments = [tournament.serialized()
                                  for tournament in self.tournaments]
        print(serialized_tournaments)                          
        tournaments_table = self.db.table("tournaments")
        tournaments_table.truncate()
        tournaments_table.insert_multiple(serialized_tournaments)

    def recover_players(self, players):
        "recreate the player list based on players dictionary list"
        player_list = []
        for player in players:
            player = Player(player["surname"], player["name"],
                            player["birthdate"], player["gender"], player["ranking"])
            player_list.append(player)
        return player_list

    def recover_rounds(self, rounds):
        """Return the list of rounds objects based on the list of rounds dictionaries"""
        rounds = []
        for round in rounds:
            matches = []
            serialized_matches = round["matches"]
            for match in serialized_matches:
                player_1_serialized = match["player_1"]
                player_1 = Player(player_1_serialized["surname"], player_1_serialized["name"],
                                  player_1_serialized["birthdate"], player_1_serialized["gender"], player_1_serialized["ranking"])
                player_2_serialized = match["player_2"]
                player_2 = Player(player_2_serialized["surname"], player_2_serialized["name"],
                                  player_2_serialized["birthdate"], player_2_serialized["gender"], player_2_serialized["ranking"])
                new_match = ([player_1, match["result_player_1"]], [player_2, match["result_player_2"]])          
                matches.append(new_match)               
            new_round = Round(
                round["round_number"], round["start_time"], round["end_time"], matches)
            rounds.append(new_round)
        return rounds

    def load_tournaments(self):
        tournaments_table = self.db.table("tournaments")
        tournaments = tournaments_table.all()
        for tournament in tournaments:
            tournament_players = self.recover_players(tournament["players"])
            tournament_rounds = self.recover_rounds(tournament["round_list"])
            new_tournament = Tournament(tournament["name"], tournament["place"], tournament["date"], tournament["time_management"],
                                        tournament["description"], tournament["round_number"])
            new_tournament.set_players(tournament_players)       
            new_tournament.set_rounds(tournament_rounds)                     
            self.tournaments.append(new_tournament)

    def add_players(self):
        """Add players to the application"""
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
            print(
                f"{count} -- Rank {player_ranking} : {player_name} {player_surname}")
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
            tournament_info["time"], tournament_info["description"], tournament_info['rounds'])
        return tournament

    def run(self):
        """Run the application"""
        while(True):
            self.view.display_menu()
            option = int(input("Entrez votre choix: "))
            if option == 1:
                print("Vous avez choisi d'ajouter des joueurs.")
                players_list = self.add_players()
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
                players_list = self.players
                launched_tournament = self.view.choose_tournaments(self.tournaments)
                launched_tournament.choose_players(players_list)
                launched_tournament.run_tournament()
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
                choice = int(
                    input("Choississez un joueur à modifier en tapant son numéro:"))
                player = players[choice-1]
                ranking = int(input("Indiquer le rang du joueur: "))
                player.set_ranking(ranking)
            elif option == 8:
                print("vous avez choisi de sauvegarder les joueurs dans la database")
                self.save_players()
            elif option == 9:
                print(
                    "vous avez choisi de charger les joueurs présents dans la base de données")
                self.load_players()
            elif option == 10:
                print("Vous avez choisi de sauvegarder les tournois")
                self.save_tournaments()    
            elif option == 11:
                print("Vous avez choisi de charger les tournois")
                self.load_tournaments()    
            elif option == 12:
                print("Vous avez choisi d'afficher la liste des joueurs d'un tournois'")
                tournament = self.view.choose_tournament(self.tournaments)
                tournament.get_player_list()
            elif option == 13:
                print("Vous avez choisi d'afficher le classement des joueurs d'un tournois")
                tournament = self.view.choose_tournament(self.tournaments)
                tournament.get_playersrank()
            elif option == 14:
                print("vous avez choisi d'afficher les tours d'un tournois")
                
            elif option == 15:
                print("vous avez choisi d'afficher les matchs d'un tournois")
            elif option == 16:
                print("Vous avez choisi de quitter l'application. Bye bye !")
                quit()        
            else:
                print("Choix invalide. Merci de saisir un nombre entre 1 et 8.")

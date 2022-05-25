from operator import attrgetter
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from typing import List

class Controller:
    """main controller"""
    def __init__(self,view):
        """Has a view and a list of players"""
        # View
        self.view = view

        #Models
        self.players: List[Player] = []

    def get_players(self):
        """get the tournament players"""
        while len(self.players) < 9:
            player_info = self.view.get_player()
            player = Player(player_info["surname"], player_info["name"], player_info["birthdate"], player_info["gender"], player_info['ranking'])
            self.players.append(player)

    def create_tournament(self):
        """Collect tournament infos from user"""       
        tournament_name = self.view.get_tournament_name()
        tournament_place = self.view.get_tournament_place()
        tournament_date = self.view.get_tournament_date()
        tournament_description = self.view.get_tournament_description()
        tournament_number_of_round = self.view.get_number_of_rounds()
        tournament_time_management = self.view.get_tournament_time_management()
        tournament = Tournament(tournament_name, tournament_place, tournament_date, self.players, tournament_time_management, tournament_description, tournament_number_of_round)
        return tournament

    def create_a_round(self, round_number, matches):
        round_start_date = self.view.get_round_start_date()
        round_start_time = self.view.get_round_start_time()
        round_end_date = self.view.get_round_end_date()
        round_end_time = self.view.get_round_end_time()
        round = Round(matches, round_number, round_start_time, round_start_date, round_end_time, round_end_date)

    def create_matches(self, round):
        if round == 1:
            self.players.sort(key=attrgetter("ranking"))
        elif round > 1:
            self.players.sort(key=attrgetter("score"))
        lenght_list = len(self.players)
        middle_index = lenght_list // 2
        low_ranked_players = self.players[:middle_index]
        high_ranked_players = self.players[middle_index:]
        matches = []
        for i in range(lenght_list):
            match = [low_ranked_players[i], high_ranked_players[i]]
            matches.append(match)
        return matches    

    def run(self):
        """Start the application"""
        players = self.get_players()
        print(players)


                        
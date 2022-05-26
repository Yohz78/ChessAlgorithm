from operator import attrgetter
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from typing import List


class Controller:
    """main controller"""

    def __init__(self, view):
        """Has a view and a list of players"""
        # View
        self.view = view

        # Models
        self.players: List[Player] = []
        self.rounds: List[Round] = []

    def get_players(self):
        """get the tournament players"""
        while len(self.players) < 9:
            player_info = self.view.get_player()
            player = Player(player_info["surname"], player_info["name"],
                            player_info["birthdate"], player_info["gender"], player_info['ranking'])
            self.players.append(player)

    def create_first_pairs(self):
        """Return a list of pairs of players for the first round"""
        self.players.sort(key=attrgetter("ranking"))
        lenght_list = len(self.players)
        middle_index = lenght_list // 2
        low_ranked_players = self.players[:middle_index]
        high_ranked_players = self.players[middle_index:]
        pairs = []
        for i in range(lenght_list):
            match = [low_ranked_players[i], high_ranked_players[i]]
            pairs.append(match)
        return pairs

    def create_next_pairs(self):
        """ Return a list of pairs of players based on score and already met players for each player"""
        self.players.sort(key=attrgetter("ranking"))
        lenght_list = len(self.players)
        middle_index = lenght_list // 2
        low_ranked_players = self.players[:middle_index]
        high_ranked_players = self.players[middle_index:]
        matches = []
        for i in range(lenght_list):
            match = [low_ranked_players[i], high_ranked_players[i]]
            matches.append(match)
        return matches  

    def save_match_results(self, pair):
        """ Return an object match after asking for a pair of player results from the user. Increment player score."""
        player_1 = pair[0]
        player_2 = pair[1]
        player_1_result = self.view.get_player_result()
        player_2_result = self.view.get_player_result()
        player_1.increment_player_score(player_1_result)
        player_2.increment_player_score(player_2_result)
        match = Match(player_1, player_1_result,player_2, player_2_result)
        return match

    # To change
    # def create_tournament(self):
    #     """Return an object tournament after asking for infos from the user"""
    #     tournament_name = self.view.get_tournament_name()
    #     tournament_place = self.view.get_tournament_place()
    #     tournament_date = self.view.get_tournament_date()
    #     tournament_description = self.view.get_tournament_description()
    #     tournament_number_of_round = self.view.get_number_of_rounds()
    #     tournament_time_management = self.view.get_tournament_time_management()
    #     tournament = Tournament(tournament_name, tournament_place, tournament_date, self.players,
    #                             tournament_time_management, tournament_description, tournament_number_of_round)
    #     return tournament



    def create_a_round(self, round_number, matches):
        """Return an object round"""
        round_start_date = self.view.get_round_start_date()
        round_start_time = self.view.get_round_start_time()
        round_end_date = self.view.get_round_end_date()
        round_end_time = self.view.get_round_end_time()
        round = Round(matches, round_number, round_start_time,
                      round_start_date, round_end_time, round_end_date)   
        return round              

    def saving_round_results(self, round_number, pairs):
        """return an object round having saved the matches tuples from a round's pairs"""
        matches = []
        for pair in pairs:
            match = self.save_match_results(pair)
            match = match.get_match_tuple()
            matches.append(match)
        round = self.create_a_round(round_number, matches)
        return round    
                  
    def run(self):
        """Run the application's controller"""
        self.get_players()
        round_number = self.view.get_number_of_rounds()
        for i in range(round_number-1):
            if i == 0:
                first_pairs = self.create_first_pairs
                first_round = self.saving_round_results(round_number, first_pairs)
                self.rounds.append(first_round)
            # else:
            #     pairs=    


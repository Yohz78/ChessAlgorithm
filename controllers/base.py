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
        self.rounds: List[Round] = []

        # Views
        self.view = view

# Player's related controller's methods
    def get_players(self):
        """get the tournament players"""
        players = []
        while len(players) < 4:
            player_info = self.view.get_player()
            player = Player(player_info["surname"], player_info["name"],
                            player_info["birthdate"], player_info["gender"], player_info['ranking'])
            players.append(player)
        return players

# Pair creation related controller's methods
    def save_pairs(self, pairs, saved_pairs):
        """Save a list of names pair for the players in the input list of players
        in the list saved_pairs given in input"""
        for pair in pairs:
            player_1 = pair[0]
            player_2 = pair[1]
            player_1_name = player_1.get_player_name()
            player_2_name = player_2.get_player_name()
            pair_names = [player_1_name, player_2_name]
            saved_pairs.append(pair_names) 
        return saved_pairs   

# Match related controller's methods
    def save_match_results(self, pair):
        """ Return an object match after asking for a pair of player results from the user.
         Increment player score."""
        player_1 = pair[0]
        player_2 = pair[1]
        player_1_result = self.view.get_player_result(player_1)
        player_2_result = self.view.get_player_result(player_2)
        player_1.increment_player_score(player_1_result)
        player_2.increment_player_score(player_2_result)
        match = Match(player_1, player_1_result, player_2, player_2_result)
        match_results = match.get_match_tuple()
        return match_results

# Round related controller's methods
    def create_a_round(self, round_number):
        """Return an object round"""
        now = datetime.now()
        start_time = now.strftime("%d/%m/%Y %H:%M:%S")        
        round = Round(round_number, start_time)
        # self.rounds.append(round)
        return round

    def get_end_time(self):        
        now = datetime.now()
        end_time= now.strftime("%d/%m/%Y %H:%M:%S")
        return end_time

# Tournament related controller's methods
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
        tournament = self.create_tournament() 
        players_list = self.get_players()
        tournament.set_players(players_list)
        total_rounds = tournament.get_round_number()
        current_round = 0
        saved_pairs = []
        while current_round != total_rounds: 
            new_round = self.create_a_round(current_round+1)      
            if current_round == 0:
                pairs = new_round.create_pairs(players_list)
                print("First pairs")
                print(pairs)
                saved_pairs = self.save_pairs(pairs, saved_pairs)
            else:
                pairs = new_round.create_new_pairs(players_list, saved_pairs)
                print("new pairs")
                print(pairs)
                saved_pairs = self.save_pairs(pairs, saved_pairs)
                print(f"saved pairs {saved_pairs}")
            new_round.save_matches(pairs)
            print(new_round.__str__())    
            tournament.add_round(new_round)
            current_round += 1
        rounds = tournament.get_rounds()
        for round in rounds:
            matches = round.get_round_matches()
            print(matches)


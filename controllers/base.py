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
        while len(players) < 8:
            player_info = self.view.get_player()
            player = Player(player_info["surname"], player_info["name"],
                            player_info["birthdate"], player_info["gender"], player_info['ranking'])
            players.append(player)
        return players

# Pair creation related controller's methods
    def create_pairs(self, players):
        """Return the first round list of pairs of players"""
        players_list = players
        players_list.sort(key=attrgetter("ranking"))
        lenght_list = len(players_list)
        middle_index = lenght_list // 2
        low_ranked_players = players_list[:middle_index]
        high_ranked_players = players_list[middle_index:]
        pairs = []
        for i in range(0, middle_index):
            match = [low_ranked_players[i], high_ranked_players[i]]
            pairs.append(match)
        return pairs

    # def get_previous_pairs(self):
    #     """Return a list of the tournament previous rounds pairs of player"""
    #     pairs = []
    #     for round in self.rounds:
    #         matches = round.get_round_matches()
    #         round_pairs = round.get_pairs(matches)
    #         pairs.append(round_pairs)
    #     return pairs[0]
    def save_pairs(self, pairs, saved_pairs):
        """Return a list of the tournament previous rounds pairs of player"""
        for pair in pairs:
            player_1 = pair[0]
            player_2 = pair[1]
            player_1_name = player_1.get_player_name()
            player_2_name = player_2.get_player_name()
            pair_names = [player_1_name, player_2_name]
            saved_pairs.append(pair_names) 
        return saved_pairs


    def compare_pairs(self, pair, saved_pairs):
        """ Return true if a pair has NOT already been matched. Otherwise, return false"""
        for saved_pair in saved_pairs:
            if pair == saved_pair:
                return False
        return True

    def has_already_played(self, player, player_list):
        if player in player_list:
            return True
        return False    

    def create_new_pairs(self, list, saved_pairs):
        """Return a list of pairs according to Swiss matchmaking rules after first round.
        If two player have already been matched, 
        the app will match them with the next player if possible."""
        players_list = list
        players_list.sort(key=attrgetter("ranking"))  
        already_played = []
        new_pairs = []
        for player_1 in players_list:
            if self.has_already_played(player_1, already_played) == False:
                already_played.append(player_1)
                for player_2 in players_list:
                    if self.has_already_played(player_2, already_played) == False:
                        match = [player_1, player_2]
                        player_1_name = player_1.get_player_name()
                        player_2_name = player_2.get_player_name()
                        match_names = [player_1_name, player_2_name]
                        match_check = self.compare_pairs(match_names, saved_pairs)
                        if match_check == True:
                            already_played.append(player_2)
                            new_pairs.append(match)
                            break
                        # elif len(already_played) == len(players_list)-2:
                        #     new_pairs.append(match)
                        #     break
            else:
                if len(already_played) != len(players_list):
                    continue             
        return new_pairs        

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
    def create_a_round(self, round_number, matches, start_time):
        """Return an object round"""
        end_time = self.get_round_time()
        round = Round(matches, round_number, start_time, end_time)
        self.rounds.append(round)
        return round

    def saving_round_results(self, round_number, pairs, start_time):
        """return an object round having saved the matches tuples from a round's pairs"""
        matches = []
        for pair in pairs:
            match = self.save_match_results(pair)
            matches.append(match)
        round = self.create_a_round(round_number, matches, start_time)
        return round

    def get_round_time(self):
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        return dt_string
        


# Tournament related controller's methods
    def get_tournament_info(self):
        tournament_info = self.view.get_tournament()
        tournament_info['time'] = self.view.get_tournament_time_management()
        tournament_info['rounds'] = self.view.get_number_of_rounds()
        return tournament_info

    def create_tournament(self, tournament_info, rounds):
        """Return an object tournament"""
        tournament = Tournament(
            tournament_info["name"], tournament_info["place"], tournament_info['date'], 
            tournament_info["time"], tournament_info["description"], self.players, rounds)
        return tournament

# Run method
    def run(self):
        """Run the application"""
        tournament_info =  self.get_tournament_info()       
        players_list = self.get_players()
        total_rounds = tournament_info["rounds"]
        current_round = 0
        saved_pairs = []
        rounds = []
        while current_round != total_rounds: 
            players  = players_list            
            if current_round == 0:
                pairs = self.create_pairs(players_list)
                saved_pairs = self.save_pairs(pairs, saved_pairs)
            else:
                pairs = self.create_new_pairs(players, saved_pairs)
                print(pairs)
                saved_pairs = self.save_pairs(pairs, saved_pairs)
            start_time = self.get_round_time()        
            round = self.saving_round_results(current_round, pairs, start_time)
            rounds.append(round)
            current_round += 1
            print(" saved_pairs")
            print(saved_pairs)
        tournament = self.create_tournament(tournament_info, rounds)   
        return tournament

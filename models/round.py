from operator import attrgetter
from datetime import datetime
from models.match import Match
from typing import List

class Round:
    "Objet round"

    def __init__(self,  round_number, start_time, end_time="Round has not ended yet"):
        self.matches: List[Match] = []
        self.round_number = round_number
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"round number is {self.round_number}"

    def set_end_time(self):
        """Set the end time and date of the round"""
        now = datetime.now()
        self.end_time= now.strftime("%d/%m/%Y %H:%M:%S")

    def get_player_result(self, player):
        """ask for the player's match result"""
        player_name = player.get_player_name()
        result_string = input(f"Merci de saisir le resultat de {player_name} : ")
        result = float(result_string)
        return result

    def save_matches(self, pairs):
        """save one instance of match in the matches list of the round"""
        self.set_end_time()
        for pair in pairs:
            player_1 = pair[0]
            player_2 = pair[1]
            player_1_result = self.get_player_result(player_1)
            player_2_result = self.get_player_result(player_2)
            player_1.increment_player_score(player_1_result)
            player_2.increment_player_score(player_2_result)
            match = Match(player_1, player_1_result, player_2, player_2_result)
            match_tuple = match.get_match_tuple()
            self.matches.append(match_tuple)

    def get_round_matches(self):
        """return the list of match tuples"""
        return self.matches
    
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
            else:
                if len(already_played) != len(players_list):
                    continue             
        return new_pairs       
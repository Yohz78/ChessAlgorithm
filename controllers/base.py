from operator import attrgetter
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
from views.base import View
from typing import List
from datetime import date


class Controller:
    """main controller"""

    def __init__(self):
        """Has a list of players, a list of rounds and the tournament info."""
        # Models
        self.players: List[Player] = []
        self.rounds: List[Round] = []

# Player's related controller's methods
    def get_players(self):
        """get the tournament players"""
        while len(self.players) < 9:
            player_info = View.get_player()
            player = Player(player_info["surname"], player_info["name"],
                            player_info["birthdate"], player_info["gender"], player_info['ranking'])
            self.players.append(player)

# Pair creation related controller's methods
    def create_pairs(self):
        """Return the first round list of pairs of players"""
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

    def get_previous_pairs(self):
        """Return a list of the tournament previous rounds pairs of player"""
        pairs = []
        for round in self.rounds:
            round_pairs = round.get_pairs()
            pairs.append(round_pairs)
        return pairs

    def compare_pairs(self, pair, previous_pairs):
        """ Return true if a pair has NOT already been matched. Otherwise, return false"""
        for previous_pair in previous_pairs:
            if pair == previous_pair:
                return False
        return True

    def create_new_pairs(self):
        """Return a list of pairs according to Swiss matchmaking rules after first round.
        If two player have already been matched, 
        the app will match them with the next player if possible."""
        players_list = self.players.sort(key=attrgetter("ranking"))
        previous_pairs = self.get_previous_pairs()
        new_pairs = []
        for player in players_list:
            players_list.remove(player)
            for other_player in players_list:
                match = [player, other_player]
                match_check = self.compare_pairs(match, previous_pairs)
                if match_check == True:
                    new_pairs.append(match)
                    players_list.remove(other_player)
                elif len(players_list) < 2:
                    new_pairs.append(match)
                    players_list.remove(other_player)
                else:
                    continue
        return new_pairs


# Match related controller's methods

    def save_match_results(self, pair):
        """ Return an object match after asking for a pair of player results from the user.
         Increment player score."""
        player_1 = pair[0]
        player_2 = pair[1]
        player_1_result = View.get_player_result()
        player_2_result = View.get_player_result()
        player_1.increment_player_score(player_1_result)
        player_2.increment_player_score(player_2_result)
        match = Match(player_1, player_1_result, player_2, player_2_result)
        return match

# Round related controller's methods
    def create_a_round(self, round_number, matches):
        """Return an object round"""
        round_start_date = View.get_round_start_date()
        round_start_time = View.get_round_start_time()
        round_end_date = View.get_round_end_date()
        round_end_time = View.get_round_end_time()
        round = Round(matches, round_number, round_start_time,
                      round_start_date, round_end_time, round_end_date)
        self.rounds.append(round)
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

# Tournament related controller's methods
    def create_tournament(self, tournament_info):
        """Return an object"""
        tournament = Tournament(
            tournament_info["name"], tournament_info["place"], tournament_info[date], self.players,
            tournament_info["time"], tournament_info["description"], tournament_info["rounds"])
        return tournament

# Run method
    def run(self):
        """Run the application"""
        self.get_players()
        round_number = View.get_number_of_rounds()
        for i in range(round_number-1):
            if i == 0:
                first_pairs = self.create_first_pairs
                first_round = self.saving_round_results(
                    round_number, first_pairs)
                self.rounds.append(first_round)
            # else:
            #     pairs=

from typing import List
from models.round import Round
from datetime import datetime


class Tournament:
    """Objet tournois"""

    def __init__(self, name, place, date, time_management, description, players, rounds):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.time_management = time_management
        self.description = description
        self.rounds = rounds
        self.rounds_list: List[Round] = []

    def get_round_number(self):
        """return the number of round expected for the tournament"""
        return self.rounds

    def get_name(self):
        """Return tournament's name"""
        return self.name

    def get_rounds(self):
        """return the number of round expected for the tournament"""
        return self.rounds_list

    def add_round(self, round):
        """Append a round of matches to the inner list of a tournament"""
        self.rounds_list.append(round)

    def set_players(self, players):
        """Update the player list of the tournament"""
        self.players = players

    def create_a_round(self, round_number):
        """Return an object round"""
        now = datetime.now()
        start_time = now.strftime("%d/%m/%Y %H:%M:%S")
        round = Round(round_number, start_time)
        return round

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

    def choose_players(self, players):
        """Allow to choose the tournament's player based on players in the input list"""
        print("Choisissez 8 joueurs dans la liste ci dessous:")
        count = 1
        for player in players:
            player_name = player.get_name()
            player_surname = player.get_surname()
            print(f"Joueur{count} : {player_name} {player_surname}")
            count += 1
        choice = 0
        player_list = []
        while choice < 8:
            player_number = int(
                input("please choose a player using his number:"))
            player = self.players[player_number]
            player_list.append(player)
        self.set_players(player_list)

    def run_tournament(self):
        """Run the tournament"""
        total_rounds = self.get_round_number()
        current_round = 0
        saved_pairs = []
        while current_round != total_rounds:
            new_round = self.create_a_round(current_round+1)
            if current_round == 0:
                pairs = new_round.create_pairs(self.players)
                saved_pairs = self.save_pairs(pairs, saved_pairs)
            else:
                pairs = new_round.create_new_pairs(self.players, saved_pairs)
                saved_pairs = self.save_pairs(pairs, saved_pairs)
            new_round.save_matches(pairs)
            self.add_round(new_round)
            current_round += 1

from typing import List
from models.round import Round

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

    def get_rounds(self):
        """return the number of round expected for the tournament"""
        return self.rounds_list

    def add_round(self, round):
        """Append a round of matches to the inner list of a tournament"""
        self.rounds_list.append(round)

    def set_players(self,players):
        """Update the player list of the"""
        self.players = players

class Tournament:
    """Objet tournois"""
    def __init__(self, name, place, date, players, time_management, description, rounds):
        self.name = name
        self.place = place
        self.date = date
        self.players = players
        self.time_management = time_management
        self.description = description
        self.rounds = rounds

    def get_tournament_rounds(self):
        return self.rounds    
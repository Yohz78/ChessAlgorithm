class Player:
    """Player."""
    def __init__(self, surname, name, birthdate, gender, ranking, score=0):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def get_player_name(self):
        return self.name

    def get_player_ranking(self):
        return self.ranking    

    def get_player_score(self):
        return self.score    
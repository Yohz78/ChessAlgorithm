class Player:
    """Player."""

    def __init__(self, surname, name, birthdate, gender, ranking, score=0.0):
        self.surname = surname
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def __str__(self):
        return self.name   

    def get_player_name(self):
        """return the player's name"""
        return self.name

    def get_player_ranking(self):
        """return the player's ranking"""
        return self.ranking

    def get_player_score(self):
        """return theplayer's score"""
        return self.score

    def increment_player_score(self, result):
        """add the result of a round to the score total of a player"""
        self.score += result

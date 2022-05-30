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

    def get_name(self):
        """return the player's name"""
        return self.name

    def get_surname(self):
        """return the player's surname"""
        return self.surname

    def get_ranking(self):
        """return the player's ranking"""
        return self.ranking

    def get_player_score(self):
        """return the player's score"""
        return self.score

    def set_ranking(self, ranking):
        """set the player's rank"""
        self.ranking = ranking    

    def increment_player_score(self, result):
        """add the result of a round to the score total of a player"""
        self.score += result

    def reset_score(self):
        """Reset the score of a player for a new tournament"""    
        self.score = 0

    def serialized(self):
        "Return a dictionary of the players attributes"
        serialized_player = {
            'surname' : self.surname,
            'name' : self.name,
            'birthdate' : self.birthdate,
            'ranking' : self.ranking,
            'gender' : self.gender
        }
        return serialized_player    


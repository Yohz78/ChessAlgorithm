class Round:
    "Objet round"

    def __init__(self, matches, round_number, start_time, end_time):
        self.matches = matches
        self.round_number = round_number
        self.start_time = start_time
        self.end_time = end_time

    def get_round_matches(self):
        """return the list of match tuples"""
        return self.matches
    
    def get_pairs(self, matches):
        """Return a list of matches pairs in list type, not tuple"""
        pairs = []
        for match in matches:
            pair = self.get_pair(match)
            pairs.append(pair)
        return pairs        

    def get_pair(self, match):
        """Return a pair of player with list type without their score"""
        pair = [player[0] for player in match]
        return pair



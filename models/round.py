class Round:
    "Objet round"

    def __init__(self, matches, round_number, start_time, start_date, end_time, end_date):
        self.matches = matches
        self.round_number = round_number
        self.start_time = start_time
        self.start_date = start_date
        self.end_time = end_time
        self.end_date = end_date

    def get_round_matches(self):
        """return the list of match tuples"""
        return self.matches

    def get_pair(self, match):
        """Return a pair of player with list type without their score"""
        (player_1_list, player_2_list) = match
        player_1 = player_1_list[0]
        player_2 = player_2_list[0]
        pair = [player_1, player_2]
        return pair

    def get_pairs(self):
        """Return a list of matches pairs in list type, not tuple"""
        matches = self.matches
        pairs = []
        for match in matches:
            pair = self.get_pair(match)
            pairs.append(pair)
        return pairs

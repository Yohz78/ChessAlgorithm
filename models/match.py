class Match:
    """Object Match"""
    def __init__(self, player_1, result_player_1, player_2, result_player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.result_player_1 = result_player_1
        self.result_player_2 = result_player_2

    def get_match_tuple(self):
        player1_list = [self.player_1, self.result_player_1]
        player2_list = [self.player_2, self.result_player_2]
        match_results = (player1_list, player2_list)
        return match_results
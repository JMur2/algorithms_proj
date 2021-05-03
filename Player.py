class Player:
    """
    A class that will hold a player's stats for both pre and post moving to a new team.
    This class will also handle the conversion of stats from their float values to the
    categories (Good, Neutral, and Bad)
    """
    def __init__(self, id):
        # player id to help identify
        self.player_id = id

        # arrays for player stats and stat scores
        self.pre_stats = []
        self.post_stats = []
        self.pre_scores = []
        self.post_scores = []

    def set_pre_stat_scores(self):
        # TODO: complete this function
        return self.pre_scores
    
    def set_post_stat_scores(self):
        # TODO: complete this function
        return self.post_scores

    """
    Below are 5 helper functions that return a value to the parent class, or will set a value within the current player
    """
    def get_player_id(self):
        return self.player_id
    
    def set_pre_move_stats(self, stats):
        self.pre_stats = stats

    def set_post_move_stats(self, stats):
        self.post_stats = stats

    def get_pre_move_stats(self):
        return self.pre_stats
    
    def get_post_move_stats(self):
        return self.post_stats

class Player:
    """
    A class that will hold a player's stats for both pre and post moving to a new team.
    This class will also handle the conversion of stats from their float values to the
    categories (Good, Neutral, and Bad)
    """
    def __init__(self, id):
        self.player_id = id
    
    def set_pre_move_stats(self, stats):
        self.pre_stats = stats

    def set_post_move_stats(self, stats):
        self.post_stats = stats

    def get_pre_move_stats(self):
        return self.pre_stats
    
    def get_post_move_stats(self):
        return self.post_stats

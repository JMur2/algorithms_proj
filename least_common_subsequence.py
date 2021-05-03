import pandas as pd

from openpyxl import load_workbook 
from Player import Player

class Project:

    def __init__(self):
        # data frames for storing player data
        self.pre_move_df = None
        self.post_move_df = None
        self.players = None

    def read_data(self):
        # makes use of the openpyxl library to read in data from excel
        wb = load_workbook(filename='data.xlsx', read_only=True)
        ws = wb['Sheet1']

        # selects the stats of players before they moved teams
        data_rows = []
        for row in ws['C4':'I63']:
            data_cols = []
            for cell in row:
                data_cols.append(cell.value)
            data_rows.append(data_cols)
        
        self.pre_move_df = pd.DataFrame(data_rows)

        # selects the stats of players after they moved teams
        data_rows = []
        for row in ws['K4':'Q63']:
            data_cols = []
            for cell in row:
                data_cols.append(cell.value)
            data_rows.append(data_cols)
        
        self.post_move_df = pd.DataFrame(data_rows)
        
    def set_all_player_stats(self):
        """
        This function looks at the set of players found in the excel document, and creates a player object for each unique player.
        The player object stores a player id (their number in the list), as well as the players 2 sets of stats
        """
        for i in range(self.pre_move_df.values):
            p = Player(i)

            p.set_pre_move_stats(self.pre_move_df.values[i])
            p.set_post_move_stats(self.post_move_df.values[i])

            self.players.append(p)

    def lcs(self, X, Y, m, n):
        """
        This algorithm checks for the longest common subsequence between 2 arrays and includes a modification that places a higher 
        weights on what will be a "good stat" on a player

        Solved with recursion

        Parameters:
        X: array of values
        Y: array of values
        """
        if m == 0 or n == 0:
            return 0
        elif X[m-1] == Y[n-1]:
            if X[m-1] == 0:
                # a neutral stat is considered as normal within the LCS
                return 1 + self.lcs(X, Y, m-1, n-1)
            elif X[m-1] == 1:
                # a good stat will recieve a higher value to show its importance in the LCS
                return 2 + self.lcs(X, Y, m-1, n-1)
        else:
            return max(self.lcs(X, Y, m, n-1), self.lcs(X, Y, m-1, n))

if __name__ == "__main__":
    project = Project()
    project.read_data()

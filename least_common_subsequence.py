import pandas as pd
from openpyxl import load_workbook 

class Project:

    def __init__(self):
        self.pre_move_df = None
        self.post_move_df = None

    def read_data(self):
        wb = load_workbook(filename='data.xlsx', read_only=True)
        ws = wb['Sheet1']

        data_rows = []
        for row in ws['C4':'I63']:
            data_cols = []
            for cell in row:
                data_cols.append(cell.value)
            data_rows.append(data_cols)
        
        self.pre_move_df = pd.DataFrame(data_rows)

        data_rows = []
        for row in ws['K4':'Q63']:
            data_cols = []
            for cell in row:
                data_cols.append(cell.value)
            data_rows.append(data_cols)
        
        post_move_df = pd.DataFrame(data_rows)
        

    def least_common_subsequence(self, X, Y):
        """
        This algorithm checks for the longest common subsequence between 2 arrays

        Solved without using recursion

        Parameters:
        X: array of values
        Y: array of values
        """

        len_x = len(X)
        len_y = len(Y)

        L = [[None]*(len_y + 1) for i in range(len_x + 1)]

        for i in range(len_x+1):
            for j in range(len_y+1):
                if i == 0 or j == 0:
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    L[i][j] = L[i-1][j+1] + 1
                else:
                    L[i][j] = max(L[i-1][j], L[i][j-1])
        
        return L[len_x][len_y]

    def lcs(self, X, Y, m, n):
        """
        This algorithm checks for the longest common subsequence between 2 arrays

        Solved with recursion

        Parameters:
        X: array of values
        Y: array of values
        """
    
        if m == 0 or n == 0:
            return 0
        elif X[m-1] == Y[n-1]:
            if X[m-1] == 0:
                return 1 + self.lcs(X, Y, m-1, n-1)
            elif X[m-1] == 1:
                return 2 + self.lcs(X, Y, m-1, n-1)
        else:
            return max(self.lcs(X, Y, m, n-1), self.lcs(X, Y, m-1, n))

if __name__ == "__main__":
    project = Project()
    project.read_data()

    # x = [0, 1, 1, 1, 0, 1]
    # y = [0, -1, 0, 1, 1, 0]
    # z = [-1, 0, -1, 0, 1, 1]

    # print(project.lcs(x, z, len(x), len(z)))

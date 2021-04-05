import pandas as pd

class Project:

    def __init__(self):
        pass

    def read_data(self):
        df = pd.read_excel(r'data.xlsx', sheet_name='Sheet2')
        print(df)

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
        #return L

    def lcs(self, X, Y, m, n):
        """
        This algorithm checks for the longest common subsequence between 2 arrays

        Solved with recursion

        Parameters:
        X: array of values
        Y: array of values
        m: size of array X
        n: size of array Y
        """
    
        if m == 0 or n == 0:
            return 0;
        elif X[m-1] == Y[n-1]:
            return 1 + lcs(X, Y, m-1, n-1);
        else:
            return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));

if __name__ == "__main__":
    
    project = Project()
    project.read_data()

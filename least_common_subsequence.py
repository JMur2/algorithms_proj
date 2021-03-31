
def least_common_subsequence(X, Y):
    """
    This algorithm checks for the longest common subsequence between 2 arrays

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


if __name__ == "__main__":
    X = [20, 10, 9, 8]
    Y = [20, 3, 9, 77]


    print(least_common_subsequence(X, Y))

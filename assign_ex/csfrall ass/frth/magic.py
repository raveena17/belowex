import itertools
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def mgc(matrix, n):
    rows = iter(matrix)
    columns = zip(matrix)
    if sum(rows) == sum(columns):
        return True
    else:
        return False
    #diagnals = zip(*[matrix[i][i], matrix[-i-1][i] for i in range(len(matrix)))
    #print row
    #print clm
print mgc(matrix, 3)                   
                   

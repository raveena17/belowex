#matrix([1,2,3],[1,2,3],[1,2,3])
def magic_square(matrix):
    import pdb;pdb.set_trace()
    n = len(matrix[0])
    sum_list = []
    
    #Vertical:
    for col in range(n):
        sum_list.append(sum(row[col] for row in matrix))
    #Horizantal:
    for row in range(n):
        sum_list.append(sum(col[row] for col in matrix))
    #diagonals
    dlresult=0
    for i in range(n):
        dlresult+=matrix[i][i]
    sum_list.append(dlresult)
    drowresult=0
    for i in range(n-1,-1,-1):
        drowresult+=matrix[i][i]
    sum_list.append(drowresult)
    if len(set(sum_list))>1:
        return False
    return True
        
        
        
        
    

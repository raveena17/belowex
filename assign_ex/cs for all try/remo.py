def plat(lists,n):
    result=[]
    for numbers in range (len(lists)):
        if lists[numbers]==n:
           s = lists.remove(lists[numbers])
        else:
           result.append(lists[numbers])
        return result
print plat([7,8,9,5,9],9)
        

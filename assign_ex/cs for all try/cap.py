'''def subset(capacity, items):
	    if capacity <= 0 or items == []:
	        return 0
	    elif items[0] > capacity:
	        return subset(capacity, items[1:])
	    if items[0] < capacity:
	        loseIt = subset(capacity, items[1:])
	        useIt = items[0] + subset(capacity - items[0], items[1:])
	        a = max(loseIt, useIt)
	        if capacity == a:
	             print('true')
	        else:
                     print('false')
            else:
                return 0
	        
print (subset(42, [25,1,25,10,5]))'''
def sb(cp, itms):
    cumulative_sum([itms])
    return a
print(sb(42, ['25','1','25','1','10']))

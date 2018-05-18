'''import itertools
def lk(n):
    return "".join('%s%s' %(len(list(group)),digit) for digit,group in itertools.groupby(str(n)))
print lk(10)'''
'''def morris_generator(a, b=1):
    num = str(b)
    while len(num) < a:
        yield int(num)
        num = next(num)
        print num
print morris_generator(10)'''
'''from itertools import  groupby
def lk(n):
    return "".join(str(sum(1 for x in n)) + n,n in itertools.groupby(n))
seq =['1']
for _ in xrange(10):
    seq.append(lk(seq[-1]))
print seq
print lk(10)'''
def morris(t):
    morris = '1'
    yield morris
    while True:
        print morris
        morris = ''.join(''.join(t) for t in ((str(len(list(group)))),key) for key,group in groupby(morris))
        yield morris
        print morris
print morris(10)

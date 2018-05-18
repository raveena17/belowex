def db1(x):
    return 2*x
print(map(db1, [1, 2, 3]))
def doubles(x):
    return [db1(x) for x in [1, 2, 3]]
def db2(x):
    return [db1(x) for x in [21, 22]]
def db3(x):
    return [db1(x) for x in range(10)]
def db4(x):
    return [db1(x) for x in []]
def db5(x):
    return [db1(x) for x in range(21, 23)]
def db6(x):
    return [db1(y) for y in [42, 43]]
def db7(x):
    return [db1(x) for x in range(0, 100)]
print doubles([1,2,3])
print db2([21, 22])
print db3(10)
print db4([])
print db5(23)
print db6([42, 43])
print db7(100)
def sq(x):
    return x**2
def sq1(x):
    return [sq(x) for x  in range(5)]
def sqmd(x):
    return x%4
def sqmd1(x):
    return [sqmd(x) for x in range(5)]
def mini(x):
    return  (x / 4.0)
def mini1(x):
    return[mini(x) for x in range(4)]
print (sq1(5))
print(sqmd1(5))
print(mini1(4))
def steps(low, high, N):
    return [(low )+ ((high - low)/float (N))*x for x in range(N)]
print steps(0,10,4)
print steps(41, 43, 8)
def fsteps(db1, low, high, N):
     z = ((low )+ ((high - low)/float (N))*x for x in range(N))
     return db1(z)
print fsteps(2, 0, 1, 4)
    

            


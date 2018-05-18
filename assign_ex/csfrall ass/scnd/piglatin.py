def spamlatin1(t):
    a = ['a','e','i','o','u']
    if t[0] in a: #t[0]=='a' or t[0]=='e' or t[0]=='i' or t[0]=='o' or t[0]=='u':
        res=(t[0:]+'ay')
        return res
def ind(t1):
    if t1[0] == 'y':
        res1=(t1[0:]+'way')
        return res1
def fun(t2):
    if t2[0] == 'y':
        res2=(t2[3:]+t2[0:3]+'ay')
        return res2
print(spamlatin1('abc'))
print(ind('yttrium'))
print(fun('yoohoo'))

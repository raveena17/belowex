def word(l):
    a= input('enter the num:')
    if a==1:
       Ln=l.split()
       return len(Ln)
    elif a==2:
        return len(l)
    elif a==3:
        li = 'aeiou'
        #if l in a:
        count = 0
        for i in range(len(l)):
                if a[i] in li:
                    count=count+1
        print count
print word('one')
#print word('syllables')
#print word('science')
#print word('This sentence has 4 words')
                
    
    

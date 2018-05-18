def rot(a, n):
    res=''
    for i in range(len(a)):
        ass=ord(a[i])+n
        if ass == '' or  n =='':
            return ''
        if ass>=32 and ass<=65:
            char3=ass-n
            res+=(chr(char3))
        elif ass > 97 and ass <= 122:
            res+=(chr(ass))
        elif ass>122:
             char1=ass-26
             res+=(chr(char1))
        elif ass>65 and ass <=90:
            res+=(chr(ass))
        else:
             char2 = ass-26
             res+=chr(char2)
    print res
#print rot('xyza*',1)

def rev(a,b):
        res=ord(a)+b
        if a==' ' or b==' ':
                return ' ' 
        elif res>122:
                res=res-26
                return chr(res)
        elif res>97 and res<122:
                return chr(res)
        elif res>65 and res <= 90 :
                return chr(res)
        else:
                cap=res-26
                return chr(cap)
        
def letProb( c ):
    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

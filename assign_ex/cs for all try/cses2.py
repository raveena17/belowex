def rot(a,b):

 rec=""
 for i in range(len(a)):
    res=ord(a[i])+b
    if a== ' 'or b==' ':
        return ' '
    if res>=32 and res<=65:
        scr=res-b
        rec+=(chr(scr))
    elif res>122:
        re=res-26
        rec+=(chr(re))
     # print( "\t"+chr(re)+"")
    elif res>97 and res<=122:
        rec+=(chr(res))
        #print chr(res)
    elif res>65 and res<=90:
        rec+=(chr(res))
        #print( "\t"+chr(res)+"")
    else:
        cap=res-26
        rec+=(chr(cap))
       # print("\t"+ chr(cap)+"")
 print rec
print rot('xyza',1)

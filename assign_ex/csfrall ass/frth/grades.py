
number = int(raw_input("Please enter a number: "))
num_list = []

while (number != int(-1)):
    num_list.append(number)
    number = int(raw_input("Please enter a number: "))

high = max(num_list)
low = min(num_list)
#med = numpy.median (num_list)
sm = sum(num_list)
ag = (sm/len(num_list))
li = sorted(num_list)
if len(li)%2 == 0:
    li1=len(li)/2
    med = ((li[li1] + li[li1-1])/2.0)
else:
    li1=len(li)/2
    med = li[li1]
rec="A:"
rec1="B:"
rec2="C:"
rec3="D:"
rec4="E:"
for i in range(len(li)):
    b='*'
    if li[i] >= 90 :
        rec+=b
    if li[i] >= 80 and li[i]<90:
         rec1+=b
    if li[i] >= 70 and li[i]<80:
          rec2+=b
    if li[i] >= 60 and li[i]<70:
           rec3+=b
    if li[i] >= 50 and li[i]<60:
           rec4+=b
           
print('max',high)
print('min',low)
#print(med)
print('avg',ag)
print ('Grade histogram')
print rec
print rec1
print rec2
print rec3
print rec4
print li
print med

    



 





    

    
    
    
    



# this code below welcomes the user 
print ("hello and welcome to my python quiz,my name is brandon and i am the quiz master")

print ("please type your name")

your_name = input ()

your_name = str(your_name)

score = 0# this code set the veriable to zero
# this is the question
print ("Question 1")

print ("what is 50x10")
answer = input ()
answer =int(answer)

if answer == 500:
   print ("good work")
   score = score + 1

else:

    print ("better luck next time")

    score = score - 1


print ("Question 2")

print ("what is (5x10)-4x2")
answer = input ()
answer =int(answer)

if answer == 94:
   print ("good work")
   score = score + 1

else:

    print ("better luck next time")

    score = score - 1

print ("Question 3")

print ("what is 600000000x10")
answer = input ()
answer =int(answer)

if answer == 6000000000:
   print ("good work")
   score = score + 1

else:

    print ("better luck next time")

    score = score - 1

print ("Question 4")

print ("what is 600000000/10")
answer = input ()
answer =int(answer)

if answer == 60000000:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print ("Question 5")

print ("what is 19x2-2")
answer = input ()
answer =int(answer)

if answer == 36:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print ("Question 6")

print ("what is (8x4) x 9")
answer = input ()
answer =int(answer)

if answer == 288:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print ("Question 7")

print ("what is 15 x4")
answer = input ()
answer =int(answer)

if answer == 60:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print ("Question 8")

print ("what is 19 x9")
answer = input ()
answer =int(answer)

if answer == 171:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print ("Question 9")

print ("what is 9 x9")
answer = input ()
answer =int(answer)

if answer == 81:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print ("Question 10")

print ("what is 10 x10")
answer = input ()
answer =int(answer)

if answer == 171:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1    


print ("Question 10")

print ("what is 10 x10")
answer = input ()
answer =int(answer)

if answer == 171:
   print ("good work")
   score = score + 1

else:

    print ("try again")

    score = score - 1

print("Question 11")

print ("6+8x2: \n\
1.28 \n\
2.14 \n\
3.38 \n\
4.34 \n"
answer =int(input (Menu))

if answer ==   1.:
       print ("well done")
elif answer == 2.:
       print ("better luck next time")
elif answer == 3.:
       print ("looser")
elif answer == 4.:
       print ("go back to primary school and learn how to add")

print("Question 12")

print ("6194+10x2: \n\
1.12409 \n\
2.124081 \n\
3.14321 \n\
4.12408 \n"
       answer =int(input (Menu))

if answer ==   1.:
       print ("well done")
elif answer == 2.:
       print ("better luck next time")
elif answer == 3.:
       print ("looser")
elif answer == 4.:
       print ("go back to primary school and learn how to add")





if score > 8:# this line tells the program if the user scored 2 points or over to print the line below

   print("amazing your score is" + str(score))# this code tells the user that they have done well if they have got 2or more points or over

elif score < 4:
    print ("good work your score is" + str(score))
else:
    print ("better look next time your scor is" + str(score))

print("well done your score is " +str (score))#this print the users score

print("thank you for playing in the python maths quiz")


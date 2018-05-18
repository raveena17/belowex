import questions


def Quiz(subject):
    total=10
    correct=0
    wrong=0
    skip=0

    print subject

    global Questions

    
    for i in range(len(questions.Questions.get(subject))):
        print questions.Questions.get(subject).get(i+1)
        ans1=raw_input("Enter the answer: ")
        length = len(ans1)
        res1=questions.ans.get(subject).get(i+1)
        
##      res2=questions.java_ans.get(subject).get(i+1)

        if res1==ans1:
            correct+=1
           
        elif length == 0:
            skip+=1

        elif res1!= ans1 and length != 0:
            wrong+=1
##
##        elif ans1 not in "abc":
##            print("Invalid choice, sequence coule only contain the following options (a,b,c)")

##            elif do_not_continue:
##           return

        
##
        elif ans1 not in ('abc'):
            print ("Invalid questions")
            break
        
        else:
            continue
            


                  
    print "Total answer is: ",total
    print "Correct answer is: ",correct
    print "Wrong answer is: ",wrong
    print "Skip questions: ",skip








#print skip
#print ans.get("python").get(1)

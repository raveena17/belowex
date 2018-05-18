import questions
import tkMessageBox


def Quiz(subject):
    total=10
    correct=0
    wrong=0
    
    print subject
    global questions
    
    for i in range(len(questions.Questions.get(subject))):
        print questions.Questions.get(subject).get(i+1)
        answer=raw_input("Enter the answer: ")
        
        result=questions.ans.get(subject).get(i+1)
        #print result
        
        if result == answer:
            correct += 1

        elif result == "":
            skip += 0
            s
        elif result != answer:
            wrong += 1       # system counting (user skip the questions-> system takes, it's Wrong ans)


    tkMessageBox.showinfo(title="Result", message="Display Your Result !")
    print "\n"
    print "RESULT:"
    print "Total answer is: ",total
    print "Correct answer is: ",correct
    print "Skip answer is: ", skip
    print "Wrong answer is: ",wrong
    


#print ans.get("python").get(1)

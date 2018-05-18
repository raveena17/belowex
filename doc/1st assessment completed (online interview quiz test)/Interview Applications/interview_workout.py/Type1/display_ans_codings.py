import questions


def Quiz(subject):
    total=10
    correct=0
    wrong=0
    print subject

    global questions
    
    for i in range(len(questions.Questions.get(subject))):
        print questions.Questions.get(subject).get(i+1)
        
        ans1=raw_input("Enter the answer: ")
        
        res=questions.python_ans.get(subject).get(i+1)
        #res=questions.java_ans.get(subject).get(i+1)
        if res==ans1:
            correct+=1
        elif res!=ans1:
            wrong+=1       # system counting (user skip the questions-> system takes, it's Wrong ans)

    print "Total answer is: ",total
    print "Correct answer is: ",correct
    print "Wrong answer is: ",wrong


#print ans.get("python").get(1)

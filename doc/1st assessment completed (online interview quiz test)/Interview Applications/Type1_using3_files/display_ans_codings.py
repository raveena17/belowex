import Choice_questions


def Quiz(subject):
    total=10
    correct=0
    wrong=0
    print subject

    global PythonQuestions
    
    for i in range(len(Choice_questions.PythonQuestions.get(subject))):
        print Choice_questions.PythonQuestions.get(subject).get(i+1)
        ans1=raw_input("Enter the answer: ")
        res=Choice_questions.python_ans.get(subject).get(i+1)
        if res==ans1:
            correct+=1
        elif res!=ans1:
            wrong+=1       # system counting (user skip the questions-> system takes, it's Wrong ans)

    print "Total answer is: ",total
    print "Correct answer is: ",correct
    print "Wrong answer is: ",wrong


#print ans.get("python").get(1)

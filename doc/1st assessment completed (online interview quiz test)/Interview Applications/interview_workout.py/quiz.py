import Ques
def Quiz(subject):
    total=10
    correct=0
    wrong=0
    skip=0
    print subject

    global PythonQuestions
    
    for i in range(len(Ques.PythonQuestions.get(subject))):
        print Ques.PythonQuestions.get(subject).get(i+1)
        ans1=raw_input("Enter the answer: ")
        res=Ques.python_ans.get(subject).get(i+1)
        if res==ans1:
            correct+=1
        elif res!=ans1:
            wrong+=1
        else:
            skip+=1

    print "Total answer is: ",total
    print "Correct answer is: ",correct
    print "Wrong answer is: ",wrong


#print skip
#print ans.get("python").get(1)

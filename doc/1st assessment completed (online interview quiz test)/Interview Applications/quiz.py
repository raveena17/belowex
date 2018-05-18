from Question import *
def Quiz():
    total=10
    correct=0
    wrong=0
    skip=0

    for i in range(len(PythonQuestions.get("python"))):
        print PythonQuestions.get("python").get(i+1)
        ans1=raw_input("Enter the answer: ")
        res=ans.get("python").get(i+1)
        if res==ans1:
            correct+=1
        elif res!=ans1:
            wrong+=1
        else:
            skip+=1

    print "Total answer is: ",total
    print "Correct answer is: ",correct
    print "Wrong answer is: ",wrong

Quiz()

#print skip
#print ans.get("python").get(1)

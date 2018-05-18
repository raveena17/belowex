def python_questions():
    correct_ans=0

    print ("Question 1")

    print ("python is a?")
    print "options = a.Development environment,  b.Programming language,  c. Set of editing tools"
    answer = raw_input("write your answer: ")
    answer1 =str(answer)

    if answer == answer1:
       correct_ans = correct_ans + 1

    else:
       correct_ans = correct_ans - 1
       
return correct_ans

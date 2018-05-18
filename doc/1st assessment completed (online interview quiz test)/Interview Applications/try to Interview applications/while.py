def PythonQuestions():
    correct_ans=0
    wrong_ans=0
    print "Question 1-----python is a ?"
    print ("""
    a.Development environment"
    b.Programming language
    c.Set of editing tools
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="b": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #print correct_ans

    print "Question 2-----Which of these statements is true"
    print ("""
        a.CPython is an implementation of python
        b.Pyhon code must be always compiled
        c.Python 1.7 is the most widely used version
        """)
    ans=raw_input("What would you like to do? ") 
    if ans=="a": 
        correct_ans+=1
    else:
        wrong_ans+=1

    print correct_ans
    print wrong_ans

    
PythonQuestions()

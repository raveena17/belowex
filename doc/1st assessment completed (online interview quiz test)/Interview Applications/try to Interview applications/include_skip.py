def PythonQuestions():
    correct_ans=0
    wrong_ans=0
    skip_questions=0

    #question 1
    print "python is a ?"
    print ("""
    a.Development environment"
    b.Programming language
    c.Set of editing tools
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="b": 
        correct_ans+=1
    elif ans=="a" or "b":
        wrong_ans+=1
    else:
        skip_questions+=1

    #print correct_ans
    
        

    #question 2
    print "Which of these statements is true"
    print ("""
        a.CPython is an implementation of python
        b.Pyhon code must be always compiled
        c.Python 1.7 is the most widely used version
        """)
    ans=raw_input("What would you like to do? ") 
    if ans=="a": 
        correct_ans+=1
    elif ans=="b" or "c":
        wrong_ans+=1
    else:
        skip_questions+=1

    #print correct_ans
    #print wrong_ans
    #print skip_question

        
    #question 3
    print "Which line code produces an error?"
    print('''
        a."7"+'eight'
        b.'5'+6
        c. 3+4
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="b": 
        correct_ans+=1
    elif ans=="c" or "a":
        wrong_ans+=1
    else:
        skip_questions+=1

    #question 4
    print "What are anonymous functions called ?"
    print ('''
        a.lamdas
        b.lombdas
        c.lambdas
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="c": 
        correct_ans+=1
    elif ans=="a" or "b":
        wrong_ans+=1
    else:
        skip_questions+=1


    #question 5
    print "What statement is used in funcions to turn them into generators ?"
    print('''
        a.yield
        b.generate
        c.return
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="a": 
        correct_ans+=1
    elif ans=="b" or "c":
        wrong_ans+=1
    else:
        skip_questions+=1


    #question 6
    print "Which of the following data types does not allow duplicate values ?"
    print('''
        a.Dictionaries
        b.Tuples
        c.Sets
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="c": 
        correct_ans+=1
    elif ans=="a" or "b":
        wrong_ans+=1
    else:
        skip_questions+=1
        

    #question 7
    print "What is the result of this code ?"
    print('''
        a.0
        b.1
        c.7
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="b": 
        correct_ans+=1
    elif ans=="c" or "a":
        wrong_ans+=1
    else:
        skip_questions+=1

    #question 8
    print "What type of object is a method ?"
    print ('''
        a.Integer
        b.class
        c.Function
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="c": 
        correct_ans+=1
    elif ans=="a" or "b":
        wrong_ans+=1
    else:
        skip_questions+=1

    #question 9
    print "What error is caused by trying to access unknown attributes ?"
    print ('''
        a.NameError
        b.ValueError
        c.AttributeError
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="c": 
        correct_ans+=1
    elif ans=="a" or "b":
        wrong_ans+=1
    else:
        skip_questions+=1

    #question 10
    print "What is the superclass of a class ?"
    print ('''
        a.The class it inherits from
        b.The class it is an instance of
        c.The first class that inherits from it
        ''')
    ans=raw_input("What would you like to do? ") 
    if ans=="a": 
        correct_ans+=1
    elif ans=="b" or "c":
        wrong_ans+=1
    else:
        skip_questions+=1

    print "How many answer is correct: ",correct_ans
    print "How many answer is Wrong: ",wrong_ans
    print "How many questions are skipped: ",skip_questions
    
        
    
    
PythonQuestions()

#CODINGS:

def PythonQuestions():
    correct_ans=0
    wrong_ans=0

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
    else:
        wrong_ans+=1

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
    else:
        wrong_ans+=1

    #print correct_ans
    #print wrong_ans

        
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
    else:
        wrong_ans+=1

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
    else:
        wrong_ans+=1


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
    else:
        wrong_ans+=1


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
    else:
        wrong_ans+=1
        

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
    else:
        wrong_ans+=1

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
    else:
        wrong_ans+=1

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
    else:
        wrong_ans+=1

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
    else:
        wrong_ans+=1

    print "How many answer is correct: ",correct_ans
    print "How many answer is Wrong: ",wrong_ans
    
        
    
    
PythonQuestions()


#OUTPUT:


python is a ?

    a.Development environment"
    b.Programming language
    c.Set of editing tools
    
What would you like to do? b
Which of these statements is true

        a.CPython is an implementation of python
        b.Pyhon code must be always compiled
        c.Python 1.7 is the most widely used version
        
What would you like to do? a
Which line code produces an error?

        a."7"+'eight'
        b.'5'+6
        c. 3+4
        
What would you like to do? b
What are anonymous functions called ?

        a.lamdas
        b.lombdas
        c.lambdas
        
What would you like to do? c
What statement is used in funcions to turn them into generators ?

        a.yield
        b.generate
        c.return
        
What would you like to do? c
Which of the following data types does not allow duplicate values ?

        a.Dictionaries
        b.Tuples
        c.Sets
        
What would you like to do? b
What is the result of this code ?

        a.0
        b.1
        c.7
        
What would you like to do? a
What type of object is a method ?

        a.Integer
        b.class
        c.Function
        
What would you like to do? c
What error is caused by trying to access unknown attributes ?

        a.NameError
        b.ValueError
        c.AttributeError
        
What would you like to do? c
What is the superclass of a class ?

        a.The class it inherits from
        b.The class it is an instance of
        c.The first class that inherits from it
        
What would you like to do? a
How many answer is correct:  7
How many answer is Wrong:  3

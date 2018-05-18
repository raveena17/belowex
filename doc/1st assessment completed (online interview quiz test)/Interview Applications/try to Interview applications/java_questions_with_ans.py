def JavaQuestions():
    
    Total_questions=10
    correct_ans=0
    wrong_ans=0

    #question 1
    print "1.Can we compare int variable with a boolean variable?"
    print ("""
    a.True
    b.False
    """)
    ans=raw_input("Enter your answer: ") 
    if ans=="b": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #print correct_ans
        

    #question 2
    print "2. What is the size of boolean variable?"
    print ("""
        a.8 bit
        b.16 bit
        C.32 bit

        """)
    ans=raw_input("Enter your answer: ") 
    if ans=="b": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #print correct_ans
    #print wrong_ans

        
    #question 3
    print "3. What is the default value of String variable?"
    print('''
        a. ""
        b. ''
        c. null
        ''')
    ans=raw_input("Enter your answer: ") 
    if ans=="c": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #question 4
    print "4. Which of the following is false about String?"
    print ('''
        a.String is immutable.
        b.String can be created using new operator.
        c.String is a primary data type.
        ''')
    ans=raw_input("Enter your answer:") 
    if ans=="c": 
        correct_ans+=1
    else:
        wrong_ans+=1


    #question 5
    print "5. What is local variable?"
    print('''
        a.Variables defined inside methods, constructors or blocks are called local variables.
        b.Variables defined outside methods, constructors or blocks are called local variables.
        c.Static variables defined outside methods, constructors or blocks are called local variables.

        ''')
    ans=raw_input("Enter your answer: ") 
    if ans=="a": 
        correct_ans+=1
    else:
        wrong_ans+=1


    #question 6
    print "6. What is static block?"
    print('''
        a.It is used to create syncronized code.
        b.There is no such block.
        c.It is used to initialize the static data member., It is excuted before main method at the time of class loading.
        ''')
    ans=raw_input("Enter your answer: ") 
    if ans=="c": 
        correct_ans+=1
    else:
        wrong_ans+=1
        

    #question 7
    print "7. When static binding occurs?"
    print('''
        a.Static binding occurs during Compile time.
        b.Static binding occurs during load time.
        c.Static binding occurs during runtime.
        ''')
    ans=raw_input("Enter your answer:") 
    if ans=="a": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #question 8
    print "8.What is Serialization?"
    print ('''
        a.Serialization is the process of writing the state of an object to another object.
        b.Serialization is the process of writing the state of an object to a byte stream.
        c.Both of the above.

        ''')
    ans=raw_input("Enter your answer:") 
    if ans=="b": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #question 9
    print "9. Can constructor be inherited?"
    print ('''
        a.True.
        b.False.
        ''')
    ans=raw_input("Enter your answer: ") 
    if ans=="b": 
        correct_ans+=1
    else:
        wrong_ans+=1

    #question 10
    print "10.What is a marker interface?"
    print ('''
        a.marker interface is an interface with no method.
        b.marker interface is an interface with single method, mark().
        c.marker interface is an interface with single method, marker().

        ''')
    ans=raw_input("Enter your answer:") 
    if ans=="a": 
        correct_ans+=1
    else:
        wrong_ans+=1
        
    print "Total questions is: ",Total_questions
    print "How many answer is correct: ",correct_ans
    print "How many answer is Wrong: ",wrong_ans

    print"Thanks,Now You Check The Correct Answers: "
    print'''
            question 1---->b
            question 2---->b
            question 3---->c
            question 4---->c
            question 5---->a
            question 6---->c
            question 7---->a
            question 8---->b
            question 9---->b
            question 10---->a
            '''
    
        
    
    
JavaQuestions()



#output:

1.Can we compare int variable with a boolean variable?

    a.True
    b.False
    
Enter your answer: b
2. What is the size of boolean variable?

        a.8 bit
        b.16 bit
        C.32 bit

        
Enter your answer: b
3. What is the default value of String variable?

        a. ""
        b. ''
        c. null
        
Enter your answer: c
4. Which of the following is false about String?

        a.String is immutable.
        b.String can be created using new operator.
        c.String is a primary data type.
        
Enter your answer:c
5. What is local variable?

        a.Variables defined inside methods, constructors or blocks are called local variables.
        b.Variables defined outside methods, constructors or blocks are called local variables.
        c.Static variables defined outside methods, constructors or blocks are called local variables.

        
Enter your answer: a
6. What is static block?

        a.It is used to create syncronized code.
        b.There is no such block.
        c.It is used to initialize the static data member., It is excuted before main method at the time of class loading.
        
Enter your answer: b
7. When static binding occurs?

        a.Static binding occurs during Compile time.
        b.Static binding occurs during load time.
        c.Static binding occurs during runtime.
        
Enter your answer:b
8.What is Serialization?

        a.Serialization is the process of writing the state of an object to another object.
        b.Serialization is the process of writing the state of an object to a byte stream.
        c.Both of the above.

        
Enter your answer:b
9. Can constructor be inherited?

        a.True.
        b.False.
        
Enter your answer: b
10.What is a marker interface?

        a.marker interface is an interface with no method.
        b.marker interface is an interface with single method, mark().
        c.marker interface is an interface with single method, marker().

        
Enter your answer:b
Total questions is:  10
How many answer is correct:  7
How many answer is Wrong:  3
Thanks,Now You Check The Correct Answers

            question 1---->b
            question 2---->b
            question 3---->c
            question 4---->c
            question 5---->a
            question 6---->c
            question 7---->a
            question 8---->b
            question 9---->b
            question 10---->a
            

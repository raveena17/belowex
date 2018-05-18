class Language:

    #def __init__(self, python,java):
        #self.python = python
        #self.java = java
    
    def PythonQuestions(self):

        print "                 [--- Start the Python Questions ---]               "


        Total_questions=10
        correct_ans=0
        wrong_ans=0
        skip_questions=0

        #question 1
        print "1.python is a ?"
        print ("""
        a.Development environment"
        b.Programming language
        c.Set of editing tools
        """)
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
        elif ans=="a":
            wrong_ans+=1
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1


        #print correct_ans
            

        #question 2
        print "2. Which of these statements is true"
        print ("""
            a.CPython is an implementation of python
            b.Pyhon code must be always compiled
            c.Python 1.7 is the most widely used version
            """)
        ans=raw_input("Enter your answer: ") 
        if ans=="a": 
            correct_ans+=1
        elif ans=="b":
            wrong_ans+=1
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1


        #print correct_ans
        #print wrong_ans

            
        #question 3
        print "3. Which line code produces an error?"
        print('''
            a."7"+'eight'
            b.'5'+6
            c. 3+4
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
        elif ans=="c":
            wrong_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1


        #question 4
        print "4. What are anonymous functions called ?"
        print ('''
            a.lamdas
            b.lombdas
            c.lambdas
            ''')
        ans=raw_input("Enter your answer:") 
        if ans=="c": 
            correct_ans+=1
        elif ans=="a":
            wrong_ans+=1
        elif ans=="b":
            wrong_ans+=1
        else:
            skip_questions+=1



        #question 5
        print "5. What statement is used in funcions to turn them into generators ?"
        print('''
            a.yield
            b.generate
            c.return
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="a": 
            correct_ans+=1
        elif ans=="b":
            wrong_ans+=1
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1



        #question 6
        print "6. Which of the following data types does not allow duplicate values ?"
        print('''
            a.Dictionaries
            b.Tuples
            c.Sets
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="c": 
            correct_ans+=1
        elif ans=="a":
            wrong_ans+=1
        elif ans=="b":
            wrong_ans+=1
        else:
            skip_questions+=1

            

        #question 7
        print "7. What is the result of this code ?"
        print('''
            a.0
            b.1
            c.7
            ''')
        ans=raw_input("Enter your answer:") 
        if ans=="b": 
            correct_ans+=1
        elif ans=="c":
            wrong_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1


        #question 8
        print "8. What type of object is a method ?"
        print ('''
            a.Integer
            b.class
            c.Function
            ''')
        ans=raw_input("Enter your answer:") 
        if ans=="c": 
            correct_ans+=1
        elif ans=="b":
            wrong_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1


        #question 9
        print "9. What error is caused by trying to access unknown attributes ?"
        print ('''
            a.NameError
            b.ValueError
            c.AttributeError
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="c": 
            correct_ans+=1
        elif ans=="b":
            wrong_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1


        #question 10
        print "10.What is the superclass of a class ?"
        print ('''
            a.The class it inherits from
            b.The class it is an instance of
            c.The first class that inherits from it
            ''')
        ans=raw_input("Enter your answer:") 
        if ans=="a": 
            correct_ans+=1
        elif ans=="b":
            wrong_ans+=1
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1


        print "Total questions is: ",Total_questions
        print "How many answer is correct: ",correct_ans
        print "How many answer is Wrong: ",wrong_ans
        print "How many questions is skip: ",skip_questions

        print"Thanks,Now You Check The Correct Answers: "
        print'''
                question 1---->b
                question 2---->a
                question 3---->b
                question 4---->c
                question 5---->a
                question 6---->c
                question 7---->b
                question 8---->c
                question 9---->c
                question 10---->a
                '''


    
    def JavaQuestions(self):

        print "                 [--- Start the Java Questions ---]               "
        
        Total_questions=10
        correct_ans=0
        wrong_ans=0
        skip_questions=0

        #question 1
        print "1.Can we compare int variable with a boolean variable?"
        print ("""
        a.True
        b.False
        """)
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1

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
        elif ans=="c":
            wrong_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1

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
        elif ans=="a":
            wrong_ans+=1
        elif ans=="b":
            wrong_ans+=1
        else:
            skip_questions+=1

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
        elif ans=="a":
            wrong_ans+=1
        elif ans=="b":
            wrong_ans+=1
        else:
            skip_questions+=1


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
        elif ans=="b":
            wrong_ans+=1
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1


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
        elif ans=="a":
            wrong_ans+=1
        elif ans=="b":
            wrong_ans+=1
        else:
            skip_questions+=1
            

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
        elif ans=="b":
            wrong_ans+=1
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1

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
        elif ans=="c":
            wrong_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1

        #question 9
        print "9. Can constructor be inherited?"
        print ('''
            a.True.
            b.False.
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
        elif ans=="a":
            wrong_ans+=1
        else:
            skip_questions+=1

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
        elif ans=="b":
            wrong_ans+=1
            
        elif ans=="c":
            wrong_ans+=1
        else:
            skip_questions+=1
            
        print "Total questions is: ",Total_questions
        print "How many answer is correct: ",correct_ans
        print "How many answer is Wrong: ",wrong_ans
        print "How many questions is skip: ",skip_questions

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

m=Language()  #object created
        
def main():


    print "            [--- User Details ---]            "



    user_name = raw_input("Enter the name: ")
    user_qualification = raw_input("Enter the qualification: ")
    user_mailid = raw_input("Enter the  mail-ID: ")
    user_mobile_no = input("Enter the mobile no: ")
    

    """ Employee Detais"""
    
    print("(1) Continue!")
    print("(2) Python")
    print("(3) Java")
    print("(0) Break!  (quit)")
    print()
    
        
    while True:
            
        userchoice=input("Choose an option: ")

        if userchoice == 0:
            break

        elif userchoice == 1:
            continue

        elif userchoice == 2:
            m.PythonQuestions()

        elif userchoice == 3:
            m.JavaQuestions()
        else:
            print(userchoice, "?")
                   

main()
 
        
        




   
    
    

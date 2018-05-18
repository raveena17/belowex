from __future__ import print_function 
import tkMessageBox




class Languages:

    #def __init__(self, python,java):
        #self.python = python
        #self.java = java


    
    
    def PythonQuestions(self):
        
        tkMessageBox.showinfo(title="Python Questions", message="Are you ready, will be Start the Python Questions")

        Wrong_ans_list=[]
        Total_questions=10
        correct_ans=0
        wrong_ans=0
        skip_questions=0

        

        #question 1
        print ("1.python is a ?")
        
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
            x=("Question No 1 == Your answer is a:Development environment, but it's  wrong answer. The correct answer is b:Programming language")
            Wrong_ans_list.append(x)
        
        elif ans=="c":
            wrong_ans+=1
            x=("\n Question No 1 == Your answer is c:Set of editing tools ,but it's  wrong answer. The correct answer is b:Programming language")
            Wrong_ans_list.append(x)
        else:
            skip_questions+=1


        
            

        #question 2
        print ("2. Which of these statements is true")
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
            x=("\n Question No 2 == Your answer is b:Pyhon code must be always compiled, but it's  wrong answer. The correct answer is a:CPython is an implementation of python")
            Wrong_ans_list.append(x)
            
        elif ans=="c":
            wrong_ans+=1
            x=("\n Question No 2 == Your answer is c:Python 1.7 is the most widely used version, but it's  wrong answer. The correct answer is a:CPython is an implementation of python")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1


    

            
        #question 3
        print ("3. Which line code produces an error?")
        print('''
            a.str(7)+'eight'
            b.'5'+6
            c. 3+4
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
        elif ans=="c":
            wrong_ans+=1
            x=("Question No 3 == Your answer is c:3+4, but it's  wrong answer. The correct answer is b:'5'+6")
            Wrong_ans_list.append(x)
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 3 == Your answer is a:str(7)+'eight', but it's  wrong answer. The correct answer is b:'5'+6")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            


        #question 4
        print ("4. What are anonymous functions called ?")
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
            x=("Question No 4 == Your answer is a:lamdas, but it's  wrong answer. The correct answer is c:lambdas")
            Wrong_ans_list.append(x)
            
        elif ans=="b":
            wrong_ans+=1
            x=("Question No 4 == Your answer is b:lombdas, but it's  wrong answer. The correct answer is c:lambdas")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            



        #question 5
        print ("5. What statement is used in funcions to turn them into generators ?")
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
            x=("Question No 5 == Your answer is b:generate, but it's  wrong answer. The correct answer is a:yield")
            Wrong_ans_list.append(x)
            
        elif ans=="c":
            wrong_ans+=1
            x=("Question No 5 == Your answer is c:return, but it's  wrong answer. The correct answer is a:yield")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1




        #question 6
        print ("6. Which of the following data types does not allow duplicate values ?")
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
            x=("Question No 6 == Your answer is a:Dictionaries, but it's  wrong answer. The correct answer is c:Sets")
            Wrong_ans_list.append(x)
            
        elif ans=="b":
            wrong_ans+=1
            x=("Question No 6 == Your answer is b:Tuples, but it's  wrong answer. The correct answer is c:Sets")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1
            

            

        #question 7
        print ("7. What is the result of this code ?")
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
            x=("Question No 7 == Your answer is c:7, but it's  wrong answer. The correct answer is b:1")
            Wrong_ans_list.append(x)
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 7 == Your answer is a:0, but it's  wrong answer. The correct answer is b:1")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            


        #question 8
        print ("8. What type of object is a method ?")
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
            x=("Question No 8 == Your answer is b:class, but it's  wrong answer. The correct answer is  c:Function")
            Wrong_ans_list.append(x)
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 8 == Your answer is a:Integer, but it's  wrong answer. The correct answer is  c:Function")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            


        #question 9
        print ("9. What error is caused by trying to access unknown attributes ?")
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
            x=("Question No 9 == Your answer is b:ValueError, but it's  wrong answer. The correct answer is c:AttributeError")
            Wrong_ans_list.append(x)
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 9 == Your answer is a:NameError,but it's  wrong answer. The correct answer is c:AttributeError")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            


        #question 10
        print ("10.What is the superclass of a class ?")
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
            x=("Question No 10 == Your answer is b:The class it is an instance of, but it's  wrong answer. The correct answer is a:The class it inherits from")
            Wrong_ans_list.append(x)
            
        elif ans=="c":
            wrong_ans+=1
            x=("Question No 10 == Your answer is c:The first class that inherits from it, but it's  wrong answer. The correct answer is a:The class it inherits from")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            
        print(sep='\n\n\n')
        print("RESULT:")
        
        print(sep='\n\n')
        print ("Total questions is: ",Total_questions)
        print(sep='\n\n')

        
        print ("How many answer is correct: ",correct_ans)
        print(sep='\n\n')

        
        print ("How many answer is Wrong: ",wrong_ans)
        print(sep='\n\n')
        
        tkMessageBox.showinfo(title="Wrong Questions details", message="I will show Which Questions is Wrong 'ok' ")
       
        print("WRONG ANSWER LIST:")
        print(sep='\n\n\n')
        
        print(*Wrong_ans_list,sep='\n\n')
        #print Wrong_ans_list
        
        
        print(sep='\n\n')
        print ("How many questions is skip: ",skip_questions)
        print(sep='\n\n')
        
        print("Thanks,Now You Check The Correct Answers: ")
        print(sep='\n\n')
        print('''
                question 1---->b.Programming language
                question 2---->a.CPython is an implementation of python
                question 3---->b.'5'+6
                question 4---->c.lambdas
                question 5---->a.yield
                question 6---->c.Sets
                question 7---->b.1
                question 8---->c.Function
                question 9---->c.AttributeError
                question 10---->a.The class it inherits from
                ''')


    


    def JavaQuestions(self):

        
                              
        tkMessageBox.showinfo(title="Java Questions", message="Are you ready, will be Start the Java Questions!")

        Wrong_ans_list=[]
        Total_questions=10
        correct_ans=0
        wrong_ans=0
        skip_questions=0


        

        #question 1
        print ("1.Can we compare int variable with a boolean variable?")
        print ("""
        a.True
        b.False
        """)
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 1 == Your answer is a:True, but it's  wrong answer. The correct answer is b:False")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            

     

        #question 2
        print ("2. What is the size of boolean variable?")
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
            x=("Question No 2 == Your answer is c:32 bit, but it's  wrong answer. The correct answer is b:16 bit")
            Wrong_ans_list.append(x)
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 2 == Your answer is  a:8 bit, but it's  wrong answer. The correct answer is b:16 bit")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            

       

            
        #question 3
        print ("3. What is the default value of String variable?")
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
            x=("Question No 3 == Your answer is a: "", but it's  wrong answer. The correct answer is  c: null")
            Wrong_ans_list.append(x)
            
        elif ans=="b":
            wrong_ans+=1
            x=("Question No 3 == Your answer is b: '', but it's  wrong answer. The correct answer is  c: null")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            

        #question 4
        print ("4. Which of the following is false about String?")
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
            x=("Question No 4 == Your answer is a:String is immutable., but it's  wrong answer. The correct answer is c:String is a primary data type.")
            Wrong_ans_list.append(x)
            
        elif ans=="b":
            wrong_ans+=1
            x=("Question No 4 == Your answer is b:String can be created using new operator., but it's  wrong answer. The correct answer is c:String is a primary data type.")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            


        #question 5
        print ("5. What is local variable?")
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
            x=("Question No 5 == Your answer is b:Variables defined outside methods, constructors or blocks are called local variables, but it's  wrong answer. The correct answer is a:Variables defined inside methods, constructors or blocks are called local variables")
            Wrong_ans_list.append(x)
            
        elif ans=="c":
            wrong_ans+=1
            x=("Question No 5 == Your answer is c:Static variables defined outside methods, constructors or blocks are called local variables, but it's  wrong answer. The correct answer is a:Variables defined inside methods, constructors or blocks are called local variables")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            


        #question 6
        print ("6. What is static block?")
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
            x=("Question No 6 == Your answer is a:It is used to create syncronized code, but it's  wrong answer. The correct answer is c:It is used to initialize the static data member., It is excuted before main method at the time of class loading.")
            Wrong_ans_list.append(x)
            
        elif ans=="b":
            wrong_ans+=1
            x=("Question No 6 == Your answer is b:There is no such block, but it's  wrong answer. The correct answer is c:It is used to initialize the static data member., It is excuted before main method at the time of class loading.")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            
            

        #question 7
        print ("7. When static binding occurs?")
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
            x=("Question No 7 == Your answer is b:Static binding occurs during load time, but it's  wrong answer. The correct answer is a:Static binding occurs during Compile time")
            Wrong_ans_list.append(x)
            
        elif ans=="c":
            wrong_ans+=1
            x=("Question No 7 == Your answer is c:Static binding occurs during load time, but it's  wrong answer. The correct answer is a:Static binding occurs during Compile time")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1


            

        #question 8
        print ("8.What is Serialization?")
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
            x=("Question No 8 == Your answer is c:Both of the above, but it's  wrong answer. The correct answer is b:Serialization is the process of writing the state of an object to a byte stream")
            Wrong_ans_list.append(x)
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 8 == Your answer is a:Serialization is the process of writing the state of an object to another object, but it's  wrong answer. The correct answer is b:Serialization is the process of writing the state of an object to a byte stream")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1

            

        #question 9
        print ("9. Can constructor be inherited?")
        print ('''
            a.True.
            b.False.
            ''')
        ans=raw_input("Enter your answer: ") 
        if ans=="b": 
            correct_ans+=1
            
        elif ans=="a":
            wrong_ans+=1
            x=("Question No 9 == Your answer is a:True, but it's  wrong answer. The correct answer is b:False")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1


            

        #question 10
        print ("10.What is a marker interface?")
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
            x=("Question No 10 == Your answer is b:marker interface is an interface with single method, mark(), but it's  wrong answer. The correct answer is a:marker interface is an interface with no method")
            Wrong_ans_list.append(x)
            
            
        elif ans=="c":
            wrong_ans+=1
            x=("Question No 10 == Your answer is c:marker interface is an interface with single method, marker(), but it's  wrong answer. The correct answer is a:marker interface is an interface with no method")
            Wrong_ans_list.append(x)
            
        else:
            skip_questions+=1
            

        print(sep='\n\n\n')
        print("RESULT:")
        
        print(sep='\n\n')    
        print ("Total questions is: ",Total_questions)
        print(sep='\n\n')
        
        print ("How many answer is correct: ",correct_ans)
        print(sep='\n\n')
        
        print ("How many answer is Wrong: ",wrong_ans)
        print(sep='\n\n')

        tkMessageBox.showinfo(title="Wrong Questions details", message="I will show Which Questions is Wrong 'ok' ")

        print("WRONG ANSWER LIST:")
        print(sep='\n\n\n')
        
        print(*Wrong_ans_list,sep='\n\n')
        
        #for k in Wrong_ans_list:
            #print k
         

        
        print ("How many questions is skip: ",skip_questions)
        print(sep='\n\n')

        print("Thanks,Now You Check The Correct Answers: ")
        print(sep='\n\n')
         
        print('''
                question 1---->b.False
                question 2---->b.16 bit
                question 3---->c. null
                question 4---->c.String is a primary data type.
                question 5---->a.Variables defined inside methods, constructors or blocks are called local variables.
                question 6---->c.It is used to initialize the static data member., It is excuted before main method at the time of class loading.
                question 7---->a.Static binding occurs during Compile time.
                question 8---->b.Serialization is the process of writing the state of an object to a byte stream.
                question 9---->b.False.
                question 10---->a.marker interface is an interface with no method.
                ''')

m=Languages()  #object created


        
class Mainfunction:
    
    def Userdetails(self):   # it's main function
        

        tkMessageBox.showinfo(title="Greetings", message="Plz Enter Your Details!")

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
                m.PythonQuestions()   #function call
                break

            elif userchoice == 3:
                m.JavaQuestions()     #function call
                break
            else:
                print(userchoice, "?")
                       

k=Mainfunction()   #another class create a object "k"


k.Userdetails()   # main function call
 
        
        


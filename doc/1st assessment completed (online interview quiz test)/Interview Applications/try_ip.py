from __future__ import print_function

class Languages:

    #def __init__(self, python,java):
        #self.python = python
        #self.java = java


    
    
    def PythonQuestions(self):
        
        #tkMessageBox.showinfo(title="Python Questions", message="Are you ready, will be Start the Python Questions")

        Wrong_ans_list=[]
        Total_questions=10
        correct_ans=0
        wrong_ans=0
        skip_questions=0
        
        

        A=1
        x="1.python is a ?"
        
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


        
            

        B=2
        x="2. Which of these statements is true"
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


    

            
        C=3
        x="3. Which line code produces an error?"
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

            


        D=4
        x="4. What are anonymous functions called ?"
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

            

        =5
        x="5. What statement is used in funcions to turn them into generators ?"
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


        
        print("RESULT:")
        print ("Total questions is: ",Total_questions)
        print ("How many answer is correct: ",correct_ans)
        print ("How many answer is Wrong: ",wrong_ans)
        print("WRONG ANSWER LIST:")
        print(*Wrong_ans_list,sep='\n\n')
        print ("How many questions is skip: ",skip_questions)
        print("Thanks,Now You Check The Correct Answers: ")
        
m=Languages()  #object created


        
class Mainfunction:
    
    def Userdetails(self):   # it's main function
        

        tkMessageBox.showinfo(title="Details", message="Plz Enter Your Details!")

        user_name = raw_input("Enter the name: ")
        user_qualification = raw_input("Enter the qualification: ")
        user_mailid = raw_input("Enter the  mail-ID: ")
        user_mobile_no = input("Enter the mobile no: ")
        

        """ Employee Detais"""
        print("(1) Python")
        print("(2) Java")
        
            
        while True:
                
            userchoice=input("Choose an option: ")
            
            if userchoice == 1:
                m.PythonQuestions()   #function call
                break

            elif userchoice == 2:
                m.JavaQuestions()     #function call
                break
            else:
                break
                       

k=Mainfunction()   #another class create a object "k"


k.Userdetails()   # main function call
 
        
        



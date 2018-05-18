import display_ans_codings1
import tkMessageBox


class Student:


    def __init__(self, total,correct, wrong):
        self.total = total
        self.correct = correct
        self.wrong = wrong
    
    def Userdetails(self):   # it's main function
        
        global subject
        
       
        tkMessageBox.showinfo(title="UserDetais", message="Plz Enter Your Details!")
        user_name = raw_input("Enter the name: ")
        user_qualification = raw_input("Enter the qualification: ")
        user_mailid = raw_input("Enter the  mail-ID: ")
        user_mobile_no = input("Enter the mobile no: ")


        
        
        tkMessageBox.showinfo(title="Language", message="Language Display")
        print("(1) Python")
        print("(2) Java")

        
        
            
        while True:
                
            userchoice=input("Choose an Language: ")

            
            if userchoice == 1:
                subject="python"
                display_ans_codings1.Quiz(subject)
                break

            if userchoice == 2:
                subject="Java"
                display_ans_codings1.Quiz(subject)
                break
            
            else:
                print(userchoice, "?")
                       

result = Student(10,0,0)
result.Userdetails()  # main function call
 
        
        


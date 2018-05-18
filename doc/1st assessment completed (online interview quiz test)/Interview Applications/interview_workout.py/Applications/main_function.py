import display_ans_codings

class Student:
    

    def __init__(self,  username, qualification ):
        self.username = username
        self.qualification = qualification
    
    def Userdetails(self):   # it's main function
        
        global subject
        
       

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
                subject="python"
                display_ans_codings.Quiz(subject)
                break

            if userchoice == 2:
                subject="Java"
                display_ans_codings.Quiz(subject)
                break
            
            else:
                print(userchoice, "?")
                       

mathu = Student('mathu', 'BE')
mathu.Userdetails()  # main function call
 
        
        


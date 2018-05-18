class Exam:
    

    def __init__(self, correct, wrong, skip):
        self.correct=correct
        self.wrong=wrong
        self.skip=skip
        
    
    def UserDetails(self):   # it's main function

        user_name = raw_input("Enter the name: ")
        user_qualification = raw_input("Enter the qualification: ")
        user_mailid = raw_input("Enter the  mail-ID: ")
        user_mobile_no = input("Enter the mobile no: ")
        userchoice_ques = raw_input("Choose which question: ")
        if userchoice_ques == 'Python':
               Test(python_questions)
                    
        elif userchoice_ques == 'Java':
                Test(java_questions)




a=Exam()
a.UserDetails()

class Languages:

    def __init__(self,total=10, correct=0, wrong=0, skip=0):
        self.total=total
        self.correct=correct
        self.wrong=wrong
        self.skip=skip


    
    

   m=Languages()  #object created


        
class Mainfunction:
    
    def Userdetails(self):   # it's main function
        

        tkMessageBox.showinfo(title="Details", message="Plz Enter Your Details!")

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
 
        
        


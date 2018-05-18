def main_UserDetails():
    user_name = raw_input("Enter the user name: ")
    user_qualification = raw_input("Enter the user qualification: ")
    user_mailid = raw_input("Enter the user mail-ID: ")
    

    """ Employee Detais"""
    #class object creat
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

        #elif userchoice == 2:

            

            
        #elif userchoice == 3:


            

        else:
            print(userchoice, "?")
               

main_UserDetails()

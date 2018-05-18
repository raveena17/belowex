def keep_going():
    answer = raw_input("Do you wish to continue?")
    if answer == "yes":
        print "You have chosen to continue on"
        return "keep going"
    else:
        print "You have chosen to quit this program"
        return "please exit"

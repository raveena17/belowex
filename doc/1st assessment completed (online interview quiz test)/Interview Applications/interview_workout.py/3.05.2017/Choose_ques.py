class Scores:
    

    def __init__(self,correct, wrong,skip ):
        self.correct = correct
        self.wrong = wrong
        self.skip = skip

    def Validate(self):# answer validation
        
	#correct, wrong, skip = 0, 0, 0
	for qus_no, qus in questions.iteritems():
		valid = True
		print str(qus_no) + ':' + qus['QUS'] 
		for opt, ans in qus['OPTIONS'].iteritems():
			print opt + ':' + ans
		while valid:
			ans = raw_input("Choose your answer: ")
			if ans in qus['OPTIONS'].keys():
				valid = False
			elif ans == "":
				valid = False
			else:
				tkMessageBox.showinfo(title="INVALID OPTION", message="Plz check Your option!")
		if ans == qus['ANS']:
			correct += 1 
		elif ans == "":
			skip += 1		
		else:
			wrong += 1

        
	print "\n RESULT:"
	print "Total Questions: 10"
	print "Correct Answer: " + str(correct)
	print "Wrong Answer: " + str(wrong)
	print "Skip Questions: " + str(skip)

	

    def start_test(self):
        
        tkMessageBox.showinfo(title="UserDetais", message="Plz Enter Your Details!")
        user_name = raw_input("Enter the name: ")
        user_qualification = raw_input("Enter the qualification: ")
        user_mailid = raw_input("Enter the  mail-ID: ")
        user_mobile_no = input("Enter the mobile no: ")
        
        print 'Languages  :  Python ,Java'
        userchoice_ques = raw_input("Choose which language: ")
        
        if userchoice_ques == 'Python':
             Validate(python_questions)
                    
        elif userchoice_ques == 'Java':
             Validate(java_questions)

   
            
            
Student = Scores(0,0,0)
Student.start_test()

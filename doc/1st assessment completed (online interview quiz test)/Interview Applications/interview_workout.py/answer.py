import questions

def Test(questions):
	correct, wrong, skip = 0, 0, 0
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
				print "INVALID OPTION"
		if ans == qus['ANS']:
			correct += 1 
		elif ans == "":
			skip += 1		
		else:
			wrong += 1
	print "Correct: " + str(correct)
	print "Wrong: " + str(wrong)
	print "Skip: " + str(skip)

##print "Choose which question?"
##print "A: Python"
##print "B: Java"	
##language = raw_input("Choose your language: ")
##if language == 'A':
##	Test(python_questions)
##elif language == 'B':
##	Test(java_questions)
##

python_questions = {
	1 : {
		'QUS': 'Who are you?',
		'OPTIONS': {
			'A': 'hi',
			'B': 'Raveena'
		},
		'ANS': 'B'
	},
	2 : {
		'QUS': 'Who are you?',
		'OPTIONS': {
			'A': 'hi',
			'B': 'Raveena'
		},
		'ANS': 'B'
	},
	3 : {
		'QUS': 'Who are you?',
		'OPTIONS': {
			'A': 'hi',
			'B': 'Raveena'
		},
		'ANS': 'B'
	}		
}

java_questions = {
	1 : {
		'QUS': 'F are you?',
		'OPTIONS': {
			'A': 'q',
			'B': 'hi'
		},
		'ANS': 'B'
	},
	2 : {
		'QUS': 'F are you?',
		'OPTIONS': {
			'A': 'a',
			'B': 'hi'
		},
		'ANS': 'B'
	},
	3 : {
		'QUS': 'F are you?',
		'OPTIONS': {
			'A': 'd',
			'B': 'hi'
		},
		'ANS': 'B'
	}		
}

def exam(questions):
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

print "Choose which question?"
print "A: Python"
print "B: Java"	
q = raw_input("Choose your answer: ")
if q == 'A':
	exam(python_questions)
elif q == 'B':
	exam(java_questions)

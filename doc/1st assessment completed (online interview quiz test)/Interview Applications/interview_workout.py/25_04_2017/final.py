python_questions = {
                    
	1 : {
		'QUS': 'python is a ?',
		'OPTIONS': {
			'A': 'Development environment',
			'B': 'Programming language',
                        'C': 'Set of editing tools'
		},
		'ANS': 'B'
	},
	2 : {
		'QUS': ' Which of these statements is true',
		'OPTIONS': {
			'A': 'CPython is an implementation of python',
			'B': 'Pyhon code must be always compiled',
                        'C': 'Python 1.7 is the most widely used version'
		},
		'ANS': 'A'
	},
	3 : {
		'QUS': 'Which line code produces an error?',
		'OPTIONS': {
			'A': 'str(7)+str(eight)',
			'B': 'str(5)+6',
                        'C': '3+4',
		},
		'ANS': 'B'
	},
        4 : {
		'QUS': 'What are anonymous functions called',
		'OPTIONS': {
			'A': 'lamdas',
			'B': 'lombdas',
                        'C': 'lambdas'
		},
		'ANS': 'C'
	},
        5 : {
		'QUS': 'What statement is used in funcions to turn them into generators',
		'OPTIONS': {
			'A': 'yield',
			'B': 'generate',
                        'C': 'return'
		},
		'ANS': 'A'
	},
        6 : {
		'QUS': 'Which of the following data types does not allow duplicate values',
		'OPTIONS': {
			'A': 'Dictionaries',
			'B': 'Tuples',
                        'C': 'Sets'
		},
		'ANS': 'C'
	},
        7 : {
		'QUS': 'What is the result of this code ?',
		'OPTIONS': {
			'A': '0',
			'B': '1',
                        'C': '7'
		},
		'ANS': 'B'
	},
        8 : {
		'QUS': 'What type of object is a method ?',
		'OPTIONS': {
			'A': 'Integer',
			'B': 'class',
                        'C': 'Function'
		},
		'ANS': 'C'
	},
        9 : {
		'QUS': 'What error is caused by trying to access unknown attributes ?',
		'OPTIONS': {
			'A': 'NameError',
			'B': 'ValueError',
                        'C': 'AttributeError'
		},
		'ANS': 'C'
	},
        10 : {
		'QUS': 'What is the superclass of a class ?',
		'OPTIONS': {
			'A': 'The class it inherits from',
			'B': 'The class it is an instance of',
                        'C': 'The first class that inherits from it'
		},
		'ANS': 'A'
	}
            
}

java_questions = {
                    
	1 : {
		'QUS': 'Can we compare int variable with a boolean variable?',
		'OPTIONS': {
			'A': 'True ',
			'B': 'False'
                },
		'ANS': 'B'
	},
	2 : {
		'QUS': 'What is the size of boolean variable?',
		'OPTIONS': {
			'A': '8 bit',
			'B': '16 bit',
                        'C': '32 bit'
		},
		'ANS': 'B'
	},
	3 : {
		'QUS': 'What is the default value of String variable?',
		'OPTIONS': {
			'A': '""',
			'B': '', 
                        'C': 'null'
		},
		'ANS': 'C'
	},
        4 : {
		'QUS': 'Which of the following is false about String?',
		'OPTIONS': {
			'A': 'String is immutable',
			'B': 'String can be created using new operator',
                        'C': 'String is a primary data type'
		},
		'ANS': 'C'
	},
        5 : {
		'QUS': 'What is local variable?',
		'OPTIONS': {
			'A': 'Variables defined inside methods, constructors or blocks are called local variables',
			'B': 'Variables defined outside methods, constructors or blocks are called local variables',
                        'C': 'Static variables defined outside methods, constructors or blocks are called local variables'
		},
		'ANS': 'A'
	},
        6 : {
		'QUS': 'What is static block?',
		'OPTIONS': {
			'A': 'It is used to create syncronized code',
			'B': 'There is no such block',
                        'C': 'It is used to initialize the static data member,It is excuted before main method at the time of class loading'
		},
		'ANS': 'C'
	},
        7 : {
		'QUS': 'When static binding occurs?',
		'OPTIONS': {
			'A': 'Static binding occurs during Compile time',
			'B': 'Static binding occurs during load time',
                        'C': 'Static binding occurs during runtime'
		},
		'ANS': 'A'
	},
        8 : {
		'QUS': 'What is Serialization?',
		'OPTIONS': {
			'A': 'Serialization is the process of writing the state of an object to another object',
			'B': 'Serialization is the process of writing the state of an object to a byte stream',
                        'C': 'Both of the above'
		},
		'ANS': 'B'
	},
        9 : {
		'QUS': 'Can constructor be inherited?',
		'OPTIONS': {
			'A': 'True',
			'B': 'False'
                    
		},
		'ANS': 'B'
	},
        10 : {
		'QUS': 'What is the superclass of a class ?',
		'OPTIONS': {
			'A': 'marker interface is an interface with no method',
			'B': 'marker interface is an interface with single method, mark()',
                        'C': 'marker interface is an interface with single method, marker()'
		},
		'ANS': 'A'
	}
            
}


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

print "Choose which question?"
print "A: Python"
print "B: Java"	
q = raw_input("Choose your answer: ")
if q == 'A':
	Test(python_questions)
elif q == 'B':
	Test(java_questions)







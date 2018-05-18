python_questions = {
                        
            '1' : {
                    'QUS': '1. python is a ?',
                    'OPTIONS': {
                            'A': 'Development environment',
                            'B': 'Programming language',
                            'C': 'Set of editing tools'
                    },
                    'ANS': 'B'
            },
            '2' : {
                    'QUS': '2. Which of these statements is true',
                    'OPTIONS': {
                            'A': 'CPython is an implementation of python',
                            'B': 'Pyhon code must be always compiled',
                            'C': 'Python 1.7 is the most widely used version'
                    },
                    'ANS': 'A'
            },
            '3' : {
                    'QUS': '3. Which line code produces an error?',
                    'OPTIONS': {
                            'A': 'str(7)+str(eight)',
                            'B': 'str(5)+6',
                            'C': '3+4',
                    },
                    'ANS': 'B'
            },
            '4' : {
                    'QUS': '4. What are anonymous functions called',
                    'OPTIONS': {
                            'A': 'lamdas',
                            'B': 'lombdas',
                            'C': 'lambdas'
                    },
                    'ANS': 'C'
            },
            '5' : {
                    'QUS': '5. What statement is used in funcions to turn them into generators',
                    'OPTIONS': {
                            'A': 'yield',
                            'B': 'generate',
                            'C': 'return'
                    },
                    'ANS': 'A'
            },
            '6' : {
                    'QUS': '6. Which of the following data types does not allow duplicate values',
                    'OPTIONS': {
                            'A': 'Dictionaries',
                            'B': 'Tuples',
                            'C': 'Sets'
                    },
                    'ANS': 'C'
            },
            '7' : {
                    'QUS': '7. What is the result of this code ?',
                    'OPTIONS': {
                            'A': '0',
                            'B': '1',
                            'C': '7'
                    },
                    'ANS': 'B'
            },
            '8' : {
                    'QUS': '8. What type of object is a method ?',
                    'OPTIONS': {
                            'A': 'Integer',
                            'B': 'class',
                            'C': 'Function'
                    },
                    'ANS': 'C'
            },
            '9' : {
                    'QUS': '9. What error is caused by trying to access unknown attributes ?',
                    'OPTIONS': {
                            'A': 'NameError',
                            'B': 'ValueError',
                            'C': 'AttributeError'
                    },
                    'ANS': 'C'
            },
            '10' : {
                    'QUS': '10. What is the superclass of a class ?',
                    'OPTIONS': {
                            'A': 'The class it inherits from',
                            'B': 'The class it is an instance of',
                            'C': 'The first class that inherits from it'
                    },
                    'ANS': 'A'
            }
                
    }

java_questions = {
                        
            '1' : {
                    'QUS': '1. Can we compare int variable with a boolean variable?',
                    'OPTIONS': {
                            'A': 'True ',
                            'B': 'False'
                    },
                    'ANS': 'B'
            },
            '2' : {
                    'QUS': '2. What is the size of boolean variable?',
                    'OPTIONS': {
                            'A': '8 bit',
                            'B': '16 bit',
                            'C': '32 bit'
                    },
                    'ANS': 'B'
            },
            '3' : {
                    'QUS': '3. What is the default value of String variable?',
                    'OPTIONS': {
                            'A': '""',
                            'B': '', 
                            'C': 'null'
                    },
                    'ANS': 'C'
            },
            '4' : {
                    'QUS': '4. Which of the following is false about String?',
                    'OPTIONS': {
                            'A': 'String is immutable',
                            'B': 'String can be created using new operator',
                            'C': 'String is a primary data type'
                    },
                    'ANS': 'C'
            },
            '5' : {
                    'QUS': '5. What is local variable?',
                    'OPTIONS': {
                            'A': 'Variables defined inside methods, constructors or blocks are called local variables',
                            'B': 'Variables defined outside methods, constructors or blocks are called local variables',
                            'C': 'Static variables defined outside methods, constructors or blocks are called local variables'
                    },
                    'ANS': 'A'
            },
            '6' : {
                    'QUS': '6. What is static block?',
                    'OPTIONS': {
                            'A': 'It is used to create syncronized code',
                            'B': 'There is no such block',
                            'C': 'It is used to initialize the static data member,It is excuted before main method at the time of class loading'
                    },
                    'ANS': 'C'
            },
            '7' : {
                    'QUS': '7. When static binding occurs?',
                    'OPTIONS': {
                            'A': 'Static binding occurs during Compile time',
                            'B': 'Static binding occurs during load time',
                            'C': 'Static binding occurs during runtime'
                    },
                    'ANS': 'A'
            },
            '8' : {
                    'QUS': '8. What is Serialization?',
                    'OPTIONS': {
                            'A': 'Serialization is the process of writing the state of an object to another object',
                            'B': 'Serialization is the process of writing the state of an object to a byte stream',
                            'C': 'Both of the above'
                    },
                    'ANS': 'B'
            },
            '9' : {
                    'QUS': '9. Can constructor be inherited?',
                    'OPTIONS': {
                            'A': 'True',
                            'B': 'False'
                        
                    },
                    'ANS': 'B'
            },
            '10' : {
                    'QUS': '10. What is the superclass of a class ?',
                    'OPTIONS': {
                            'A': 'marker interface is an interface with no method',
                            'B': 'marker interface is an interface with single method, mark()',
                            'C': 'marker interface is an interface with single method, marker()'
                    },
                    'ANS': 'A'
            }
                
    }


class Attendee:
        def __init__(self, name, language):
                self.name = name
                self.language = language
                
                if self.language == "python":
                        self.questions = python_questions
                else:
                        self.questions = java_questions
                        
                self.current_question = '1'
                self.correct_answers = 0
                self.wrong_answers = 0
                self.skiped_questions = 0
                

                
        def start(self):
               
               print self.questions[self.current_question]['QUS']
               for op_key , key_val in self.questions[self.current_question]['OPTIONS'].iteritems():
                   print op_key + ':' + key_val

               ans = raw_input("Enter your answer: ")
               print ("N --> Next questions / P --> Previous questions / finish --> submit")
               move = raw_input("Move the question: ")
               
               if move == "N":
                   self.next()
               elif move == "P":
                   self.previous()
               elif ans == "S":
                   self.skiped_questions += 1
               elif move == "submit":
                   self.submit()
               elif ans == self.questions[self.current_question]['ANS']:
                   self.correct_answers += 1
               else:
                   self.wrong_answers += 1

        
        def next(self):
                self.current_question = str(int(self.current_question)+1)
                self.start()
            
        def previous(self):
                self.current_question = str(int(self.current_question)-1)
                self.start()

        def submit(self):
                print "correct_answers: ", self.correct_answers
                print "wrong_answers: ", self.wrong_answers
                print "skiped_questions: ", self.skiped_questions
            

    
        

raveena = Attendee("raveena","python")
raveena.start()

        

































                     

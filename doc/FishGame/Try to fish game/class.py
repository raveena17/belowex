class Arithmetic():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
            
    def __add__(self):
        #print("Addition = {0}+{1}".format(self.a,self.b))
        x = self.a+self.b
        return x

    def __sub__(self):
        #print("Subtraction = {0}-{1}".format(self.a,self.b))
        x = self.a-self.b
        return x


    def __mul__(self):
        #print("Multiplication = {0}*{1}".format(self.a,self.b))
        x = self.a*self.b
        return x


    def __div__(self):
        #print("Divition = {0}/{1}".format(self.a,self.b))
        x = self.a/self.b
        return x


def main():
        """Arithmetic operation"""
        m= Arithmetic(25,5)                   # m is a object
        print("(0) Continue!")
        print("(1) __add__")
        print("(2) __sub__")
        print("(3) __mul__")
        print("(4) __div__")
        print("(5) Break!  (quit)")
        print()
    
        
        while True:
            
            
            userchoice=input("Choose an option: ")

            if userchoice == 5:
                break

            elif userchoice == 0:
                continue

            elif userchoice == 1:
                a = m.__add__()
                print("Adding two value:",a)

            elif userchoice == 2:
                b = m.__sub__()
                print("Subtraction two value:",b)

            elif userchoice == 3:
                c = m.__mul__()
                print("Multiplication two value:",c)

            elif userchoice == 4:
                d = m.__div__()
                print("Division two value:",d)

            else:
                print(userchoice, "?")

        print()
        print("Thank you")



#OUTPUT:


>>> main()
(0) Continue!
(1) __add__
(2) __sub__
(3) __mul__
(4) __div__
(5) Break!  (quit)
()
Choose an option: 0
Choose an option: 1
Addition = 25+5
('Adding two value:', 30)
Choose an option: 2
Subtraction = 25-5
('Subtraction two value:', 20)
Choose an option: 3
Multiplication = 25*5
('Multiplication two value:', 125)
Choose an option: 4
Divition = 25/5
('Division two value:', 5)
Choose an option: 5
()
Thank you
>>> 







#(prgm):
class MyClass(object):  


    def greet(self):
        print("Hello World")


class MyNextClass(object):

    def greetAgain(self):
        print("Hello again")

#Now I can import this module from anywhere I wish

import Classes

if __name__ == '__main__':

    a=Classes.MyClass()
    a.greet()

    b=Classes.MyNextClass()
    b.greetAgain()





    

def operation():
    """Arithmetic operation"""
    print("(0) Continue!")
    print("(1) Addition")
    print("(2) Subtraction")
    print("(3) Multiplication")
    print("(4) Division")
    print("(5) Break!  (quit)")
    print()



def Addition(x,y):
    return x+y

def Subtraction(x,y):
    return x-y

def Multiplication(x,y):
    return x*y

def Division(x,y):
    return x/y

def main():
    #initial x value and y valu
    x=8
    y=5

    while True:
        print ("x and y value",x,y)
        operation()
        userchoice=input("Choose an option: ")

        if userchoice == 5:
            break

        elif userchoice == 0:
            continue

        elif userchoice == 1:
            a = Addition(x,y)
            print("Adding two value:",a)

        elif userchoice == 2:
            b = Subtraction(x,y)
            print("Subtraction two value:",b)

        elif userchoice == 3:
            c = Multiplication(x,y)
            print("Multiplication two value:",c)

        elif userchoice == 4:
            d = Division(x,y)
            print("Division two value:",d)

        else:
            print(userchoice, "?")

    print()
    print("Thank you")





#OUTPUT:


>>> main()
('x and y value', 8, 5)
(0) Continue!
(1) Addition
(2) Subtraction
(3) Multiplication
(4) Division
(5) Break!  (quit)
()
Choose an option: 0
('x and y value', 8, 5)
(0) Continue!
(1) Addition
(2) Subtraction
(3) Multiplication
(4) Division
(5) Break!  (quit)
()
Choose an option: 1
('Adding two value:', 13)
('x and y value', 8, 5)
(0) Continue!
(1) Addition
(2) Subtraction
(3) Multiplication
(4) Division
(5) Break!  (quit)
()
Choose an option: 4
('Division two value:', 1)
('x and y value', 8, 5)
(0) Continue!
(1) Addition
(2) Subtraction
(3) Multiplication
(4) Division
(5) Break!  (quit)
()
Choose an option: 2
('Subtraction two value:', 3)
('x and y value', 8, 5)
(0) Continue!
(1) Addition
(2) Subtraction
(3) Multiplication
(4) Division
(5) Break!  (quit)
()
Choose an option: 3
('Multiplication two value:', 40)
('x and y value', 8, 5)
(0) Continue!
(1) Addition
(2) Subtraction
(3) Multiplication
(4) Division
(5) Break!  (quit)
()
Choose an option: 5
()
Thank you

"""
    *Python Calculator
    
    *Matt Chupp

    *Last Edited -- 5/2/14

"""

def add(x , y):

    return x + y

def sub(x, y):

    return x - y

def mult(x, y):

    return x * y

def div(x, y):

    return x / y


# get user input

num1 = float(raw_input("Enter a number "))
num2 = float(raw_input("Enter a number "))

sign = raw_input("Enter an operator < + - / * > ")


if sign == '+':
    total = add(num1, num2)

    print total

elif sign == '-':
    total = sub(num1, num2)

    print total

elif sign == '*':
    total = mult(num1, num2)

    print total

elif sign == '/':
    total = div(num1, num2)

    print total

else:
    print "***Invalid Operator***"
    
    





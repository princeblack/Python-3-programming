import random
def randgww(ttt):
    for i in range(5):
        print(random.randint(10, 50))

def game():
    count=0
    secret_number = random.randint(1,20)
    print('I am currently thinking of a Number.')
    print(secret_number)
    for i in range(1,4):
        print('Try to guess the number!')
        guess = int(input('Enter number Between 1 and 20:  '))
        if secret_number == guess:
            print('Wow you Winn!!!!!!')
            break
        else:
            count = count +1
            if count == 3:
                print('You are Loser')
                break
            print('sorry try again')

def reverse_string(string):
    print(string[::-1])

# area of a circle

def Radius_circle():
    while True:
        red = input('Enter Radius of Circle: ')
        if red == 'x':
            break
        else:
            redius = float(red)
            area = 3.14 * redius * redius
            print(str(redius) + ' result')

# simple Python calculator
def calculator (num1,symbol,num2):

    if symbol == "+":
        print(num1 + num2)
    elif symbol == "-":
        print(num1 - num2)
    elif symbol == "*":
        print( num1 * num2)
    elif symbol == "/":
        print(num1 / num2)
calculator(1500,'/',6)

def calculator_promt():
    print("+ :  Addition")
    print("- :  Subtraction")
    print("* :  multiplication")
    print("/ :  Division")
    try:
        num = int(input("First Number : "))
        signe = input("What to do ? (+) (-) (*) (/): ")
        num2 = int(input("Seconde Number : "))
    except ValueError:
        print("you didn't give any value")
    except TypeError:
        print("The value is not Number")
    try:
        if  signe == "+":
           print("{}{}{}".format(num,signe,num2) + "= " + format(num + num2))
        elif signe == "-":
           print("{}{}{}".format(num,signe,num2) + "= " + format(num - num2))
        elif signe == "*":
           print("{}{}{}".format(num,signe,num2) + "= " + format(num * num2))
        elif signe == "/":
           print("{}{}{}".format(num,signe,num2) + "= " + format(num / num2))
        elif signe != '+' and '-' and '*' and '/' :
            print("test")
    except ZeroDivisionError:
        print(" the  Number  can't be calculed")

calculator_promt()

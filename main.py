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

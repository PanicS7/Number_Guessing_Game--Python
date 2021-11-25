import random
def numberGuessingGame():
    '''This is a simple game, where a program randomly chooses 1 number. And the goal of the player is to guess this number.
    '''
    secretNumber = random.randint(1,10)
    userNumber = int(input("Please enter a number from 1 to 10: "))
    correct = False
    while (correct == False):
        if(userNumber == secretNumber):
            return "You find a secret number!!!"
            correct = True
        elif(userNumber < secretNumber):
            userNumber = int(input("Enter bigger number: "))
        elif(userNumber > secretNumber):
            userNumber = int(input("Enter smaller number: "))
        else:
            pass
    
    return secretNumber
    
print(numberGuessingGame())

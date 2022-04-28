#rock paper scissors game with functions

import random

def User_options():
    print("Enter your choice:\n 1 for Rock\n 2 for paper\n 3 for scissor \n")

def ComputerRandomNumberGen():
    computer_choice = random.randint(1, 3)
    return computer_choice

def displayUserChoice(userChoice):
    if userChoice == 1:
        print("User choice : Rock")
    elif userChoice == 2:
        print("User choice : Paper")
    elif userChoice == 3:
        print("User choice : Scissors")
    else:
        print("Invalid User Choice")

def displayComputerChoice(computerChoice):
    if computerChoice == 1:
        print("Computer choice : Rock")
    elif computerChoice == 2:
        print("Computer choice : Paper")
    elif computerChoice == 3:
        print("Computer chooice : Scissors")

def userinformation():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    phonenumber = input("Enter your phonenumber: ")
    return name, age, address, phonenumber

def displayUserInfo(name, age, address, phonenumber): #to display if user wins
    print("Name : {}".format(name))
    print("Age : {}".format(age))
    print("Address : {}".format(address))
    print("Phone number : {}".format(phonenumber))

def DetermineWinnerofRPS():
    count = 0 #for returning to main function
    userChoice = int(input("Enter your choice: "))
    computerChoice = ComputerRandomNumberGen()
    displayUserChoice(userChoice)
    displayComputerChoice(computerChoice)
    if userChoice != computerChoice:
        if userChoice == 1 and computerChoice == 2:
            print("Computer wins\n")
        elif userChoice == 2 and computerChoice == 3:
            print("Computer wins\n")
        elif userChoice == 3 and computerChoice == 1:
            print("Computer wins\n")
        elif userChoice == 1 and computerChoice == 3:
            print("User with the following information wins\n")
            count = count + 1 #only increment if user wins
        elif userChoice == 2 and computerChoice == 1:
            print("User with the following information wins\n")
            count = count + 1 #only increment if user wins
        elif userChoice == 3 and computerChoice == 2:
            print("User with the following information wins\n")
            count = count + 1 #only increment if user wins
        return count

    else:
        print("It is a tie. The game continues.\n")
        User_options()
        DetermineWinnerofRPS()

def main():
    print("\n\t\t\t\tThis is a Rock-Paper-Scissor game.\t\t\t")
    User_options()
    name, age, address, phonenumber = userinformation()
    count = DetermineWinnerofRPS() #return count value if user have won
    if count > 0: # this qualifies if the user has won, if so then displays user information 
        displayUserInfo(name, age, address, phonenumber)

main()

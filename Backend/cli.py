'''
Imports functions from api.py and allows the user to run them on the command line
'''
from api import *

energy = EnergyProductionAPI()

'''
The command line program should allow the user to keep selecting functions until they decide to quit.
what data will be expected by each function, in what format, etc. It should also demonstrate what data the function calls will return (and in what format).
'''
functionNames = ["(1) getEnergyForState : \n     Sums all electricity generation by all catagories in a given state",
                 "(2) getTotalRenewableEnergyByState : \n     Sums and returns the total amount of renewable energy throughout the year for a given state",
                 "(3) getTotalEnergyForStateByMonth : \n     Retrieves monthly total electricity generation throughout the year for a given state",
                 "(4) getEnergyByCategoryForState : \n     Returns the total renewable energy by category of renewable energy for a specified state"]

# displays a list of possible functions and how to properly call them
while (1):
    print("*Note: all numerical return values for energy production will be floats in thousand megawatt hours*\nPlease enter one of the following numbers corresponding to a function name: \n ---")
    for function in functionNames:
        print(function)

    print("---")
    print("Note: type 'exit' to stop the program")

    # scan user's inputs
    userInput = input()

    # if input is valid, call the specified function
    if userInput in ['1', '2', '3', '4']:
        # conditional ladder where each corresponds to a respective function call
        if userInput == "1":
            userInputedState = input(
                "This function takes a state as a string parameter and returns the total energy generated in that state as an int. \nPlease enter a US state abbreviation: ")
            print(energy.getEnergyForState(userInputedState))

        elif userInput == "2":
            userInputedState = input(
                "This function takes a state as a string parameter returns the total energy generated via renewable sources in the specified state as an int. \nPlease enter a US state abbreviation: ")
            print(energy.getTotalRenewableEnergyByState(
                userInputedState))

        elif userInput == "3":
            userInputedState = input(
                "This function takes a state as a string parameter and returns a list where the values are the total energy produced for each month in the specified state. \nPlease enter a US state abbreviation: ")
            print(energy.getTotalEnergyForStateByMonth(
                userInputedState))

        elif userInput == "4":
            userInputedState = input(
                "This function takes a state as string parameter and returns a dictionary where the keys are a category of energy production and the values are the total energy produced for that category. \nPlease enter a US state abbreviation: ")
            print(energy.getEnergyByCategoryForState(
                userInputedState))

    elif userInput.lower() == "exit":
        print("Exiting the program")
        break
    else:
        print("That is not a valid function name. ")
        continue

    # prompt the user if they would like to continue
    userChoice = input("Would you like to exit the program? Y/N: ")

    if userChoice.lower() == "y":
        print("Exiting the program")
        break

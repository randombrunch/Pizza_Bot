# Pizza bot program
import random
from random import randint

# List of random names
names = ["Mark", "Sally", "Robbie", "Phill", "Fredrick", "Jeremy", "Gregory", "Susan", "Fritz", "Gabriel"]

# Welcome message with random name
def welcome():
    '''
    Purpose: To generate a random name from the list and print out 
    a welcome message 
    Parameters: None 
    Returns: None 
    '''
    num = randint(0,9)
    name = (names[num])
    print("*** Welcome to The Best Pizza You Will Ever Eat ***")
    print("*** My name is" ,name, "***")
    print("You and me we got this Im here to help you order your BEST pizza")


# Menu for pickup or delivery






# Pick up information  - name and phone number  






# Delivery information - name address and phone 





# Choose total Number of Pizzas - max 5






# Pizza menu 






# Pizza order - from menu - print each pizza ordered with cost 





# Print order out - including if order is deliverying or pick up and names and price of each pizza - total cost including any delivery charge 




# Ability to cancel or proceed with order 





# Option for new order or to exit 







# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message 
    Parameters: None 
    Returns: None 
    '''
    welcome()


main()
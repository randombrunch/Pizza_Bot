# Pizza bot program
import random
from random import randint

# List of random names
names = ["Mark", "Sally", "Robbie", "Phill", "Fredrick", "Jeremy", "Gregory", "Susan", "Fritz", "Gabriel"]

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

def pickup(): 
    print ("Hey buddy would you prefer I delivery to your address or you come pick it up?")
    print ("If you want I can delivery it to you if you want just type the number 1")
    print ("If delivery isn't your style rather order it for pickup by typing in 2 instead")
    while True:
        try: 
            delivery = int(input("Alright time to choose delivery or pickup?"   )) 
            if delivery >= 1 and delivery <= 2:      
                if delivery == 1:
                    print ("Delivery it is see you soon with your BEST pizza")
                    break
            
                elif delivery == 2:
                    print ("Alright pickup it is it'll be nice and warm by the time you get here") 
                    break    
            else: 
                print ("Sorry buddy I think you typed it wrong don't worry try again, if you want delivery type 1 or if you want pickup type 2")
        except ValueError:
            print ("Sorry buddy I think you typed it wrong don't worry try again")
            print ("If you want delivery type 1 or if you want pickup type 2")






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
    pickup()

main()
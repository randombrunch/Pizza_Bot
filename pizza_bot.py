# Pizza bot program
import random
from random import randint

# List of random names
names = ["Mark", "Sally", "Robbie", "Phill", "Fredrick", "Jeremy", "Gregory", "Susan", "Fritz", "Gabriel"]
# Customer details dictionary 
customer_details = {}

# Valitate inputs to check if they are blank
def not_blank(question):
    valid = False 
    while not valid:
        response = input(question)
        if response != "":
            return response 
        else:
            print("Sorry buddy but I need your details or else this pickup won't work")


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

def order_type(): 
    print ("But first would you prefer I delivery to your address or you come pick it up?")
    print ("If you want I can delivery it to you if you want just type the number 1")
    print ("If delivery isn't your style rather order it for pickup by typing in 2 instead")
    while True:
        try: 
            delivery = int(input("Alright time to choose delivery or pickup? "   )) 
            if delivery >= 1 and delivery <= 2:      
                if delivery == 1:
                    print ("Delivery it is see you soon with your BEST pizza")
                    break
                elif delivery == 2:
                    print ("Alright pickup it is it'll be nice and warm by the time you get here") 
                    pickup() 
                    break  
            else: 
                print ("Sorry buddy I think you typed it wrong don't worry try again, if you want delivery type 1 or if you want pickup type 2")
        except ValueError:
            print ("Sorry buddy I think you typed it wrong don't worry try again")
            print ("If you want delivery type 1 or if you want pickup type 2")



# Pick up information  - name and phone number  
def pickup():
    question = ("Alright now can I get your name please ")
    customer_details['name'] = not_blank(question )
    # print (customer_details['name'])

    question = ("Nice job now can you please give me your phone number ")
    customer_details['phone'] = not_blank(question )
    # print (customer_details['phone'])
    print(customer_details)





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
    order_type()
    

main()
# Pizza bot program
# 18/02/2022
# Bugs - Phone number input allows letters 
#      - Name input allows numbers 




import random
import sys
from random import randint

# List of random names
names = ["Mark", "Sally", "Robbie", "Phill", "Fredrick", "Jeremy", "Gregory", "Susan", "Fritz", "Gabriel"]
# Lists of pizza names
pizza_names = ["Pepperoni", "Margherita", "Hawaiian", "Cheese", "Italian", "Veggie", "Vegan", "Chicken Deluxe ", 
               "Mega Meat Deluxe", "Seafood Deluxe", "Apricot Chicken Deluxe", "BBQ Chicken Deluxe"]

# Lists of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List of store ordered pizzas
order_list =[]
# List to store pizza prices 
order_cost =[]

# Customer details dictionary 
customer_details = {}

# Valitate inputs to check if they are blank
def not_blank(question):
    valid = False 
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
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
    del_pick = ""
    print ("But first would you prefer I delivery to your address or you come pick it up?")
    print ("If you want I can delivery it to you if you want just type the number 1")
    print ("If delivery isn't your style rather order it for pickup by typing in 2 instead")
    while True:
        try: 
            delivery = int(input("Alright time to choose delivery or pickup? "   )) 
            if delivery >= 1 and delivery <= 2:      
                if delivery == 1:
                    print ("Delivery it is see you soon with your BEST pizza")
                    order_list.append("Delivery Charge")
                    order_cost.append(5)
                    delivery_info()
                    del_pick = "delivery" 
                    break
                elif delivery == 2:
                    print ("Alright pickup it is it'll be nice and warm by the time you get here")
                    del_pick = "pickup"
                    pickup_info() 
                    break  
            else: 
                print ("Sorry buddy I think you typed it wrong don't worry try again, if you want delivery type 1 or if you want pickup type 2")
        except ValueError:
            print ("Sorry buddy I think you typed it wrong don't worry try again")
            print ("If you want delivery type 1 or if you want pickup type 2")
    return del_pick



# Pick up information  - name and phone number  
def pickup_info():
    question = ("Alright now can I get your name please ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    question = ("Nice job now can you please give me your phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])
    print(customer_details)



# Delivery information - name address and phone 
def delivery_info():
    question = ("Alright now can I get your name please ")
    customer_details['name'] = not_blank(question )
    print (customer_details['name'])

    question = ("Nice job now can you please give me your phone number ")
    customer_details['phone'] = not_blank(question )
    print (customer_details['phone'])
        
    question = ("Good now in order to delivery we need your house information starting with your house number ")
    customer_details['home'] = not_blank(question)
    print (customer_details['home'])

    question = ("Now I need your street name please ")
    customer_details['street'] = not_blank(question)
    print (customer_details['street'])


    question = ("Finally I need your suburb then your delivery information will be complete ")
    customer_details['suburb'] = not_blank(question)
    print (customer_details['suburb'])
    print(customer_details)


# Pizza menu 
def menu():
    number_pizzas = 12 



    for count in range (number_pizzas):
        print("{} {} ${:.2f}" .format(count+1, pizza_names[count], pizza_prices[count]))


# Choose total Number of Pizzas - max 5


# Pizza order - from menu - print each pizza ordered with cost 
def order_pizza():
    # Ask for total number of pizzas ordered 
    num_pizzas = 0


    while True:
        try:
            num_pizzas = int(input("How many pizzas would you like to order?"))
            if num_pizzas >= 1 and num_pizzas <= 5: 
                break
            else:
                print("Sorry Sir/Maam but your number must between 1 - 5")
        except ValueError:
            print("Sorry but that is not a valid number")
            print("Pleases enter a number from 1 to 5 ")

    print (num_pizzas)

    # Choose pizza from menu 

    for item in range (num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("Please select the pizza you want if the corrosponding number "))
                    if pizza_ordered >= 1 and pizza_ordered <= 12:
                        break
                    else:
                        print("Sorry but you number must be from 1 to 12")
                except ValueError:
                    print ("This is not a valid number")
                    print("Sorry but you number must be from 1 to 12")
            pizza_ordered = pizza_ordered -1
            order_list.append(pizza_names[pizza_ordered])
            order_cost.append(pizza_prices[pizza_ordered])
            print("{} ${:.2f}" .format(pizza_names[pizza_ordered], pizza_prices[pizza_ordered]))
            num_pizzas = num_pizzas -1

    print(order_list)
    print(order_cost)




# Print order out - including if order is deliverying or pick up and names and price of each pizza - total cost including any delivery charge 

def print_order(del_pick):
    total_cost = sum(order_cost)
    print ("Customer Details")
    if del_pick == "Pickup":
        print (f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']}")
        print ("Your order will be for pickup")
    elif del_pick == "Delivery":
        print ("Your order will be delivered too you")
        print (f"Customer Name: {customer_details['name']} \nCustomer Phone: {customer_details['phone']} \nCustomer Address: {customer_details['house']} {customer_details['street']} {customer_details['suburb']}")
    
    print() 
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")



# Ability to cancel or proceed with order 
def confirm_cancel():
    print ("Is this your correct order?")
    print ("To confirm presss 1")
    print ("To cancel press 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("Order is all good to go")
                    new_exit()
                    break

                elif confirm == 2:
                    print ("Alright your order has been canceled")
                    new_exit()
                    break
            else:
                print ("The number must be 1 or 2")
        except ValueError:
            print ("Sorry that is not a valid number")
            print ("Please put numbers 1 or 2")


 



# Option for new order or to exit 
def new_exit():
    print ("Do you want to start another order?")
    print ("For yes press 1")
    print ("To exit press 2")
    while True:
        try:
            confirm = int(input("Please enter a number "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print ("New order")
                    order_list.clear()
                    order_cost = [].clear()
                    customer_details.clear()
                    main()
                    break

                elif confirm == 2:  
                    print ("Alright hope you enjoy your pizza   ")
                    order_list.clear()
                    order_cost = [].clear()
                    customer_details.clear()
                    sys.exit()
                    break
            else:
                print ("The number must be 1 or 2")
        except ValueError:
            print ("Sorry that is not a valid number")
            print ("Please put numbers 1 or 2")






# Main function
def main():
    '''
    Purpose: To run all functions
    a welcome message 
    Parameters: None 
    Returns: None 
    '''
    welcome()
    del_pick = order_type()
    menu()
    order_pizza()
    print_order(del_pick)
    confirm_cancel()

main()
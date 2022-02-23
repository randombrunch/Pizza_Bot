# Customer details dictionary 
customer_details = {}

# Basic intrusctions
print("Alright now I need you to fill out the pickup information")

# Customer name not blank
valid = False
while not valid:
    customer_details['name'] = input("Alright first tell me your name ")
    if customer_details['name'] != "":
        print (customer_details['name'])
        break
    else:
        print("Sorry buddy but I need your name or else I won't know who to give it to")


# Customer phone number not blank
valid = False
while not valid:    
    customer_details['phone'] = input("Now can you please enter your phone number ")
    if customer_details['phone'] != "":
        print (customer_details['phone'])
        break
    else:
        print("Sorry but I need your phone number in order to complete your pickup order")

print (customer_details)
# Bug - Accepts blank input



print("Alright now I need you to fill out the pickup information")

# Customer name
valid = False
while not valid:
    name = input("Alright first tell me your name ")
    if name != "":
        print (name)
        break
    else:
        print("Sorry buddy but I need your name or else I won't know who to give it to")


# Customer phone number 
valid = False
while not valid:    
    phone = input("Now can you please enter your phone number ")
    if phone != "":
        print (phone)
        break
    else:
        print("Sorry but I need your phone number in order to complete your pickup order")

# Customer details dictionary 
customer_details = {}


def not_blank(question):
    valid = False 
    while not valid:
        response = input(question)
        if response != "":
            return response 
        else:
            print("Sorry buddy but I need your details or else this pickup won't work")



# Basic intrusctions
question = ("Alright can you first please tell me your name ")
customer_details['name'] = not_blank(question )
print (customer_details['name'])

question = ("Nice job now can you please give me your phone number ")
customer_details['phone'] = not_blank(question)
print (customer_details['phone'])
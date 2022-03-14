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


def delivery():
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


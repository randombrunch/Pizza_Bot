# Menu so that user can choose either pickup or delivery 

# Bug - Need to make it so that it only accept 1 or 2

print ("Hey buddy would you prefer I delivery to your address or you come pick it up?")

print ("If you want I can delivery it to you if you want just type the number 1")
print ("If delivery isn't your style rather order it for pickup by typing in 2 instead")





while True:
    try: 
        delivery = int(input("Alright time to choose delivery or pickup?")) 
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
         
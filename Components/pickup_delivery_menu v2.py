# Bugs
# Will only work for valid input "D" and "P"

# Menu so that user can choose either pickup or delivery 

print ("Hey buddy would you prefer I delivery to your address or you come pick it up?")

print ("If you want I can delivery to you if you want just type the letter D")
print ("If delivery isn't your style rather order it for pickup by typing in P instead")

delivery = input() 

if delivery == "D":
    print ("Delivery it is see you soon with your BEST pizza")

elif delivery == "P":
    print ("Alright pickup it is it'll be nice and warm by the time you get here") 

else:
    print ("Sorry buddy I think you typed it wrong don't worry try again D for delivery or P for pickup")
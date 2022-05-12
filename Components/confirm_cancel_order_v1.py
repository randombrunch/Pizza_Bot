import sys

# List of store ordered pizzas
order_list =[]
# List to store pizza prices 
order_cost =[]

# Customer details dictionary 
customer_details = {}



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

main():
# List of pizza names 
pizza_names = ["Margherita", "Pepporoni", "Hawaiian", "Cheese", "Italian", "Veggie", "Vegan", "Chicken Deluxe ", 
               "Mega Meat Deluxe", "Seafood Deluxe", "Apricot Chicken Deluxe", "BBQ Chicken Deluxe"]
# List of pizza prices
pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

# List of store ordered pizzas
order_list =[]
# List to store pizza prices 
order_cost =[]

# List to store order cost 

def menu():
    number_pizzas = 12 



    for count in range (number_pizzas):
        print("{} {} ${:.2f}" .format(count+1, pizza_names[count], pizza_prices[count]))




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
            print("Pleases enter a number from 1 to 5")

    print (num_pizzas)

    # Choose pizza from menu 

    for item in range (num_pizzas):
        while num_pizzas > 0:
            while True:
                try:
                    pizza_ordered = int(input("Please select the pizza you want if the corrosponding number"))
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

menu()

order_pizza()
pizza_names = ["Pepperoni", "Margherita", "Hawaiian", "Cheese", "Italian", "Veggie", "Vegan", "Chicken Deluxe ", 
               "Mega Meat Deluxe", "Seafood Deluxe", "Apricot Chicken Deluxe", "BBQ Chicken Deluxe"]

pizza_prices = [8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 8.50, 13.50, 13.50, 13.50, 13.50, 13.50]

number_pizzas = 12 

print("How many pizzas do you want to order?")
num_pizza = int(input())

for count in range (number_pizzas):
    print(count, pizza_names[count], pizza_prices[count])
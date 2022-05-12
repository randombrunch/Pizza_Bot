# List of store ordered pizzas
order_list = ['Pepperoni', 'Margherita', 'Hawaiian', 'BBQ Chicken Deluxe']
# List to store pizza prices 
order_cost = [8.50, 8.50, 8.50, 13.50]


cust_details = {'name': 'Mark', 'phone': '274609365', 'house': '45', 'street': 'Harry', 'suburb': 'Howick'}


def print_order():
    total_cost = sum(order_cost)
    print ("Customer Details")
    print (f"Customer Name: {cust_details['name']} \nCustomer Phone: {cust_details['phone']} \nCustomer Address: {cust_details['house']} {cust_details['street']} {cust_details['suburb']}")
    print() 
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
        count = count+1
    print()
    print("Total Order Cost")
    print(f"${total_cost:.2f}")

print_order()
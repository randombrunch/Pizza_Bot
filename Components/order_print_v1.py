# List of store ordered pizzas
order_list = ['Pepperoni', 'Margherita', 'Hawaiian', 'BBQ Chicken Deluxe']
# List to store pizza prices 
order_cost = [8.50, 8.50, 8.50, 13.50]


cust_details = {'name': 'Mark', 'phone': '274609365', 'house': '45', 'street': 'Harry', 'suburb': 'Howick'}


print("\n Name: {} \n Phone: {} \n House: {} \n Street: {} \n Suburb: {}" .format(cust_details['name'], cust_details['phone'], cust_details['house'], cust_details['street'], cust_details['suburb'] ))




count = 0
for item in order_list:
    print("Ordered: {}  Cost ${:.2f}".format(item, order_cost[count]))
    count = count+1
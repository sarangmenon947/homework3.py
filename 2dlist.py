# Creating a 2D list for food items
food_menu = [
    ["Masala Dosa", "Crispy rice crepe filled with spiced potatoes", 50],
    ["Vada", "Spicy lentil donut", 20],
    ["Idli", "Steamed rice cakes", 30],
    ["Chole Bhature", "Spicy chickpeas served with deep-fried bread", 80],
    ["Paratha", "Stuffed flatbread", 40]
]

# Printing the food menu
print("Food Menu:")
for item in food_menu:
    print(item)

# Extracting data using row and column index
row_index = 1

# Extracting name, description, and price of Vada
food_name = food_menu[row_index][0]          # Name
food_description = food_menu[row_index][1]   # Description
food_price = food_menu[row_index][2]         # Price

# Print the extracted information
print("\nExtracted Data:")
print(f"Food Name: {food_name}")
print(f"Description: {food_description}")
print(f"Price: ₹{food_price}")

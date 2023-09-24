# 2D list = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "cheeseburger", "hotdog"]
dessert = ["cake", "ice cream"]

food = [drinks, dinner, dessert]

print(food)

#The first list will be at index 0.  To pinpoint a specific item,
# you must list the index of the list and the item as below
print(food[0][0])

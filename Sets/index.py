# sets = a collection which is unordered and un-indexed. Has no duplicate values.

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

utensils.add("napkin")
print(utensils)

utensils.remove("fork")
print(utensils)

#This will add all the utensil set to the dishes set and print all
dishes.update(utensils)
print(dishes)

for x in dishes:
    print(x)

#Join both sets together under a new set
dinner_table = utensils.union(dishes)
print(dinner_table)

#Will print what elements that utensils has that dishes doesn't
print(utensils.difference(dishes))

#Will print what elements that both have in common
print(utensils.intersection(dishes))

utensils.clear()
print(utensils)
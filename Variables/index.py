# variable = a container for a value. Behaves as the value it contains.

#Strings
first_name = "Kyzer"
last_name = "Sose"
full_name = first_name + " " + last_name
print("Hello " + full_name)

#How to assess what class of data an item is
print(type(full_name))

#Intergers
age = 21
age += 1
print(age)
print(type(age))

# How to concatenate strings and intergers
print("You are " + str(age) + " years old!")

#Floats
height = 250.5

print("Your height is " + str(height) + " !")
print(type(height))


#Booleans
human = True
print(human)
print(type(human))
print("Are you a human: " + str(human))

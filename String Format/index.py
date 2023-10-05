# str.format = optional method that gives users
#              more control when displaying output


animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item)

#Using format fields
print("The {} jumped over the {}".format(animal,item))

#Using positional arguments
print("The {0} jumped over the {1}".format(animal,item))

#Using keyword arguments
print("The {bovine} jumped over the {terrain}".format(bovine="cow",terrain="moon"))

pi = 3.14159
print("The number pi is {:.3f}".format(pi))

number = 1000

print("The number is {:.3f}".format(number))
#Adds comma at thousands
print("The number is {:,}".format(number))
#Binary
print("The number is {:b}".format(number))
#Octal number
print("The number is {:o}".format(number))
#Hexidecimal number
print("The number is {:x}".format(number))
#Scientific Notation
print("The number is {:e}".format(number))
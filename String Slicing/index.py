# Slicing = Create a substring by extracting elements from another string
#         = indexing[] or slice()
#         = [atert:stop:step]


name = "Spongebob Squarepants"

#Starting index and index aftyer last (The zero can also be blank [:3])
first_name = name[0:9] 

#Starting index through all remaining
last_name = name[10:]

#Starting index, ending index, and increment
funky_name = name[::2]

#Starting index, ending index, and increment
reversed_name = name[::-1]

print(name)
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)


website1 = "http://google.com"
website2 = "http://wikipedia.com"
#Substring will begin at 7 to remove "http://", stop index is -4 to remove ".com"
slice = slice(7, -4)

print(website1[slice])
print(website2[slice])
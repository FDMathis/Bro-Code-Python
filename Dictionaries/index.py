# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allows us access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Delhi',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals)
print(capitals.items)
print(capitals.keys)
print(capitals.values)

for key,value in capitals.items():
    print(key,value)

capitals.update({'Germany':'Berlin'})
print(capitals)

capitals.update({'USA':'Las Vegas'})
print(capitals)

capitals.pop('China')
print(capitals)

# If a key is not listed it would cause an error, so use the "get" method instead
print(capitals['Germany'])
print(capitals.get('Cuba'))

capitals.clear
print(capitals)
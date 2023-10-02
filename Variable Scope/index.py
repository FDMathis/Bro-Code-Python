# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped version of a variable can be created


# GLOBAL SCOPE (available inside and outside of functions)
name = "Bro"

# LOCAL SCOPE (available only inside this function)
def display_name():
    name = "Code"
    print(name)

display_name()
print(name)


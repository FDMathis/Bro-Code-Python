# logical operators = (and, or, not) are used to check if two or more conditional
#                     statements are true


temp = int(input("What is the temperature outside?"))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside and play!")

elif temp < 0 or temp > 30:
    print("The temperature is bad outside today.")
    print("It is best that you stay indoors.")
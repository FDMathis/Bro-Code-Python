# exception = events detected during execution that interrupt program flow

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator

except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero, Idiot!")

except ValueError as e:
    print(e)
    print("Enter only numkbers!")

except Exception as e:
    print(e)
    print("Something went wrong.")

else: 
    print(result)

finally:
    print("This will always execute at the end.  Can be used to close files and other stuff.")

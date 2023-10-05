# These methods do not create true random numbers, but pseudo-random numbers,
# which is close enough for most uses

#import random module
import random

#random number between 1 and 6 like dice roll
x = random.randint(1,6)
print(x)

#Random floating point num between 0 and 1.
y = random.random()
print(y)

#RPS game
myList = ['rock','paper','scissors']
z = random.choice(myList)
print(z)

#A deck of cards
cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
#Use the shuffle method
random.shuffle(cards)
print(cards)
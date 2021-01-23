# Author: Paul Quaife
# Date: 1/19/2020
# Description: Asks for numbers, then lists the min and max.


print("How many integers would you like to enter?")
num_int = input(int())
print("Please enter " + num_int + " integers")
num_random = input(int())
min = num_random
max = num_random
index = 0

while index < int(num_int) - 1:
    num_random = int(input(''))
    if num_random >= max:
        max = int(num_random)
    if num_random <= min:
        min = int(num_random)
    index = index + 1
print("min: ", min, )
print("max: ", max, )

# Author: Paul Quaife
# Date: 1/19/2021
# Description: Asks for numbers, then lists the min and max.

print("How many integers would you like to enter?")
num_inp = (input())
print("Please enter " + num_inp + " integers.")
num_random = int(input())
min_val = 0
max_val = 0
index = 0

while index < int(num_inp) - 1:
    num_random = int(input())
    if num_random >= max_val:
        max_val = int(num_random)
    if num_random <= min_val:
        min_val = int(num_random)
    index = index + 1
print("min: ", min_val,)
print("max: ", max_val,)

# Euler Problem 001
# Solved January 2021

# If we list all the natural numbers below 10 
# that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 
# below 1000.

import math

total = 0
i = 0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        total = i + total
    i = i + 1
print(total)
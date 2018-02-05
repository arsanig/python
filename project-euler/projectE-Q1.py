# BRUTE FORCE O(n)
sum = 0;
for i in range(0, 1000):
    if ((i % 3) == 0 or (i % 5) == 0):
        sum += i
print(sum)

# MORE EFFICIENT O(1)
# Based on the idea that the sum of all numbers less than n that divides d equals d times the sum of all numbers less than n/d
import math
sumThree = 3 * math.floor(999/3) * (math.floor(999/3)+1)/2
sumFive = 5 * math.floor(999/5) * (math.floor(999/5)+1)/2
sumGCD = 15 * math.floor(999/15) * (math.floor(999/15)+1)/2
print(sumThree + sumFive - sumGCD)
import numpy as np
from math import comb # Technically cheating by using a non standard library but I am NOT going to code in an nCr function.

file = open('day_10_data.txt')
data = np.empty((0,0), dtype = int)
for line in file:
	data = np.append(data, int(line))

data = np.append(data, max(data)+3)
data = np.sort(data)
missing_numbers = np.setdiff1d(np.linspace(1, max(data), max(data), dtype = int), data) # All numbers missing in the sequence between the maximum and 1
threes = len(missing_numbers)/2
ones = len(data)-threes 
print(ones*threes)

## Assignment 2
#please clap I spend way too much time on this
#
#GAME PLAN:
# Only place where we can replace numbers is where there are atleast 3 consecutive numbers
# Amount of states the consecutive numbers can be in depends on how many numbers you can maximally remove to keep a still working series. This is 1 number for length 3, 2 for length 4 and 2 for length 5. Higher is not required and I cant be arsed to caculate it as a function of n.
# Then using the max amount of possible numbers removed ( I shall call it N) you can calculate the amount of states it can be in by NCk where k is every integer in [0, N].
# Amount of total states the big data series can be in is calculated by multiplying all the different states its subsets can be in.
# ???
# profit
missing_numbers = np.insert(missing_numbers, 0, -1) 
jumps = np.empty((0,0), dtype = int)

for k in range(0, len(missing_numbers)-2): 
	jumps = np.append(jumps, missing_numbers[k+1]-missing_numbers[k])

def states(n):
	total = 0
	for k in range(0, min(2, n-2)+1): # completly arbitrary way to find out max amount of possible changes, does not hold up for sequences with more than 5 numbers in it.
		total += comb(n-2, k)
	return total
	
n = 1
for element in jumps[jumps>=4]:
	n *= states(element-1)

print(n)
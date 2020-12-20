import numpy as np

data = np.array([2,0,1,9,5,19])

numbers = {}
for k in range(len(data)):
	numbers[data[k]] = k+1

T = len(numbers)
current = data[-1]

del numbers[current]
print(numbers)

while T != 30000000:
	print('TURN', T)
	#print(current)
	if current in numbers:
		old_pos = numbers[current]
		numbers[current] = T
		current = T-old_pos
	else:
		numbers[current] = T
		current = 0
	T += 1
	
print(current)
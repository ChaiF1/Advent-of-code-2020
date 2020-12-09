import numpy as np
file = open('day_9_data.txt')

data = np.empty((0,0), dtype = int)
for line in file:
	data = np.append(data, int(line))

def addition_check(number, data):
	for n in data:
		if number-n in data:
			return True
	return False

def main():
	for k in range(26, len(data)):
		if not addition_check(data[k], data[k-25:k]):
			return k
	return None

# Assignment 2
fault = data[main()] # Number where everything went wrong.
snake = np.array(data[0]) # The snake is an array sliding through all the data values, if it finds its sum to be higher than the fault number it will lose values at the tail and if it it is too low it will add numbers at its head.

h = 1 # Head start position

while np.sum(snake) != fault:
	if np.sum(snake)<fault:
		snake = np.append(snake, data[h])
		h += 1
	elif np.sum(snake)>fault:
		snake = np.delete(snake, [0], axis = 0)

print(snake)
print(np.min(snake)+np.max(snake))
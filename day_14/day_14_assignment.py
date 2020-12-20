import numpy as np

bit = np.array(list('{:036b}'.format(11)), dtype=int)
memory = {}

#### Assignment 1
def masker_1(bit, mask):
	bit = np.logical_and(bit, mask, out = bit, where = mask != 2).astype(int)
	bit = np.logical_or(bit, mask, out = bit, where = mask != 2).astype(int)
	return bit

def assignment_1():
	for line in open('day_14_data.txt'):
		if 'mask' == line[0:4]:
			mask = np.array(list(line.strip('mask = \n').replace('X', '2')), dtype=int)
		else:
			index = int(line[4:line.find(']')])
			value = int(line[line.find(']')+4:])
			bit = np.array(list('{:036b}'.format(value)), dtype=int)
			bit = masker_1(bit, mask)
			memory[index] = int("".join(str(x) for x in bit), 2)

#### Assignment 2
def masker_2(bit, mask):
	bit = np.logical_or(bit, mask, out = bit, where = mask != 2).astype(int)
	bit[mask == 2] = 0
	return bit
	
def combinations(array):
	comb = np.empty((0,0), dtype=int)
	a = array[0]
	if len(array) == 1:
		return np.append(array, 0)
	rest = combinations(np.delete(array, 0))
	return np.append(rest, rest+a)

def assignment_2():
	for line in open('day_14_data.txt'):
		if 'mask' == line[0:4]:
			mask = np.array(list(line.strip('mask = \n').replace('X', '2')), dtype=int)
			floaters = np.equal(np.ones(36)*2, mask).astype(int)
		else:
			index = int(line[4:line.find(']')])
			value = int(line[line.find(']')+4:])
			bit = np.array(list('{:036b}'.format(index)), dtype=int)
			bit = masker_2(bit, mask)
			index = int("".join(str(x) for x in bit), 2)
			floated_values = np.empty((0,0), dtype=int)
			for k in range(len(floaters)):
				if floaters[k] == 1:
					floated_values = np.append(floated_values, 2**(len(floaters)-1-k))
			combs = combinations(floated_values)
			for comb in combs:
				memory[comb+index] = int(value)



assignment_2()		
print(sum(memory.values()))

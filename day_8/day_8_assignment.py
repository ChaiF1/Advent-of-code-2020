import numpy as np
file = open('day_8_data.txt')

all_lines = np.empty((0,0))

for line in file:
	all_lines = np.append(all_lines, line.replace('\n', '').replace('bags', 'bag')) # Array of all commands

def command(n, acc, lines):
	command, number = lines[n].split(' ')
	number = int(number)
	if command == 'acc':
		return n+1, acc+number
	if command == 'jmp':
		return n+number, acc
	if command == 'nop':
		return n+1, acc	

def replace(line):
	if line.find('nop') == -1:
		return line.replace('jmp', 'nop')
	else:
		return line.replace('nop', 'jmp')
		
def brute_force(edit): # At this point I just accept that I am horrible at being clever and brute forcing is my only way out.
	edited_lines = np.copy(all_lines)
	edited_lines[edit] = replace(all_lines[edit])

	visited = np.empty((0,0), dtype = int)
	acc = 0
	n = 0
	while not n in visited:
		if n == 637:
			print(acc)
		visited = np.append(visited, n)
		n, acc = command(n, acc, edited_lines)
	return acc, visited


acc, visited_real = brute_force(0)
for k in visited_real: # NOTE: getting an error in the code means it is working
	if all_lines[k].find('acc') == -1:
		dont_care1, dont_care2 = brute_force(k)
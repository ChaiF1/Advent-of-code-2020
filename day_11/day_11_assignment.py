import numpy as np
from math import floor
from itertools import combinations

file = open('day_11_data.txt')

boat = np.array(list(file.readline().strip('\n')), ndmin = 2)
directions = np.array([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)])
# This is by far the most innefficient and bad code I have yet to write for this whole advent but it works. 
for line in file:
	add = np.array(list(line.strip('\n')), ndmin = 2)
	boat = np.append(boat, add, axis = 0)

squares = boat.shape[0]*boat.shape[1]

# assignment 1 function
#def seat_counter(pos):
#	seats = 0
#	for k in range(9):
#		adj = pos[0]-1+floor(k/3), pos[1]-1+k%3
#		try:
#			if boat[adj] == '#' and adj[0] >= 0 and adj[1] >= 0:
#				seats += 1
#		except:
#			seats = seats
#	return seats

def seat_counter(pos):
	seats = 0
	for k in range(9):
		adj = np.empty((0,0), dtype = int)
		adj = np.append(adj, (pos[0]-1+floor(k/3),pos[1]-1+k%3))
		while adj[0] in range(boat.shape[0]) and adj[1] in range(boat.shape[1]) and boat[adj[0]][adj[1]] == '.':
			adj[0] += directions[k][0]
			adj[1] += directions[k][1]
		try:
			if boat[adj[0]][adj[1]] == '#' and adj[0] >= 0 and adj[1] >= 0:
				seats += 1
		except:
			seats = seats
	return seats

def seat_changer(boat):
	boat_copy = np.copy(boat)
	for k in range(squares):
		pos = floor(k/boat.shape[1]), k%(boat.shape[1])
		if boat[pos] == 'L' and seat_counter(pos) == 0:
			boat_copy[pos] = '#'
		elif boat[pos] == '#' and seat_counter(pos) >= 6:
			boat_copy[pos] = 'L'
	return boat_copy

tries = 0
while not np.array_equal(boat, seat_changer(boat)):
	boat = seat_changer(boat)
	tries += 1
	print(tries)

filled_seats = 0
for k in range(squares):
	pos = floor(k/boat.shape[1]), k%(boat.shape[1])
	if boat[pos] == '#':
		filled_seats += 1

print(boat)
print(filled_seats)
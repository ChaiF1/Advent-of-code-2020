from math import cos, sin, pi, e
file = open("day_12_data.txt")
# Forgot to save how I did the first one assignment but nothing really exciting happened there.
ship = 0+0j
way = 10+1j

for line in file:
	if line[0] == 'N':
		way += int(line[1:])*1j
	elif line[0] == 'S':
		way -= int(line[1:])*1j
	elif line[0] == 'E':
		way += int(line[1:])
	elif line[0] == 'W':
		way -= int(line[1:])
	elif line[0] == 'L':
		way = (way-ship)*e**(1j*int(line[1:])*pi/180)+ship
	elif line[0] == 'R':
		way = (way-ship)*e**(-1j*int(line[1:])*pi/180)+ship
	elif line[0] == 'F':
		diff = way-ship
		ship += (way-ship)*int(line[1:])
		way = ship+diff

print(abs(ship.real) + abs(ship.imag))
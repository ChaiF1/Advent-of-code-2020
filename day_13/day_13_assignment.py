import numpy as np
from math import ceil, floor

# Assignment 1:
#Game plan:
# I know that if I divide the minimum depart time by the bus ID's the number in that array with the highest decimal point must be my bus line, as it is the closest to an integer.
# Then I can round the result from the division up to get and multiply times the bus ID to get the time it arrives. So then I have the bus ID and the wait time

depart_time = 1000434
bus_lines = np.array([17, 41, 983, 29, 19, 23, 397, 37, 13])

bus_ID_decimal = (depart_time/bus_lines)%1
bus_ID_index = np.where(max(bus_ID_decimal)==bus_ID_decimal)
k = depart_time/bus_lines[bus_ID_index]
bus_ID = bus_lines[bus_ID_index]
m = ceil(k)*bus_ID-depart_time

## Assignment 2
bus_lines =[17,1,1,1,1,1,1,41,1,1,1,1,1,1,1,1,1,983,1,29,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,19,1,1,1,23,1,1,1,1,1,1,1,397,1,1,1,1,1,37,1,1,1,1,1,1,13]
#bus_lines = np.array([1789,37,47,1889])

#It is assumed that the numbers are coprime otherwise it is impossible for the given situation to be achieved.


def EEA(a, b): # Extendend Euclidean algorithm
	if a == 0:
		return b, 0, 1
		
	gcd, x1, y1 = EEA(b%a, a)
	x = y1 - (b//a)*x1
	y = x1
	return gcd, x, y 	

def finder(i):
	if bus_lines[i-1] == 1:
		return finder(i-1)
	return bus_lines[i-1]

T = len(bus_lines)-1

for i in range(len(bus_lines)-2, -1, -1):
	if bus_lines[i] != 1:
		print('CYCLE', i)
		n1, n2 = bus_lines[-1], bus_lines[i]
		gcd, m1, m2 = EEA(n1, n2)
		#print(T, bus_lines[-1])
		#print(i, bus_lines[i])
		T = (T*m2*n2+i*m1*n1)%(n1*n2)
		print(T, n1*n2, (T-61)%13)
		bus_lines[-1] = n1*n2
		
answer = bus_lines[-1]-T
print(answer)
import numpy as np

#### Assignment 1
file = open("day_5_data.txt")
answers = np.array([])

for seat in file:
	seat = seat.replace('F', '0')
	seat = seat.replace('B', '1')
	seat = seat.replace('L', '0')
	seat = seat.replace('R', '1')
	row_seat = seat[0:7]
	col_seat = seat[7:]
	row_seat = int(row_seat, 2)
	col_seat = int(col_seat, 2)
	answers = np.append(answers, 8*row_seat+col_seat)



#### Assignment 2
filter = answers > 7
filter2 = answers < 1016
answers = answers[np.logical_and(filter, filter2)]
pos_seats = np.linspace(0, 1023, 1024)
pos_seats = np.setdiff1d(pos_seats, answers, assume_unique = True).astype(int)


for element in pos_seats:
	if not element + 1 in pos_seats and not element -1 in pos_seats:
		print(element)
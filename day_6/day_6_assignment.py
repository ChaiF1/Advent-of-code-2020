file = open("day_6_data.txt")


# To get the answer from the first part make answers set itself to the empty set and take the union instead of the intersection.

answers = set('abcdefghijklmnopqrstuvwxyz')
tot_answers = 0

for line in file:
	if line == '\n':
		tot_answers += len(answers-{'\n'})
		answers = set('abcdefghijklmnopqrstuvwxyz')
	else:
		answers = answers & set(line)

print(tot_answers)
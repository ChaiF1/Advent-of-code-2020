import numpy as np
allowed = np.empty((0,0), dtype=int)
nearby_tickets = False
correct_tickets = np.empty((0, 20), dtype=int)
answer = 0
rules = {}

def check_ticket(ticket):
	if len(np.setdiff1d(ticket, allowed)) == 0:
		return True
	return False

def check_field(column):
	correct_rules = np.empty((0,0))
	for rule in rules:
		range1 = np.arange(rules[rule][0], rules[rule][1]+1, 1)
		range2 = np.arange(rules[rule][2], rules[rule][3]+1, 1)
		test = np.union1d(range1, range2)
		if len(np.setdiff1d(column, test)) == 0:
			correct_rules = np.append(correct_rules, rule)
	
	return correct_rules
	

for line in open('day_16_data.txt'):
	if line[0] == 'r':
		line = line[1:]
		rule, numbers = line.strip('\n').split(': ')
		range1, range2 = numbers.split(' or ')
		range1 = np.array(range1.split('-'), dtype=int)
		range2 = np.array(range2.split('-'), dtype=int)
		rules[rule] = np.union1d(range1, range2)
		range1 = np.arange(range1[0], range1[1]+1, 1)
		range2 = np.arange(range2[0], range2[1]+1, 1)
		allowed = np.union1d(allowed, range1)
		allowed = np.union1d(allowed, range2)

	if nearby_tickets:
		ticket = np.array(line.strip('\n').split(','), dtype=int, ndmin=2)
		if check_ticket(ticket):
			correct_tickets = np.append(correct_tickets, ticket, axis=0)

	if line == 'nearby tickets:\n':
		nearby_tickets = True

fields = {}
for k in range(len(correct_tickets[0])):
	correct_rules = check_field(correct_tickets[:,k])
	fields[k] = correct_rules


assigned = np.empty((0,0))

while len(assigned) != 20:
	for field in fields:
		if len(fields[field]) == len(assigned)+1:
			fields[field] = np.setdiff1d(fields[field], assigned)
			assigned = np.union1d(assigned, fields[field])
	
print(157*151*83*149*79*137)
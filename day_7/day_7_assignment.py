import numpy as np
file = open('day_7_data.txt')
# The 'level' of a bag is how deep one must search until the bags contain no more bags. So if a bag contains no other bags it is level 0 and if it contains a level 0 bag it is level 1 etc.



def bag_name(line): # Function giving the name of a bag for which a rule is set up.
	a = line.find('bag')
	return line[0:a+len('bag')]

all_bags = np.empty((0,0))
all_lines = np.empty((0,0))
level_0 = np.empty((0,0)) 
for line in file:
	all_bags = np.append(all_bags, bag_name(line)) # Array of all bag names
	all_lines = np.append(all_lines, line.replace('\n', '').replace('bags', 'bag')) # Array of all rules
	if line.find('no') != -1:
		level_0 = np.append(level_0, bag_name(line)) # Level 0 bags are bags which cannot contain any other bags.


def bag_searcher(name): # Create a nx2 array containing all the information of which bags are in the bag. 
	if name in level_0:
		return None

	a = np.where(all_bags == name)
	bag_rule = all_lines[a[0][0]]
	bag_contents = np.empty((0, 2))
	bags_amount = bag_rule.count('bag')-1

	start = bag_rule.find('contain') + len('contain')+1
	end = bag_rule.find('bag', start) + len('bag')
	for bag in range(0, bags_amount):
		contained_bag_num = bag_rule[start]
		contained_bag_name = bag_rule[start+2:end]
		start = end + len(', ')
		end = bag_rule.find('bag', start) + len('bag')
		bag_contents = np.append(bag_contents, np.array([[contained_bag_num, contained_bag_name]]), axis = 0)
	return bag_contents
	

good_bags = np.array(['shiny gold bag'])
def bag_check(name): # Recursive function checking if a bag can contain the shiny gold bag or if any of its children can contain it.
	if name in level_0: # Base case
		return False

	contents = bag_searcher(name)
	for row in range(0, np.shape(contents)[0]):
		if contents[row][1] in good_bags:
			return True
		elif bag_check(contents[row][1]):
			return True
			
# It is assumed that if a bag has a lower level than the shiny gold bag it cannot contain a shiny gold bag, technically not true but i have midterms today goddamnit and dont have a lot of time to fix this. 
#correct = 0
#for bag in all_bags:
#	if bag_check(bag):
#		correct += 1

## Assignment 2:

def bag_counter(name): # Really simiral to bag_searcher but instead of returning true or false it will return numbers.
	if name in level_0:
		return 1
	contents = bag_searcher(name)
	total_bags = 0
	for row in range(0, np.shape(contents)[0]):
		 total_bags += int(contents[row][0])*bag_counter(contents[row][1])
	return total_bags+1

print(bag_counter('shiny gold bag')-1)
file = open('day_4_data.txt')
keywords = {'byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'}
haircolors = {'#', 'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
eyecolors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


passport = ''
correct = 0
words = 0

def count_keys(passport):
	keys = 0
	for key in keywords:
		if passport.find(key) != -1:
			keys += 1
	return keys

def restrictions(passport):
	for key in keywords:
		i_key = passport.find(key)
		i_comma = passport.find(',', i_key)
		value = passport[i_key+4:i_comma]
		if key == 'byr:':
			if len(value) != 4 or int(value) < 1920 or int(value) > 2002:
				print(key, value)
				return False

		if key == 'iyr:':
			if len(value) != 4 or int(value) < 2010 or int(value) > 2020:
				print(key, value)
				return False

		if key == 'eyr:':
			if len(value) != 4 or int(value) < 2020 or int(value) > 2030:
				print(key, value)
				return False

		if key == 'hgt:':
			if value.find('cm') == 3:
				height = int(value[:value.find('cm')])
				if  height < 150 or height > 193:
					print(key, value)
					return False
			elif value.find('in') == 2:
				height = int(value[:value.find('in')])
				if  height < 59 or height > 76:
					print(key, value)
					return False
			else:
				print(key, value)
				return False

		if key == 'hcl:':
			if value[0] != '#' or len(value) != 7 or len(set(value)-haircolors) != 0:
				print(key, value)
				return False

		if key == 'ecl:':
			if not value in eyecolors:
				print(key, value)
				return False

		if key == 'pid:':
			if len(value) != 9:
				print(key, value)
				return False
	return True


for line in file:
	if line == '\n':
		words = count_keys(passport)
		if words == 7:
			if restrictions(passport) == True:
				correct += 1
		passport = ''
	else:
		line = line.replace(' ', ',')
		passport = passport + line + ','
		passport = passport.replace('\n', '')
		
print(correct)
import pandas as pd
data = pd.read_csv("day_2_data.csv")
errors = 0

for n in range(0, len(data)):
	min = data['min'][n]
	max = data['max'][n]
	letter = data['letter'][n]
	p = data['password'][n]
	c1 = p[min-1] == letter
	c2 = p[max-1] == letter

	if not c1^c2:
		errors +=  1
		
print(len(data)-errors)
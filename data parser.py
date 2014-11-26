"""This script was writting for a particular dataset to 
extract and average the last vales. It is scaled for large 
files."""

import re

number = .000001
count = 1

with open("data.txt") as f:
	for line in f:
		if re.match("[16000]", line) is None:
			pass
		else:
			the_line = re.findall("[0-9]+", line) #seeking a list of all numbers
			the_line.reverse() #the number I'm seeking is in the end
			if not the_line: #some of the lines are empty
				continue
			else:
				pass
			if 1000 < int(the_line[0]) < 1000000: #excluding obvious typos
				number = number + int(the_line[0]) #summing total sum with current value
				count += 1
			else:
				pass

print number / count

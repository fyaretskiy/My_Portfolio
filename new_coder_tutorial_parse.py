"""
My parse function created through the newcoder.io tutorial
"""

import csv

#He notes unchanged variables are writting in upper case

MY_FILE = "sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
	#open the file
	opened_file = open(raw_file)
	#put it in an object #CSV stands for comma seperated values, who knew!
	csv_data = csv.reader(opened_file, delimiter=delimiter)
	#create and empty list
	parsed_data = []

	#skip over the first line in csv_data, which is the header
	#I will have to double check this later, but next seemed to open the first line, and functioned like readline
	fields = next(csv_data)

	#The iteration, the zip returns an iterator of tuples, that aggregated fields and rows. This turns into a dict object which is appended to the list.
	#Essentially, parsed_data is a list of dict objects formed through the zip() function.
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))

	opened_file.close()

	return parsed_data
	#where parsed_data is a list 

def main():
	#this I have to learn more about
	#Call our fuction
	print_this = parse(MY_FILE, ',')
	print(print_this)

if __name__ == "__main__":
	main()








"This graph.py functions takes our last file and adds to it"

from collections import Counter

import csv
import matplotlib.pyplot as plt 
import numpy as np 

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


def visualize_days():
	"""visualize data by days of week"""
	data_file = parse(MY_FILE, ",")
	#parsed data is a list of dictionary objects
	counter = Counter(item["DayOfWeek"] for item in data_file)
	#The above list comprehension iterates through items in data_file. Because data_file is a list of dictionaries, DaysOfWeek is the key,
	#and the value of the key is returned.  
	#Counter creates a dictionary, it recieves the values of the data_file and sets them as keys for counter object. 
	"""
	A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as 
	dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero 
	or negative counts. The Counter class is similar to bags or multisets in other languages.
	print(counter)
	An object is hashable if it has a hash value which never changes during its lifetime
	Python dictionaries are also known as associative arrays or hash tables
	A hash function is any function that can be used to map digital data of arbitrary size to digital data of fixed size, 
	with slight differences in input data producing very big differences in output data. The values returned by a hash 
	function are called hash values, hash codes, hash sums, or simply hashes

	"""
	#Data list creates a list in order, remembering counter is a dictionary object, data list is a list of counts in order.
	data_list = [
				  counter["Monday"],
				  counter["Tuesday"],
				  counter["Wednesday"],
				  counter["Thursday"],
				  counter["Friday"],
				  counter["Saturday"],
				  counter["Sunder"],
				]
	
	day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])
	#assigns data to a plot
	plt.plot(data_list)
	#Now assign the label to our plot, we use xsticks
	plt.xticks(range(len(day_tuple)), day_tuple) 
	# Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Days.png".  This is our graph!
	plt.savefig("Days.png")
	#and finally close the plot
	plt.clf()

def visualize_type():
	"""visualize data by category in a bar graph."""
	#Putting strings in triple quotes below the function def i believe works with the help function/

	data_file = parse(MY_FILE, ",")
	#This is just our parse functions that creates a list of dictionaries
	counter = Counter(item["Category"] for item in data_file)
	#counter creates dictionaries by counting the item, though it is a list comprehension above. 
	labels = tuple(counter.keys())
	#labels is just a touple, I'm assuming that plt.xticks takes touples 
	xlocations = np.arange(len(labels)) + 0.5
	#xlocations may the the coordinates from 0
	width = 0.5

	#The pyplot fuctions we use are bar, xticks, subplots, rcParams, savefig, and clf
	plt.bar(xlocations, counter.values(), width=width)

	plt.xticks(xlocations + width / 2, labels, rotation = 90)

	plt.subplots_adjust(bottom=0.4)

	plt.rcParams['figure.figsize'] = 12, 8
	
	plt.savefig("Type.png")

	plt.clf()

#This existed in the part 1, from the parse function.
def main():
	#this I have to learn more about
	#Call our fuction
	#visualize_days()
	visualize_type()

if __name__ == "__main__":
	main()

from bs4 import BeautifulSoup
import csv
import requests
import unicodedata 
import re


raw = requests.get(DropBox HTML)

Soup = BeautifulSoup(raw.text, 'html.parser')

csvfile = open('allan.csv', 'wb') 
spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamwriter.writerow(['name', 'link', 'location', 'tags', 'followers'])


A = Soup.find("div", class_="with_data dts27 frs86 _a _jm")
A = A.findAll("div", class_=" dts27 frw44 _a _jm")


for i in A:
	name = i.find("div", class_="name").text
	name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
	name = name.replace("\n", "")
	link = i.find("div", class_="name").find("a", class_="profile-link")['href']
	link = list_of_tags = unicodedata.normalize('NFKD', link).encode('ascii','ignore')
	link = link.replace("\n", "")
	list_of_tags = []
	tags = i.findAll("div", class_="tags")
	for x in tags:
		list_of_tags.append(x.text)
	list_of_tags = list_of_tags[0]
	list_of_tags = unicodedata.normalize('NFKD', list_of_tags).encode('ascii','ignore')
	list_of_tags = list_of_tags.split(",")
	location = list_of_tags[0]
	location = location.replace("\n", "")
	list_of_tags.pop(0)
	list_of_tags = list_of_tags[0]
	list_of_tags = list_of_tags.replace("\n", "")
	followers = i.find("div", class_="column followers selected").find("div", class_="value").text
	followers = re.findall('[0-9]+', followers)
	followers = unicodedata.normalize('NFKD', followers[0]).encode('ascii','ignore')
	spamwriter.writerow([name, link, location, list_of_tags, followers])
	print repr(name)
	print repr(link) 
	print repr(location)
	print repr(list_of_tags)
	print repr(followers)


B = Soup.findAll("div", class_=" dts27 frs86 _a _jm")

for b_item in B:
	x = b_item.findAll("div", class_=" dts27 frw44 _a _jm")
	for i in x:
		name = i.find("div", class_="name").text
		name = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
		name = name.replace("\n", "")
		link = i.find("div", class_="name").find("a", class_="profile-link")['href']
		link = list_of_tags = unicodedata.normalize('NFKD', link).encode('ascii','ignore')
		link = link.replace("\n", "")
		list_of_tags = []
		tags = i.findAll("div", class_="tags")
		for x in tags:
			list_of_tags.append(x.text)
		list_of_tags = list_of_tags[0]
		list_of_tags = unicodedata.normalize('NFKD', list_of_tags).encode('ascii','ignore')
		list_of_tags = list_of_tags.split(",")
		location = list_of_tags[0]
		location = location.replace("\n", "")
		list_of_tags.pop(0)
		list_of_tags = list_of_tags[0]
		list_of_tags = list_of_tags.replace("\n", "")
		followers = i.find("div", class_="column followers selected").find("div", class_="value").text
		followers = re.findall('[0-9]+', followers)
		followers = unicodedata.normalize('NFKD', followers[0]).encode('ascii','ignore')
		spamwriter.writerow([name, link, location, list_of_tags, followers])



csvfile.close()


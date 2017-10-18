# -*- coding: <UTF-8> -*-

import CSVReader
import WebScraper
import re
import matplotlib.pyplot as plt
import numpy

typeVsEXP = CSVReader.CSVWorker('/home/taidgh/Code/Python/Pokemon/typeVsEXP.csv', 'typeVsEXP.csv')

def listCleaner(list):
	cString = re.sub('\[|\]| |\'', '', list)
	return(cString.split(','))


def fileGen():	
	
	
	#Check if the file exsits, if it does, load type vs EXP else do the Web Scraping.
	#This makes it so if the data is already retrieved the time can be saved. 
	
	if(typeVsEXP.isFile):
		typeVsEXP.getRows([1,2])
	#Load the data
	else:	
		data = toCSV()
		typeVsEXP.createNWD(data)
		fileGen()
	#Create the file, then load the data. 

def CSVToDict():
	data = {}
	for row in typeVsEXP.rows[1:]:
		t = listCleaner(row[0])
		for ty in t: 
			if ty in data:
				data[ty].append(int(row[1]))
			else:
				data[ty] = [int(row[1])]

	return(data)

fileGen()

data = CSVToDict() 
label = ['']
spread = []

colors = ['#78C850', '#A040A0', '#F08030', '#A890F0', '#6890F0', '#A8B820', '#A8A878', '#F8D030', '#E0C068', '#EE99AC', '#C03028', '#F85888', '#B8A038', '#B8B8D0', '#98D8D8', '#705898', '#7038F8', '#705848']

for key, val in data.items():
	label.append(key)
	spread.append(val)

vplot = plt.violinplot(spread, widths = 0.5)

for patch, color in zip(vplot['bodies'], colors):
	patch.set_facecolor(color)

plt.xticks(numpy.arange(len(label) + 1), label, rotation = 45)

plt.xlabel('Pokemon Type')
plt.ylabel('Base Experience')

plt.title('Pokemon Type Versus Base Experience')
plt.show()
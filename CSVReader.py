#CSV Reader
#Author: Taidgh Robinson

#A CSV managing tool. I was reading and writing data and these were just helpful functions

import csv
import os

class CSVWorker():

	#This makes it work for all csvs and reserves the memory for rows
	def __init__(self, filepath, filename):
		self.filepath = filepath
		self.isFile = os.path.isfile(filename)
		self.rows = []

	#Only gets the rows selected. This saves memory and makes the csv reader useful for large files	
	def getRows(self, cols):

		with open(self.filepath, 'r') as cs:
			reader = csv.reader(cs)

			for row in reader:
				tempRow = []
				for col in cols:
					tempRow.append(row[col])

				self.rows.append(tempRow)

	#Filters out any rows where a column contains any amount of keywords.			
	def filter(self, rowNum, kws):
		temp = []

		for row in self.rows:
			if(row[rowNum] not in kws):
				temp.append(row)

		self.rows = temp

	def createNWD(self, data): #Create mew with data

		with open(self.filepath, 'w') as f: 
			writer = csv.writer(f, dialect='excel', lineterminator = '\n')
			for row in data:
				writer.writerow([row[0]] + [row[1]] + [row[2]])
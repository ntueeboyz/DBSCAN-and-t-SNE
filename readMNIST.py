"""
Read the csv file and output as a array
The first column should be digit label.
The fisrt row shold be the pixel label.
The matrix from second column and second row is the Sample (digits) X feature (brightness value of pixels)

"""

import numpy as np
import csv

def readMNIST_CSV(fileName):
	with open(fileName, newline = '') as csvfile:
		minst_csv = csv.reader(csvfile)
		
		data = []
		label = []
		rowCount = 0
		for row in minst_csv:
			if rowCount > 0: # Exclude the fisrt row (the pixel row)
				label.append(row[0])
				data.append(row[1:])

			rowCount += 1

		# Transform strings to integers
		for i in range(len(data)):
			label[i] = int(label[i])
			for j in range(len(data[i])):
				data[i][j] = int(data[i][j])

		return label, data
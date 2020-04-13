"""
Plot the dimensional reduction data on 2-D space
The data should include the labels.
label: 1-D array
embedded_data: 2-D array
fileName: string ('file_name.png')

"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('muted')
sns.set_context("notebook", font_scale=1.5, 
	rc={"lines.linewidth": 2.5})

def DR_Plot(label, embedded_data, fileName):
	uniqueLabel = np.unique(label)
	palette = np.array(sns.color_palette("hls", len(uniqueLabel)))

	f = plt.figure(figsize=(15, 15))
	plt.axis('off')

	for i in range(len(uniqueLabel)):
		plotDataX = []
		plotDataY = []
		for j in range(len(label)):
			if uniqueLabel[i] == label[j]:
				plotDataX.append(embedded_data[j,0])
				plotDataY.append(embedded_data[j,1])

		plt.scatter(plotDataX, plotDataY, c = np.tile(palette[i], (len(plotDataX),1)),
			label = uniqueLabel[i])

	plt.legend(loc = 'best', fontsize = 15)
	plt.savefig(fileName)



def DR_Plot_black(label, embedded_data, fileName):
	uniqueLabel = np.unique(label)

	f = plt.figure(figsize=(15, 15))
	plt.axis('off')

	for i in range(len(uniqueLabel)):
		plotDataX = []
		plotDataY = []
		for j in range(len(label)):
			if uniqueLabel[i] == label[j]:
				plotDataX.append(embedded_data[j,0])
				plotDataY.append(embedded_data[j,1])

		plt.scatter(plotDataX, plotDataY, c = 'k')

	plt.savefig(fileName)

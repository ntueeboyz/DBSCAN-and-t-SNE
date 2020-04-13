

from readMNIST import readMNIST_CSV
import numpy as np
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from DR_Plot import DR_Plot
from DR_Plot import DR_Plot_black
from sklearn.cluster import DBSCAN
import xlwt

# Import the data from the csv file
label, data = readMNIST_CSV('train.csv')

# Select the very first 300 data samples of each digit
sel_data = []
sel_label = []
idx = 0
for i in range(0,len(label),6000):
	count = 1
	for j in range(len(data)):
		sel_data.append(data[j+idx])
		sel_label.append(label[i])

		count += 1
		if count > 300:
			break
	idx += 6000

# List to array
sel_label = np.array(sel_label)
sel_data = np.array(sel_data)

# t-SNE (2-D)
tsne = TSNE(n_components=2, perplexity=30).fit_transform(sel_data)
print(tsne)

# PCA (2-D)
pca = PCA(n_components=2)
pca = pca.fit_transform(sel_data, sel_label)

# Clustering 
clustering = DBSCAN(eps=4, min_samples=20).fit(tsne)
clustering_pca = DBSCAN(eps=60, min_samples=8).fit(pca)


# Plot
DR_Plot(sel_label, tsne, 'tsne')
DR_Plot(sel_label, pca, 'pca')

DR_Plot(clustering.labels_, tsne, 'clustering_tsne')
DR_Plot(clustering_pca.labels_, pca, 'clustering_pca')

DR_Plot_black(sel_label, tsne, 'tsne_black')
DR_Plot_black(sel_label, pca, 'pca_black')

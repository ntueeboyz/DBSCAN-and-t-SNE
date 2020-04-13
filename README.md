# DBSCAN-and-t-SNE

## Functions description
### main.py
The main function imports the MNIST csv file and reduces the high dimensionality to 2-D.
Then plots the t-SNE figure with labels and the t-SNE figure with DBSCAN clustering.

### DR_plot.py
The file includes two functions, DR_Plot and DR_Plot_black. 

#### DR_plot:
Input sample labels, n x 2 embedded array, and the "filename" you want to save.
The output would be the scatter figure with color label depending on samples.

#### DR_plot_black:
Input sample n x 2 embedded array, and the "filename" you want to save.
The output would be the scatter figure.

### readMNIST.py
To import the MNIST csv file and output with the data matrix and sample labels.

## Result
### t-SNE with sample labels
![Image description](https://github.com/NTUEEboy/DBSCAN-and-t-SNE/blob/master/figure/tsne.png)
### t-SNE clustered by DBSCAN
![Image description](https://github.com/NTUEEboy/DBSCAN-and-t-SNE/blob/master/figure/clustering_tsne.png)

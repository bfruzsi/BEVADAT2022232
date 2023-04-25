import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
from scipy.stats import mode
from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_digits
import pandas as pd

class KMeansOnDigits:
    def __init__(self, n_clusters, random_state):
        self.n_clusters = n_clusters
        self.random_state = random_state
        self.dataset = []

    def load_dataset(self):
        self.dataset = load_digits()

    def predict(self):
        kmeans = KMeans(n_clusters = 10, random_state = 0)

        self.clusters = kmeans.fit_predict(self.dataset.data)

    def get_labels(self):
        result_array = np.zeros(len(self.clusters)) #kmeans_pred
        for i in range(len(self.clusters)):
            mask = (self.clusters == i)
    
            xd = self.dataset.target[mask]
        d_mode, kaki = mode(xd)

        result_array[mask] = d_mode
        print(d_mode)
        print(kaki)
        print(result_array)
        return result_array

    def calc_accuracy(self):
        self.predicted_labels = self.get_labels()
        self.accuracy = accuracy_score(self.dataset.target, self.predicted_labels)
        return self.accuracy.round(decimals=2)

    def confusion_matrix(self):
        conf_matrix = confusion_matrix(self.clusters, self.predicted_labels)
        sns.heatmap(conf_matrix, annot = True)
    

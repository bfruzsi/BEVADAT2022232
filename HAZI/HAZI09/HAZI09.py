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

    def load_dataset(self):
        self.digits = load_digits()

    def predict(self):
        self.kmeans = KMeans(n_clusters = self.n_clusters, random_state = self.random_state)

        self.clusters = self.kmeans.fit_predict(self.digits.data, self.digits.target)

    def get_labels(self):
        self.labels = np.empty(shape=self.clusters.shape) #kmeans_pred
        for i in range(len(self.clusters)):
            mask = (self.clusters == i)
    
            self.labels[mask] = mode(self.digits.target[mask], keepdims=False).mode

    def calc_accuracy(self):
        self.accuracy = np.round(accuracy_score(self.digits.target, self.labels), 2)
        # self.rounded_acc = self.accuracy.round(decimals=2)

    def confusion_matrix(self):
        self.mat = confusion_matrix(self.digits.target, self.labels)
        # sns.heatmap(conf_matrix, annot = True)
    

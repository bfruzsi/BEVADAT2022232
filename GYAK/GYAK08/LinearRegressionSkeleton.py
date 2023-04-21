import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr
        self.m = 0
        self.c = 0
        self.losses = []

        # self.iris = load_iris()
        # self.df = pd.DataFrame(self.iris.data, columns=self.iris.feature_names)


    def fit(self, X: np.array, y: np.array):
        L = 0.0001  # The learning Rate

        n = float(len(X)) # Number of elements in X

        # Performing Gradient Descent 
        
        for i in range(self.epochs): 
            y_pred = self.m * X + self.c  # The current predicted value of Y

            residuals = y - y_pred
            loss = np.sum(residuals ** 2)
            self.losses.append(loss)
            D_m = (-2/n) * sum(X * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + L * D_m  # Update m
            self.c = self.c + L * D_c  # Update c


    def predict(self, X):
        return self.m * X + self.c
    

    def evaluate(self, X, y):
        pred = self.predict(X)
        return np.mean((pred - y)**2)

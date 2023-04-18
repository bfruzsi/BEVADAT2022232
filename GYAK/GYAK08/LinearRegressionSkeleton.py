import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs = epochs
        self.lr = lr

        self.iris = load_iris()
        self.df = pd.DataFrame(self.iris.data, columns=self.iris.feature_names)

    def fit(self, X: np.array, y: np.array):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Building the model
        self.m = 0
        self.c = 0

        L = 0.0001  # The learning Rate
        # epochs = 5000  # The number of iterations to perform gradient descent

        n = float(len(self.X_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(self.epochs): 
            y_pred = self.m * self.X_train + self.c  # The current predicted value of Y

            residuals = y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            self.m = self.m + L * D_m  # Update m
            self.c = self.c + L * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(self.y_train-y_pred))

    def predict(self, X):
        self.y_pred = self.m * X + self.c
        plt.scatter(self.X_test, self.y_test)
        plt.plot([min(self.X_test), max(self.X_test)], [min(self.y_pred), max(self.y_pred)], color='red') # predicted
        plt.show()

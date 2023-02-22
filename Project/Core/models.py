import pandas as pd
import numpy as np

from sklearn.svm import SVR
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV

class Models:

    def __init__(self):
        self.reg = {
            'SVR': SVR(),
            'GBR': GradientBoostingRegressor()
        }

        self.params = {
            'SVR': {
                'kernel': ['linear', 'poly', 'rbf'],
                'C': [1, 5, 10],
                'gamma': ['auto', 'scale']
            },
            'GBR': {
                'loss': ['squared_error', 'absolute_error'],
                'learning_rate': [0.01, 0.05, 0.1],
            }
        }
    
    def get_best_model(self, X, y):

        best_model = None
        best_score = 0

        for name, model in self.reg.items():
            grid = GridSearchCV(model, self.params[name], cv=3)
            grid.fit(X, y.values.ravel())
            score = np.abs(grid.best_score_)

            if score > best_score:
                best_score = score
                best_model = grid.best_estimator_
        
        return best_model, best_score
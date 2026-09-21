# This is a file for sample linear regression.

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from statsmodels.api import OLS
from matplotlib import pyplot as plt


# Create some data.
n, k, eps = 1000, 10, 1e-3
X = np.random.random((n, k))
beta = np.random.random((k, 1))
y = X.dot(beta) + np.random.random((n, 1))*eps

# Create sklearn model.
model = LinearRegression()
model.fit(X, y)
y_hat = model.predict(X)
print(model.get_params())

# Create statsmodels model.
model = OLS(y, X)
res = model.fit()
print(res.summary())
y_hat = model.predict(X)



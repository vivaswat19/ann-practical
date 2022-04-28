from pylab import plot, axis, show, pcolor, colorbar, bone
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range=(0, 1))
data = pd.read_csv('creditcard.csv')

X = data.iloc[:, 1:14].values
y = data.iloc[:, -1].values
X = sc.fit_transform(X)

som_grid_rows = 10
som_grid_columns = 10
iterations = 20000
sigma = 1
learning_rate = 0.5
som = MiniSom(x=som_grid_rows, y=som_grid_columns, input_len=13,
              sigma=sigma, learning_rate=learning_rate)

som.random_weights_init(X)

# Training
som.train_random(X, iterations)
bone()
pcolor(som.distance_map().T)
colorbar()

markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor=colors[y[i]],
         markerfacecolor='None',
         markersize=10,
         markeredgewidth=2)
show()

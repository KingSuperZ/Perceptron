import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import Perceptron

X = np.array([[1],[4],[5],[0]])
y = np.array([-1,1,1,-1])

alg = Perceptron()
alg.fit(X,y)

zeros = np.zeros(len(X))
plt.scatter(X,zeros, c = y)

slope = alg.coef_
yint = alg.intercept_

m = slope[0,0]
b = yint[0]

xpoints = np.array([0,1,2,3,4,5])
ypoints = m*xpoints+b
xint = -b/m # calculation for the x intercept
plt.plot(xpoints,ypoints)
plt.scatter(xint,0, marker = "x")
plt.hlines(y = 1, xmin = xint, xmax = max(X), colors = "red")
plt.hlines(y = -1, xmin = xint, xmax = min(X), colors = "red")
plt.vlines(x = xint, ymin = -1, ymax = 1, colors = "red")
plt.hlines(y = 0, xmin = -1, xmax = 7, colors = "black", linewidths = 1)
plt.vlines(x = 0, ymin = -3, ymax = 2, colors = "black", linewidths = 1)
plt.axis("equal")
plt.grid()

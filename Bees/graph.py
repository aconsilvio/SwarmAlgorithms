import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import random
import bees
import helper
import matplotlib.animation as animation

def fun(x, y):
  return 4000 - 100 * (x**2 - y)**2 - (1 -x)**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(helper.DOMAIN[0], helper.DOMAIN[1], .5)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

max_scout = bees.bee_algorithm([],0)
print max_scout

ax.plot_surface(X, Y, Z)

for scout in max_scout[2]:
	x = scout.position[0]
	y = scout.position[1]
	plt.plot([x], [y], [fun(x,y)],'wv')
	for f in scout.foragers:
		x = f.position[0]
		y = f.position[1]
		plt.plot([x], [y], [fun(x,y)],'y^')
plt.plot([max_scout[1][0]], [max_scout[1][1]], [max_scout[0]],'ro')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
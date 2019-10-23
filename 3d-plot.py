from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

x, y, z = np.meshgrid(np.arange(-1, 1, 0.3),
                      np.arange(-1, 1, 0.3),
                      np.arange(-1, 1, 0.7))

u = (-(np.power(x, 2) + np.power(y, 2))*y)
v = ((np.power(x,2) + np.power(y,2)*x))
w = x * z
ax.quiver(x, y, z, u, v, w, length=0.3)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()

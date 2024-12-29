import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10,6),dpi=128)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors='none',s=10)
ax.set_aspect('equal')

#emphasize the first and the last point
ax.scatter(0,0,c="green",edgecolors='none',s=10)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=10)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.set_title("Random Walk Visualization")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
plt.show()

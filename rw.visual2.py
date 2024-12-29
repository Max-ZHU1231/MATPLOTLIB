import matplotlib.pyplot as plt

from random_walk import RandomWalk

rw = RandomWalk(500)
rw.fill_walk()


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10,6),dpi=128)
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth=1)
ax.set_aspect('equal')

#emphasize the first and the last point
ax.scatter(0,0,s=10,color='Red')
ax.scatter(rw.x_values[-1],rw.y_values[-1],s=10,color='green')

ax.set_title("Random Walk Visualization")
ax.set_xlabel("X Values")
ax.set_ylabel("Y Values")
plt.show()
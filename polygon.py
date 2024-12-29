import matplotlib.pyplot as plt

fig, (ax_1, ax_2) = plt.subplots(1, 2, dpi=500)

x = [0,1,2,3,4,5]
y_1 = [0,1,4,9,16,25]
y_2 = [1,2,3,4,5,6]

ax_1.plot(x,y_1,'r-')
ax_1.set_title('First Plot')
ax_1.set_xlabel('X axis')
ax_1.set_ylabel('Y axis')

ax_2.plot(x,y_2,'g--')
ax_2.set_title('Second Plot')
ax_2.set_xlabel('X axis')
ax_2.set_ylabel('Y axis')

plt.legend()
plt.tight_layout()

plt.show()
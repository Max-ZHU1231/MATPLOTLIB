import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, vert=True, patch_artist=True)

plt.title('箱型图示例')
plt.xlabel('组别')
plt.ylabel('值')

plt.xticks([1, 2, 3], ['组1', '组2', '组3'])

print()
plt.show()
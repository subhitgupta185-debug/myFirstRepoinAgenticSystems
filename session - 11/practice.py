import numpy as np

data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(data.mean())

mean = data.mean(axis=0)
mean2 = data.mean(axis=1)

print(mean)
print(mean2)

import numpy as np

np.random.seed(42)

data = np.random.randn(100, 3)

mean = data.mean(axis=0)
std = data.std(axis=0)

normalize = (data - mean) / std

train = normalize[:80]
test = normalize[80:]

train[0, 0] = 999

print("original data shape:", data.shape)
print("Mean shape : ", mean.shape)
print("Std shape : ", std.shape)
print("Train shape : ", train.shape)
print("test shape:", test.shape)
print("Notes : Modifying slice affected orignal array")
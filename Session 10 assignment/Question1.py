import numpy as np

data = np.array([10,20,30,40])
mean = np.mean(data)
std = np.std(data)

normalized = (data - mean ) / std

reshape = normalized.reshape( 4 , 1)

print("Your data is : ", data)
print("Your mean is : ", mean)
print("STD : ", std)
print("Normalized data : ", normalized)
print("Data after reshape : ", reshape)
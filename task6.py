import numpy as np

x = np.ones((8, 8))
print('Before:')
print(x)

# Your code goes here
lenght,height = np.shape(x)

for i in range(1, lenght-1):
    for j in range(1,height-1):
        x[i][j] = 0

print('After:') 
print(x)
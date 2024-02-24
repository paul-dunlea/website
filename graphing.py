import numpy as np #imports numpy as np ( ability for statistics functions)
import matplotlib.pyplot as plt
#imports and uses csv reader function
import csv
with open('sen.csv', 'r') as f:
    temp = list(csv.reader(f, delimiter=';'))
    print(temp[:])
temp = np.genfromtxt("sen.csv", delimiter=",", dtype="float")#assigns a float values as default data types

print('Shape: ', temp.shape)
print('Datatype: ', temp.dtype)
print('Size: ', temp.size)

import matplotlib.pyplot as plt
plt.plot(temp)
plt.title("Temperature Reading")
plt.xlabel("")
plt.ylabel("Temp")
plt.show()


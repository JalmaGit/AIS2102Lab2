import numpy as np

last20rpm = np.zeros((20,),dtype=int)

for i in range(0,30,1):
    last20rpm = np.delete(last20rpm, 19, None)
    last20rpm = np.insert(last20rpm, 0, i)

print(last20rpm)
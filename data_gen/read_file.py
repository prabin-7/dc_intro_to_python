import numpy as np
data = []
from data_gen.main import filename             #tala terminal ma k khuleko xa teslae ni farak parxa 
print(filename)
with open(filename,'r+') as file:
    next(file)
    for line in file:
        row = line.strip().split(',')
        height = row[0]
        weight = row[1]
        data.append([height,weight])

loaded_np_city = np.array(data)
print(loaded_np_city)
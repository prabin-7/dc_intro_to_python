import numpy as np
filename = 'city.txt'
# import random          #dont need this line because we using numpy's random seed generator!!
if __name__ == '__main__':
    np.random.seed(1)
    height = np.round(np.random.normal(1.75,0.20,5000),2)
    weight = np.round(np.random.normal(60.32,15,5000),2)

    np_city = np.column_stack((height,weight))

    print(np_city[0,:])

   

    with open(filename,'w') as file:
        header = 'height,weight\n'
        file.write(header)
        for row in np_city:
            file.write(f'{row[0]},{row[1]}\n')
    print(f'data saved to {filename}')

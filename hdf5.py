import numpy as np
import h5py

x = np.linspace(0,5000,0.001)
y = np.sin(x)

f = open('data.txt','w')

for i in range(len(x)):
    f.write(("%f \t %f \n")%(x[i],y[i]))
f.close()

data_array = np.vstack((x,y))
write_file = h5py.File('data_set.h5')
write_file['data_1'] = data_array
write_file.close()
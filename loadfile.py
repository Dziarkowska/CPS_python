import numpy as np

def fread(filename, nelements, dtype):

	fid = open(filename, 'rb')
	if dtype is np.str:
         dt = np.uint8  # WARNING: assuming 8-bit ASCII for np.str!
	else:
         dt = dtype
	data_array = np.fromfile(fid, dt, nelements)
	data_array.shape = (nelements, 1)

	return data_array

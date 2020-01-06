
import numpy as np

def loadfile2(filename):

	with open(filename, 'rb') as data_file:
		dtype = np.dtype([('i','<i2'), ('q','<i2')])
		array = np.fromfile(data_file, dtype=dtype)
		print('data loaded')
		array = [complex(*item) for item in array]
		print('data edited')

	#print(array)
	return array
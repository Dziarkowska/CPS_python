import numpy as np
import math
import multiply_arrays as multi_arr
import matplotlib.pyplot as plt


def signal_shifting(params, data):

	time = np.arange(0.0,len(data)-1.0)
	time[:] = [x/params['fp'] for x in time] 
	arg = 2*math.pi*(params['shift']*time)

	shifted = multi_arr.multiply_arrays(data,arg)

	data = np.asarray(data[:-1])
	time = np.asarray(time)
	shifted = np.asarray(shifted)

	print(data.size, time.size, shifted.size)

	fig1, (ax1, ax2) = plt.subplots(2,num=1, clear=True, sharex=True)
	line1, = ax1.plot(time,data, 'navy')
	line2, = ax2.plot(time, shifted, 'orchid')
	plt.show()

	return shifted




import numpy as np
import math
import matplotlib.pyplot as plt


def signal_shifting(params, data):
	time = np.arange(0.0,len(data)-1.0)
	time[:] = [x/params['fp'] for x in time] 
	#arg = 2*math.pi*(params['shift']*time)
	#shifted_1 = data*math.cos(arg)
	#shifted_2 = -data*math.sin(arg)
	#shifted = shifted_1 + 1j*shifted_2

	#fig1, ax1 = plt.subplots(num=1, clear=True)
	#line1, = ax1.plot(time,data, 'navy')
	#line2, = ax1.plot(time, shifted, 'orchid')

	#return shifted




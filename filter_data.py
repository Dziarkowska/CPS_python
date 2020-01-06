import numpy as np
import math
import fir1
from scipy import signal
import matplotlib.pyplot as plt

def filter_data(params, shifted_data):

	filtered_data = []

	fir_coeff = signal.firwin(params['len'],params['band']/params['fp'], window='blackman')
	fir = fir1.Fir1(fir_coeff)

	for i in range(len(shifted_data)):
		filtered_data.append(fir.filter(float(shifted_data[i])))

	time = np.arange(0.0,len(shifted_data)-1.0)
	time[:] = [x/params['fp'] for x in time]
	filtered_data = np.asarray(filtered_data[:-1])
	time = np.asarray(time)

	fig2, ax3 = plt.subplots(num=1,clear=True)
	line3, = ax3.plot(time,filtered_data, 'g')
	plt.title('Filtered data')
	plt.show()

	return filtered_data


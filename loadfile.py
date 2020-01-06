import math
import numpy as np

def loadfile(filename):
	with open(filename, 'rb') as f:
		#iq = f.readlines()
		#for i in range(1,len(iq)-2):
			#data = iq[2*i-1] + 1j*iq[2*i]
		#iq = [float(n) for n in f]
		iq_array = np.fromfile(f, np.int8) #cos mi tu nie pasuje z ta konwersja, pomysly mile widziane
		#print('data loaded')
		print(iq_array[0:10])

		for i in range(0,len((iq_array)/2)-2):
			data = iq_array[2*i] + 1j*iq_array[2*i+1]

		#print(data[1:10])		

	return data
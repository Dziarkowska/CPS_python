import math
import numpy as np



def multiply_arrays(data, arg):
	shifted_1 = []
	shifted_2 = []
	shifted = []
	for i in range(0,len(data)-1):
		shifted_1.append(data[i]*math.sin(arg[i]))
		shifted_2.append(-data[i]*math.cos(arg[i]))
		shifted.append(shifted_1[i] + 1j*shifted_2[i])
	return shifted
import loadfile2
import signal_shifting
import filter_data
import numpy as np
import loadfile

#data1 = loadfile2.loadfile2('gqrx_20191214_143406_433502000_1800000_fc.raw')
data = loadfile.fread('gqrx_20191214_143406_433502000_1800000_fc.raw',8323967, np.complex64)
data_size = len(data)

params = {
    'fp': 1.8e6,
    'len': 99,
    'shift': -0.3965e6,
    'band' : 0.1e6,
}

data_shifted = signal_shifting.signal_shifting(params,data)

data_filtered = filter_data.filter_data(params, data_shifted)

import asyncio
import queue
import rtlsdr
import time
import threading
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
# sdr.sample_rate = 250e3  # Hz
# sdr.center_freq = 433.9e6     # Hz
# sdr.freq_correction = 60   # PPM
# sdr.gain = 'auto'

class RawDataStreamRaeder(threading.Thread):
    def __init__(self, sample_rate, center_freq):
        self.samples_buffer = []

        self.sdr = rtlsdr.RtlSdr()
        self.sdr.sample_rate = sample_rate
        self.sdr.center_freq = center_freq
        self.sdr.freq_correction = 60
        self.sdr.gain = 'auto'

        threading.Thread.__init__(self)
        self.running = True

    def run(self):
        self.ReadSamples()

    def ReadSamples(self):
        while self.running:
            self.samples_buffer = self.sdr.read_samples(256*1024)
    
    def GetSamplesBuffer(self):
        return self.samples_buffer

    def Stop(self):
        self.running = False
        self.sdr.close()


class Plotter(threading.Thread):
    def __init__(self):
        self.NFFT = 1024
        threading.Thread.__init__(self)

    def plot(self, samples, sdr_sample_rate, sdr_center_freq):
        fig = plt.figure()
        graph_out = fig.add_subplot(1, 1, 1)
        graph_out.psd(samples, self.NFFT, sdr_sample_rate/1e6, sdr_center_freq/1e6)
        plt.show()

if __name__ == '__main__':
    sdr_sample_rate = 250e3
    sdr_center_freq = 433.9e6
    rawDataStreamRaeder = RawDataStreamRaeder(sdr_sample_rate,sdr_center_freq)
    rawDataStreamRaeder.start()   
    
    time.sleep(15)

    plotter = Plotter()
    plotter.plot(rawDataStreamRaeder.GetSamplesBuffer(), sdr_sample_rate, sdr_center_freq)

    rawDataStreamRaeder.join()
import numpy
import matplotlib.pyplot as plt
#import pandas as pd

paper = numpy.loadtxt(r'C:\Users\Nihal\Desktop\average spectra\paper\paper.txt')
tape = numpy.loadtxt(r'C:\Users\Nihal\Desktop\average spectra\tape\tape.txt')
waves = numpy.loadtxt(r'C:\Users\Nihal\Desktop\average spectra\tape\waves.txt')

plt.plot(waves, paper/tape, 'r')
plt.ylabel('Contrast, paper reflectance/ tape reflectance')
plt.show()

#what is in the csv file!!!
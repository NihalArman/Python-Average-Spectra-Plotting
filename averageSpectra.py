import matplotlib.pyplot as plt
import numpy
import tkinter
from tkinter import*

#Read Spectral Image
path = r'F:\PHD\UEF Thesis\image set\card photogrammetry\Green paper photogrametry spectral images set\409\capture'

#Read HDR Content
hdr_path = r'F:\PHD\UEF Thesis\image set\card photogrammetry\Green paper photogrametry spectral images set\409\capture\409.hdr'

SpectralSample = 0
SpectralBand = 0
SpectralLine = 0

def read_hdr(hdr_path):
    f=open(hdr_path, "r")
    filelines = f.readlines()

    # This reads everything from hdr file
#     for fileline in filelines:
#         print(fileline)
# read_hdr(hdr_path)
    f.close()
    bands = ''
    for fileline in filelines:
        if 'samples' in fileline.lower():
            samples = int(fileline.replace('samples = ',''))
            #print("print sample: ", end ='')
            #print(samples)

            #saving the value globally
            global SpectralSample
            SpectralSample = samples
        if bands == '' and 'bands' in fileline.lower():
            bands = int(fileline.replace('bands = ',''))
            #print(bands)

            # saving the value globally
            global SpectralBand
            SpectralBand = bands
        if 'lines' in fileline.lower():
            lines = int(fileline.replace('lines = ',''))
            # saving the value globally
            global SpectralLine
            SpectralLine = lines

#run function
read_hdr(hdr_path)
#print
print("print spectral sample: ", end ='')
print(SpectralSample)

print("print spectral band: ", end ='')
print(SpectralBand)

print("print spectral lines: ", end ='')
print(SpectralLine)

#Read Waves
n = 0

f=open(hdr_path, "r")
filelines = f.readlines()
bands = ''
n1 = filelines.index('wavelength = {\n')+1
n2 = n1 + SpectralBand
#print(n1)
#print(n2)

waves = numpy.zeros(n2-n1,)
for i in range(n1,n2):
    waves[n] = float(filelines[i].replace(',\n', ''))
    n=n+1

#print waves

# print('print waves = ')
# for wave in waves:
#     print(wave)

#_______________________________________________________________________________

#--------------------FINDING AVERAGE OF 2 PLOT---------------------------------
spatial_pixels = 512
sample_lines = 512
spectral_bands = 204
open_path = r'F:\PHD\UEF Thesis\image set\card photogrammetry\Green paper photogrametry spectral images set\409\capture\409.raw'
fopen = open(open_path, "rb")
u = numpy.fromfile(fopen, dtype=numpy.uint16) #uint16 float32 #count=spatial_pixels*sample_lines*spectral_bands
print(u.shape)
print(spatial_pixels*sample_lines*spectral_bands)
spectral_image = numpy.reshape(u, (sample_lines, spectral_bands, spatial_pixels))
print(spectral_image.shape)
#_--------------------------------------


# tape x1=305 x2=310 y1=275 y2=280
# paper x1=320 x2=325 y1=275 y2=280
#Tape area:
w=161
#tape---
x1 = 295
x2 = 300
y1 = 245
y2 = 250

#paper---
# x1 = 300
# x2 = 305
# y1 = 275
# y2 = 280
# image the area we want to average
# spectral_image[x1:x2,w,y1:y2]=1000
# plt.imshow(spectral_image[:,w,:], cmap="gray")
# print(waves[w])
# plt.show()
x =  x2-x1
y =  y2-y1
n = 0
average = numpy.arange(spectral_bands)
for i in range(x1,x2):
    for j in range(y1,y2):
        plt.plot(waves, spectral_image[i,:,j], 'b')
        average = average + spectral_image[i,:,j]
        n = n + 1
plt.plot(waves, average/n, 'r')
plt.show()
savefile = r'C:\Users\Nihal\Desktop\exam prep\tape.txt'
numpy.savetxt(savefile, average)
savefile = r'C:\Users\Nihal\Desktop\exam prep\waves.txt'
numpy.savetxt(savefile, waves)

#just comment tape x1,x2,y1,y2
#and comment out paper x1,x2,y1,y2
#save as paper.txt
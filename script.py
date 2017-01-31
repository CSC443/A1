from pylab import *
from numpy.linalg import norm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy import misc
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import urllib


KB = 1024
MB = 1024 * 1024
sizes = [512,1 * KB,4 * KB,8 * KB,16 * KB,32 * KB,  1 * MB,2 * MB,4 * MB]
filenames = ["data_0.dat", "data_1.dat", "data_2.dat", "data_3.dat", "data_4.dat", "data_5.dat", "data_6.dat", "data_7.dat", "data_8.dat"]
filenames_csv = ["edges.csv", "edges_1.csv",  "edges_2.csv",  "edges_3.csv",  "edges_4.csv",  "edges_5.csv",  "edges_6.csv",  "edges_7.csv",  "edges_8.csv"]
def write_blocks_seq():
    #os.system("ls -l")
    # KB = 1024
    # MB = 1024 * 1024
    # sizes = [512,1 * KB,4 * KB,8 * KB,16 * KB,32 * KB,  1 * MB,2 * MB,4 * MB]
    for  i in range(0, len(sizes)) :
        # file = ""
        # if(i % 2 == 0):
        #     file = filenames_csv[0]
        # else:
        #     file = filenames_csv[1]
        os.system("./write_blocks_seq "+ filenames_csv[i] + " "+ str(sizes[i]))

def plot_exp1():
    
    y=[33183688.000,36218948.000,38568068.000,38708028.000,38930984.000,38818084.000,39519208.000,39505484.000,38926544.000]         
    
    
    
    x=[512,1024,4096,8192,16384,32768,1048576,2097152,4194304]


    fig = plt.figure()
    
    
    
    width = .35
    ind = np.arange(len(y))
    plt.bar(ind, y, width=width, color=(0.2588,0.4433,1.0), label="block_size")
    
    plt.xticks(ind + width / 2, x)
    
    fig.autofmt_xdate()
    plt.xlabel('Block size (bytes)')
    plt.ylabel('Write Speed (BPS)')
    plt.title('Write Speed by different block size')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
    fancybox=True, shadow=True, ncol=5)
    plt.show()    
         

def write_lines(filename):
    os.system("./write_lines "+filename )
         
         
def read_blocks_seq():
    for i in range(0,9) :
        # file = ""
        # if (i % 2 == 0):
        #     file = filenames[0]
        # else:
        #     file = filenames[1]
        os.system("./read_blocks_seq "+ filenames[i] + " "+ str(sizes[i]))

def read_ram_seq():
    # for  i in range(0,9) :
    #     file = ""
    #     if (i % 2 == 0):
    #         file = filenames[0]
    #     else:
    #         file = filenames[1]
    os.system("./read_ram_seq "+ filenames[0])

def read_blocks_rand():
    for  i in range(0,9):
        # file = ""
        # if (i % 2 == 0):
        #     file = filenames[0]
        # else:
        #     file = filenames[1]
        os.system("./read_blocks_rand "+ filenames[i] + " " + str(sizes[i]) + " 100")

def read_ram_rand():
    for i in range(0, 9):
        os.system("./read_ram_rand "+ filenames[i] + " " + str(sizes[i]) + " 100")

def write_blocks_rand():
    os.system("./write_blocks_rand " + "data_write1.dat" + " 10000")

def write_ram_rand():
    os.system("./write_ram_rand " + "data_write2.dat" + " 10000")
#85331845L
#write_blocks_seq()

#write_lines("edges_1.csv")
#read_ram_seq()
#read_blocks_rand()
read_ram_rand()
#read_blocks_seq()

#write_blocks_rand()

#write_ram_rand()
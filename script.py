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

def write_blocks_seq(filename):
    #os.system("ls -l")
    # KB = 1024
    # MB = 1024 * 1024
    # sizes = [512,1 * KB,4 * KB,8 * KB,16 * KB,32 * KB,  1 * MB,2 * MB,4 * MB]
    for  i in sizes : 
         os.system("./write_blocks_seq "+filename + " "+ str(i))

def plot_exp1():
    
    y=[33183688.000,36218948.000,38568068.000,38708028.000,38930984.000,38818084.000,39519208.000,39505484.000,38926544.000]         
    
    
    
    x=[512,1024,4096,8192,16384,32768,1048576,2097152,4194304]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x,y)
    
    #plt.axis([0,8000000, 0,60000000])
    ax.set_xlabel('block sizes in bytes')
    ax.set_ylabel('writing speed in mbps')
    ax.set_title('block size vs  wrting speed')
    plt.show()
         

def write_lines(filename):
         os.system("./write_lines "+filename )
         

                 
         
         
         
def read_blocks_seq(filename):
    for  i in sizes : 
         os.system("./read_blocks_seq "+filename + " "+ str(i))

from pylab import *
import os



KB = 1024
MB = 1024 * 1024
sizes = [512,1 * KB,4 * KB,8 * KB,16 * KB,32 * KB,  1 * MB,2 * MB,4 * MB]
big_files = ["big.dat", "big_0.dat"]
filenames = ["data_0.dat", "data_1.dat", "data_2.dat", "data_3.dat", "data_4.dat", "data_5.dat", "data_6.dat", "data_7.dat", "data_8.dat"]
filenames_csv = ["edges.csv", "edges_1.csv",  "edges_2.csv",  "edges_3.csv",  "edges_4.csv",  "edges_5.csv",  "edges_6.csv",  "edges_7.csv",  "edges_8.csv"]
def write_blocks_seq():

    for  i in range(0, len(sizes)) :
        os.system("./write_blocks_seq "+ filenames_csv[i] + " "+ str(sizes[i]))
         

def write_lines(filename):
    os.system("./write_lines "+filename )
         
         
def read_blocks_seq():
    for i in range(0,9) :
        os.system("./read_blocks_seq "+ filenames[i] + " "+ str(16 * KB))

def read_ram_seq():
    for  i in range(0,9) :
        os.system("./read_ram_seq "+ filenames[i])

def read_blocks_rand():
    for  i in range(0,9):
        os.system("./read_blocks_rand "+ filenames[i] + " " + str(16 * KB) + " 100")

def read_ram_rand():
    for i in range(0, 9):
        os.system("./read_ram_rand "+ filenames[i] + " " + str(16 * KB) + " 100")

def write_blocks_rand():
    os.system("./write_blocks_rand " + "data_write1.dat" + " 10000")

def write_ram_rand():
    os.system("./write_ram_rand " + "data_write2.dat" + " 10000")

write_blocks_seq()
write_lines("edges_1.csv")
read_ram_seq()
read_blocks_rand()
read_ram_rand()
read_blocks_seq()
write_blocks_rand()
write_ram_rand()
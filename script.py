import os


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
         
         
         
def read_blocks_seq(filename):
    for  i in sizes : 
         os.system("./read_blocks_seq "+filename + " "+ str(i))

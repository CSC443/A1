import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.tools as tls

MB = 1024 * 1024

def plot_from_file_read(filenames):
    y = []
    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")

        for line in f:
            line = line.strip('\n')
            if (int(line.split(',')[0]) == 0):
                x.append(filenames[i])
            else:
                x.append(int(line.split(',')[0]))
            y.append(float(line.split(',')[1]) * MB)
    y = np.log10(y)
    fig = plt.figure()

    width = .35
    ind = np.arange(len(y))
    result = plt.bar(ind, y, width=width, color=(0.2588, 0.4433, 1.0))
    result[len(y) - 1].set_color('r')
    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()


    #write seq
    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by different block sizes')

    plt.xlabel('Block size(Bytes)')
    plt.ylabel('Read Speed(log of BPS)')
    plt.title('Read Speed by primary/secondary storage')

    plt.xlabel('Block size(Bytes)')
    plt.ylabel('Write Speed(BPS)')
    plt.title('Write Speed by block sizes')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    plt.show()


#plot_from_file("write_block_seq.txt", "")
plot_from_file_read(["read_block_seq.txt", "read_ram_seq.txt"])

def plot_exp3(filenames):
    y = []
    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")

        for line in f:
            line = line.strip('\n')
            if(int(line.split(',')[0]) == 0):
                x.append(filenames[i])
            else:
                x.append(int(line.split(',')[0]))
            y.append(float(line.split(',')[1]) * MB)


    fig = plt.figure()


    width = .35
    ind = np.arange(len(y))
    result = plt.bar(ind, y, width=width, color=(0.2588,0.4433,1.0))
    result[len(y) - 1].set_color('r')
    result[len(y) - 2].set_color('g')
    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()

    #write seq
    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by different block sizes')



    plt.xlabel('Block size(Bytes)')
    plt.ylabel('Write Speed')
    plt.title('Write Speed by seq/random')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    plt.show()

#plot_exp3(["write_block_seq.txt", "write_block_rand.txt", "write_ram_rand.txt"])
import matplotlib.pyplot as plt
import numpy as np


MB = 1024 * 1024

def plot_from_file_read(filenames):
    y = []
    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")
        x.append(filenames[i])
        for line in f:
            line = line.strip('\n')
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

    plt.xlabel('primary/secondary storage in block size 16KB')
    plt.ylabel('Read Speed(log of BPS)')
    plt.title('Read Speed by primary/secondary storage')

    plt.show()
#plot_from_file_read(["write_block_seq.txt", "write_lines.txt"])
#plot_from_file_read(["read_block_seq.txt", "read_ram_seq.txt"])

def plot_from_exp2_2(filenames):
    y = []

    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")
        x.append(filenames[i])
        for line in f:
            line = line.strip('\n')
            y.append(float(line.split(',')[1]) * MB)


    y = np.log10(y)

    fig = plt.figure()
    width = .2
    ind = np.arange(len(y))
    result = plt.bar(ind, y, width=width, color=(0.2588, 0.4433, 1.0))
    result[1].set_color('r')
    result[2].set_color('g')
    result[3].set_color('y')
    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()

    plt.xlabel('primary/secondary storage in block size 16KB')
    plt.ylabel('Read Speed(log of BPS)')
    plt.title('Random/Sequential Read Speed by primary/secondary storage')

    plt.show()

#plot_from_exp2_2(["read_block_seq.txt", "read_block_rand.txt", "read_ram_rand.txt", "read_ram_seq.txt"])


def plot_from_exp3(filenames):
    y = []

    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")

        for line in f:
            line = line.strip('\n')
            x.append(filenames[i])


            y.append(float(line.split(',')[1]) * MB)

    y = np.log10(y)

    fig = plt.figure()
    width = .2
    ind = np.arange(len(y))
    result = plt.bar(ind, y, width=width, color=(0.2588, 0.4433, 1.0))

    result[1].set_color('r')
    result[2].set_color('g')
    result[3].set_color('y')
    result[4].set_color('m')
    result[5].set_color('c')
    result[6].set_color('k')

    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()


    plt.xlabel('primary/secondary storage in block size 16KB')
    plt.ylabel('Read Speed(log of BPS)')
    plt.title('Random/Sequential Read/WRITE Speed by primary/secondary storage')

    plt.show()

plot_from_exp3(["read_block_seq.txt", "read_block_rand.txt", "read_ram_rand.txt", "read_ram_seq.txt", "write_ram_rand.txt", "write_block_rand.txt", "write_block_seq_opt.txt"])
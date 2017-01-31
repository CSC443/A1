import matplotlib.pyplot as plt
import numpy as np


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

    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by block sizes')

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    plt.show()
#plot_from_file_read(["write_block_seq.txt", "write_lines.txt"])
#plot_from_file_read(["read_block_seq.txt", "read_ram_seq.txt"])

def plot_from_exp2_2(filenames):
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")

        for line in f:
            line = line.strip('\n')
            if (int(line.split(',')[0]) == 0):
                x.append(filenames[i])
            else:
                x.append(int(line.split(',')[0]))
            if(i == 0):
                y1.append(float(line.split(',')[1]) * MB)
            if (i == 1):
                y2.append(float(line.split(',')[1]) * MB)
            if (i == 2):
                y3.append(float(line.split(',')[1]) * MB)
            if (i == 3):
                y4.append(float(line.split(',')[1]) * MB)

    y1 = np.log10(y1)
    y2 = np.log10(y2)
    y3 = np.log10(y3)
    y4 = np.log10(y4)
    fig = plt.figure()
    width = .2
    ind = np.arange(len(y1))
    result = plt.bar(ind, y1, width=width, color=(0.2588, 0.4433, 1.0), label=filenames[0])
    result2 = plt.bar(ind+width, y2, width=width, color='r', label=filenames[1])
    result3 = plt.bar(ind+width+width, y3, width=width, color='g', label=filenames[2])
    result4 = plt.bar(ind + width + width + width, y4, width=width, color='y', label=filenames[3])
    #result[len(y1) - 1].set_color('r')
    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()


    #write seq
    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by different block sizes')

    plt.xlabel('Block size(Bytes)')
    plt.ylabel('Read Speed(log of BPS)')
    plt.title('Random/Sequential Read Speed by primary/secondary storage')

    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by block sizes')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

plot_from_exp2_2(["read_block_seq.txt", "read_block_rand.txt", "read_ram_rand.txt", "read_ram_seq.txt"])


def plot_from_exp3(filenames):
    y1 = []
    y2 = []
    y3 = []
    y4 = []
    y5 = []
    y6 = []
    x = []
    for i in range(0, len(filenames)):
        f = open(filenames[i], "r")

        for line in f:
            line = line.strip('\n')
            if (int(line.split(',')[0]) == 0):
                x.append(filenames[i])
            else:
                x.append(int(line.split(',')[0]))
            if(i == 0):
                y1.append(float(line.split(',')[1]) * MB)
            if (i == 1):
                y2.append(float(line.split(',')[1]) * MB)
            if (i == 2):
                y3.append(float(line.split(',')[1]) * MB)
            if (i == 3):
                y4.append(float(line.split(',')[1]) * MB)
            if (i == 4):
                y5.append(float(line.split(',')[1]) * MB)
            if (i == 5):
                y6.append(float(line.split(',')[1]) * MB)

    y1 = np.log10(y1)
    y2 = np.log10(y2)
    y3 = np.log10(y3)
    y4 = np.log10(y4)
    y5 = np.log10(y5)
    y6 = np.log10(y6)
    fig = plt.figure()
    width = .1
    ind = np.arange(len(y1))
    result = plt.bar(ind, y1, width=width, color=(0.2588, 0.4433, 1.0), label=filenames[0])
    result2 = plt.bar(ind+width, y2, width=width, color='r', label=filenames[1])
    result3 = plt.bar(ind+width+width, y3, width=width, color='g', label=filenames[2])
    result4 = plt.bar(ind + width + width + width, y4, width=width, color='y', label=filenames[3])
    result5 = plt.bar(ind + width*4, y5, width=width, color='m', label=filenames[4])
    result6 = plt.bar(ind + width*5, y6, width=width, color='c', label=filenames[5])
    #result[len(y1) - 1].set_color('r')
    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()


    #write seq
    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by different block sizes')

    plt.xlabel('Block size(Bytes)')
    plt.ylabel('Read Speed(log of BPS)')
    plt.title('Random/Sequential Read/WRITE Speed by primary/secondary storage')

    # plt.xlabel('Block size(Bytes)')
    # plt.ylabel('Write Speed(BPS)')
    # plt.title('Write Speed by block sizes')

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

#plot_from_exp3(["read_block_seq.txt", "read_block_rand.txt", "read_ram_rand.txt", "read_ram_seq.txt", "write_ram_rand.txt", "write_block_rand.txt"])
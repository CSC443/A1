import matplotlib.pyplot as plt

def plot_from_file(filename):
    f = open(filename, "r")
    y = []
    x = []
    for line in f:
        print(line)
        line = line.strip('\n')
        print(line.split(','));
        x.append(int(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(x, y)

    # plt.axis([0,8000000, 0,60000000])
    ax.set_xlabel('block sizes in bytes')
    ax.set_ylabel('read speed in mbps')
    ax.set_title('block size vs  read speed')
    plt.show()

plot_from_file("read_block_seq.txt")
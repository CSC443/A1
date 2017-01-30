import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.tools as tls

def plot_from_file(filename, filename2):
    f = open(filename, "r")
    y = []
    x = []
    for line in f:
        line = line.strip('\n')
        x.append(int(line.split(',')[0]))
        y.append(float(line.split(',')[1]))
    if(filename2 != ""):
        f2 = open(filename2, "r")
        y2 = []
        for line in f2:
            line = line.strip('\n')
            y2.append(float(line.split(',')[1]))

    fig = plt.figure()


    width = .35
    ind = np.arange(len(y))
    plt.bar(ind, y, width=width, color=(0.2588,0.4433,1.0), label=filename)
    if(filename2 != ""):
        plt.bar(ind + width, y2, width, color=(1.0, 0.5, 0.62), label=filename2)
    plt.xticks(ind + width / 2, x)

    fig.autofmt_xdate()
    plt.xlabel('Block size')
    plt.ylabel('Read Speed')
    plt.title('Read Speed by primary/secondary storage')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    plt.show()


plot_from_file("read_block_seq.txt" , "read_ram_seq.txt")
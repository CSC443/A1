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
    plt.scatter(x, y)
    plt.show()

plot_from_file("read_block_seq.txt")
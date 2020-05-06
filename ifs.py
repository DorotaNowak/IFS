import bisect
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from json import load


def parse(filename):
    with open(filename) as file:
        f = load(file)
        n = int(f["n"])
        prob = [int(a) for a in f["probabilities"]]
        trans = []
        for i in range(n):
            one = [float(a) for a in f["transformations"][i][0]]
            two = [float(a) for a in f["transformations"][i][1]]
            arr = np.array((one, two))
            trans.append(arr)
    return prob, trans


def draw(prob, trans, n_iter=50000):
    coord = np.zeros((2, n_iter + 1))
    iter = 0

    for i in range(n_iter):
        z = randint(1, 100)
        pos = bisect.bisect_left(prob, z)
        arr = trans[pos][:, :2]
        new_coord = arr.dot(coord[:, iter]) + trans[pos][:, 2]
        iter += 1
        coord[:, iter] = new_coord

    plt.scatter(coord[0, :], coord[1, :], s=0.2, edgecolors='green')
    plt.savefig("results/" + filename)
    plt.show()


filename = "fern"
prob, trans = parse("examples/" + filename + ".json")

for i in range(len(prob) - 1):
    prob[i + 1] += prob[i]

draw(prob, trans)

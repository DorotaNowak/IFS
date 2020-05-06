import bisect
import itertools
import matplotlib.pyplot as plt
import numpy as np
from random import randint
from json import load


def parse(filename: str):
    with open(filename) as file:
        f = load(file)
        n = f["number_of_transformations"]
        prob = f["probabilities"]
    return prob, [np.array(f["transformations"][i]) for i in range(n)]


def draw(n_iter=50000):
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
    plt.savefig(f"results/{filename}")
    plt.show()


filename = "barnsley-fern"
prob, trans = parse(f"examples/{filename}.json")
prob = list(itertools.accumulate(prob, lambda x, y: x + y))
draw()

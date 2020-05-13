import bisect
import itertools
import numpy as np
import matplotlib.pyplot as plt
import math
from random import randint
from math import cos, sin


class Fractal:
    def __init__(self, name, trans, prob):
        self.name = name
        self.trans = trans
        self.prob = list(itertools.accumulate(prob, lambda x, y: x + y))

    def draw(self, n_iter=50000):
        coord = np.zeros((2, n_iter + 1))
        iter = 0

        for i in range(n_iter):
            z = randint(1, 100)
            pos = bisect.bisect_left(self.prob, z)
            arr = self.trans[pos][:, :2]
            new_coord = arr.dot(coord[:, iter]) + self.trans[pos][:, 2]
            iter += 1
            coord[:, iter] = new_coord

        plt.scatter(coord[0, :], coord[1, :], s=0.2, edgecolors='blue')
        plt.savefig(f"results/{self.name}")
        plt.show()


alpha = 2 * math.pi / 3
r = 0.7
f1 = np.array([[r * cos(alpha), -r * sin(alpha), 0], [r * sin(alpha), r * cos(alpha), 1]])
f2 = np.array([[r * cos(alpha), r * sin(alpha), 0], [-r * sin(alpha), r * cos(alpha), 1]])
f3 = np.array([[1, 0, 0], [0, 1, 0]])
transformations = [f1, f2, f3]
probabilities = [33, 33, 34]

symmetric_tree = Fractal('symmetric-tree', transformations, probabilities)
symmetric_tree.draw()

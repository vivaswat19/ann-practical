# self organising map
import numpy as np
import random


def findNearest(w, x, n, m):
    closest = 0
    val = 1000000.0
    for i in range(n):
        temp = 0.0
        for j in range(m):
            temp += pow(w[j][i] - x[j], 2)

        if(val > temp):
            val = temp
            closest = i

    return closest


def main():
    n = int(input("Enter number of output vectors (cluster): "))
    m = int(input("Enter size of input vector: "))
    a = float(input("Enter Learning Rate: "))
    w = np.zeros((m, n))
    for i in range(m):
        for j in range(n):
            w[i][j] = random.uniform(0, 1)

    print("Weights before update: ")
    for i in range(m):
        for j in range(n):
            print(w[i][j], end=" ")
        print()

    print("----------------------------------")

    q = int(input("Enter number of vector to update weights: "))

    for _ in range(q):
        x = input("Enter vector of size {}: ".format(m)).strip().split(" ")
        x = [int(i) for i in x]

        col = findNearest(w, x, n, m)
        print("Cluster closest to the given input{}: {}".format(x, col+1))

        for i in range(m):
            w[i][col] += a * (x[i] - w[i][col])

        print("Weights after update: ")
        for i in range(m):
            for j in range(n):
                print(w[i][j], end=" ")
            print()

        print("----------------------------------")


if __name__ == '__main__':
    main()

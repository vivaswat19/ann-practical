# Hopfield
import numpy as np


def threshold(val, theta):
    if val > theta:
        return 1
    elif val < theta:
        return 0
    else:
        return val


def main():
    n = int(input("Enter number of training vectors: "))
    s = int(input("Enter size of array: "))
    theta = int(input("Enter Theta: "))
    w = np.zeros((s, s))

    for i in range(n):
        x = input("Enter vector: ").strip().split(' ')
        x = [int(i) for i in x]

        for j in range(s):
            for k in range(s):
                w[j][k] += x[j]*x[k]

    for i in range(s):
        w[i][i] = 0

    print("Weights after update: ")
    for i in range(s):
        for j in range(s):
            print(w[i][j], end=" ")
        print()

    print("--------------Testing--------------------")

    q = int(input("Enter number of queries to test: "))

    for _ in range(q):
        x = input("Enter vector: ").strip().split(' ')
        x = [int(i) for i in x]

        print("Testing by missing entries at index 1 and 2")
        y = np.copy(x)
        y[0] = 0
        y[1] = 0

        print("Vector after missing data: ")
        for i in range(s):
            print(y[i], end=" ")
        print()

        for i in range(2):
            check = True

            for j in range(s):
                if(x[i] != y[i]):
                    check = False

            if(check == True):
                print("Vector after updating index {}: ".format(i+1))
                for i in range(s):
                    print(y[i], end=" ")
                print()
                break
            temp = 0.0
            for j in range(s):
                temp += y[j]*w[j][i]

            y[i] = threshold(x[i] + temp, theta)

            print("Vector after updating index {}: ".format(i+1))
            for i in range(s):
                print(y[i], end=" ")
            print()


if __name__ == '__main__':
    main()


# Enter number of training vectors: 4
# Enter size of array: 4
# Enter Theta: 0
# Enter vector: 1 1 1 - 1
# Enter vector: 1 - 1 - 1 1
# Enter vector: -1 1 1 1
# Enter vector: 1 1 1 1
# Weights after update:
# 0.0 0.0 0.0 0.0
# 0.0 0.0 4.0 0.0
# 0.0 4.0 0.0 0.0
# 0.0 0.0 0.0 0.0
# --------------Testing--------------------
# Enter number of queries to test: 1
# Enter vector: 1 1 1 0
# Testing by missing entries at index 1 and 2
# Vector after missing data:
# 0 0 1 0
# Vector after updating index 1:
# 1 0 1 0
# Vector after updating index 2:
# 1 1 1 0

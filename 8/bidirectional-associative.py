import numpy as np


def train(p, t, w):
    p = np.array(p).reshape((-1, 1))
    t = np.array(t).reshape((1, -1))
    w = np.add(w, np.dot(p, t))
    return w


def patternToLabel(p, w):
    p = np.array(p).reshape((1, -1))
    t = np.dot(p, w)[0]

    for i in range(len(t)):
        if t[i] < 0:
            t[i] = -1
        else:
            t[i] = 1

    return t


def labelToPattern(t, w):
    p = np.dot(t, np.transpose(w))

    for i in range(len(p)):
        if p[i] < 0:
            p[i] = -1
        else:
            p[i] = 1

    return p


def main():
    inp = input('Enter size of Pattern (Row Column) : ').strip().split(' ')
    n, m = int(inp[0]), int(inp[1])

    p1, t1 = [], []
    p2, t2 = [], []
    print("Enter Pattern 1: ")
    for r in range(n):
        temp = input().strip().split(' ')
        temp = [1 if x == '1' else -1 for x in temp]
        p1.append(temp)

    print("Enter Target 1: ")
    t1 = input().strip().split(' ')
    t1 = [1 if x == '1' else -1 for x in t1]

    print("Enter Pattern 2: ")
    for r in range(n):
        temp = input().strip().split(' ')
        temp = [1 if x == '1' else -1 for x in temp]
        p2.append(temp)

    print("Enter Target 2: ")
    t2 = input().strip().split(' ')
    t2 = [1 if x == '1' else -1 for x in t2]

    w = np.zeros((len(p1)*len(p1[0]), len(t1)))
    w = train(p1, t1, w)
    w = train(p2, t2, w)

    print("Weight Matrix: ")
    for i in range(len(w)):
        for j in range(len(w[0])):
            print(w[i][j], end=" ")
        print()

    print("----------------Training Complete---------------")

    k = int(input("Enter number of patterns to test: "))
    for _ in range(k):
        p = input('Enter pattern {}:'.format(_+1)).strip().split(' ')
        if(len(p) != n*m):
            print("invalid Pattern: Size does not match")
        else:
            p = [int(x) for x in p]
            t = patternToLabel(p, w)
            print("Label found: {}".format(t))

    k = int(input("Enter number of labels to test: "))
    for _ in range(k):
        t = input('Enter Label {}: '.format(_+1)).strip().split(' ')
        if(len(t) != len(t1)):
            print("invalid Label: Size does not match")
        else:
            t = [int(x) for x in t]
            p = labelToPattern(t, w)
            print("pattern found: {}".format(p))


main()

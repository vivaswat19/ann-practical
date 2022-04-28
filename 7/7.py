# auto/hetero associative
def activationFun(value):
    if(value > 0):
        return 1
    else:
        return -1


def train(x, y, w, n):
    for i in range(n):
        for j in range(n):
            w[i][j] = w[i][j] + x[i]*y[j]

    return w


def test(x, w, n):
    y = []
    for j in range(n):
        temp = 0
        for i in range(n):
            temp += x[i]*w[i][j]
        y.append(temp)
    return y


def activationFunction(value):
    if value > 0:
        return 1
    elif value == 0:
        return 0
    else:
        return -1


def trainingalgo(x, y, w, n, m):
    for i in range(n):
        for j in range(m):
            w[i][j] += x[i]*y[j]

    return w


def testingalgo(x, w, n, m):
    y = []
    for j in range(m):
        temp = 0
        for i in range(n):
            temp += x[i]*w[i][j]
        y.append(temp)
    return y


def main():

    check = int(input(
        'Do you want to use HetroAssociative Memory(1) or Associative Memory(2): '))
    if(check == 1):
        print("--------* Training Begins *--------")
        rows = int(input("Enter number of inputs: "))
        n = int(input("Enter number of elements in input: "))
        m = int(input("Enter number of elements in output: "))
        w = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(0)
            w.append(temp)
        print("Initial weight matrix: ")

        for a in range(n):
            for b in range(m):
                print(w[a][b], end=" ")
            print()
        print()

        for i in range(rows):
            print("Enter input: ")
            x = input().strip().split(' ')
            x = list(int(a) for a in x)

            print("Enter output: ")
            y = input().strip().split(' ')
            y = list(int(a) for a in y)

            w = trainingalgo(x, y, w, n, m)
            print("Updated Weights :")

            for a in range(n):
                for b in range(m):
                    print(w[a][b], end=" ")
                print()

        print("--------* Testing Begins *-----")

        t = int(input("Enter number of testing inputs: "))

        for i in range(t):
            print("Enter input: ")
            x = input().strip().split(" ")
            x = list(int(a) for a in x)

            y_in = testingalgo(x, w, n, m)
            print("Output for current Input: ")
            for j in range(len(y_in)):
                print(activationFunction(y_in[j]), end=" ")

            print()

    else:
        print("------------Training--------------")
        rows = int(input("Enter number of inputs: "))
        n = int(input("Enter number of elements in input: "))
        w = []
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(0)
            w.append(temp)

        print("Initial weight matrix: ")
        for a in range(n):
            for b in range(n):
                print(w[a][b], end=" ")
            print()
        print()

        for i in range(rows):
            print("Enter input: ")
            x = input().strip().split(' ')
            x = list(int(a) for a in x)

            print("Enter output: ")
            y = input().strip().split(' ')
            y = list(int(a) for a in y)

            w = train(x, y, w, n)
            print("Updated Weights:")
            for a in range(n):
                for b in range(n):
                    print(w[a][b], end=" ")
                print()
            print()

        print("------------Testing--------------")

        t = int(input("Enter number of testing inputs: "))

        for i in range(t):
            print("Enter input: ")
            x = input().strip().split(" ")
            x = list(int(a) for a in x)

            y_in = test(x, w, n)
            print("Output for current Input: ")
            for j in range(len(y_in)):
                print(activationFun(y_in[j]), end=" ")

            print("\n")


main()

# ------------Training--------------
# Enter number of inputs: 4
# Enter number of elements in input: 4
# Initial weight matrix:
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 0

# Enter input:
# 1 1 1 1
# Enter output:
# 1 1 1 1
# Updated Weights:
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1

# Enter input:
# 1 -1 -1 1
# Enter output:
# 1 -1 -1 1
# Updated Weights:
# 2 0 0 2
# 0 2 2 0
# 0 2 2 0
# 2 0 0 2

# Enter input:
# -1 1 -1 1
# Enter output:
# -1 1 -1 1
# Updated Weights:
# 3 -1 1 1
# -1 3 1 1
# 1 1 3 -1
# 1 1 -1 3

# Enter input:
# 1 1 -1 -1
# Enter output:
# 1 1 -1 -1
# Updated Weights:
# 4 0 0 0
# 0 4 0 0
# 0 0 4 0
# 0 0 0 4

# ------------Testing--------------
# Enter number of testing inputs: 1
# Enter input:
# 1 1 -1 -1
# Output for current Input:
# 1 1 -1 -1

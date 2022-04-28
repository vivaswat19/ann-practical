def actFn(x, theta):
    if x < -theta:
        return -1
    if -theta <= x <= theta:
        return 0
    return 1


class Perceptron:
    def __init__(self, N, theta=0, alpha=1):
        self.N = N
        self.weights = [0] * N
        self.bias = 0
        self.theta = theta
        self.alpha = alpha
        self.expectedInOuts = []

    def addexpectedInOut(self, inp, out):
        self.expectedInOuts.append([inp, out])

    def getNetinp(self, inp):
        netinp = self.bias
        for i in range(len(inp)):
            netinp += inp[i] * self.weights[i]
        return netinp

    def getNetOut(self, inp):
        return actFn(self.getNetinp(inp), self.theta)

    # eg - x1 x2 1  t  yin  y   dw1 dw2 db  w1 w2 b
    def printLine(self, x, t, yin, y, dw, db, w, b):
        def formattedStr(str): return '{:>4}'.format(str)

        s = ''
        for val in x:
            s += formattedStr(val)
        s += formattedStr(1)
        s += '  |  '
        s += formattedStr(t)
        s += '  |  '
        s += formattedStr(yin)
        s += '  |  '
        s += formattedStr(y)
        s += '  |  '
        for val in dw:
            s += formattedStr(val)
        s += formattedStr(db)
        s += '  |  '
        for val in w:
            s += formattedStr(val)
        s += formattedStr(b)

        print(s)

    def train(self):
        changed = True
        epoch = 1

        self.printLine(
            ['x{}'.format(i) for i in range(1, self.N + 1)],
            't',
            'yin',
            'y',
            ['dw{}'.format(i) for i in range(1, self.N + 1)],
            'db',
            ['w{}'.format(i) for i in range(1, self.N + 1)],
            'b'
        )

        while changed:
            changed = False
            print('EPOCH -', epoch)

            for x, t in self.expectedInOuts:
                yin = self.getNetinp(x)
                y = self.getNetOut(x)
                dw = [0] * self.N
                db = 0
                if y != t:
                    for i in range(self.N):
                        dw[i] = self.alpha * t * x[i]
                        self.weights[i] += dw[i]
                    db = self.alpha * t
                    self.bias += db
                    changed = True

                self.printLine(x, t, yin, y, dw, db, self.weights, self.bias)

            epoch += 1

    def test(self, inp):
        return self.getNetOut(inp)


print("----- AND NOT using PERCEPTRON -----")
andNot = Perceptron(N=2, theta=0, alpha=1)
andNot.addexpectedInOut([1, 1], 1)
andNot.addexpectedInOut([1, -1], -1)
andNot.addexpectedInOut([-1, 1], 1)
andNot.addexpectedInOut([-1, -1], 1)

andNot.train()
print(andNot.weights, andNot.bias)

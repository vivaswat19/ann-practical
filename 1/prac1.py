def And(x1, x2, w1, w2, th):
    yin = x1 * w1 + x2 * w2
    threshMax = w1 + w2 + 1
    print(f"Threshold difference: {abs(th - threshMax)}")
    if yin >= th:
        return 1
    else:
        return 0


x1 = int(input())
x2 = int(input())
w1 = int(input())
w2 = int(input())
th = int(input())
print(f"Output: {And(x1, x2, w1, w2, th)}")

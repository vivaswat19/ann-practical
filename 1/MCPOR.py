x1 = int(input("please enter the input1:"))
x2 = int(input("please enter the input2:"))

# Layer1
w1 = 1
w2 = 1
thresh1 = 1
outputFinal = 0
inputLayer1 = (x1*w1)+(x2*w2)
if(inputLayer1 >= thresh1):
    outputFinal = 1


print('the output of the OR gate is ', outputFinal)

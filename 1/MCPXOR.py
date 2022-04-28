x1=int(input("please enter the input1:"))
x2=int(input("please enter the input2:"))

#Layer1
w1=-1
w2=1
thresh1=1
outputLayer1=0
inputLayer1=(x1*w1)+(x2*w2)
if(inputLayer1>=thresh1):
        outputLayer1=1
        
#Layer2
w1=1
w2=-1
thresh2=1
outputLayer2=0
inputLayer2=(x1*w1)+(x2*w2)
if(inputLayer2>=thresh2):
        outputLayer1=1

#OR gate to combine the two hidden layers
w1=1
w2=1
outputFinal=0
inputFinal=(outputLayer1*w1)+(outputLayer2*w2)
thresholdFinal=1
if(inputFinal>=thresholdFinal):
    outputFinal=1
    
print('the output of the XOR gate is ',outputFinal)
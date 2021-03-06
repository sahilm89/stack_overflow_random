#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit
import bigfloat
 
precision = 100
def sigmoid(s):
    y = []
    for k in s:
        z=[]
        for l in k:
            z.append( bigfloat.div( 1. , bigfloat.add(1,bigfloat.exp(-l,bigfloat.precision(precision)))))
        y.append(z)
    return np.array(y)

def getInfo(data, target, theta):
    afterSigmoid = sigmoid(data.dot(theta))

    firstList = [ ]
    for k in afterSigmoid:
        m = []
        for x in k:
            m.append(bigfloat.log(x,bigfloat.precision(precision)))
        firstList.append(m)

    secondList = [ ]
    for k in afterSigmoid:
        m = []
        for x in k:
            m.append(bigfloat.log( bigfloat.sub(1. , x) , bigfloat.precision(precision)))
        secondList.append(m)
    
    Ein = 0.
    m = []
    for x,y in zip(firstList, secondList):
        for a,b,t in zip(x,y,target):
            value = bigfloat.add( bigfloat.mul(t[0],a, bigfloat.precision(precision)) , bigfloat.mul( bigfloat.sub(1. ,t[0], bigfloat.precision(precision)) ,a, bigfloat.precision(precision)))
            m.append(value)
    for item in m:
        Ein = bigfloat.add(item, Ein, bigfloat.precision(precision))
    
    Ein = - Ein
    print(Ein)
    gradient = -data.T.dot(target-afterSigmoid)
    return (Ein, gradient)
   
def getTheta(data, target, theta):
    iterations = 1000
    it = 0
    step = 0.001
    while(it <= iterations):
        (Ein, vt) = getInfo(data, target, theta)
        theta -= step*vt
        it += 1
    return theta
   
def run(data, target):
    d = len(data[0])
    theta = data[0]
    theta = theta.reshape(d,1)
    theta = getTheta(data, target, theta)
    i = 0
    correct = 0
    for x in data:
        prediction = -1
        if(sigmoid([x.dot(theta)])>=0.5):
            prediction = 1
        else:
            prediction = 0
        if(prediction == target[i]):
            correct = correct + 1
        i = i + 1
    print("Train accuracy: ", float(correct)/len(data))
   
if __name__ == '__main__':
   
    data = np.array([[1,1],[1,2],[1,3],[1,4],[1,5],[10,1],[10,2],[10,3],[10,4],[10,5]])
    target = np.array([1,1,1,1,1,0,0,0,0,0])
    target = target.reshape(len(target),1)
    run(data,target)
   
    x=data[:,0]
    y=data[:,1]
    specified_colours={1:'red',0:'blue',3:'green'}
    colours=[specified_colours[xx] for xx in target[:,0]]
    plt.scatter(x, y,c=colours)
    plt.show()

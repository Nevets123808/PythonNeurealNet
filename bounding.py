from math import e
def sigmoid(x, a):
        return pow(1+(pow(e, -a*x)), -1)

def relu(x, a):
        return x if x>0 else 0
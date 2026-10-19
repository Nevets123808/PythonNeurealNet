import numpy as np
from bounding import sigmoid as bounding
class Layer():
    def __init__(self, input_num, nodes):
        self.weights = np.random.random((input_num, nodes))
        self.biases = np.random.random(nodes)

    def output(self, input):
        values = np.matmul(input, self.weights) + self.biases
        return np.array([bounding(value, 1) for value in values])


if __name__ == "__main__":
    layer = Layer(6,4)
    print(layer.weights)
    print("#############")
    print(layer.biases)
    print("#############")
    print(layer.output(np.random.random(6)))
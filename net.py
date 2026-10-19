import numpy as np
import random
from math import e, pow
from layer import Layer

class Net():
    def __init__(self, input_nodes, layers, layer_nodes, output_nodes):
        self.input_nodes = np.zeros(input_nodes)
        self.layers = [Layer(input_nodes,layer_nodes)]
        for _ in range(layers-1):
            self.layers.append(Layer(layer_nodes,layer_nodes))
        self.output_layer = Layer(layer_nodes, output_nodes)

    def back_propogate(self):
        pass

    def output(self, inputs):
        self.input_nodes = np.array(inputs)
        values = self.input_nodes
        for layer in self.layers:
            values = layer.output(values)
        return self.output_layer.output(values)

if __name__ == "__main__":
    net = Net(4, 2, 5, 4)
    print(net.output([np.random.random(4)]))

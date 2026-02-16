from layer import Layer
from activation import act_sigmoid

class Network:
    def __init__(self, input_size:int, activation):
        self.input = input_size
        self.layers = []  
        self.activation = activation
    
    def add(self, weights, biases):
        nouvelle_layer = Layer(weights, biases)
        self.layers.append(nouvelle_layer)
    
    def feedforward(self, x):
        current = x
        for layer in self.layers:
            raw = layer.forward(current)
            current = [self.activation(val) for val in raw]
        return current
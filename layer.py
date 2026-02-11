from neuron import Neuron

class Layer:
    def __init__(self, weights_list:list, biases_list:list):
        self.weights_list = weights_list
        self.biases_list = biases_list
    
    def forward(self, entry:list=[])->list:
        output = []
        for i in range(len(self.weights_list)):
            neuron = Neuron(self.weights_list[i],self.biases_list[i])
            output.append(neuron.forward(entry))
        return output
import random
class Neuron:
    '''
    Docstring for Neuron
    A neuron represents an elementary computing unit. It can at least :
        -Stocks its weight and bias
        -Calculate its output from an input vector
    '''

    def __init__(self, weights:list, bias:float):
        '''
        Docstring for __init__
        
        :param self: Description
        :param weights: Strength of connections between neurons
        :type weights: list
        :param bias: Refine and modify the predictions
        :type bias: float
        '''
        
        self.weights = weights
        self.bias = bias
    
    def forward(self,entry:list=[])->float:
        '''
        Docstring for forward
        
        The output formula of a hidden neuron will always be in the form :
        Y = W · X + B

        :param entry: Description
        :type entry: list
        :return: Description
        :rtype: float
        '''
        output = 0
        #scalar product
        for i in range(len(entry)):
            output += (self.weights[i]) * (entry[i])
        
        #final output
        return output + self.bias
        
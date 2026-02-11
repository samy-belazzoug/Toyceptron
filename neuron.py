import random
class Neuron:
    '''
    Docstring for Neuron
    A neuron represents an elementary computing unit. It can at least :
        -Stocks its weight and bias
        -Calculate its output from an input vector
    '''

    def __init__(self, weights:list=None , bias:float=None):
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
        
        :param entry: Description
        :type entry: list
        :return: Description
        :rtype: float
        '''
        f = None
        return f
        
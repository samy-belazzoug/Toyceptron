from math import exp

def act_sigmoid(x):
    return 1 / (1 + exp(-x))
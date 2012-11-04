'''
Python artificial neural network example

'''

import math

class Node:

    inputs   = []
    act_func = None

    def calculate(self):
        '''Calculates the output from this node'''

        total = 0

        for n,i in enumerate(self.inputs):
            total += i * weights[n]

        return self.act_func( total )
E = 0
errors = []
alpha = 0.1
weights = [0,0,0]
deltas = []
tdata = [[1,1,1],
         [1,0,0],
         [0,1,0],
         [0,0,0]]

g = lambda z: 1.0 / ( 1.0 + math.exp( -z ) )


X =  [ e[:2] for e in tdata] 

for x in X: x.insert(0, 1)

y = [ e[2] for e in tdata]

m = len(y)

def backprop( e, x, y, network):
    deltas = []
    for i in range(0, m):
        deltas.append(h_x - y[i])


def sqerr( x,y, network ):
    '''
    a_j^l - j is the node index and l is the layer index

    L = 1 
    because there is only one node in the network and one 'varying' layer (i.e. output), I am using a_L to represent a^1_0
    '''
    
    deltas = []
    errors = []

    
    t = 0.0
    for i in range(0, m):
        network.inputs = x[i]
        a_L = network.calculate() 
        d = a_L - y[i]
        deltas.append(d)
        e = d ** 2.0
        errors.append(e)
        t += e


    E = 1.0 / ( 2.0 * m ) * t

    
    for i in range(0, len(weights)):
        weights[i] -= E * alpha * (y[i] - a_L) * g(1.0 - a_L)

    print E
    print weights

    return errors #        

def andgate():

        def thresh( z ):

            if z > 0 : return 1
            else:      return 0


        n = Node()
        n.act_func = g
        sqerr( X, y, n)
        

        

if __name__ == "__main__":
    print weights

    for i in range(0,400):
        andgate()

    x = int( raw_input(">>>") )
    y = int( raw_input(">>>") )

    n = Node()
    n.act_func = g
    n.inputs = [1, x, y]

    print n.calculate()


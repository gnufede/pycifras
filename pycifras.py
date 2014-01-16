#!/usr/bin/env python3
import sys, getopt, itertools
import math

states = dict()
results = ()
expected_res = 0

def addToStates(key, value):
    global states
    if key not in states:
        states[key] = value
        return True
    else:
        return False

def addToResults(key, value):
    global results
    if len(results):
        if key < results[0]:
            results = (key, value)
    else:
        results = (key,value)

class State():
    global states
    global results
    global expected_res

    def __init__(self, **kwargs):
        vars(self).update(kwargs)
        self.result = 1
        if self.operation:
            self.result = self.oper()
            self.operations = self.operations[::]
            self.operations.append(\
                    '='.join((self.operation,str(self.result))))
            self.numbers.append(self.result)
            self.numbers.sort()
            addToResults(int(self.distanceToResult()), self)
        if addToStates(str(self.numbers), self):
            if self.result != 0 and (0 not in results):
                self.iterate()

    def distanceToResult(self):
        return math.fabs(expected_res-self.result)

    def oper(self):
        return eval(self.operation)

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return str(self.operations)

    def inStates(self):
        return str(self.numbers.sort()) in states

    def iterate(self):
        #if self.distanceToResult:
        for operator in "+*/-":
            for x,y in itertools.combinations(self.numbers, 2):
                tempnumbers = self.numbers[::]
                tempnumbers.remove(x)
                tempnumbers.remove(y)
                child = State(numbers=tempnumbers,
                        operations=self.operations,
                        operation=operator.join((str(x),str(y))))

def compute(result, arguments):
    global expected_res
    intargs = [int(x) for x in arguments]
    expected_res = int(result)
    state = State(numbers=intargs, operations=list(), operation=None)
    return str(results[0])+': '+str(results[1])
#    print(results[0].operations)

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"h")
    except getopt.GetoptError:
       print('pycifras.py <target_number> <inputnumber1> <inputnumber2>...')
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print('pycifras.py <target_number> <inputnumber1> <inputnumber2>...')
          sys.exit()
    if len(args) > 1:
        print(compute(args[0], args[1:]))

if __name__ == '__main__':
    main(sys.argv[1:])

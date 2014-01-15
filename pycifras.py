#!/usr/bin/env python3
import sys, getopt, itertools
import math

states = dict()
results = dict()

def addToDic(dic, key, value):
    if key not in dic:
        dic[key] = []
        dic[key].append(value)
    else:
        dic[key].append(value)

def addOrNotToDic(dic, key, value):
    if len(dic):
        if key < list(dic.keys())[0]:
            dic.clear()
            dic[key] = []
            dic[key].append(value)
    else:
        dic[key] = []
        dic[key].append(value)

class State():
    global states
    global results

    def __init__(self, expected_res, numbers, operation, operations):
        self.expected_res = expected_res
        self.operation = operation
        self.result = self.oper()
        opers = operations[::]
        tempoper = '='.join((operation,str(self.result))),
        opers.append(tempoper)
        self.operations = opers
        self.numbers = numbers
        self.numbers.append(self.result)
        addOrNotToDic(results, int(self.distanceToResult()), self)
        addToDic(states, str(self.numbers.sort()), self)
        if self.result != 0:
            self.iterate()

    def distanceToResult(self):
        return math.fabs(self.expected_res-self.result)

    def oper(self):
        return eval(self.operation)

    def __unicode__(self):
        return self.__str__()

    def __str__(self):
        return str(self.operations)

    def inStates(self):
        return str(self.numbers.sort()) in results

    def iterate(self):
        #if self.distanceToResult:
        if not self.inStates():
            for oper in "+*/-":
                for x,y in itertools.combinations(self.numbers, 2):
                    tempnumbers = self.numbers[::]
                    tempnumbers.remove(x)
                    tempnumbers.remove(y)
                    child = State(self.expected_res,
                            tempnumbers,
                            oper.join((str(x),str(y))),
                            self.operations)
        else:
            print(self.operations)

def compute(result, arguments):
    intargs = [int(x) for x in arguments]
    state = State(expected_res=int(result), numbers=intargs, operation='1', 
            operations=list())
    return [str(x)+': '+str(y[0]) for x,y in results.items() if len(y)]
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
        print( '\n'.join(compute(args[0], args[1:])) )

if __name__ == '__main__':
    main(sys.argv[1:])

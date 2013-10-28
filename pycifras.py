#!/usr/bin/env python2
import sys, getopt, itertools

def main(argv):
    try:
       opts, args = getopt.getopt(argv,"h")
    except getopt.GetoptError:
       print 'pycifras.py <target_number> <inputnumber1> <inputnumber2>...'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
          print 'pycifras.py <target_number> <inputnumber1> <inputnumber2>...'
          sys.exit()
    if len(args) > 1:
        compute(args[0], args[1:])

def compute(target_number, number_ops):
    results = dict()
    operators = ['+','-','*','/']
    for operation in itertools.product(operators,repeat=len(number_ops)):
        for number_perm in itertools.permutations(number_ops):
            c = [ item for pair in zip(number_perm, operation) for item in pair ][:-1]
            stroperation = ''.join(map(str,c))
            if eval(stroperation) == int(target_number):
                if stroperation not in results:
                    results[stroperation]=stroperation
                    print stroperation

if __name__ == '__main__':
    main(sys.argv[1:])

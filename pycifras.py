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

def compute(target_number, numbers):
    operators = ['+','-','*','/']
    for i in range(1,len(numbers)):
        for oper in itertools.product(operators,repeat=i):
            for num_perm in itertools.permutations(numbers, i+1):
                c = [ it for p in zip(num_perm, oper) for it in p ]+[num_perm[-1]]
                stroperation = ''.join(map(str,c))
                if eval(stroperation) == int(target_number):
                    print stroperation

if __name__ == '__main__':
    main(sys.argv[1:])

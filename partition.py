#!/usr/bin/python

import sys
from src.partitionFunction import PartitionFunction


def main(argv):
    party = PartitionFunction()
    result = party.value(int(sys.argv[1]))
    print "P(" + sys.argv[1] + ") = " + str(result)

if __name__ == "__main__":
   main(sys.argv[1:])
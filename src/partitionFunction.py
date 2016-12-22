#!/usr/bin/python

def my_range(end, start, step):
    while start <= end:
        yield end
        end += step

class PartitionFunction:

    count = 0

    @staticmethod
    def value(original):
        PartitionFunction.count = 0
        for i in my_range(original, 1, -1):
            PartitionFunction.extract(original, i)
        return PartitionFunction.count

    @staticmethod
    def extract(original, request):
        diferente = original - request
        if diferente < 0:
            PartitionFunction.count = -1
        else:
            if diferente == 0 or diferente == 1:
                PartitionFunction.count += 1
            else:
                PartitionFunction.next(diferente, request)

    @staticmethod
    def next(original, request):
        for i in my_range(original, 1, -1):
            if i <= request:
                PartitionFunction.extract(original, i)












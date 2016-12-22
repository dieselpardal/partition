#!/usr/bin/python

def my_range(end, start, step):
    while start <= end:
        yield end
        end += step

class PartitionFunction:

    count = 0

    @staticmethod
    def value(original):
        count = 0
        for i in my_range(original, 1, -1):
            PartitionFunction.extP(original, i)
        return count

    def extP(original, request):
        diferente = original - request
        if diferente < 0:
            count = -1
        else:
            if diferente == 0 or diferente == 1:
                PartitionFunction.count += 1
            else:
                PartitionFunction.xP(diferente, request)

    def xP(original, request):
        for i in my_range(original, 1, -1):
            if i <= request:
                PartitionFunction.extP(original, i)












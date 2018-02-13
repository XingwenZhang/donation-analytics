
# coding: utf-8

import math
from min_max_heap import MinHeap, MaxHeap

# Reference: https://cs.stackexchange.com/questions/57542/find-pth-percentile-of-a-stream-of-numbers
# Reference: https://www.geeksforgeeks.org/median-of-stream-of-running-integers-using-stl/
# Reference: https://en.wikipedia.org/wiki/Percentile


class StreamingPercentile(object):
    '''
    According to the https://en.wikipedia.org/wiki/Percentile to compute the location index of percentile value
    Compare with the index, keep max heap's size equal to index and only store the smaller values;
    store the rest values into min heap
    '''
    def __init__(self, percentile):
        self.__percentile = percentile
        self.__min_heap = MinHeap()
        self.__max_heap = MaxHeap()
        self.__total_amount = 0
        self.__total_counts = 0
        
    def push(self, donation_amount):
        self.__total_amount += donation_amount
        self.__total_counts += 1
        
        index = int(math.ceil(self.__percentile * self.__total_counts / 100.0))
        
        # Insert and then adjust the two heaps size
        if len(self.__max_heap) == 0 or donation_amount < self.__max_heap.heaptop():
            self.__max_heap.heappush(donation_amount)
        else:
            self.__min_heap.heappush(donation_amount)
            
        while len(self.__max_heap) != index:
            if len(self.__max_heap) > index:
                self.__min_heap.heappush(self.__max_heap.heappop())
            else:
                self.__max_heap.heappush(self.__min_heap.heappop())
            
    @property  
    def percentile_value(self):
        return self.__max_heap.heaptop()
    
    @property
    def total_counts(self):
        return self.__total_counts
    
    @property
    def total_amount(self):
        return self.__total_amount


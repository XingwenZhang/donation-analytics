import unittest
from min_max_heap import MinHeap, MaxHeap 

class TestHeap(unittest.TestCase):

    def test_init(self):
        min_heap = MinHeap() 
        max_heap = MaxHeap() 
        self.assertTrue(isinstance(min_heap, MinHeap))
        self.assertTrue(isinstance(max_heap, MaxHeap))

    def test_push(self):
        min_heap = MinHeap() 
        max_heap = MaxHeap() 
        min_heap.heappush(1)
        max_heap.heappush(1)
        self.assertEqual(min_heap.h[0], 1)
        self.assertEqual(max_heap.h[0].val, 1)

    def test_pop(self):
        min_heap = MinHeap() 
        max_heap = MaxHeap()
        min_heap.heappush(1)
        max_heap.heappush(1)
        self.assertEqual(min_heap.heappop(), 1)
        self.assertEqual(max_heap.heappop(), 1)

    def test_top(self):
        min_heap = MinHeap() 
        max_heap = MaxHeap()
        min_heap.heappush(1)
        max_heap.heappush(1)
        self.assertEqual(min_heap.heaptop(), 1)
        self.assertEqual(max_heap.heaptop(), 1)

if __name__ == '__main__':
    unittest.main()
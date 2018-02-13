
# coding: utf-8

# In[5]:

import heapq


# In[6]:


# Reference: https://stackoverflow.com/questions/2501457/what-do-i-use-for-a-max-heap-implementation-in-python


# In[7]:

class MaxHeapObj(object):
    def __init__(self,val): self.val = val
    def __lt__(self,other): return self.val > other.val
    def __eq__(self,other): return self.val == other.val
    def __str__(self): return str(self.val)

class MinHeap(object):
    def __init__(self): self.h = []
    def heappush(self,x): heapq.heappush(self.h,x)
    def heappop(self): return heapq.heappop(self.h)
    def heaptop(self):
        if not self.h:
            return None
        return self.h[0]
#     def __getitem__(self,i): return self.h[i]
    def __len__(self): return len(self.h)

class MaxHeap(MinHeap):
    def heappush(self,x): heapq.heappush(self.h,MaxHeapObj(x))
    def heappop(self): return heapq.heappop(self.h).val
    def heaptop(self):
        if not self.h:
            return None
        return self.h[0].val
#     def __getitem__(self,i): return self.h[i].val
    


# In[8]:

# minh = MinHeap()
# maxh = MaxHeap()
# # add some values
# minh.heappush(12)
# maxh.heappush(12)
# minh.heappush(4)
# maxh.heappush(4)
# # fetch "top" values
# print(minh[0],maxh[0]) # "4 12"
# # fetch and remove "top" values
# print(minh.heappop(),maxh.heappop()) # "4 12"


# In[ ]:




from heapq import *

def find_Kth_smallest_number(nums, k):
  
  max_heap = list()
  
  for index in range(k):
      heappush(max_heap, -nums[index])      

  for index in range(k, len(nums)):
      if -nums[index] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[index])                

  return -max_heap[0]  
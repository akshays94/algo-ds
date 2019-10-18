from heapq import *


def find_k_largest_numbers(nums, k):
  
  min_heap = list()

  for index in range(k):
    heappush(min_heap, nums[index])

  for index in range(k, len(nums)):
    if nums[index] > min_heap[0]:
      heappop(min_heap)
      heappush(min_heap, nums[index])

  return min_heap
from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
  min_heap = list()
  for rope_length in ropeLengths:
    heappush(min_heap, rope_length)

  result = 0
  while len(min_heap) > 1:
    new_rope_length = heappop(min_heap) + heappop(min_heap)
    result += new_rope_length
    heappush(min_heap, new_rope_length)

  return result 
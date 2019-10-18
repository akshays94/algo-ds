import math

from heapq import *

def find_closest_points(points, k):
  
  max_heap = list()
  dist_to_points_map = dict()

  for index in range(k):
    point = points[index]
    dist_to_origin = math.sqrt( point.x**2 + point.y**2 )
    heappush(max_heap, -dist_to_origin)
    dist_to_points_map.update({ -dist_to_origin: point })

  for index in range(k, len(points)):
    point = points[index]
    dist_to_origin = math.sqrt( point.x**2 + point.y**2 )
    if -dist_to_origin > max_heap[0]:
      heappop(max_heap)
      heappush(max_heap, -dist_to_origin)
      dist_to_points_map.update({ -dist_to_origin: point })

  max_heap = list(map(lambda dist: dist_to_points_map[dist], max_heap))
  return max_heap
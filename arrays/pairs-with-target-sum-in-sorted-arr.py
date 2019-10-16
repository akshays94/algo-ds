def pair_with_targetsum(arr, target_sum):
  start, end = 0, len(arr) - 1
  while start < end:
    start_num, end_num = arr[start], arr[end]
    if start_num + end_num == target_sum:
      return [start, end]
    elif start_num + end_num > target_sum:
      end -= 1
    else:
      start += 1     
  return [-1, -1]


def pair_with_targetsum_1(arr, target_sum):
  # using hashtable
  visited = dict()
  
  for index in range(len(arr)):
    
    curr_no = arr[index]
    other_num = target_sum - curr_no
    
    if other_num in visited:
      return [visited[other_num], index]
    visited[curr_no] = index
  
  return [-1, -1]      

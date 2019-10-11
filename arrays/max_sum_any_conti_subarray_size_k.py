'''
Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

Example 1:

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].
'''


def max_sub_array_of_size_k(k, arr):
  # [2, 1, 5, 1, 3, 2], k=3
  max_sum = -1
  window_sum = 0
  window_start = 0
  
  for window_end in range(len(arr)):
    window_sum += arr[window_end]
    
    is_window_completed = window_end - window_start + 1 == k
    if is_window_completed:
      if max_sum < window_sum:
        max_sum = window_sum
      window_sum -= arr[window_start]
      window_start += 1

  return max_sum
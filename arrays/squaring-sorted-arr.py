'''
Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.
'''

def make_squares(arr):
  squares = list()
  
  for number in arr:
    squared = number ** 2
    squares.append(squared)

    last_elem = squares[-1]
    if len(squares) > 1 and last_elem < squares[-2]:
      index = len(squares) - 2
      while index >= 0 and squares[index] > last_elem:
        squares[index + 1] = squares[index]
        index -= 1
      squares[index + 1] = last_elem  
  
  return squares


def make_squares(arr):
  squares = list()
  start, end = 0, len(arr) - 1
  
  while start <= end:
    start_sq, end_sq = arr[start] ** 2, arr[end] ** 2 
    if start_sq >= end_sq:
      start += 1
      squares.insert(0, start_sq)
    else:
      end -= 1
      squares.insert(0, end_sq)
  return squares  
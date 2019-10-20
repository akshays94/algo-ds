'''
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.
'''

def fruits_into_baskets(fruits):

  start, end = 0, 0
  curr_max, max_length = 0, float('-inf')
  fruit_freq = dict()

  while end < len(fruits):
    
    fruit = fruits[end]
    fruit_freq[fruit] = fruit_freq[fruit] + 1 if fruit in fruit_freq else 1

    if len(fruit_freq) <= 2:
      end += 1
      curr_max += 1
      if curr_max > max_length:
        max_length = curr_max

    else:
      # exceeded, so shrink window
      while len(fruit_freq) > 2:
        start_fruit = fruits[start]
        fruit_freq[start_fruit] -= 1
        
        if fruit_freq[start_fruit] <= 0:
          del fruit_freq[start_fruit]
        
        curr_max -= 1
        start += 1  

      curr_max += 1
      end += 1

  return max_length 
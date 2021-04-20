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


def fruits_into_baskets(arr):
    maximum_fruits = 0
    NO_OF_BASKETS = 2
    window_char_freq = dict()
    window_start = 0
    
    for window_end in range(len(arr)):
        curr_fruit = arr[window_end]
        window_char_freq.update({
            curr_fruit: window_char_freq.get(curr_fruit, 0) + 1
        })
        
        while len(window_char_freq) > NO_OF_BASKETS:
            remove_fruit = arr[window_start]
            
            # remove fruit
            window_char_freq.update({
                remove_fruit: window_char_freq.get(remove_fruit, 0) - 1
            })
            if window_char_freq[remove_fruit] <= 0:
                del window_char_freq[remove_fruit]
            
            window_start += 1
        
        maximum_fruits = max(maximum_fruits, window_end - window_start + 1)
    
    return maximum_fruits

# print(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']))
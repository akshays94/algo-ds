'''
Given a string, find the length of the longest substring which has no repeating characters.
'''

def non_repeat_substring(word):
  
  end = 0
  max_length, curr_max = float('-inf'), 0
  visited = dict()
  
  while end < len(word):
    letter = word[end]
    if letter in visited:
      # second visit
      visited.clear()
      visited[letter] = True
      curr_max = 1
      end += 1
    else:
      # not visited
      visited[letter] = True
      curr_max += 1
      if curr_max > max_length:
        max_length = curr_max
      end += 1
  return max_length  
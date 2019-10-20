'''
Given a string and a pattern, find out if the string contains any permutation of the pattern.
'''

def find_permutation(word, pattern):
  
  pattern_map = dict()
  for letter in pattern:
    pattern_map[letter] = pattern_map.get(letter, 0) + 1

  is_found = False
  start, end = 0, 0
  visited = dict()
  pattern_map_copy = pattern_map.copy()
      
  while end < len(word):
    letter = word[end]
    if letter in pattern_map_copy:
      pattern_map_copy[letter] -= 1
      if pattern_map_copy[letter] <= 0:
        del pattern_map_copy[letter]
      end += 1
      if len(pattern_map_copy) == 0:
        return True
    else:
      pattern_map_copy = pattern_map.copy()
      start += 1
      end += 1
  
  return is_found
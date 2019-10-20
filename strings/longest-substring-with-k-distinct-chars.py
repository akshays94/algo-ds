def longest_substring_with_k_distinct(word, k):
  
  start, end = 0, 0
  char_freq = dict()
  max_length = float('-inf')
  curr_max = 0

  while end < len(word):
    letter = word[end]
    char_freq[letter] = char_freq[letter] + 1 if letter in char_freq else 1
    if len(char_freq) <= k:
      curr_max += 1
      end += 1
      if curr_max > max_length:
        max_length = curr_max
    else:
      # chars exceeded, start shrinking
      while len(char_freq) > k:
        start_letter = word[start]
        char_freq[start_letter] -= 1
        if char_freq[start_letter] <= 0:
          del char_freq[start_letter]
        start += 1
        curr_max -= 1

      curr_max += 1
      end += 1

  return max_length
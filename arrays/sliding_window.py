# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
arr = [2, 1, 5, 1, 3, 2]
def find_averages(arr, windowSize):
    results = list()
    windowSum = 0.0
    windowStartIndex = 0
    for windowEndIndex in range(len(arr)):
        number = arr[windowEndIndex]
        windowSum += number
        if windowEndIndex >= windowSize - 1:
            results.append(windowSum / windowSize)
            windowSum -= arr[windowStartIndex]
            windowStartIndex += 1
    return results

def find_max_sum(arr, windowSize):
    max_sum = 0
    windowSum = 0.0
    windowStartIndex = 0
    for windowEndIndex in range(len(arr)):
        windowSum += arr[windowEndIndex]
        if windowEndIndex >= windowSize - 1:
            max_sum = max(max_sum, windowSum)
            windowSum -= arr[windowStartIndex]
            windowStartIndex += 1
    return max_sum

import math
def find_len_of_smallest_conti_subarray(arr, S):
    window_sum, window_start = 0, 0
    smallest = math.inf
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= S:
            smallest = min(smallest, (window_end - window_start) + 1)
            window_sum -= arr[window_start]
            window_start += 1
    return 0 if smallest == math.inf else smallest

def find_long_substring_distinct_chars(arr, K):
    window_start = 0
    window_char_freq = {}
    longest = 0
    for window_end in range(len(arr)):
        curr_char = arr[window_end]
        window_char_freq.update({
            curr_char: window_char_freq.get(curr_char, 0) + 1
        })
        while len(window_char_freq) > K:
            remove_char = arr[window_start]
            updated_count = window_char_freq[remove_char] - 1
            if updated_count == 0:
                del window_char_freq[remove_char]
            else:
                window_char_freq.update({ remove_char: updated_count })
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    return longest

#print(find_averages(arr, 5))
#print(find_max_sum(arr, 3))
#print(find_len_of_smallest_conti_subarray([2, 1, 5, 2, 3, 2], 7))
print(find_long_substring_distinct_chars('araacicicibxxxxxxxxxxxx', 2))

def find_no_repeat_substring(word):
    longest = 0
    window_char_freq = dict()
    window_start = 0
    
    def any_char_freq_grt_one(freq_map):
        for k, v in freq_map.items():
            if v > 1:
                return True
        return False
    
    for window_end in range(len(word)):
        letter = word[window_end]
        window_char_freq.update({
            letter: window_char_freq.get(letter, 0) + 1
        })
        
        while any_char_freq_grt_one(window_char_freq):
            remove_char = word[window_start]
            window_char_freq.update({
                remove_char: window_char_freq.get(remove_char, 0) - 1
            })
            if window_char_freq[remove_char] < 1:
                del window_char_freq[remove_char]
            window_start += 1

        longest = max(longest, window_end - window_start + 1)

    return longest

print(find_no_repeat_substring('aabccbbxdffgre'))


def find_longest_sstr_with_same_letter_aftr_replacement(word, K):
    longest = 0
    
    window_start = 0
    window_char_freq = {}
    
    def is_incorrect_config(freq):
        is_extra_letter = len(freq) > (K + 1)
        if is_extra_letter:
            return True
        if len(freq) == (K + 1):
            is_first_grt_one_found = False
            for char_count in freq.values():
                if char_count > 1:
                    if is_first_grt_one_found:
                        return True
                    else:
                        is_first_grt_one_found = True
                        continue
        return False
    
    for window_end in range(len(word)):
        letter = word[window_end]
        window_char_freq.update({
            letter: window_char_freq.get(letter, 0) + 1
        })
        while is_incorrect_config(window_char_freq):
            remove_char = word[window_start]
            window_char_freq.update({
                remove_char: window_char_freq.get(remove_char, 0) - 1
            })
            if window_char_freq[remove_char] == 0:
                del window_char_freq[remove_char]
            window_start += 1
        longest = max(longest, window_end - window_start + 1)
    
    return longest

print(find_longest_sstr_with_same_letter_aftr_replacement('aabccbbxxxxxxxxxx', 2))

def find_longest_subarr_having_all_ones(arr, K):
    longest = 0
    window_start, ones_in_window = 0, 0
    
    for window_end in range(len(arr)):
        number = arr[window_end]
        if number == 1:
            ones_in_window += 1
    
        while window_end - window_start + 1 - ones_in_window > K:
            if arr[window_start] == 1:
                ones_in_window -= 1
            window_start += 1

        longest = max(longest, window_end - window_start + 1)
        
    return longest

print(find_longest_subarr_having_all_ones(
    [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(find_longest_subarr_having_all_ones(
    [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
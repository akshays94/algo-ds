'''
largest range:

write a function that takes in an array of integer and returns an array of length 2 representing the largest range of numbers contained in that array

'''

def largest_range_1(arr):
    
    arr.sort()
        
    max_size = 1
    best_range = [arr[0]] * 2
    
    curr_max = 1
    curr_range = [arr[0]] * 2
    
    for i in range(1, len(arr)):        
        prev = arr[i - 1]
        curr = arr[i]        
        is_excatly_next_number = prev == curr - 1 or prev == curr        
        if is_excatly_next_number:
            curr_range[1] = curr
            curr_max += 1
        else:
            curr_range = [curr] * 2
            curr_max = 1            
        if curr_max > max_size:
            max_size = curr_max
            best_range[0], best_range[1] \
                = curr_range[0], curr_range[1]
    return best_range


def largest_range_2(arr):
    
    is_visited = { number: False for number in arr }
    
    max_size = float('-inf')
    best_range = [float('-inf'), float('-inf')]

    for number in arr:
        
        if not is_visited[number]:

            curr_size = 1
            curr_range = [number] * 2

            is_visited[number] = True

            prev = number - 1
            while prev in is_visited:
                is_visited[prev] = True
                curr_range[0] = prev
                prev -= 1
                curr_size += 1
                
            upcoming = number + 1        
            while upcoming in is_visited:
                is_visited[upcoming] = True
                curr_range[1] = upcoming
                upcoming += 1
                curr_size += 1

        if curr_size >= max_size:
            max_size = curr_size
            best_range = curr_range

    return best_range                    
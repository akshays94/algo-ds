

def get_permutations(arr):
	permutations = list()
	permutations_helper(arr, [], permutations)
	return permutations

def permutations_helper(arr, curr_permutation, permutations):
	if not len(arr) and len(curr_permutation):
		permutations.append(curr_permutation)
	else:
		for i in range(len(arr)):
			new_arr = arr[:i] + arr[i + 1:]
			new_perm = curr_permutation.append(arr[i])
			permutations_helper(new_arr, new_permm permutations)
					
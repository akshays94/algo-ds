def find_level_averages(root):
  result = []

  if root is None:
    return result

  curr_level = [root]

  while curr_level:
    this_level, next_level = list(), list()
    curr_avg = sum( list(map(lambda node: node.val, curr_level)) ) / len(curr_level)
    result.append(curr_avg)
    for curr_node in curr_level:
      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)
    curr_level = next_level        

  return result
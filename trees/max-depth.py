def find_maximum_depth(root):
  if root is None:
    return 0

  curr_level = [root]
  max_levels = 0

  while curr_level:
    next_level = list()
    max_levels += 1
    for curr_node in curr_level:
      # if curr_node.left is None and curr_node.right is None:
        # return min_levels
      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)  
    curr_level = next_level
  
  return max_levels
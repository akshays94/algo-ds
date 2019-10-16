def traverse(root):
  result = []
  
  if root is None:
    return result

  curr_level = [root]
  is_reverse = True

  while curr_level:
    this_level = list()
    next_level = list()

    for curr_node in curr_level:
      this_level.append(curr_node.val)
      if is_reverse:
        if curr_node.right:
          next_level.append(curr_node.right)
        if curr_node.left:
          next_level.append(curr_node.left)    
      else:  
        if curr_node.left:
          next_level.append(curr_node.left)
        if curr_node.right:
          next_level.append(curr_node.right)
    
    result.append(this_level)
    curr_level = next_level
    is_reverse = not is_reverse      

  return result
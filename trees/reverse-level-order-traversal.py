def traverse(root):
    result = []
  
    if root is None:
      return result
    
    curr_level = [root]

    while curr_level:
      
      this_level = list()
      next_level = list()

      for curr_node in curr_level:
        this_level.append(curr_node.val)
        if curr_node.left is not None:
          next_level.append(curr_node.left)
        if curr_node.right is not None:
          next_level.append(curr_node.right)

      result.insert(0, this_level)
      curr_level = next_level      
    
    return result
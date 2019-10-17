def tree_right_view(root):
  if root is None:
    return []

  curr_level = [root]
  result = []
  
  while curr_level:
    
    next_level = list()  
    for index in range( len(curr_level) ):
      
      curr_node = curr_level[index]

      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)  

    result.append(curr_level[-1]) 

    curr_level = next_level  

  return result
  
def find_successor(root, key):
  if root is None:
    return None

  curr_level = [root]
  is_next_level_first_num_successor = False

  while curr_level:
    next_level = list()
    
    for index in range(len(curr_level)):
      
      curr_node = curr_level[index]

      if is_next_level_first_num_successor:
        return curr_node

      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)    

      if key == curr_node.val:
        is_last_node_in_level = index == len(curr_level) - 1
        if is_last_node_in_level:
          is_next_level_first_num_successor = True
        else:
          return curr_level[index + 1]  

    curr_level = next_level  

  return None
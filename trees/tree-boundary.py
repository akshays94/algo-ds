def find_leaves(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [root]
  return find_leaves(root.left) + find_leaves(root.right)  


def find_tree_boundary(root):
  result = []
  if root is None:
    return result

  curr_level = [root]

  left_view = list()
  right_view = list()

  while curr_level:
    next_level = list()
    for index in range( len(curr_level) ):
      curr_node = curr_level[index]
      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)
      
      if index == 0:    
        left_view.append(curr_node)
      if index == len(curr_level) - 1:
        right_view.insert(0, curr_node)
    
    curr_level = next_level  

  leaves = find_leaves(root)

  result = left_view
  
  for leaf in leaves:
    if leaf not in result:
      result.append(leaf)

  for right_view_node in right_view:
    if right_view_node not in result:
      result.append(right_view_node)    

  return result

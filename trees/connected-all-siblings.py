def connect_all_siblings(root):
  # TODO: Write your code here
  if root is None:
    return

  curr_level = [root]

  while curr_level:
    next_level = list()

    for index in range( len(curr_level) ):
      curr_node = curr_level[index]

      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)  

      is_last_node_level = index == len(curr_level) - 1
      if is_last_node_level:
        if next_level:
          curr_node.next = next_level[0]
        else:
          curr_node.next = None      
      else:
        curr_node.next = curr_level[index + 1]     

    curr_level = next_level
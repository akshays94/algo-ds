def connect_level_order_siblings(root):
  # TODO: Write your code here
  if root is None:
    return

  curr_level = [root]
  while curr_level:
    next_level = list()
    for index in range(len(curr_level)):
      curr_node = curr_level[index]
      if index == len(curr_level) - 1:
        curr_node.next = None
      else:
        curr_node.next = curr_level[index + 1]
      if curr_node.left:
        next_level.append(curr_node.left)
      if curr_node.right:
        next_level.append(curr_node.right)      
    curr_level = next_level 
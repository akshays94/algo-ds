def has_path(root, sum):
  
  if root is None:
    return False
    
  if root.left is None and root.right is None:
    if root.val == sum:
      return True
    return False  

  new_sum = sum - root.val
  return has_path(root.left, new_sum) or has_path(root.right, new_sum)

def reverse(head):
  
  if head is None or head.next is None:
    return head

  prev, curr, next = None, head, None

  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
  
  return prev
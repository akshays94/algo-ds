
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '[{}]'.format(self.value)


class LinkedList(object):
    def __init__(self):
        self.head = None

    def __str__(self):
        curr = self.head
        list_items = list()
        while curr is not None:
            list_items.append(curr.value)
            curr = curr.next
        return '=>'.join(map(lambda i: '[{}]'.format(i), list_items)) if list_items else '[EMPTY]'

    def insert_at_start(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    

if __name__ == "__main__":
    new_list = LinkedList()
    print('new_list', new_list)                    

    items_to_add = list(range(1, 10))    
    for item in items_to_add:
        new_list.insert_at_start(item)

    items_to_add = list(range(81, 91))    
    for item in items_to_add:
        new_list.insert_at_end(item)

    positions = [3, 2, 1, 5, 7]
    items_to_add = [3000, 2000, 1000, 5000, 7000]
    for index, item in enumerate(items_to_add):
        new_list.insert_at_position(item, positions[index])       

    print('new_list', new_list)                    
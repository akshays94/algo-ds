class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data=data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None 
        data = self.top.data
        self.top = self.top.next
        return data
    
    def is_empty(self):
        return True if not self.top else False
    
    def peek(self):
        return None if not self.top else self.top.data

def main():
    print('Running stack')
    s = Stack()
    s.push('a')
    s.push('k')
    s.push('s')
    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.push('h')
    print(s.pop())
    print(s.peek())
    s.push('a')
    s.push('y')
    print(s.peek())

if __name__ == '__main__':
    main()
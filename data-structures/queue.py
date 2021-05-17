class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.back = None

    def enqueue(self, data):
        new_node = Node(data=data)
        if not self.front:
            self.front = new_node
        else:
            self.back.next = new_node
        self.back = new_node

    def dequeue(self):
        if not self.front: 
            return None
        data = self.front.data
        self.front = self.front.next
        return data
    
    def is_empty(self):
        return True if not self.front else False

def main():
    print('Running queue')
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(6)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())


if __name__ == '__main__':
    main()
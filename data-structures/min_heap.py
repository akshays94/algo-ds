'''
            0
        1       2
    3     4   5     6 
Left child: 2i + 1
Right child: 2i + 2
Left child's parent [ODD INDEX]: (i - 1)/2
Right child's parent [EVEN INDEX]: (i - 2)/2
'''

class MinHeap:

    def __init__(self):
        self.heap = []
    
    def get_parent(self, i):
        return (i - 2) / 2 if i % 2 == 0 else (i - 1) / 2
    
    def get_child(self, i, category='LEFT'):
        i = (2 * i) + 1 if category == 'LEFT' else (2 * i) + 2
        if i > len(self.heap) - 1:
            return -1  # no child
        return i

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i] 

    def perform_bubble_up(self):
        index = len(self.heap) - 1
        parent_index = self.get_parent(index)
        while parent_index >= 0 and self.heap[parent_index] > self.heap[index]:
            self.swap(parent_index, index)
            index = parent_index
            parent_index = self.get_parent(index)

    def perform_bubble_down(self):
        index = 0
        left_child_i = self.get_child(index, 'LEFT')
        right_child_i = self.get_child(index, 'RIGHT')

        while(
            (left_child_i >= 0 and self.heap[left_child_i] < self.heap[index])
            or (right_child_i >= 0 and self.heap[right_child_i] < self.heap[index])
        ):
            left_diff = \
                self.heap[index] - self.heap[left_child_i] if left_child_i >= 0 else float('-inf')
            
            right_diff = \
                self.heap[index] - self.heap[right_child_i] if right_child_i >= 0 else float('-inf')
            
            if left_diff > 0 and right_diff > 0:  # both min
                if left_diff >= right_diff:  # choose left if smaller
                    self.swap(left_child_i, index)
                    new_child_i = left_child_i
                else:  # choosing right
                    self.swap(right_child_i, index)
                    new_child_i = right_child_i
            else:
                if left_diff > 0: # only left small
                    self.swap(left_child_i, index)
                    new_child_i = left_child_i

                elif right_diff > 0: # only right small
                    self.swap(right_child_i, index)
                    new_child_i = right_child_i

            index = new_child_i
            left_child_i = self.get_child(new_child_i, 'LEFT')
            right_child_i = self.get_child(new_child_i, 'RIGHT')


    def push(self, data):
        self.heap.append(data)
        self.perform_bubble_up()
    
    def poll(self):
        if not self.heap:
            return None
        root = 0
        last_index = len(self.heap) - 1
        self.heap[root], self.heap[last_index] = \
            self.heap[last_index], self.heap[root]

        # remove last element (which was the root)
        data = self.heap.pop()

        self.perform_bubble_down()
        return data   


def main():
    print('Running min heap')
    h = MinHeap()
    h.push(10)
    h.push(2)
    h.push(2500)
    h.push(59500)
    h.push(3)
    h.push(4)
    h.push(44)
    h.push(500)
    h.push(1)
    h.push(-1)
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())
    print(h.poll())

if __name__ == '__main__':
    main()
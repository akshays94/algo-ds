
class Node: 

    def __init__(self, data):
        self.data = data
        self.parent = self
    
    def __repr__(self):
        if self.data == self.parent.data:
            return '[{}]'.format(self.data) 
        return '[{}={}]'.format(self.data, self.parent.data)


class UnionFind:

    def __init__(self):
        self.parent_position = []
        self.elements_map = {}

    def add(self, data):
        new_node = Node(data)
        self.elements_map.update({data: new_node})
        # print(self.elements_map)

    def find(self, data):
        return self.find_parent(self.elements_map[data])

    def find_parent(self, node):
        while node.parent != node:
            node = node.parent
        return node

    def union(self, x, y):
        x_node = self.elements_map[x]
        y_node = self.elements_map[y]
        x_parent = self.find_parent(x_node)
        y_parent = self.find_parent(y_node)

        if x_parent.data != y_parent.data:
            x_parent.parent = y_parent

        # print('*', self.elements_map)

def main():
    print('Running union find ...')
    uf = UnionFind()
    uf.add('A')
    uf.add('B')
    uf.add('C')
    uf.add('D')
    uf.add('E')
    uf.add('F')
    uf.add('Foo')
    uf.add('Bar')

    uf.union('A', 'C')
    uf.union('C', 'E')
    uf.union('F', 'A')
    uf.union('B', 'D')
    uf.union('B', 'Foo')
    uf.union('A', 'Foo')
    uf.union('D', 'Bar')

    print(uf.find('A'))
    print(uf.find('B'))
    print(uf.find('C'))
    print(uf.find('D'))
    print(uf.find('E'))
    print(uf.find('F'))
    print(uf.find('Foo'))
    print(uf.find('Bar'))

if __name__ == '__main__':
    main()
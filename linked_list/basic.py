class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
node1 = Node(10)
node2 = Node(20)
node1.next = node2
print(f"Data: {node1.data},Address: {node1.next}")
print(f"Data: {node1.next.data}, Address: {node2.next}")
print(node1)
print(node2)
print(type(node1))
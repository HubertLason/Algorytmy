class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def newNode(key):
    return Node(key)

a = Node(2)
a.next = Node(8)
a.next.next = Node(21)
a.next.next.next = Node(56)

b=Node(7)
b.next=Node(9)
b.next.next=Node(24)

v=[]
while (a is not None):
    v.append(a.key)
    a = a.next

while (b is not None):
    v.append(b.key)
    b=b.next

v.sort()
result=Node(-1)
temp=result
for i in range(len(v)):
    result.next=Node(v[i])
    result=result.next
temp=temp.next

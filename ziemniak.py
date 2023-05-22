import random

class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)


def hotPotato(names, num):
    q=Queue()
    for name in names:
        q.enqueue(name)

    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())

        q.dequeue()

    return q.dequeue()

a=random.randint(3,20)
print(hotPotato(["a","b","c","d","e","f"],a))

class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


open=["[", "{", "("]
close=["]", "}", ")"]

def check(myStr):
    s = Stack()
    for i in myStr:
        if i in open:
            s.push(i)
        elif i in close:
            a = close.index(i)
            if s.size() > 0 and open[a] == s.peek():
                s.pop()
            else:
                return False
    if s.size() == 0:
        return True
    else:
        return False

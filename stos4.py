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

def onp(SymbolString):
    s=Stack()
    index=0
    while index < len(SymbolString):
        symbol=SymbolString[index]
        if symbol.isdigit()==True:
            s.push(symbol)

        elif symbol=="+" or symbol=="-" or symbol=="/" or symbol=="*":
            a=str(s.peek())
            s.pop()
            b=str(s.peek())
            s.pop()
            c=eval(b+symbol+a)
            s.push(c)

        elif symbol=="^":
            symbol="**"
            a=str(s.peek())
            s.pop()
            b=str(s.peek())
            s.pop()
            c=eval(b+symbol+a)
            s.push(c)

        elif symbol=="=":
            return s.peek()
        index+=1

print(onp( "7 3 + 5 2 - 2 ^ * =" ))




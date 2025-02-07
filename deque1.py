'''
empty,append,appendleft,pop,popleft,peek,peekleft,size)
'''
class Deque:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def append(self,value):
        self.items.append(value)
    def appendleft(self,value):
        self.items.insert(2,value)
    def pop(self):
        if self.isempty():
            raise IndexError("pop is not preformed");
        return self.items.pop()
    def popleft(self):
        if self.isempty():
            raise IndexError("popleft is not preformed");
        return self.items.pop(0)
    def peek(self):
        if self.isempty():
            raise IndexError("peek is not preformed");
        return self.items[-1]
    def peekleft(self):
        if self.isempty():
            raise IndexError("peek is not preformed");
        return self.items[0]
    def size(self):
        return len(self.items)
if __name__=="__main__":
    d=Deque()
    d.append(10)
    d.append(20)
    d.append(30)
    print(d.items)
    d.appendleft(100)
    d.appendleft(200)
    d.appendleft(300)
    print(d.items)
    pop1=d.pop()
    print("Pop elements:",pop1)
    popleft1=d.popleft()
    print("Pop elements:",popleft1)
    print(d.items)
    print("Peek:",d.peek())
    print("Peekleft:",d.peekleft())
    print("Size:",d.size())
    

    
        

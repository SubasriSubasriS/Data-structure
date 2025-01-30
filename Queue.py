class Queue:
    def __init__(self):
        self.items=[]
    def size(self):
        return len(self.items)
    def isempty(self):
        return len(self.items)==0
            
    def enqueue(self,val):
        return self.items.append(val)
    def dequeue(self):
        return self.items.pop()
    def front(self):
        if not self.isempty():
            return self.items[0]
    def print(self):
        print("QUEUE:","->".join(map(str,self.items)))
if __name__=="__main__":
    e=Queue()
    e.enqueue(10)
    e.enqueue(200)
    e.enqueue(90)
    e.enqueue(40)
    e.print()
    e.dequeue()
    e.print()
    print("Front Element:", e.front())  # Print front element
    print("Queue Size:", e.size())
    print("Empty:",e.isempty())
    


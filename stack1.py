class Stack:
    def __init__(self):  
        self.items = []

    def size(self):
        return len(self.items)

    def isempty(self):
        return len(self.items) == 0

    def push(self, val):
        self.items.append(val)

    def pop(self):
        if not self.isempty():
            return self.items.pop()  

    def top(self):
        if not self.isempty():
            return self.items[-1]  

    def print_stack(self):
        print("Stack:", " -> ".join(map(str, self.items)))

if __name__ == "__main__":  
    st = Stack()
    
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(20)
    
    st.print_stack()
    print("Size:",st.size())
    print("pop:",st.pop())
    print("EMpty:",stisempty())
    print("Top:", st.top())  

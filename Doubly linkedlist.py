class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None
        self.previous = None  


class DoublyLinkedList:
    def __init__(self):
        self.head = None  
        self.tail = self.head  
        self.length = 0  

    def print_list(self):
        if self.head == None:
            print("Empty")
        else:
            current_node = self.head
            while current_node != None:
                print(current_node.data, end='->')  # Print data of each node
                current_node = current_node.next
        print()

    def append(self, data):
        new_node = Node(data)  # Create a new node
        if self.head == None:
            self.head = new_node  # If list is empty, set head to new node
            self.tail = self.head  # Tail is also the new node
            self.length += 1
            return
        else:
            new_node.previous = self.tail  # Link new node to the tail
            self.tail.next = new_node  # Link tail to the new node
            self.tail = new_node  # Update the tail to the new node
            self.length += 1
            return

    def prepend(self, data):
        new_node = Node(data)  # Create a new node
        if self.head == None:
            self.head = new_node  # If list is empty, set head to new node
            self.tail = self.head  # Tail is also the new node
            self.length += 1
            return
        else:
            new_node.next = self.head  # Link new node to the head
            self.head.previous = new_node  # Link head to the new node
            self.head = new_node  # Update the head to the new node
            self.length += 1
            return

    def insert(self, position, data):
        if position == 0:
            self.prepend(data)  # Insert at the head
            return
        if position >= self.length:
            self.append(data)  # Insert at the tail
            return
        else:
            new_node = Node(data)  # Create a new node
            current_node = self.head
            for i in range(position - 1):
                current_node = current_node.next  # Traverse to the position
            new_node.previous = current_node  # Link new node to the current node
            new_node.next = current_node.next  # Link new node to the next node
            current_node.next = new_node  # Link current node to the new node
            new_node.next.previous = new_node  # Link next node to the new node
            self.length += 1
            return

    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return

        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next  # Move head to the next node
            if self.head == None or self.head.next == None:
                self.tail = self.head  # Update tail if list is empty or has one node
            if self.head != None:
                self.head.previous = None  # Update head's previous pointer
            self.length -= 1
            return
        try:
            while current_node != None and current_node.next.data != data:
                current_node = current_node.next  # Traverse to the node to be deleted
            if current_node != None:
                current_node.next = current_node.next.next  # Skip the node to delete
                if current_node.next != None:
                    current_node.next.previous = current_node  # Update previous pointer
                else:
                    self.tail = current_node  # Update tail if last node is deleted
                self.length -= 1
                return
        except AttributeError:
            print("Given value not found.")
            return
        
if __name__ == '__main__':
    dll=DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    
    dll.prepend(0)
    dll.prepend(-1)
    
    dll.insert(2,100)
    
    dll.delete_by_value(2)
    
    dll.print_list()
    

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
        self.length=0
    def append(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            self.length=1
        else:
            self.tail.next=newnode
            self.tail=newnode
            self.length+=1
    def prepend(self,data):
        newnode=Node(data)
        if self.head==None:
            self.head=newnode
            self.tail=self.head
            self.length+=1
        else:
            newnode.next=self.head
            self.head=newnode
            self.length +=1
        
    def println(self):
        if self.head==None:
            print("LinkedList is empty")
        else:
            currentnode=self.head
            while currentnode!=None:
                print("LinkedList",currentnode.data)
                currentnode = currentnode.next
        print()
    def delete_by_value(self, data):
        if self.head == None:
            print("Linked List is empty. Nothing to delete.")
            return
        current_node = self.head
        if current_node.data == data:
            self.head = self.head.next  # Update head
            if self.head == None or self.head.next == None:
                self.tail = self.head  # Update tail
            self.length -= 1
            return
        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next  # Traverse list
        if current_node.next != None:
            current_node.next = current_node.next.next  # Delete node
            if current_node.next == None:
                self.tail = current_node  # Update tail
            self.length -= 1
            return
        else:
            print("Given value not found.")
def print_menu():
        print("\nMenu:")
        print("1. Append an element")
        print("2. Prepend an element")
        print("3. Delete an element by value")
        print("4. Print the list")
        print("5. Exit")
        
    
if __name__ == "__main__":
    l=LinkedList()
   
    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            try:
                data = int(input("Enter the integer value to append: "))
                l.append(data)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "2":
            try:
                data = int(input("Enter the integer value to prepend: "))
                l.prepend(data)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "3":
            try:
                data = int(input("Enter the integer value to delete: "))
                l.delete_by_value(data)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == "4":
            l.println()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


    
    
            
    

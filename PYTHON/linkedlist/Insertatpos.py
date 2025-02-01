

# Class to create a single node in the linked list
class Node:
    def __init__(self, data):
        # Each node has some data and a pointer to the next node
        self.data = data
        self.next = None

# Class to create a linked list
class LinkedList:
    def __init__(self):
        # Initialize the head of the list as None (empty list)
        self.Head = None

    # Method to insert a node at the end of the list
    def Insert_at_end(self, data):
        NewNode = Node(data)  # Create a new node with the given data
        
        # If the list is empty, the new node becomes the head
        if self.Head is None:
            self.Head = NewNode
            return
        
        # Traverse to the last node
        current = self.Head
        while current.next is not None:
            current = current.next
        
        # Append the new node at the end of the list
        current.next = NewNode

    # Method to insert a node at the start of the list
    def Insert_at_start(self, data):
        NewNode = Node(data)  # Create a new node with the given data
        NewNode.next = self.Head  # Point the new node to the previous head
        self.Head = NewNode  # Make the new node the new head

    # Method to insert a node at a specific position
    def Insert_at_pos(self, pos, data):
        NewNode = Node(data)  # Create a new node with the given data

        # If the list is empty, the new node becomes the head
        if self.Head is None:
            self.Head = NewNode
            return

        # If inserting at the start, use Insert_at_start method
        if pos == 0:
            self.Insert_at_start(data)
            return

        # Traverse to the position where the new node is to be inserted
        count = 0
        current = self.Head
        prev = None  # To keep the previous node reference

        # Traverse till the position is reached
        while current is not None and count < pos:
            prev = current
            current = current.next
            count += 1
        
        # Insert the new node at the position
        if prev is not None:
            NewNode.next = current
            prev.next = NewNode

    # Method to display the entire list
    def Display(self):
        # Check if the list is empty
        if self.Head is None:
            print("List is Empty")
            return
        
        # Start from the head and follow next pointers till end of list
        current = self.Head
        while current is not None:
            print(current.data, end=' --> ')  # Display the current node data
            current = current.next
        print('Ending the List Here')  # Indicate the end of the list

if __name__ == '__main__':
    l1 = LinkedList()
    l1.Insert_at_end(10)
    l1.Insert_at_end(20)
    l1.Insert_at_end(30)
    l1.Insert_at_end(40)
    l1.Insert_at_end(50)
    l1.Insert_at_end(60)
    
    l1.Display()  # Displays the list

    l1.Insert_at_start(5)  # Inserts 5 at the start of the list

    l1.Display()  # Displays the list

    l1.Insert_at_pos(3, 3)  # Inserts 3 at the 4th position (position index starts from 0)

    l1.Display()  # Displays the list

    l1.Insert_at_pos(5, 'fifth')  # Inserts 'fifth' at the 6th position
    
    l1.Display()  # Displays the final list

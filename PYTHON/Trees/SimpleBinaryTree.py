class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def Insert(self, data):
        
        if self.root is None:
            self.root = Node(data)
        
        else:
            self._Insert(self.root, data)
        
    
    def _Insert(self, node, data):
        
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                
            else:
                self._Insert(node.left, data)
                
        elif data > node.data:
            
            if node.right is None:
                node.right = Node(data)
            else:
                self._Insert(node.right, data)
    
    
    def in_order_traversal_start(self):
        
        self.in_order_traversal(self.root)
        
    
    def in_order_traversal(self, node):
         if node:
             self.in_order_traversal(node.left)
             print(node.data,end = ' ')
             self.in_order_traversal(node.right)



if __name__ == '__main__':
    bt = BinaryTree()
    bt.Insert(10)
    bt.Insert(5)
    bt.Insert(15)
    bt.Insert(3)
    bt.Insert(7)
    bt.Insert(12)
    bt.Insert(18)
    
    print("In-order Traversal:")
    bt.in_order_traversal_start()

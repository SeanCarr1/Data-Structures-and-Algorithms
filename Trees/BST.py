class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root == None:
            self.root = TreeNode(value)
            return

        self._insert_recursively(self.root, value)
    
    def _insert_recursively(self, node, value):   
        current_node = node
        new_node = TreeNode(value)
        left = current_node.left
        right = current_node.right

        if value < current_node.value:
            #go left
            if not left:
                current_node.left = new_node
                return
            
            self._insert_recursively(left, value)
            return
        
        if value >= current_node.value:
            if not right:
                current_node.right = new_node
                return
            
            self._insert_recursively(right, value)
            return
        
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def search(self, value):
        curr_node = self.root

        while curr_node and curr_node.value != value:
            node_val = curr_node.value
            
            if value > node_val:
                curr_node = curr_node.right
                continue

            if value < node_val:
                curr_node = curr_node.left

        return True


bst = BinarySearchTree()
bst.insert(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(6)
bst.insert(7)
bst.inorder_traversal(bst.root)
print(bst.search(8))
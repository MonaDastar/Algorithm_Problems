class TreeNode:
    """
    Represents a node in a binary tree.
    
    Attributes:
        data: The data stored in the node.
        left: Reference to the left child node.
        right: Reference to the right child node.
    """
    def __init__(self, data) :
        """
        Initializes a TreeNode.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    """
    Represents a binary tree.

    Attributes:
        root: Reference to the root node of the binary tree.
    """
    
    def __init__(self):
        """
        Initializes an empty BinaryTree.
        """
        self.root = None
        
    def insert(self, data):
        """
        Inserts a new node with the given data into the binary tree.

        Args:
            data: The data to be inserted into the tree.
        """
        if not self.root:
            self.root = TreeNode(data) #composition involves creating instances of one class within another to combine their functionalities. In your code, the BinaryTree class has an instance variable, self.root, which is an instance of the TreeNode class. This allows the BinaryTree class to use and manage TreeNode instances as part of its internal structure.
        else:
            self._recursive_insertion(self.root, data)
        
    def _recursive_insertion(self, current, data):
        """An internal method used for the recursive insertion of nodes into the binary tree. It is not intended to be called directly by users of the class. Users are expected to call the public insert method.
            Recursively inserts a new node with the given data into the binary tree.
            Args:
            current: The current node being considered.
            data: The data to be inserted into the tree.

        """
        if data < current.data:
            if not current.left:
                current.left = TreeNode(data)
            else:
                self._recursive_insertion(current.left,data)
        else:
            if not current.right:
                current.right = TreeNode(data)
            else:
                self._recursive_insertion(current.right, data)
                
    def search(self, data):
        """
        Searches for a node with the given data in the binary tree.

        Args:
            data: The data to search for.

        Returns:
            True if the data is found in the tree; otherwise, False.
        """
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, current, data):
        """
        Recursively searches for a node with the given data in the binary tree.

        Args:
            current: The current node being considered.
            data: The data to search for.

        Returns:
            True if the data is found in the tree; otherwise, False.
        """
        if current is None:
            return False
        if data == current.data:
            return True
        elif data < current.data:
            return self._search_recursive(current.left , data)
        else:
            return self._search_recursive(current.right , data)

    def inorder_traverse(self):
        """
        Performs an inorder traversal of the binary tree.

        Returns:
            A list containing the elements of the tree in sorted order.
        """
        result = []
        self._inorder_recursive(self.root,result)
        return result
    
    def _inorder_recursive(self,node, result):
        """
        Recursively performs an inorder traversal of the binary tree.

        Args:
            node: The current node being considered.
            result: A list to store the elements in sorted order.
        """
        if node:
            self._inorder_recursive(node.left,result)
            result.append(node.data)
            self._inorder_recursive(node.right,result)
        









tree = BinaryTree()
unsorted_array = [5,8,1,3,4,10,9]
for node in unsorted_array:
    tree.insert(node)
print(tree.inorder_traverse())
print(tree.search(5))
tree.insert(80)
print(tree.inorder_traverse())

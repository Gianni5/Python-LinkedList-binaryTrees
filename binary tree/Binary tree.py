class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []

        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

    def delete_Node(self, node, key):
        if node.data == key and node.right is not None and node.left is not None:
            if root.data == key:
                temp = node
                node = temp.right.left
                node.right = temp.right
                node.left = temp.left
                node.right.left = None
                return node
            else:
                temp = node
                node = temp.left
                node.right = temp.right
                return node

        # if root doesn't exist, just return it
        if not node:
            return node
        # Find the node in the left subtree	if key value is less than root value
        if node.data > key:
            node.left = self.delete_Node(node.left, key)
        # Find the node in right subtree if key value is greater than root value,
        elif node.data < key:
            node.right = self.delete_Node(node.right, key)
            return node
        # Delete the node if root.value == key
        else:
            # If there is no right children delete the node and new root would be root.left
            if not node.right:
                return node.left
            # If there is no left children delete the node and new root would be root.right
            if not node.left:
                return node.right
            # If both left and right children exist in the node replace its value with
            # the minimum value in the right subtree. Now delete that minimum node
            # in the right subtree
            temp_val = node.right
            mini_val = temp_val.data
            while temp_val.left:
                temp_val = temp_val.left
                mini_val = temp_val.data
            # Delete the minimum node in right subtree
            node.data = self.delete_Node(node.right, mini_val)

        return node


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.insert(50)

print(f" before1:", root.inorderTraversal(root))
print(f" before2:", root.PreorderTraversal(root))
print(f" before3:", root.PostorderTraversal(root))
root = root.delete_Node(root, 27)
print(f" after1:", root.inorderTraversal(root))
print(f" after2:", root.PreorderTraversal(root))
print(f" after3:", root.PostorderTraversal(root))
print(root.data)

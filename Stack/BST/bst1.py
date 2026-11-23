# Binary Search Tree

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return
        else:
            temp = self.root

            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left

                elif new_node.data >= temp.data:
                    if temp.right is None:
                        temp.right = new_node
                        return
                    else:
                        temp = temp.right


# Inorder Traversal
def inorder(temp):
    if temp is None:
        return
    else:
        inorder(temp.left)
        print(temp.data, end=" ")
        inorder(temp.right)


# Count total nodes
def count_nodes(temp):
    if temp is None:
        return 0
    else:
        return 1 + count_nodes(temp.left) + count_nodes(temp.right)


btree = BST()

btree.insert(Node(10))
btree.insert(Node(5))
btree.insert(Node(2))
btree.insert(Node(25))
btree.insert(Node(13))
btree.insert(Node(40))

print("Inorder Traversal:")
inorder(btree.root)

print("\nTotal Nodes:", count_nodes(btree.root))
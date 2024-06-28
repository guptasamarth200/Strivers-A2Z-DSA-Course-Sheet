# Python code for post-order tree traversal

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Post-order traversal:")
post_order_traversal(root)  # Output: 4 5 2 3 1
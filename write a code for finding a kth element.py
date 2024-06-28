# write a  code for finding a kth element inn binary search tree ?
# Define a Node class to represent a node in the Binary Search Tree (BST)
class Node:
    def __init__(self, val):
        # Initialize the node with a value, and set its left and right children to None
        self.val = val
        self.left = None
        self.right = None

# Define a function to insert a new node into the BST
def insert_node(root, val):
    # If the root is None, create a new node with the given value and return it
    if root is None:
        return Node(val)
    # If the value is less than the root's value, insert it into the left subtree
    if val < root.val:
        root.left = insert_node(root.left, val)
    # If the value is greater than or equal to the root's value, insert it into the right subtree
    else:
        root.right = insert_node(root.right, val)
    # Return the updated root node
    return root

# Define a function to find the kth smallest element in the BST
def kth_smallest(root, k):
    # Initialize a stack to keep track of nodes to visit
    stack = []
    # Initialize a counter to keep track of the kth smallest element
    k_counter = k
    # Traverse the BST in-order (i.e., ascending order)
    while root or stack:
        # Move to the leftmost node (i.e., the smallest node)
        while root:
            stack.append(root)
            root = root.left
        # Backtrack and visit the node at the top of the stack
        root = stack.pop()
        # Decrement the k counter
        k_counter -= 1
        # If we've reached the kth smallest element, return its value
        if k_counter == 0:
            return root.val
        # Move to the right subtree
        root = root.right
    # If we've traversed the entire BST and haven't found the kth smallest element, return None
    return None

# Define a main function to interact with the user
def main():
    # Initialize the root node to None
    root = None
    # Ask the user to input the number of nodes to insert into the BST
    num_nodes = int(input("Enter the number of nodes: "))
    # Loop through and insert each node into the BST
    for i in range(num_nodes):
        val = int(input(f"Enter node {i+1} value: "))
        root = insert_node(root, val)
    # Ask the user to input the value of k
    k = int(input("Enter the value of k: "))
    # Find the kth smallest element in the BST
    result = kth_smallest(root, k)
    # Print the result
    if result is not None:
        print(f"The {k}th smallest element is {result}")
    else:
        print(f"There are less than {k} nodes in the BST")

# Call the main function when the script is run
if __name__ == "__main__":
    main()
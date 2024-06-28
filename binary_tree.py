class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sum_root_to_leaf(root):
    def helper(node, current_number):
        if node is None:
            return 0
        current_number = current_number * 10 + node.val
        if node.left is None and node.right is None:
            return current_number
        return helper(node.left, current_number) + helper(node.right, current_number)

    return helper(root, 0)

def main():
    root = None
    num_nodes = int(input("Enter the number of nodes: "))
    for i in range(num_nodes):
        val = int(input(f"Enter node {i+1} value: "))
        if root is None:
            root = Node(val)
        else:
            nodes = [root]
            while nodes:
                node = nodes.pop(0)
                if node.left is None:
                    node.left = Node(val)
                    break
                else:
                    nodes.append(node.left)
                if node.right is None:
                    node.right = Node(val)
                    break
                else:
                    nodes.append(node.right)

    sum = sum_root_to_leaf(root)
    print("The sum of all root-to-leaf numbers is:", sum)

if __name__ == "__main__":
    main()
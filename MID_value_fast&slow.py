# Python code to find the middle value of a linked list using fast and slow pointers

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def find_middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow.value

# Example usage:
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Middle value:", find_middle(head))  # Output: 3
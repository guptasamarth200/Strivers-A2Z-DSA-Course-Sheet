class Queue:
    def __init__(self):
        # Initialize two stacks to implement the queue
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        # Add element to stack1 (acting as the "rear" of the queue)
        self.stack1.append(element)

    def dequeue(self):
        # If stack2 is empty, transfer elements from stack1 to stack2 (reversing the order)
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        # Return the top element of stack2 (acting as the "front" of the queue)
        return self.stack2.pop()

    def is_empty(self):
        # Check if both stacks are empty
        return not self.stack1 and not self.stack2

    def size(self):
        # Return the total size of the queue (elements in both stacks)
        return len(self.stack1) + len(self.stack2)
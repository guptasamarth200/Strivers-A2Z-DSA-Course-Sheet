# class node :
#      def __init__(self, data):
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def _init_(self):
#         self.head = None #Initialize the head of the list to None (empty list)
#     def append (self,data):
#         new_node = Node(data) #create a ne node with given data  
#         if self.head is None: # checking if the list is  empty 
#             self.head = new_node # so after checking if  the list is empty so set the new node  asthe head  
#             return #exit 
#         last_node = self.head  # Start from the head node
#         while last_node.next:  # Traverse to the last node
#             last_node = last_node.next  # Move to the next node
#         last_node.next = new_node  # Link the last node to the new node

#     # Method to print all nodes in the list for visualization
#     def print_list(self):
#         current_node = self.head  # Start from the head node
#         while current_node:  # Traverse until the end of the list
#             print(current_node.data, end=" -> ")  # Print the data of the current node
#             current_node = current_node.next  # Move to the next node
#         print("None")  # Indicate the end of the list


# # Usage example
# llist = LinkedList()  # Create an empty linked list
# llist.append(1)  # Append a node with data 1
# llist.append(2)  # Append a node with data 2
# llist.append(3)  # Append a node with data 3
# llist.print_list()  # Output the list: 1 -> 2 -> 3 -> None

#*******************************************************************

# Define the Node class to represent each element in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # Store the data of the node
        self.next = None  # Initialize the next pointer to None (no next node yet)

# Define the LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None (empty list)

    # Method to add a new node with the given data at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # Check if the list is empty
            self.head = new_node  # If empty, set the new node as the head
            return  # Exit the method since the new node is already added
        last_node = self.head  # Start from the head node
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next  # Move to the next node
        last_node.next = new_node  # Link the last node to the new node

    # Method to print all nodes in the list for visualization
    def print_list(self):
        current_node = self.head  # Start from the head node
        while current_node:  # Traverse until the end of the list
            print(current_node.data, end=" -> ")  # Print the data of the current node
            current_node = current_node.next  # Move to the next node
        print("None")  # Indicate the end of the list

# Function to take user input and populate the linked list
def populate_linked_list():
    llist = LinkedList()  # Create an empty linked list
    while True:
        user_input = input("Enter a number to add to the list (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break  # Exit the loop if the user is done entering numbers
        try:
            data = int(user_input)  # Convert the input to an integer
            llist.append(data)  # Append the data to the linked list
        except ValueError:
            print("Please enter a valid number.")  # Handle invalid input

    llist.print_list()  # Print the linked list after all inputs

# Call the function to populate the linked list
populate_linked_list()


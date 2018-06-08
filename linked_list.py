class Node(object):
    def __init__(self, data):
        '''Initialize this node with the given data'''
        self.data = data
        self.next = None

    def __repr__(self):
        '''Return a string representation of this node'''
        return 'Node({!r})'.format(self.data)

class LinkedList(object):
    def __init__(self, iterable=None):
        '''Initialize this linked list and append the given items if any'''
        self.head = None # Pointer to the first node in our linked list
        self.tail = None # Pointer to the last node in our linked list
        self.size = 0 # Integer value representing the number of nodes

        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        '''Return a list of the node's data in the linked list'''
        result = [] # Space efficiency when creating a new array
        current_node = self.head # Representing the first node in our linked list by pointing the head to it

        # Iterating through available nodes in the linked list
        while current_node is not None:
            result.append(current_node.data)

            current_node = current_node.next  # Setting the current node to the next node for the next iteration

        return result # Returning an array of the data in the nodes of our linked list

    def is_empty(self):
        return self.head is None # Going to return boolean value based off is the linked list is empty

    def length(self):
        '''Returns the length of the linked list'''
        return self.size # Constant time to return integer value

    def get_at_index(self, index_of_node):
        '''Retrieves a node a specific index in the linked list'''

        current_node = self.head # Instantiating the first node in our linked list

        # Counter that we are keeping to track the indexes of the nodes in our linked list
        node_index = 0
        if not (0 <= index_of_node < self.size): # If the index the user passes in is not valid raise value error
            raise ValueError('List index error out of range: {}'.format(index_of_node))

        if index_of_node == 0:
            return self.head.data # current_node.data Before we start iterating we can return the first nodes data

        if index_of_node == (self.size - 1): # If the index of the node that the user is looking for is the last node then we can return the tails data
            return self.tail.data

        while current_node is not None:
            current_node = current_node.next # We can bump the iteration as soon as we start the while loop because we already checked the first node saving duplicate work
            node_index += 1

            if node_index == index_of_node: # If the counter that we are keeping matches the index that the user passed in return the current nodes data
                return current_node.data

    def get_node_at_index(self, index_of_node):
        '''Retrieves a node a specific index in the linked list'''

        current_node = self.head  # Instantiating the first node in our linked list

        # Counter that we are keeping to track the indexes of the nodes in our linked list
        node_index = 0
        if not (0 <= index_of_node < self.size):  # If the index the user passes in is not valid raise value error
            raise ValueError('List index error out of range: {}'.format(index_of_node))

        if index_of_node == 0:
            return self.head  # current_node.data Before we start iterating we can return the first nodes data

        if index_of_node == (self.size - 1):  # If the index of the node that the user is looking for is the last node then we can return the tails data
            return self.tail

        while current_node is not None:
            current_node = current_node.next  # We can bump the iteration as soon as we start the while loop because we already checked the first node saving duplicate work
            node_index += 1

            if node_index == index_of_node:  # If the counter that we are keeping matches the index that the user passed in return the current nodes data
                return current_node

    def get_node_at_index_recursively(self, index_of_node, current_node=None, node_index=None):
        if current_node is None:
            current_node = self.head # Setting the current node to the head of the linked list for the first recursive call
            node_index = 0

        if not (0 <= index_of_node < self.size):  # If the index the user passes in is not valid raise value error
            raise ValueError('List index error out of range: {}'.format(index_of_node))

        if index_of_node == 0:
            return self.head

        if index_of_node == (self.size - 1):
            return self.tail

        if current_node is not None:
            current_node = current_node.next
            node_index += 1
            if node_index == index_of_node:
                return current_node
        return self.get_node_at_index_recursively(index_of_node, current_node,node_index)



    def append(self, node_data):
        '''Insert the given node data at the tail of the linked list'''

        appended_node = Node(node_data) # Representing the node that the user wants to append to the linked list
        current_node = self.head

        # If the linked list is empty
        if self.is_empty() is True: # Constant time operation to check if the linked list is empty
            self.head = appended_node

        while current_node is not None:
            if current_node.next is None:
                current_node.next = appended_node
                self.tail = appended_node
                self.size += 1
                return
            current_node = current_node.next

        self.size += 1 # Either way we are appending to the linked list therefore we have to increment the size of LL

    def reverse_linked_list_iterative(self):
        '''Reverses a linked list in a iterative fashion'''

        current_node = self.head # Represents the first node in our linked list

        previous_node = None # Represents the previous node in our linked list

        while current_node is not None:
            # Saving the next node before we reverse the pointers
            next_node = current_node.next

            current_node.next = previous_node # Settig the current nodes next pointer to the previous node in the linked list

            previous_node = current_node # Bumping up the position of the previous node to the current node for the next iteration

            current_node = next_node # Bumping up the current node to the next node that we had saved for the next iteration

        self.head = previous_node # After the while loop is finished executing set the head to the previous node which
        # is now in the front of the linked list due to our reversal

    def reverse_linked_list_recursively(self, previous_node=None, current_node=None):
        if previous_node is None and current_node is None:
            previous_node = None
            current_node = self.head

        if current_node is not None:
            next_node = current_node.next # Saving the next node for when we reverse the pointers
            current_node.next = previous_node  # Setting the current nodes next pointer to the previous node
            previous_node = current_node   # Bumping up the previous node to the current node's position for the next iteration
            current_node = next_node   # Setting the current node to the next node for the next iteration 
        else:
            self.head = previous_node
            return None # We need a case to stop the recursion and that is when we are done with all the nodes in the LL
        
        return self.reverse_linked_list_recursively(previous_node, current_node)


    def delete(self, node_data):
        '''Delete the desired node from the linked list based of the data that the user provides'''
        current_node = self.head # Representing the first node in the linked list

        found = False
        node_counter = 0

        # If the linked list is empty from the start
        if self.is_empty() is True:
            return None

        elif self.size == 1 and current_node.data == node_data:  # If the size of the linked list is 1 to start with
            self.head = None
            self.tail = None
            self.size -= 1
            return

        # If the node that the user wants to delete is the head
        elif current_node.data == node_data:
            # Saving the next node
            next_node = current_node.next

            # Setting the pointer to the next node to None
            current_node.next = None
            self.head = next_node # Setting the head to the next node that we saved
            self.size -=1

        elif self.tail.data == node_data:
            previous_node = self.get_node_at_index(self.size - 2)
            previous_node.next = None

            self.tail = previous_node
            self.size -= 1
        else:
            while current_node is not None and not found: # The purpose of this double conditional for the while loop is that so we can iterate through the rest of the node and the case then we do find the node before finishing
                if current_node.data == node_data:
                    found = True
                    print('This is the current node before setting previous node %s' %(current_node))
                    previous_node = self.get_node_at_index(node_counter - 1) # IS THERE ANOTHER WAY TO FIND THE PREVIOUS NODE IN  A SINGLY LINKED LIST
                    previous_node.next = current_node.next # Bumping out the current node from the list and setting the previous node next pointer to the next node
                    self.size -= 1

                current_node = current_node.next
                node_counter += 1

    def delete_recursively(self, node_data, current_node=None, current_node_counter=None):
        if current_node is None and current_node_counter is None:
            current_node = self.head
            current_node_counter = 0

        if self.is_empty() is True:
            return 'No nodes in the linked list to be deleted'

        elif self.size == 1 and current_node.data == node_data:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        elif current_node.data == node_data:
            next_node = current_node.next
            current_node.next = None
            self.head = next_node
            self.size -= 1
            return
        elif self.tail.data == node_data:
            print('This is the data of the tail node %s' %(self.tail.data))
            previous_node = self.get_node_at_index_recursively(self.size - 2) # Have to get the node before the tail
            previous_node.next = None
            self.tail = previous_node
            self.size -= 1
            return
        else:

            if current_node is not None:
                current_node_counter += 1  # Set it to 1 at first since we already checked for the head node
                current_node = current_node.next
                if current_node.data == node_data:

                    print('This is the current node counter %s' %(current_node))
                    previous_node = self.get_node_at_index_recursively(current_node_counter - 1)
                    previous_node.next = current_node.next
                    self.size -= 1
                    return

        return self.delete_recursively(node_data, current_node, current_node_counter)


def two_sum_alternative(number_array, target_number):
    # Keep two counters lower and upper bound
    sorted_number_array = number_array.sort()
    lower_bound_index = 0
    higher_bound_index = len(number_array) - 1

    while lower_bound_index < higher_bound_index: # O(N) time iterating
        if number_array[lower_bound_index] + number_array[higher_bound_index] > target_number: # Condtionals constant time checking and indexing
            higher_bound_index -= 1
        elif number_array[lower_bound_index] + number_array[higher_bound_index] < target_number:
            lower_bound_index += 1
        elif number_array[lower_bound_index] + number_array[higher_bound_index] == target_number:
            return number_array[lower_bound_index], number_array[higher_bound_index]

    return 'No pair found '

print(two_sum_alternative([1,2,4,6], 8))




ll = LinkedList(['A', 'B', 'C'])
ll.reverse_linked_list_iterative()
print(ll.get_node_at_index_recursively(1))
ll.delete_recursively('C')

print(ll.items())
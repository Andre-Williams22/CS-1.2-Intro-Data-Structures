#!python
from utils import time_it

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)



class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())
    @time_it 
    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list
    @time_it 
    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None


    @time_it 
    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions? Traverses through each item in the list"""
        # TODO: Loop through all nodes and count one for each
        if self.is_empty():
            return 0
        
        node = self.head
        count = 0
        while node is not None:
            node = node.next 
            count += 1
        return count
    @time_it 
    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions? The item is being added to the last item in the list. It takes constant time."""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists

        new = Node(item) # refers to the node class and creates a node object called new
        if self.is_empty(): # self refers to the linked list
            self.head = new # initialize the head node
            self.tail = new 
        else:
            self.tail.next = new   
            self.tail = new
    @time_it 
    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions? The item is being added to the beginning of the list it takes constant time."""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_head = Node(item)
        if self.is_empty():
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head = new_head

    @time_it 
    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Why and under what conditions? The item your looking for is the first item in the list
        TODO: Worst case running time: O(n) Why and under what conditions? The item in the list could be the last item""" 
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function

        node = self.head 

        while node is not None:
            if quality(node.data) == True: # check if data is equal to quality
                return node.data # node is found
            node = node.next # move to next node in the list

        return None  
            
    @time_it 
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions? The item could be the first item in the list
        TODO: Worst case running time: O(n) Why and under what conditions? the item could be the last item in the list"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        
        # initializes start
        current_node = self.head
        prev_node = None 
        # while there are no more nodes in the list
        while current_node is not None:
            # node with item's found
            if current_node.data == item:
                # if item we're removing is at head
                if prev_node is None:
                    # make head next node
                    self.head = current_node.next
                    # head is also tail
                    if current_node.next is None:
                        self.tail = prev_node
                    # item we want to remove is at tail 
                elif current_node.next is None: 
                    prev_node.next = None
                    self.tail = prev_node
                #item we want to remove is not there
                else:
                    prev_node.next = current_node.next 

                return 
                # havent found item but keep traversing linkedlist
            else:
                prev_node = current_node
                current_node = current_node.next

        raise ValueError(f'Item not found: {item}')



    def traverse(self):
        node = self.head
        while node is not None:
            node = node.next
            

    @time_it
    def replace(self, old_node, new_node):
        found = False
        if self.length() == 0:
            raise ValueError('Item not found: {}'.format(old_node))


        if self.head.data == old_node:
            self.head = new_node
            if self.length() == 0:
                self.tail = None
            return True

        current_node = self.head

        while current_node is not None:
            if current_node.data == old_node:
                current_node = new_node
                found = True
                
            current_node = current_node.next

        if found == False:
            raise ValueError('Item not found: {}'.format(old_node))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()

# main.py
# Daniel Kogan
# 12.30.2021

from copy import copy

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self, data):
        node = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = node
        else:
            self.head = node
            
    def print(self):
        print_list = []
        current = self.head
        while (current):
            print_list.append(current.data)
            current = current.next
        print(print_list)
        
    def reverse(self):
        reversed_list = LinkedList()
        current = self.head # this is the current element (first)
        last_elem = copy(current) # copy so that i am not taking a reference, last element bc reversed
        last_elem.next = None # last element should have no reference
        reversed_list.head = Node(current.next.data, last_elem)
        current = current.next # skipped an element in reversed list to reference the final element, therefore skip the same element here too
        while(current):
            if (current.next): # if there are still more elements, do this
                reversed_current = copy(reversed_list.head)
                reversed_current_next = Node(current.next.data, reversed_current)
                reversed_list.head = reversed_current_next
            current = current.next
        return reversed_list
    
ll = LinkedList()
for i in range(10):
    ll.insert(i)
    
ll.print()
rll = ll.reverse()
rll.print()
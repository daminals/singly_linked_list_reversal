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
        current = self.head
        last_elem = copy(current)
        last_elem.next = None
        reversed_list.head = Node(current.next.data, last_elem)
        current = current.next
        while(current):
            if (current.next):
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
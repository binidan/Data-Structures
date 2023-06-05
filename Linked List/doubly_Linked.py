class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete(self, data):
        if self.is_empty():
            print("Empty Linked List")
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        while current and current.data != data:
            current = current.next
        if current:
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            print("Not found!")

    def display(self):
        current = self.head
        if current == None:
            print("Empty")

        else:
            while current:
                print(current.data, end=' -> ')
                current = current.next
            print("None")

    def insert(self, data, index):
        new_node = Node(data)
        i = 0
        current = self.head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            while current and i != index:
                current = current.next
                i += 1
            new_node.next = current.next
            current.next = new_node

    def reverse(self):
        current = self.head
        prev = None

        while current:
            new_node = current.next
            current.next = prev
            prev = current
            current = new_node

        self.head = prev

    def concatenate(self, second_list):
        current = self.head
        while current.next:
            current = current.next
        current.next = second_list.head
    
    def merge_sorted_lists(self, list1, list2):
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        self.head = dummy.next
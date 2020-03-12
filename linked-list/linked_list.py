class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        if self.head == None:
            self.head = Node(item)
        elif self.tail == None:
            self.tail = Node(item)
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            temp = Node(item)
            temp.previous = self.tail
            self.tail.next = temp
            self.tail = temp

    def pop(self):
        if self.tail:
            temp = self.tail
            self.tail = self.tail.previous
            return temp.value

    def shift(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp.value

    def unshift(self, item):
        if self.tail == None:
            self.tail = Node(item)
        elif self.head == None:
            self.head = Node(item)
            self.head.next = self.tail
            self.tail.previous = self.head
        else:
            temp = Node(item)
            temp.next = self.head
            self.head.previous = temp
            self.head = temp

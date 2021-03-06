import sys
sys.stdout = open('LinkedList/output.txt', 'w')
sys.stdin = open('LinkedList/input.txt', 'r')

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split())) 

#Node class
class Node:
    #Function to initialise Node object
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked list class which uses Node object
class LinkedList:
    #Function to initialize head
    def __init__(self):
        self.head = None
    
    def insertBefore(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, new_data):
        new_node = Node(new_data)
        #Store head node: never change original head node in linked list
        temp = self.head
        if temp is None:
            self.head = new_node
            return
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

    def deleteNode(self, key):
        temp = self.head
        #if head node points to key
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        #Search in list for the key
        while temp.next is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        
        if temp == None:
            return
        
        prev.next = temp.next
        temp = None

    def print(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    
    def Partition(self, p):
        left_part_head = Node(0)
        left_part_tail = left_part_head
        right_part_head = Node(0)
        right_part_tail = right_part_head
        
        temp = self.head
        while temp is not None:
            if temp.data < p:
                new_node = Node(temp.data)
                left_part_tail.next = new_node
                left_part_tail = new_node
            else:
                new_node = Node(temp.data)
                right_part_tail.next = new_node
                right_part_tail = new_node
            temp = temp.next
        left_part_head = left_part_head.next
        left_part_tail.next = right_part_head.next
        temp1 = left_part_head
        while temp1:
            print(temp1.data)
            temp1 = temp1.next
        return left_part_head


def main():
    t = inp()
    while t > 0:
        k = inp()
        arr = inlt()
        # Start with the empty list 
        llist = LinkedList() 
        for i,val in enumerate(arr):
            llist.insertAfter(val)
        llist.Partition(k)
        t -= 1

if __name__ == "__main__": 
    main()

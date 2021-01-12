import sys
from collections import deque

sys.stdin = open('LinkedList/input.txt', 'r')
sys.stdout = open('LinkedList/output.txt', 'w')

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
    
    #Using Iterative method i.e. check first half matches with rest half by using stack
    #As the Length is not known, we will also use slow-fast runner approach
    # Push elements from first half of linked list onto stack. When fast runner
    # (which is moving at 2x speed) reaches the end of the linked list, then we
    # know we're at the middle *1 
    def IsPalindrome(self):
        sptr = self.head
        fptr = self.head
        stack = deque()
    
        while(sptr and fptr and fptr.next):
            stack.append(sptr.data)
            sptr = sptr.next
            fptr = fptr.next.next
        if fptr is not None:
            sptr = sptr.next
        while(sptr):
            val = stack.pop()
            if val != sptr.data:
                print("False")
                return
            sptr = sptr.next
        print("True")
        return

def main():
    t = inp()
    while t > 0:
        arr = inlt()
        # Start with the empty list 
        llist = LinkedList() 
        for i,val in enumerate(arr):
            llist.insertAfter(val)
        llist.IsPalindrome()
        t -= 1

if __name__ == "__main__": 
    main()

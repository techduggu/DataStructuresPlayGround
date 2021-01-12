import sys
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
    
    
    #Solution-1: Using Recursion
    def FindkthToLast_Recursion(self, k):
        temp = self.head
        if temp is None:
            return
        (index, result) = self.findkth(temp, 0, k)
        print(result)
        return
    
    def findkth(self, temp, index, k):
        if temp is None:
            return (index + 1, None)
        (index, result) = self.findkth(temp.next, index, k)
        if index == k:
            result = temp.data
        index += 1
        return (index, result)
    
    #Solution-2: Using Iterative with Two-pointers
    def FindkthToLast_Iterative(self, k):
        p1 = self.head
        p2 = p1
        index = 1
        while p2 is not None and index < k:
            index += 1
            p2 = p2.next
        while p1 is not None and p2 is not None:
            if p2.next == None:
                print(p1.data)
                return
            p1 = p1.next
            p2 = p2.next
        return

def main():
    t = inp()
    while t > 0:
        k = inp()
        arr = inlt()
        # Start with the empty list 
        llist = LinkedList() 
        for i,val in enumerate(arr):
            llist.insertAfter(val)
        #llist.FindkthToLast_Recursion(k)
        llist.FindkthToLast_Iterative(k)
        t -= 1

if __name__ == "__main__": 
    main()

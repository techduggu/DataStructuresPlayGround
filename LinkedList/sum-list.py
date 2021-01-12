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
    
    def sumlist(self, l1, l2, carry):
        if l1 is None and l2 is None and carry == 0:
            return
        value = carry
        if l1 is not None:
            value += l1.data
        if l2 is not None:
            value += l2.data
        data = value % 10
        result = Node(data)
        #Recurse
        nextNode = self.sumlist((None if l1 is None else l1.next),
                (None if l2 is None else l2.next),
                1 if value >= 10 else 0)
        result.next = nextNode
        return result


def main():
    t = inp()
    while t > 0:
        list1 = inlt()
        list2 = inlt()
        # Start with the empty list 
        llist1 = LinkedList() 
        for i,val in enumerate(list1):
            llist1.insertAfter(val)
        llist2 = LinkedList() 
        for i,val in enumerate(list2):
            llist2.insertAfter(val)
        result = llist1.sumlist(llist1.head, llist2.head, 0)
        temp = result
        while temp is not None:
            print(temp.data)
            temp = temp.next
        t -= 1

if __name__ == "__main__": 
    main()

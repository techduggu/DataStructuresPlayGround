import sys

sys.stdin = open('Trees/input.txt', 'r')
sys.stdout = open('Trees/output.txt', 'w')


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

#binary tree node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAfter(self, new_data):
        new_node = ListNode(new_data)
        if self.head == None:
            self.head = new_node
            return
        #Store head node: never change original head node in linked list
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node

def list_of_depths_bfs(node):
    queue = []
    list = []
    queue.append(node)
    while queue:
        levelNodes = len(queue)
        llist = LinkedList()
        while levelNodes > 0:
            n = queue.pop(0)
            llist.insertAfter(n.data)
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
            levelNodes -= 1
        list.append(llist)
    return list
        

def main():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)
    list = list_of_depths_bfs(node)
    for i in list:
        temp = i.head
        while(temp):
            if temp.next:
                print(temp.data, end="->")
            else:
                print(temp.data)
            temp = temp.next

if __name__ == "__main__": 
    main()

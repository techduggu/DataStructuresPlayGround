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

def createminimaltree(arr, start, end):
    if start > end:
        return
    mid = int((start + end) / 2)
    node = Node(arr[mid])
    node.left = createminimaltree(arr, start, mid-1)
    node.right = createminimaltree(arr, mid+1, end)
    return node

def preOrder(node): 
    if not node: 
        return
    print(node.data) 
    print(preOrder(node.left)) 
    print(preOrder(node.right))  

def main():
    t = inp()
    while t > 0:
        arr = inlt()
        n = createminimaltree(arr, 0, len(arr) - 1)
        preOrder(n)
        t -= 1

if __name__ == "__main__": 
    main()

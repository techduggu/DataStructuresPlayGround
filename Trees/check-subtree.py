import sys

# sys.stdin = open('Trees/input.txt', 'r')
# sys.stdout = open('Trees/output.txt', 'w')


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

#Solution-1: Simple by using pre-order traversal and check if T2's substring is part of T1
#Solution-2: Optimized version below:
def check_subtree(t1, t2): #20, 5
    if t2 is None:
        return True #empty tree is always a subtree
    if t1 is None:
        return False #big tree empty & subtree still not found
    if (t1.data == t2.data and matchTree(t1, t2)):
        return True
    return check_subtree(t1.left, t2) or check_subtree(t1.right, t2)

def matchTree(t1, t2):
    if t1 == None and t2 == None:
        return True #nothing left in both tree's sub-trees
    elif t1 is None or t2 is None:
        return False #if one of them reaches empty, then trees don't match
    elif t1.data != t2.data:
        return False #if data doesn't match
    else:
        return matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right)

def main():
    node1 = Node(20)
    node1.left = Node(10)
    node1.right = Node(30)
    node1.left.left = Node(5)
    node1.left.right = Node(15)
    node1.left.left.left = Node(3)
    node1.left.left.right = Node(7)
    node1.left.right.right = Node(17)
    
    node2 = Node(5)
    node2.left = Node(3)
    node2.right = Node(7)
    result = check_subtree(node1, node2)
    print(result)

if __name__ == "__main__": 
    main()

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

# global variable prev - to keep track 
# of previous node during Inorder  
# traversal 
prev = None

#Solution-1
def validate_bst_inorder(node):
    # prev is a global variable 
    global prev
    if bst_inorder_utility(node):
        print("True")
    else:
        print("False")

def bst_inorder_utility(root):
    # prev is a global variable 
    global prev

    # if tree is empty return true 
    if root is None: 
        return True
    
    #recurse in left sub-tree
    if bst_inorder_utility(root.left) is False: 
        return False
    
    # if previous node'data is found  
    # greater than the current node's 
    # data return fals 
    if prev is not None and prev.data > root.data: 
        return False
  
    # store the current node in prev 
    prev = root

    #recurse in right sub-tree 
    if bst_inorder_utility(root.right) is False:
        return False
    
    #if everything passes at this point, return true
    return True

#Solution-2
def validate_bst_max_min_approach(node):
    if max_min_utility(node, None, None):
        print("True")
    else:
        print("False")

def max_min_utility(node, maxi, mini):
    if node is None:
        return True
    
    if (mini != None and node.data <= mini) or (maxi != None and node.data > maxi):
        return False

    if max_min_utility(node.left, maxi=node.data, mini=mini) is False:
        return False
    if max_min_utility(node.right, maxi=maxi, mini=node.data) is False:
        return False
    
    return True

def main():
    node = Node(20)
    node.left = Node(10)
    node.right = Node(30)
    node.left.left = Node(5)
    node.left.right = Node(15)
    node.left.left.left = Node(3)
    node.left.left.right = Node(7)
    node.left.right.right = Node(17)
    #validate_bst_inorder(node)
    validate_bst_max_min_approach(node)

if __name__ == "__main__": 
    main()

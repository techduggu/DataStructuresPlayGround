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

#Solution-2: If node doesn't have link to its parent
#This is also an optimized solution (i.e. bubbling up p or q in the recursion tree)
def first_common_ancestor(root, p, q):
    # Initialize p and q as not visited 
    v = [False, False]
    lca = dfs_utility(root, p, q, v)
    # Returns LCA only if both p and q are present in tree
    if v[0] and v[1] or v[0] and find(lca, q) or v[1] and find(lca,p):
        print(lca.data)
        return lca
    return None

# This function retturn pointer to LCA of two given values 
# p and q  
# v1 is set as true by this function if p is found 
# v2 is set as true by this function if q is found
def dfs_utility(root, p, q, v):
    #base case
    if root == None:
        return None
    # IF either p or q matches ith root's key, report 
    # the presence by setting v1 or v2 as true and return 
    # root (Note that if a key is ancestor of other, then  
    # the ancestor key becomes LCA)
    if root.data == p:
        v[0] = True
        return root
    if root.data == q:
        v[1] = True
        return root
    # Look for keys in left and right subtree
    left_lca = dfs_utility(root.left, p, q, v)
    right_lca = dfs_utility(root.right, p, q, v)
    # If both of the above calls return Non-NULL, then one key 
    # is present in one subtree and other is present in other, 
    # So this node is the LCA 
    if left_lca and right_lca:
        return root
    
    # Otherwise check if left subtree or right subtree is LCA 
    return left_lca if left_lca != None else right_lca

def find(root, k):
    #Base case
    if root == None:
        return False
    # If key is present at root, or if left subtree or right 
    # subtree , return true 
    if root.data == k or find(root.left, k) or find(root.right, k):
        return True
    return False
        

def main():
    node = Node(20)
    node.left = Node(10)
    node.right = Node(30)
    node.left.left = Node(5)
    node.left.right = Node(15)
    node.left.left.left = Node(3)
    node.left.left.right = Node(7)
    node.left.right.right = Node(17)
    first_common_ancestor(node, 5, 17)

if __name__ == "__main__": 
    main()

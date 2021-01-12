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
        self.height = -1
        self.left = None
        self.right = None

def check_balanced(node):
    if node == None:
        return
    node.height = check_balanced_using_dfs(node)
    if node.height != sys.maxsize:
        print("True")
    else:
        print("False")

#The following function also calculates & stores height in a Node object recursively that's why it became complex
#For simplification of this problem, do not store height just calculate and pass it to above call in recursion
def check_balanced_using_dfs(node):
    if node == None:
        return -1
    if node.left is not None:
        node.left.height = check_balanced_using_dfs(node.left)
    if node.right is not None:
        node.right.height = check_balanced_using_dfs(node.right)
    if node.left is None and node.right is None:
        return 0
    elif node.left is None:
        return node.right.height + 1
    elif node.right is None:
        return node.left.height + 1

    if node.left is not None and node.right is not None:    
        node.height = abs(node.left.height - node.right.height)
    
    if node.height > 1:
        return sys.maxsize
    else:
        return max(node.left.height, node.right.height) + 1



def main():
    node = Node(1)
    node.left = Node(2)
    node.right = Node(3)
    node.left.left = Node(4)
    node.left.right = Node(5)
    node.right.left = Node(6)
    node.right.right = Node(7)
    node.right.right.left = Node(5)
    node.right.right.left.left = Node(4)
    node.right.right.left.right = Node(11)
    node.right.right.left.right.left = Node(12)
    node.right.right.left.right.left.right = Node(13)
    check_balanced(node)

if __name__ == "__main__": 
    main()

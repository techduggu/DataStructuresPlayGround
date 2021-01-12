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

#Solution-1 - Brute Force
def path_with_sum_sol1(root, totalSum):
    if root == None:
        return 0
    pathsFromRoot = countPaths(root, totalSum, 0)
    pathsFromLeft = countPaths(root.left, totalSum, 0)
    pathsFromRight = countPaths(root.right, totalSum, 0)
    return pathsFromRoot + pathsFromLeft + pathsFromRight
    

def countPaths(root, totalSum, currentSum):
    if root == None:
        return 0
    currentSum += root.data
    totalPath = 0
    if currentSum == totalSum:
        totalPath += 1
    totalPath += countPaths(root.left, totalSum, currentSum)
    totalPath += countPaths(root.right, totalSum, currentSum)
    return totalPath

#Solution-2: Optimized using HashMap to avoid repeatation of sums (similar to sub-arrays in an array with given sum)
def path_with_sum_sol2(root, totalSum):
    if root == None:
        return 0
    # approach: use a hash map to save accumulative sum of root to 
    # current node and check if there is a match when return
    # store zero sum {0: 1} as default so it will be valid for leaf node
    hashmap = {0 : 1}
    totalPath = countPaths_sol2(root, totalSum, 0, hashmap)
    return totalPath

def countPaths_sol2(root, totalSum, currentSum, hashmap):
    if root == None:
        return 0
    currentSum += root.data
    val = currentSum - totalSum
    countPath = 0
    if val in hashmap:
        countPath += hashmap.get(val)
    
    if currentSum in hashmap:
        hashmap[currentSum] += 1
    else:
        hashmap[currentSum] = 1
    countPath += countPaths_sol2(root.left, totalSum, currentSum, hashmap)
    countPath += countPaths_sol2(root.right, totalSum, currentSum, hashmap)
    hashmap[currentSum] -= 1
    return countPath

def main():
    node = Node(10)
    node.left = Node(5)
    node.right = Node(-3)
    node.left.left = Node(3)
    node.left.right = Node(2)
    node.left.left.left = Node(3)
    node.left.left.right = Node(-2)
    node.left.right.right = Node(1)
    node.right.right = Node(11)
    print(path_with_sum_sol2(node, 8))

if __name__ == "__main__": 
    main()

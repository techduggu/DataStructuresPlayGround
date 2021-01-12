import sys
from collections import defaultdict
from collections import deque

#sys.stdout = open('LinkedList/output.txt', 'w')
#sys.stdin = open('LinkedList/input.txt', 'r')

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

# This class represents a directed graph 
# using adjacency list representation
class Graph:
    #constructor
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices #number of vertices as input
    
    #Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def buildOrder(self, charToVertexNumberDictt):
        #mark all vertices as False, this is important in graph questions to avoid visiting nodes again
        visited = [False] * self.V
        stack = deque()
        # Call the recursive helper function to store Topological Sort
        # starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.dfs_util(i, visited, stack, charToVertexNumberDictt)
        while stack:
            print(stack.pop(), end='->')
    
    def dfs_util(self, v, visited, stack, charToVertexNumberDictt):
        # Mark the current node as visited.
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex 
        for i in self.graph[v]:
            if(visited[i] == False):
                self.dfs_util(i, visited, stack, charToVertexNumberDictt)
        # Push current vertex to stack which stores result
        #Here storing original character/project name in stack to print later
        stack.append(charToVertexNumberDictt.get(v))

def main():
    g = Graph(6)
    g.addEdge(0, 3)
    g.addEdge(5, 1)
    g.addEdge(1, 3)
    g.addEdge(5, 0)
    g.addEdge(3, 2)
    #Creating this dictionary to ease the dfs flow to traverse with integer vertices
    charToVertexNumberDictt = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f'}
    g.buildOrder(charToVertexNumberDictt)

if __name__ == "__main__": 
    main()

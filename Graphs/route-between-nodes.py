import sys
from collections import defaultdict

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
    def __init__(self):
        self.graph = defaultdict(list)
    
    #Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def find_route_using_bfs(self, s, d):
        if s == d:
            print("True")
            return
        #mark all the vertices as not visited
        visited = [False] * len(self.graph)
        #create a queue for BFS
        queue = []
        #Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True
        while queue:
            n = queue.pop(0)
            for i in self.graph[n]:
                if visited[i] == False:
                    if i == d:
                        print("True")
                        return
                    queue.append(i)
                    visited[i] = True
    
    def find_route_using_dfs(self, s, d):
        if s == d:
            print("True")
            return
        #mark all the vertices as not visited
        visited = [False] * len(self.graph)
        self.dfs(s, d, visited)
    
    #DFS is usually implemented using a recursive function
    def dfs(self, s, d, visited):
        visited[s] = True
        for i in self.graph[s]:
                if visited[i] == False:
                    if i == d:
                        print("True")
                        return
                    self.dfs(i, d, visited)


def main():
    g = Graph()
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    #g.find_route_using_bfs(1,3)
    g.find_route_using_dfs(1,3)

if __name__ == "__main__": 
    main()

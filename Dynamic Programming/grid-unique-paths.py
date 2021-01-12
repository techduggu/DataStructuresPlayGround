import sys
#sys.stdout = open('Arrays/output.txt', 'w')
#sys.stdin = open('Arrays/input.txt', 'r')

############ ---- Input Functions ---- ############
# def inp():
#     return(int(input()))
# def inlt():
#     return(list(map(int,input().split())))
# def insr():
#     s = input()
#     return(list(s[:len(s) - 1]))
# def invr():
#     return(map(int,input().split())) 

#https://www.youtube.com/watch?v=t_f0nwwdg5o
#i,j => position in grid
#n,m => rows, cols
def CountPaths_brute(i, j, n, m):
    #boundary check
    if i >= n or j >= m:
        return 0
    #reach end position check
    if i == (n-1) and j == (m-1):
        return 1
    #can only move right and down
    return CountPaths_brute(i+1, j, n, m) + CountPaths_brute(i, j+1, n, m)

def CountPaths_DP(i, j, n, m, memo):
    #boundary check
    if i >= n or j >= m:
        return 0
    #reach end position check
    if i == (n-1) and j == (m-1):
        return 1
    if memo[i][j] != -1:
        return memo[i][j]
    #can only move right and down
    memo[i][j] = CountPaths_DP(i+1, j, n, m, memo) + CountPaths_DP(i, j+1, n, m, memo)
    return memo[i][j]

#Refer video for optimal solution using combinatorics
#def CountPaths_Optimal(n, m)
    
def main():
    print(CountPaths_brute(0, 0, 3, 2))

if __name__ == "__main__": 
    main()

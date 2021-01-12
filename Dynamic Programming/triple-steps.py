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

def CountWays(n):
    #using DP memoization technique to store results
    memo = [-1] * (n+1)
    print(CountWays_Utility(n, memo))

def CountWays_Utility(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = CountWays_Utility(n-1, memo) + CountWays_Utility(n-2, memo) + CountWays_Utility(n-3, memo)
        return memo[n]
    
def main():
    CountWays(38)

if __name__ == "__main__": 
    main()

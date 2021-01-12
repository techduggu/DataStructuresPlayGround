import sys
sys.stdout = open('Arrays/output.txt', 'w')
sys.stdin = open('Arrays/input.txt', 'r')

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

#using sliding window technique
def SubArray(arr, n, total):
    currSum = 0 #define current window sum
    start = 0
    for i,val in enumerate(arr):
        currSum += val
        while currSum > total:
            currSum -= arr[start]
            start += 1
        if currSum == total:
            print("%d %d"%(start + 1, i + 1))
            return 1
    print("-1")
    return -1
    
def main():
    t = inp()
    while t > 0:
        n, total = invr()
        arr = inlt()
        SubArray(arr,n, total)
        t -= 1

if __name__ == "__main__": 
    main()

import sys
sys.stdin = open('Arrays/input.txt', 'r')
sys.stdout = open('Arrays/output.txt', 'w')

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

def MaxSumSubArray(arr, n):
    csum = arr[0]
    maxsum = arr[0]
    for i in range(1,n):
        csum = max(arr[i], csum + arr[i])
        maxsum = max(csum, maxsum)
    print(maxsum)

def main():
    t = inp()
    while t > 0:
        n = inp()
        arr = inlt()
        MaxSumSubArray(arr,n)
        t -= 1

if __name__ == "__main__": 
    main()

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

def RearrangeArrayAlternately(arr,n):
    start = 0
    end = n-1
    while(start < end):
        if arr[start] < arr[end]:
            k = start
            prev = arr[start]
            while(k < n):
                if k == 0:
                    arr[k] = arr[end]
                else:
                    arr[k] = prev
                k+=1

def main():
    t = inp()
    while t > 0:
        n = inp()
        arr = inlt()
        RearrangeArrayAlternately(arr,n)
        t -= 1

if __name__ == "__main__": 
    main()

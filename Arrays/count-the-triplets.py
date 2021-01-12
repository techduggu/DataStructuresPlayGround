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

def CountTriplet(arr, n):
    #sort the array for ease of solving
    arr.sort()
    j = 0 
    k = 0 
    count = 0
    for i in range(0, n-2):
        j = i+1
        k = j+1
        while k < n:
            if arr[i] + arr[j] == arr[k]:
                count += 1
                j += 1
            elif arr[i] + arr[j] < arr[k]:
                j += 1
                k -= 1
            k += 1
    print(count if count > 0 else -1)
    
def main():
    t = inp()
    while t > 0:
        n = inp()
        arr = inlt()
        CountTriplet(arr,n)
        t -= 1

if __name__ == "__main__": 
    main()

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

def magicIndex_brute(arr):
    for i,val in enumerate(arr):
        if i == val:
            return i
    return -1

#As array is sorted and distinct, we can optimize it using binary search
def magicIndex_fast(arr):
    return magicIndex_binarySearch(arr, 0, len(arr))

def magicIndex_binarySearch(arr, start, end):
    if end < start:
        return -1
    mid = int((start + end) / 2)
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        return magicIndex_binarySearch(arr, start, mid -1)
    else:
        return magicIndex_binarySearch(arr, mid+1, end)

def main():
    arr = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
    #print(magicIndex_brute(arr))
    print(magicIndex_fast(arr))

if __name__ == "__main__": 
    main()

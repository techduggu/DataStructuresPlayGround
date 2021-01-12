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

#using Two-pointer algo
#first array - loop from end to 0
#second array - loop from 0 to end
#idea is to keep small numbers in first array and large numbers in second
def PrintMergeSortedArray(arr1,arr2,n,m):
    i = n-1
    j = 0
    while(i >= 0 and j < m):
        if arr1[i] > arr2[j]:
            temp = arr1[i]
            arr1[i] = arr2[j]
            arr2[j] = temp
        i-=1
        j+=1
    arr1.sort()
    arr2.sort()
    res = ' '.join(map(str,arr1)) + ' ' + ' '.join(map(str,arr2))
    print(res)

def main():
    t = inp()
    while t > 0:
        n,m = invr()
        arr1 = inlt()
        arr2 = inlt()
        PrintMergeSortedArray(arr1,arr2,n,m)
        t -= 1

if __name__ == "__main__": 
    main()

#https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

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

#Solution-1: Sort the array and find corresponding repeating & missing
#Time:O(n log n)
#Space: O(1) (or O(N)) depending upon in-place sorting or if without modifying array
def findMissingRepeating_sol1(nums):    
    nums.sort()
    count = 1
    repeating = 0
    for i in range(len(nums)):
        if i > 0:
            if nums[i] == nums[i-1]:
                print("Repeating", nums[i])
                repeating = nums[i]
                count -= 1
        #base-case
        if nums[i] != count and nums[i] != repeating:
            print("Missing", count)
        count += 1

#Solution-2: Use Hashmap/temp array
#Time:O(N)
#Space: O(N)
def findMissingRepeating_sol2(nums):
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i] = True
        else:
            print("Repeating",i)
    for i in range(1, len(nums)+1):
        if i not in dic:
            print("Missing",i)

#Solution-3: Use values of array as indexes and mark visited places as negative
#Time: O(N)
#Space: O(1)
def findMissingRepeating_sol3(nums):
    for i in range(len(nums)):
        if nums[abs(nums[i])-1] > 0:
            nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        else:
            print("Repeating",nums[i])
    for i in range(len(nums)):
        if nums[i] > 0:
            print("Missing", i+1)

def main():
    t = inp()
    while t > 0:
        arr = inlt()
        print(findMissingRepeating_sol3(arr))
        t -= 1
    sys.stdout.close()
    sys.stdin.close()

if __name__ == "__main__": 
    main()

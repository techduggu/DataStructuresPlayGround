#https://leetcode.com/problems/find-the-duplicate-number/

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

#Solution-1: Sort the array and find corresponding duplicates
#Time:O(n log n)
#Space: O(1) (or O(N)) depending upon in-place sorting or if without modifying array
def findDuplicate_sol1(nums):    
    #base cases
    if len(nums) == 0:
        return -1
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return nums[0]
        else:
            return -1
    nums.sort()
    prev = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == prev:
            return nums[i]
        else:
            prev = nums[i]
    return -1

#Solution:2 - Using Set to store unique values
def findDuplicate_sol2(nums):
    visited = set()
    for i in nums:
        if i in visited:
            return i
        visited.add(i)

def main():
    t = inp()
    while t > 0:
        arr = inlt()
        print(findDuplicate_sol2(arr))
        t -= 1
    sys.stdout.close()
    sys.stdin.close()

if __name__ == "__main__": 
    main()

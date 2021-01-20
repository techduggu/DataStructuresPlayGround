#https://leetcode.com/problems/sort-colors/

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

#Solution-1: Simple Counting algorithm: count number of 0s,1s,2s and modify the existing array (constraint in question)
#Time:O(N) but with 2 passes
#Space:O(1)
def sortColors_sol1(nums):
    zeros = ones = twos = 0
    for i in nums:
        if i == 0:
            zeros += 1
        if i == 1:
            ones += 1
        if i == 2:
            twos += 1
    for i in range(len(nums)):
        if zeros > 0:
            nums[i] = 0
            zeros -= 1
        elif ones > 0:
            nums[i] = 1
            ones -= 1
        elif twos > 0:
            nums[i] = 2
            twos -= 1

#Solution-2: Using Dutch National Flag algorithm (http://users.monash.edu/~lloyd/tildeAlgDS/Sort/Flag/)
#Time: O(N) with 1 pass
#Space:O(1)
def sortColors_sol2(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            temp = nums[mid]
            nums[mid] = nums[high]
            nums[high] = temp
            high -=1
    return nums

def main():
    t = inp()
    while t > 0:
        arr = inlt()
        print(sortColors_sol2(arr))
        t -= 1
    sys.stdout.close()
    sys.stdin.close()

if __name__ == "__main__": 
    main()

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

def powerset_brute_iterative(arr):
    emptyset = []
    result = list()
    N = len(arr)
    result.append(emptyset)
    for i in range(N):
        orig = result[:] #store original set
        new = arr[i] #take current element
        for j in range(len(result)): #loop through current result/subset
            result[j] = result[j] + [new]  #append with current elem
        result = orig + result #join orig subset with new one (which is with current elem)
    return result

#For recursive, watch https://www.youtube.com/watch?v=LdtQAYdYLcE
#def powerset_brute_recursive(arr)

def powerset_dp_using_bitmasking(arr):
    N = len(arr)
    totalsubsets = 1<<N #Total 2^n subsets/combinations
    allsubsets = list()
    for mask in range(0,totalsubsets):
        subset = []
        for i in range(0,N):
            f = 1<<i
            if (mask & f) != 0:
                subset.append(arr[i])
        allsubsets.append(subset)
    return allsubsets

def main():
    arr = [1, 2, 3]
    #powerset_brute_iterative(arr)
    print(powerset_dp_using_bitmasking(arr))

if __name__ == "__main__": 
    main()

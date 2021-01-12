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

#apply sum of n numbers theorem (n*n+1)/2 - sum of given array = missing no.
def MissingNumber(arr, n):
    sum_of_n_numbers = n * (n+1) / 2
    sum_of_given_array = sum(arr)
    missing_number = sum_of_n_numbers - sum_of_given_array
    print(int(missing_number))

def main():
    t = inp()
    while t > 0:
        n = inp()
        arr = inlt()
        MissingNumber(arr,n)
        t -= 1

if __name__ == "__main__": 
    main()

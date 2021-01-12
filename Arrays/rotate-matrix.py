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

#e.g.
#1234
#5678
#9123
#4567

#As we need to rotate clockwise, it means rows become columns or vice-versa.
#E.g. 1234 will become last col. So with rotation, think of first transposing the
#matrix (row becomes columns).

#Step-1:
#After transpose (where row elem swaps with col elem):
#1594
#2615
#3726
#4837

#Step-2:
#4951
#5162
#6273
#7384

def RotateMatrix(matrix, N):
    if (len(matrix) == 0 or len(matrix[0]) != N):
        return -1
    #Step-1: Transpose
    for i in range(N):
        for j in range(i,N):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    #Step-2:Swap row elements using two-pointer algo to solve this in O(1) extra space
    for i in range(N):
        start = 0
        end = N - 1
        while(start <= end):
            temp = matrix[i][start]
            matrix[i][start] = matrix[i][end]
            matrix[i][end] = temp
            start += 1
            end -= 1
    #Print the rotated matrix
    for i in range(N):
        print(matrix[i])

def main():
    t = inp()
    while t > 0:
        N = inp()
        matrix = []
        for i in range(N):
            a = []
            row = inlt()
            for j in range(N):
                a.append(row[j])
            matrix.append(a)
        RotateMatrix(matrix, N)
        t -= 1

if __name__ == "__main__": 
    main()

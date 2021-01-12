import sys
sys.stdin = open('Strings/input.txt', 'r')
sys.stdout = open('Strings/output.txt', 'w')

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

MAX_CHAR = 256
def uniquechars(inputString):
    chars = [False] * MAX_CHAR
    for ch in inputString:
        index = ord(ch)
        if (chars[index] == True):
            print("False")
            return -1
        chars[index] = True
    print("True")
    return -1


def main():
    t = inp()
    while t > 0:
        inputStr = insr()
        uniquechars(inputStr)        
        t -= 1

if __name__ == "__main__": 
    main()

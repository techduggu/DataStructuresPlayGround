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

def permutation(inputStr1, inputStr2):
    if len(inputStr1) != len(inputStr2):
        return False
    dictt = {}
    for ch in inputStr1:
        if ch not in dictt:
            dictt[ch] = 1
        else:
            dictt[ch] = dictt.get(ch) + 1
    
    for ch in inputStr2:
        if ch in dictt:
            dictt[ch] = dictt.get(ch) - 1
        else:
            return False
    
    for val in dictt.values():
        if(val > 0):
            return False
    return True

def replacespaces(str, trueLength):
    index = 17
    istr = list(str)
    for i in range(trueLength-1, 0, -1):
        if(istr[i] == ' '):
            istr[index-1] = '0'
            istr[index-2] = '2'
            istr[index-3] = '%'
            index = index - 3
        else:
            istr[index-1] = istr[i]
            index = index - 1


def main():
    t = inp()
    while t > 0:
        inputStr1 = input()
        #inputStr2 = input()
        #print(permutation(inputStr1, inputStr2))
        replacespaces("Mr John Smith    ", 13)
        t -= 1

if __name__ == "__main__": 
    main()

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

def permutations(word):
    if len(word) == 0:
        return []
    if len(word) == 1:
        return [word]
    allPermutations = []
    firstChar = word[0]
    wordWithoutFirstChar = word[1:]
    perms = permutations(wordWithoutFirstChar)
    for perm in perms:
        for i in range(len(perm)+1):
            allPermutations.append(perm[:i] + firstChar + perm[i:])
    return allPermutations

def main():
    print(permutations('abc'))

if __name__ == "__main__": 
    main()

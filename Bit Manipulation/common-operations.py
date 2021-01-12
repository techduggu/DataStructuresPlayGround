import sys

#As computers can't subtract, they store -ve numbers as 2's complement e.g. For -5, flip 5 and then +1
def twos_complement():
    n = 5
    flip = ~5
    twocomplement = flip + 1
    print(twocomplement)

#Find the element that appears once in an array where every other element appears twice
#The best solution is to use XOR. XOR of all array elements gives us the number with a single occurrence
def find_unique_number():
    arr = [1,1,2,2,3,3,4]
    xor = arr[0]
    for i in range(1,len(arr)):
        xor = xor ^ arr[i]
    print(xor)

def find_even_odd():
    n = 5
    if n & 1:
        print('odd')
    else:
        print('even')

#Find count of set bits i.e. count 1s in binary number
def count_set_bits():
    n = 5
    count = 0
    while n > 0:
        count += n & 1
        n = n >> 1
    print(count)

#Find min. of bits to change in a to convert it to b
def min_bits_conversion():
    a = 11
    b = 15
    #Use XOR to find differed bits (bits that need to change)
    xor = a ^ b
    #Count Set bits (same logic as count_set_bits())
    count = 0
    while xor > 0:
        count += xor & 1
        xor = xor >> 1
    print(count)

def remove_last_set_bit():
    n = 13
    result = n & (n-1) #this is the formula to remove last set bit
    print(result)

#Using XOR Swapping
def swap():
    a = 5
    b = 7
    #Swap using XOR
    a = a ^ b
    b = b ^ a
    a = a ^ b
    print(a,b)

def extract_ith_bit():
    n = 13
    i = 2
    result = n & (1 << i) #(1 << i) is a mask (bitmasking technique)
    print(result)

def change_ith_bit():
    n = 13
    i = 1
    result = n | (1 << i)
    print(result)

def clear_ith_bit():
    n = 13
    i = 2
    result = n & ~(1 << i) #(1 << i) is a mask and then negate it to clear ith bit
    print(result)

def main():
    #find_unique_number()
    #twos_complement()
    #find_even_odd()
    #count_set_bits()
    #min_bits_conversion()
    #remove_last_set_bit()
    #swap()
    #extract_ith_bit()
    #change_ith_bit()
    clear_ith_bit()

if __name__ == "__main__": 
    main()
